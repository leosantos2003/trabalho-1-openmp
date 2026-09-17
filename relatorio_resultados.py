#!/usr/bin/env python3
"""Funções compartilhadas para consolidar as evidências dos experimentos.

Os dois scripts executáveis ficam nas respectivas pastas de experimentos. Este
módulo lê CSV, Markdown e SVG e produz o texto do relatório, sem alterar os
dados coletados nem recalcular as medições.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable


SUMMARY_COLUMNS = (
    ("Entrada", "input_set"),
    ("Threads", "threads"),
    ("Tseq (s)", "sequential_median_seconds"),
    ("Tpar(1) (s)", "parallel_one_thread_median_seconds"),
    ("Tpar(p) (s)", "parallel_median_seconds"),
    ("S(p)", "scaling_speedup"),
    ("E(p)", "scaling_efficiency"),
    ("Tseq/Tpar(p)", "baseline_speedup"),
    ("n seq", "sequential_samples"),
    ("n par", "parallel_samples"),
)


def _read_csv(path: Path) -> list[dict[str, str]]:
    """Lê um CSV UTF-8 com BOM opcional e devolve linhas nomeadas."""
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as source:
            return list(csv.DictReader(source))
    except (OSError, csv.Error, UnicodeError):
        return []


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _relative_link(base_dir: Path, target: Path, label: str | None = None) -> str:
    """Gera link relativo ao Markdown que será escrito em base_dir."""
    try:
        relative = target.relative_to(base_dir).as_posix()
    except ValueError:
        relative = target.as_posix()
    return f"[{label or relative}]({relative})"


def _escape_cell(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", "<br>")


def _table(headers: Iterable[str], rows: Iterable[Iterable[object]]) -> list[str]:
    rendered_headers = list(headers)
    lines = ["| " + " | ".join(_escape_cell(item) for item in rendered_headers) + " |"]
    lines.append("| " + " | ".join("---" for _ in rendered_headers) + " |")
    lines.extend(
        "| " + " | ".join(_escape_cell(item) for item in row) + " |" for row in rows
    )
    return lines


def _float(value: str | None) -> float | None:
    if value is None or value.strip() == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _integer(value: str | None) -> int | None:
    number = _float(value)
    if number is None or not number.is_integer():
        return None
    return int(number)


def _seconds(value: str | None) -> str:
    number = _float(value)
    return "n.d." if number is None else f"{number:.6f}"


def _ratio(value: str | None) -> str:
    number = _float(value)
    return "n.d." if number is None else f"{number:.3f}×"


def _efficiency(value: str | None) -> str:
    number = _float(value)
    return "n.d." if number is None else f"{number * 100:.1f}%"


def _count(value: str | None) -> str:
    number = _integer(value)
    return "n.d." if number is None else str(number)


def _configuration_label(row: dict[str, str]) -> str:
    fields = (
        ("entrada", "input_set"),
        ("P", "population"),
        ("B", "bits"),
        ("G", "generations"),
        ("μ", "mutation_rate"),
        ("seed", "seed"),
    )
    visible = [f"{label}={row[key]}" for label, key in fields if row.get(key, "")]
    return ", ".join(visible) if visible else "configuração não identificada"


def _select_environment_file(paths: list[Path]) -> Path | None:
    """Prefere o registro produzido junto com a bateria de tempos."""
    for path in paths:
        if path.name == "tempos_ambiente.md":
            return path
    return paths[0] if paths else None


def _environment_values(path: Path | None) -> list[tuple[str, str]]:
    """Extrai os campos de maior interesse de um registro de ambiente."""
    if path is None:
        return []

    desired = (
        "Data e hora",
        "Host",
        "Sistema operacional",
        "Kernel",
        "Modelo",
        "Núcleos físicos",
        "CPUs lógicas totais",
        "CPUs lógicas disponíveis ao processo",
        "Compilador",
        "Flags sequenciais",
        "Flags paralelas",
        "Afinidade usada pelo coletor",
        "Uptime e média de carga",
        "/proc/loadavg",
    )
    values: dict[str, str] = {}
    for line in _read_text(path).splitlines():
        compact = line.strip().removeprefix("- ").strip().replace("**", "")
        for label in desired:
            prefix = f"{label}:"
            if compact.startswith(prefix):
                value = compact[len(prefix) :].strip()
                if value:
                    values[label] = value
                break
    return [(label, values[label]) for label in desired if label in values]


def _fitness_checks(raw_rows: list[dict[str, str]]) -> list[tuple[str, str, str, str]]:
    """Valida determinismo observado sem assumir que uma ausência é sucesso."""
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in raw_rows:
        if row.get("best_fitness", "").strip():
            groups[_configuration_label(row)].append(row)

    result: list[tuple[str, str, str, str]] = []
    for config, rows in sorted(groups.items()):
        fitness = sorted({row["best_fitness"].strip() for row in rows})
        versions = ", ".join(sorted({row.get("version", "não identificada") for row in rows}))
        status = "consistente" if len(fitness) == 1 else "DIVERGENTE"
        result.append((config, str(len(rows)), versions, f"{', '.join(fitness)} ({status})"))
    return result


def _summary_rows(summary_rows: list[dict[str, str]]) -> list[list[str]]:
    ordered = sorted(
        summary_rows,
        key=lambda row: (row.get("input_set", ""), _integer(row.get("threads")) or 0),
    )
    result: list[list[str]] = []
    for row in ordered:
        result.append(
            [
                row.get("input_set", "n.d."),
                _count(row.get("threads")),
                _seconds(row.get("sequential_median_seconds")),
                _seconds(row.get("parallel_one_thread_median_seconds")),
                _seconds(row.get("parallel_median_seconds")),
                _ratio(row.get("scaling_speedup")),
                _efficiency(row.get("scaling_efficiency")),
                _ratio(row.get("baseline_speedup")),
                _count(row.get("sequential_samples")),
                _count(row.get("parallel_samples")),
            ]
        )
    return result


def _configuration_rows(summary_rows: list[dict[str, str]]) -> list[list[str]]:
    seen: set[tuple[str, ...]] = set()
    rows: list[list[str]] = []
    keys = ("input_set", "population", "bits", "generations", "mutation_rate", "seed")
    for item in summary_rows:
        signature = tuple(item.get(key, "") for key in keys)
        if signature not in seen:
            seen.add(signature)
            rows.append(list(signature))
    return sorted(rows, key=lambda row: row[0])


def _highlights(summary_rows: list[dict[str, str]]) -> list[str]:
    """Aponta máximos observados, sem atribuir causas a eles."""
    by_input: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in summary_rows:
        if row.get("input_set", ""):
            by_input[row["input_set"]].append(row)

    lines: list[str] = []
    for input_set, rows in sorted(by_input.items()):
        candidates = [row for row in rows if _float(row.get("scaling_speedup")) is not None]
        if not candidates:
            continue
        best = max(candidates, key=lambda row: _float(row.get("scaling_speedup")) or float("-inf"))
        lines.append(
            f"- `{input_set}`: maior speedup observado foi "
            f"{_ratio(best.get('scaling_speedup'))} com `p={_count(best.get('threads'))}` "
            f"(eficiência {_efficiency(best.get('scaling_efficiency'))})."
        )
    return lines


def _raw_inventory(raw_rows: list[dict[str, str]]) -> list[str]:
    if not raw_rows:
        return ["Não há linhas de tempos brutos disponíveis."]
    versions = Counter(row.get("version", "não identificada") for row in raw_rows)
    description = ", ".join(f"`{name}`: {count}" for name, count in sorted(versions.items()))
    missing_times = sum(1 for row in raw_rows if _float(row.get("elapsed_seconds")) is None)
    text = f"Foram lidas {len(raw_rows)} execuções brutas ({description})."
    if missing_times:
        text += f" Há {missing_times} linha(s) sem tempo numérico."
    return [text]


def _graphics_section(base_dir: Path, graphics_dir: Path) -> list[str]:
    figures = sorted(
        (
            path
            for path in graphics_dir.glob("*")
            if path.is_file() and path.suffix.lower() in {".svg", ".png", ".jpg", ".jpeg"}
        ),
        key=lambda path: path.name,
    )
    lines = ["## Gráficos gerados", ""]
    if not figures:
        lines.append("Não há gráficos em `graficos/`. Gere-os após a coleta com `gerar_graficos.py`.")
        return lines

    lines.append(
        "As figuras abaixo são as evidências visuais produzidas pela automação. Os valores "
        "numéricos de referência permanecem na tabela e no CSV acima."
    )
    lines.append("")
    for figure in figures:
        label = figure.stem.replace("_", " ").capitalize()
        relative = figure.relative_to(base_dir).as_posix()
        lines.extend((f"### {label}", "", f"[{label}]({relative})", "", f"![{label}]({relative})", ""))
    return lines


def _vtune_excerpt(path: Path, maximum_lines: int = 24) -> list[str]:
    lines = [line.rstrip() for line in _read_text(path).splitlines() if line.strip()]
    excerpt = lines[:maximum_lines]
    if len(lines) > maximum_lines:
        excerpt.append("[trecho interrompido; consulte o arquivo completo]")
    return excerpt


def _vtune_section(base_dir: Path) -> list[str]:
    root = base_dir / "vtune" / "resultados"
    results = (
        sorted(
            (path for path in root.iterdir() if path.is_dir() and not path.name.startswith(".")),
            key=lambda path: path.name,
        )
        if root.exists()
        else []
    )
    lines = ["## Evidências do Intel VTune Profiler", ""]
    if not results:
        lines.append(
            "Ainda não há diretórios de resultados em `vtune/resultados/`. Execute a coleta "
            "na Hype e gere este relatório novamente."
        )
        return lines

    lines.append(
        "Cada bloco preserva os artefatos coletados para uma execução. Os trechos são apenas "
        "um índice de leitura: consulte o arquivo completo e compare com os tempos sem "
        "instrumentação antes de interpretar uma causa."
    )
    lines.append("")
    for result in results:
        lines.extend((f"### `{result.name}`", ""))
        important = (
            result / "metadados.md",
            result / "ambiente.md",
            result / "snapshot" / "resumo.txt",
            result / "hotspots" / "resumo.txt",
            result / "hotspots" / "hotspots_por_funcao.txt",
            result / "hpc" / "resumo.txt",
        )
        available = [path for path in important if path.exists()]
        if not available:
            lines.extend(("Nenhum arquivo de resumo reconhecido foi encontrado nesse diretório.", ""))
            continue
        lines.extend(
            (
                "Arquivos disponíveis: " + ", ".join(_relative_link(base_dir, path) for path in available) + ".",
                "",
            )
        )
        for path in available:
            if path.name in {"ambiente.md", "metadados.md"}:
                continue
            excerpt = _vtune_excerpt(path)
            if not excerpt:
                continue
            relative = _relative_link(base_dir, path)
            lines.extend(
                (
                    f"<details><summary>Trecho de {relative}</summary>",
                    "",
                    "```text",
                    *excerpt,
                    "```",
                    "",
                    "</details>",
                    "",
                )
            )
    return lines


def write_report(base_dir: Path, output_path: Path, title: str, include_vtune: bool) -> Path:
    """Cria um relatório reproduzível e retorna o caminho absoluto do Markdown."""
    base_dir = base_dir.resolve()
    output_path = output_path.resolve()
    data_dir = base_dir / "dados"
    raw_path = data_dir / "tempos.csv"
    summary_path = data_dir / "resumo.csv"
    raw_rows = _read_csv(raw_path) if raw_path.exists() else []
    summary_rows = _read_csv(summary_path) if summary_path.exists() else []
    environment_files = sorted(data_dir.glob("*ambiente*.md"))

    now = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [f"# {title}", "", f"Gerado automaticamente em `{now}`.", ""]
    lines.extend(
        (
            "## Como ler este documento",
            "",
            "Este relatório organiza as evidências já coletadas. Ele não executa o AG, não "
            "altera CSVs e não infere causas de desempenho. Use os links para voltar aos dados "
            "brutos antes de redigir a análise ou os slides.",
            "",
            "## Inventário da coleta",
            "",
        )
    )
    for path, label in ((raw_path, "tempos brutos"), (summary_path, "resumo de medianas")):
        link = _relative_link(base_dir, path) if path.exists() else "`ausente`"
        lines.append(f"- {label.capitalize()}: {link}.")
    if environment_files:
        lines.append(
            "- Registros de ambiente: "
            + ", ".join(_relative_link(base_dir, path) for path in environment_files)
            + "."
        )
    else:
        lines.append("- Registros de ambiente: `ausentes`.")
    lines.append("")

    lines.extend(("## Ambiente de execução", ""))
    environment_file = _select_environment_file(environment_files)
    environment = _environment_values(environment_file)
    if environment:
        lines.append(
            "Resumo baseado em " + _relative_link(base_dir, environment_file) + "."
        )
        lines.append("")
        lines.extend(_table(("Campo", "Valor"), environment))
    else:
        lines.append("Não há registro de ambiente para resumir.")
    lines.append("")

    lines.extend(("## Configurações testadas", ""))
    if summary_rows:
        lines.extend(
            _table(
                ("Entrada", "População", "Bits", "Gerações", "Mutação", "Seed"),
                _configuration_rows(summary_rows),
            )
        )
    elif raw_rows:
        configurations = {_configuration_label(row) for row in raw_rows}
        lines.extend(_table(("Configuração",), ((label,) for label in sorted(configurations))))
    else:
        lines.append("Não há configurações registradas.")
    lines.append("")

    lines.extend(("## Tempos, speedup e eficiência", ""))
    if summary_rows:
        lines.append(
            "`S(p) = Tpar(1) / Tpar(p)` mede a escalabilidade da versão paralela. "
            "`E(p) = S(p) / p`. `Tseq/Tpar(p)` é mostrado separadamente como comparação "
            "com a versão sequencial. Os tempos são medianas em segundos."
        )
        lines.append("")
        lines.extend(_table((label for label, _ in SUMMARY_COLUMNS), _summary_rows(summary_rows)))
        lines.append("")
        highlights = _highlights(summary_rows)
        if highlights:
            lines.extend(("### Destaques numéricos", "", *highlights, ""))
    else:
        lines.extend(
            (
                "O arquivo `dados/resumo.csv` está ausente ou não pôde ser lido. Execute "
                "`gerar_graficos.py` depois de possuir `dados/tempos.csv`.",
                "",
            )
        )

    lines.extend(("## Integridade observada", "", *_raw_inventory(raw_rows), ""))
    checks = _fitness_checks(raw_rows)
    if checks:
        lines.append(
            "A tabela confere se todas as repetições de uma mesma configuração registraram "
            "o mesmo melhor fitness. `DIVERGENTE` deve ser investigado antes de usar uma curva "
            "como comparação de desempenho."
        )
        lines.append("")
        lines.extend(_table(("Configuração", "Linhas", "Versões", "Fitness observado"), checks))
    else:
        lines.append("Sem valores de fitness nos tempos brutos para validar.")
    lines.append("")

    lines.extend(_graphics_section(base_dir, base_dir / "graficos"))
    lines.append("")
    if include_vtune:
        lines.extend(_vtune_section(base_dir))
        lines.append("")

    lines.extend(
        (
            "## Roteiro para a análise crítica e os slides",
            "",
            "- Compare apenas pontos do mesmo ambiente e da mesma configuração de entrada.",
            "- Explique a tendência de `S(p)` e `E(p)` ao aumentar `p`, usando tempos, "
            "topologia da máquina e a carga registrada como evidências.",
            "- Discuta separadamente `Tseq/Tpar(p)` e o speedup de escalabilidade `S(p)`, pois "
            "as referências são diferentes.",
            "- Se houver VTune, relacione hotspots, sincronização e métricas de memória com uma "
            "observação específica das curvas, sem tratar o tempo instrumentado como referência.",
            "- Registre limitações: tamanho do problema, repetições, afinidade, carga concorrente "
            "e possíveis pontos com fitness divergente.",
            "",
            "## Como atualizar",
            "",
            "Após uma nova coleta, gere novamente `dados/resumo.csv` e os gráficos. Em seguida, "
            "execute o script de relatório desta pasta para sobrescrever somente este Markdown.",
            "",
        )
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
