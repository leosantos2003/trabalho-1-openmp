#!/usr/bin/env python3
"""Consolida a coleta da Hype e os resultados do VTune em Markdown."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_DIR))

from relatorio_resultados import write_report  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Organiza tempos, gráficos, ambiente e VTune da Hype em Markdown."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=SCRIPT_DIR / "resultados_hype.md",
        help="caminho do Markdown de saída (padrão: experimentos_hype/resultados_hype.md)",
    )
    args = parser.parse_args()
    output = write_report(
        base_dir=SCRIPT_DIR,
        output_path=args.output,
        title="Resultados dos experimentos na Hype",
        include_vtune=True,
    )
    print(f"Relatório atualizado: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
