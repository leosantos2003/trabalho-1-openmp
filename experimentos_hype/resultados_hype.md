# Resultados dos experimentos na Hype

Gerado automaticamente em `2026-09-17T09:08:10-03:00`.

## Como ler este documento

Este relatório organiza as evidências já coletadas. Ele não executa o AG, não altera CSVs e não infere causas de desempenho. Use os links para voltar aos dados brutos antes de redigir a análise ou os slides.

## Inventário da coleta

- Tempos brutos: [dados/tempos.csv](dados/tempos.csv).
- Resumo de medianas: [dados/resumo.csv](dados/resumo.csv).
- Registros de ambiente: [dados/tempos_ambiente.md](dados/tempos_ambiente.md).

## Ambiente de execução

Resumo baseado em [dados/tempos_ambiente.md](dados/tempos_ambiente.md).

| Campo | Valor |
| --- | --- |
| Data e hora | `2026-09-17T09:04:34-03:00` |
| Host | `bali2` |
| Sistema operacional | Debian GNU/Linux 12 (bookworm) |
| Kernel | `Linux 6.1.0-45-amd64 x86_64 GNU/Linux` |
| Modelo | Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz |
| Núcleos físicos | 16 |
| CPUs lógicas totais | 32 |
| CPUs lógicas disponíveis ao processo | 32 |
| Compilador | `gcc (Debian 12.2.0-14+deb12u1) 12.2.0` |
| Flags sequenciais | `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude` |
| Flags paralelas | `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude` |
| Afinidade usada pelo coletor | `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores` |
| Uptime e média de carga | ` 09:04:34 up 138 days,  8:23,  4 users,  load average: 4.28, 1.49, 0.58` |

## Configurações testadas

| Entrada | População | Bits | Gerações | Mutação | Seed |
| --- | --- | --- | --- | --- | --- |
| grande | 4000 | 2000 | 100 | 0.0005 | 42 |
| medio | 2000 | 2000 | 100 | 0.0005 | 42 |
| pequeno | 1000 | 1000 | 100 | 0.001 | 42 |

## Tempos, speedup e eficiência

`S(p) = Tpar(1) / Tpar(p)` mede a escalabilidade da versão paralela. `E(p) = S(p) / p`. `Tseq/Tpar(p)` é mostrado separadamente como comparação com a versão sequencial. Os tempos são medianas em segundos.

| Entrada | Threads | Tseq (s) | Tpar(1) (s) | Tpar(p) (s) | S(p) | E(p) | Tseq/Tpar(p) | n seq | n par |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grande | 1 | 5.051685 | 5.028056 | 5.028056 | 1.000× | 100.0% | 1.005× | 10 | 10 |
| grande | 2 | 5.051685 | 5.028056 | 2.546925 | 1.974× | 98.7% | 1.983× | 10 | 10 |
| grande | 4 | 5.051685 | 5.028056 | 1.442975 | 3.485× | 87.1% | 3.501× | 10 | 10 |
| grande | 8 | 5.051685 | 5.028056 | 0.773392 | 6.501× | 81.3% | 6.532× | 10 | 10 |
| grande | 16 | 5.051685 | 5.028056 | 0.415054 | 12.114× | 75.7% | 12.171× | 10 | 10 |
| grande | 20 | 5.051685 | 5.028056 | 0.437462 | 11.494× | 57.5% | 11.548× | 10 | 10 |
| medio | 1 | 2.528771 | 2.516309 | 2.516309 | 1.000× | 100.0% | 1.005× | 10 | 10 |
| medio | 2 | 2.528771 | 2.516309 | 1.274126 | 1.975× | 98.7% | 1.985× | 10 | 10 |
| medio | 4 | 2.528771 | 2.516309 | 0.722356 | 3.483× | 87.1% | 3.501× | 10 | 10 |
| medio | 8 | 2.528771 | 2.516309 | 0.388014 | 6.485× | 81.1% | 6.517× | 10 | 10 |
| medio | 16 | 2.528771 | 2.516309 | 0.209823 | 11.993× | 75.0% | 12.052× | 10 | 10 |
| medio | 20 | 2.528771 | 2.516309 | 0.220671 | 11.403× | 57.0% | 11.459× | 10 | 10 |
| pequeno | 1 | 0.636254 | 0.634193 | 0.634193 | 1.000× | 100.0% | 1.003× | 10 | 10 |
| pequeno | 2 | 0.636254 | 0.634193 | 0.321932 | 1.970× | 98.5% | 1.976× | 10 | 10 |
| pequeno | 4 | 0.636254 | 0.634193 | 0.182990 | 3.466× | 86.6% | 3.477× | 10 | 10 |
| pequeno | 8 | 0.636254 | 0.634193 | 0.098694 | 6.426× | 80.3% | 6.447× | 10 | 10 |
| pequeno | 16 | 0.636254 | 0.634193 | 0.055320 | 11.464× | 71.7% | 11.501× | 10 | 10 |
| pequeno | 20 | 0.636254 | 0.634193 | 0.058243 | 10.889× | 54.4% | 10.924× | 10 | 10 |

### Destaques numéricos

- `grande`: maior speedup observado foi 12.114× com `p=16` (eficiência 75.7%).
- `medio`: maior speedup observado foi 11.993× com `p=16` (eficiência 75.0%).
- `pequeno`: maior speedup observado foi 11.464× com `p=16` (eficiência 71.7%).

## Integridade observada

Foram lidas 210 execuções brutas (`paralelizado`: 180, `sequencial`: 30).

A tabela confere se todas as repetições de uma mesma configuração registraram o mesmo melhor fitness. `DIVERGENTE` deve ser investigado antes de usar uma curva como comparação de desempenho.

| Configuração | Linhas | Versões | Fitness observado |
| --- | --- | --- | --- |
| entrada=grande, P=4000, B=2000, G=100, μ=0.0005, seed=42 | 70 | paralelizado, sequencial | 1575 (consistente) |
| entrada=medio, P=2000, B=2000, G=100, μ=0.0005, seed=42 | 70 | paralelizado, sequencial | 1522 (consistente) |
| entrada=pequeno, P=1000, B=1000, G=100, μ=0.001, seed=42 | 70 | paralelizado, sequencial | 847 (consistente) |

## Gráficos gerados

As figuras abaixo são as evidências visuais produzidas pela automação. Os valores numéricos de referência permanecem na tabela e no CSV acima.

### Eficiencia grande

[Eficiencia grande](graficos/eficiencia_grande.svg)

![Eficiencia grande](graficos/eficiencia_grande.svg)

### Eficiencia medio

[Eficiencia medio](graficos/eficiencia_medio.svg)

![Eficiencia medio](graficos/eficiencia_medio.svg)

### Eficiencia pequeno

[Eficiencia pequeno](graficos/eficiencia_pequeno.svg)

![Eficiencia pequeno](graficos/eficiencia_pequeno.svg)

### Speedup grande

[Speedup grande](graficos/speedup_grande.svg)

![Speedup grande](graficos/speedup_grande.svg)

### Speedup medio

[Speedup medio](graficos/speedup_medio.svg)

![Speedup medio](graficos/speedup_medio.svg)

### Speedup pequeno

[Speedup pequeno](graficos/speedup_pequeno.svg)

![Speedup pequeno](graficos/speedup_pequeno.svg)


## Evidências do Intel VTune Profiler

Ainda não há diretórios de resultados em `vtune/resultados/`. Execute a coleta na Hype e gere este relatório novamente.

## Roteiro para a análise crítica e os slides

- Compare apenas pontos do mesmo ambiente e da mesma configuração de entrada.
- Explique a tendência de `S(p)` e `E(p)` ao aumentar `p`, usando tempos, topologia da máquina e a carga registrada como evidências.
- Discuta separadamente `Tseq/Tpar(p)` e o speedup de escalabilidade `S(p)`, pois as referências são diferentes.
- Se houver VTune, relacione hotspots, sincronização e métricas de memória com uma observação específica das curvas, sem tratar o tempo instrumentado como referência.
- Registre limitações: tamanho do problema, repetições, afinidade, carga concorrente e possíveis pontos com fitness divergente.

## Como atualizar

Após uma nova coleta, gere novamente `dados/resumo.csv` e os gráficos. Em seguida, execute o script de relatório desta pasta para sobrescrever somente este Markdown.
