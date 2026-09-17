# Análise crítica da coleta de desempenho

## Conclusão principal

Os resultados são internamente coerentes e mostram boa escalabilidade OpenMP no nó `bali2`. Porém, **não são resultados da Hype** e não devem ser apresentados como tal na versão final do trabalho. O arquivo de ambiente registra `Host: bali2`, 16 núcleos físicos, 32 CPUs lógicas e 31 GiB de memória, enquanto a partição solicitada para a coleta final é `hype`, cujos nós aparecem como `hype[1-5]` na consulta ao Slurm.

Portanto, esta rodada deve ser preservada como experimento preliminar no PCAD, mas a bateria precisa ser repetida dentro de uma alocação cujo `hostname`, `SLURM_JOB_PARTITION` e `SLURM_NODELIST` indiquem um nó `hype`.

## Evidências usadas

- [Tempos brutos](dados/tempos.csv): 210 execuções.
- [Resumo de medianas](dados/resumo.csv): tempos, speedup e eficiência.
- [Registro do ambiente](dados/tempos_ambiente.md): nó, topologia, compilador e carga.
- [Relatório consolidado](resultados_hype.md) e gráficos em [graficos/](graficos/).

## Validade da rodada

| Critério | Evidência | Avaliação |
| --- | --- | --- |
| Cobertura da coleta | 3 conjuntos × 10 execuções sequenciais + 3 conjuntos × 6 contagens de threads × 10 execuções paralelas = 210 linhas. | Correta. |
| Amostras | O resumo contém 10 amostras sequenciais e 10 paralelas em cada ponto. | Correta. |
| Correção funcional | O melhor fitness é constante para todas as execuções de cada conjunto: 847, 1522 e 1575. | Correta. |
| Métrica de escalabilidade | `S(1) = 1` e `E(1) = 1` em todos os conjuntos. | Correta. |
| Ambiente de desempenho | Antes da coleta, a carga média era 0,12 / 0,08 / 0,03 e não havia outro processo relevante consumindo CPU. | Adequado. |
| Nó-alvo | A coleta foi feita em `bali2`, não em `hype[1-5]`. | **Inválida como coleta final da Hype.** |
| VTune | Não há resultados em `vtune/resultados/`. | Ainda pendente. |

O aumento da carga de 1 minuto para 4,28 ao final é compatível com a própria bateria paralela que acabara de ser executada. A lista de processos não mostra outra carga concorrente relevante; portanto, ela não invalida a rodada em `bali2`.

## Comportamento medido

### Tempo e tamanho do problema

O tempo sequencial mediano cresce quase proporcionalmente ao trabalho nominal `população × bits`:

| Conjunto | Trabalho nominal relativo | Tempo sequencial mediano |
| --- | ---: | ---: |
| pequeno | 1 | 0,636254 s |
| medio | 4 | 2,528772 s |
| grande | 8 | 5,051685 s |

Do pequeno para o médio, o tempo cresce 3,97×; do pequeno para o grande, 7,94×. Os valores são próximos aos fatores de trabalho 4× e 8×. Isso indica que os três conjuntos aumentam a carga de forma previsível e são adequados para observar escalabilidade.

### Speedup e eficiência

`S(p)` usa a versão paralela com uma thread como referência: `S(p) = Tpar(1) / Tpar(p)`. `E(p) = S(p) / p`.

| Threads | Pequeno: S(p) / E(p) | Médio: S(p) / E(p) | Grande: S(p) / E(p) |
| ---: | ---: | ---: | ---: |
| 2 | 1,970× / 98,5% | 1,975× / 98,7% | 1,974× / 98,7% |
| 4 | 3,466× / 86,6% | 3,483× / 87,1% | 3,485× / 87,1% |
| 8 | 6,426× / 80,3% | 6,485× / 81,1% | 6,501× / 81,3% |
| 16 | **11,464× / 71,7%** | **11,993× / 75,0%** | **12,114× / 75,7%** |
| 20 | 10,889× / 54,4% | 11,403× / 57,0% | 11,494× / 57,5% |

O comportamento faz sentido para um algoritmo com trabalho regular por indivíduo:

- Com duas threads, a eficiência está entre 98,5% e 98,7%, quase ideal.
- A eficiência cai gradualmente a partir de quatro threads, mas ainda está entre 71,7% e 75,7% em 16 threads.
- O maior speedup de cada conjunto ocorre em 16 threads, exatamente a quantidade de núcleos físicos registrada em `bali2`.
- Ao passar de 16 para 20 threads, o tempo mediano aumenta cerca de 5,2% a 5,4% nos três conjuntos e o speedup cai cerca de 5,0%.

A explicação mais provável para a queda em 20 threads é que 20 threads ultrapassam os 16 núcleos físicos e passam a compartilhar recursos por hyperthreading. Sobrecarga de criação/sincronização de threads, competição por cache e largura de banda de memória também podem contribuir. Essas são hipóteses consistentes com os dados, mas só o VTune ou contadores de hardware poderiam quantificar cada causa.

O speedup adicional `Tseq / Tpar(p)` é muito próximo de `S(p)`: com uma thread, a diferença entre a versão sequencial e a paralela é inferior a 0,5% em todos os conjuntos. Assim, não há evidência de overhead material da infraestrutura OpenMP quando ela usa apenas uma thread.

## Estabilidade das medições

As repetições são muito estáveis na maior parte dos pontos. Para todas as medições paralelas até oito threads, o coeficiente de variação é no máximo 0,53%. Em 16 threads, apareceram duas execuções mais lentas:

| Conjunto e threads | Mediana | Maior tempo | Coeficiente de variação | Observação |
| --- | ---: | ---: | ---: | --- |
| médio, 16 | 0,209824 s | 0,244866 s | 5,20% | Uma execução foi aproximadamente 16,7% mais lenta que a mediana. |
| grande, 16 | 0,415054 s | 0,441233 s | 2,01% | Uma execução foi aproximadamente 6,3% mais lenta que a mediana. |

Esses pontos não devem ser removidos sem justificativa. O uso da mediana, já adotado no resumo, é apropriado porque reduz o efeito dessas variações isoladas. As nove demais execuções de `médio, 16` ficaram entre 0,208991 s e 0,211515 s, o que reforça a estabilidade da tendência central.

## O que pode ser dito no trabalho

É defensável afirmar que, **no nó `bali2`**, a implementação paralela apresenta escalabilidade forte: o speedup cresce de forma próxima do ideal até duas threads, chega a aproximadamente 11,5×–12,1× em 16 threads e perde desempenho ao ultrapassar os 16 núcleos físicos.

Não é defensável afirmar que esses valores caracterizam a Hype. Eles não devem compor os gráficos ou conclusões finais identificados como “Hype”, nem ser comparados numericamente aos resultados do notebook como se fossem a mesma máquina.

## Repetição obrigatória na Hype

Antes de iniciar a nova coleta, já dentro da alocação, execute e confira:

```bash
hostname
printf 'job=%s\nparticao=%s\nnos=%s\ncpus=%s\n' \
  "$SLURM_JOB_ID" "$SLURM_JOB_PARTITION" \
  "$SLURM_NODELIST" "$SLURM_CPUS_ON_NODE"
LC_ALL=C lscpu
```

Para a coleta ser válida como Hype, o resultado deve indicar:

- `hostname` com nome `hypeN`;
- `particao=hype`;
- `nos=hypeN`;
- uma contagem de threads baseada nos núcleos físicos mostrados por `lscpu`.

Faça novamente uma execução piloto com uma thread. Se a versão com uma thread ficar curta demais na Hype, aumente gerações antes da bateria de dez repetições. Só então execute `executar_testes.sh`, gere os gráficos e o relatório. Depois da validação dessa nova rodada, escolha um conjunto médio ou grande e faça o VTune na mesma partição.

## Próximos passos

1. Preserve os dados atuais como `bali2`; não use `OVERWRITE=1` sobre eles.
2. Reserve um nó da partição `hype` e valide o ambiente com os comandos acima.
3. Salve a nova rodada em arquivos distintos ou arquive a atual antes de executar a coleta válida na Hype.
4. Gere novamente `resumo.csv`, gráficos e `resultados_hype.md` somente com os dados da Hype.
5. Execute Snapshot, Hotspots e/ou HPC Performance no caso escolhido e atualize o relatório.
