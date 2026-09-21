# Análise crítica dos resultados de desempenho na Hype

Rodada analisada: 17/09/2026, 14:59–15:02, registrada em
[dados/tempos_ambiente.md](dados/tempos_ambiente.md).

## Conclusão principal

Esta é uma coleta válida de desempenho na Hype: o registro automático indica o host
hype2, com 20 núcleos físicos, 40 CPUs lógicas, dois soquetes e afinidade OpenMP
em núcleos. Foram feitas 210 execuções, todas com o fitness esperado para o
respectivo conjunto. Os gráficos e as medianas desta pasta já podem sustentar a
discussão do item de desempenho do trabalho.

A implementação apresenta escalabilidade forte até 20 threads, o total de núcleos
físicos do nó. O maior speedup de escalabilidade foi 14,64×, no conjunto grande
com 20 threads, com eficiência de 73,2%. A queda gradual de eficiência é esperada
e não há regressão ao passar de 16 para 20 threads. O perfil do VTune, entretanto,
**não foi concluído**; ainda não há evidência de hotspots para explicar
quantitativamente essa perda de eficiência.

## Evidências usadas

- [Tempos brutos](dados/tempos.csv): 210 execuções.
- [Resumo de medianas](dados/resumo.csv): tempos, speedup e eficiência.
- [Registro do ambiente](dados/tempos_ambiente.md): nó, topologia, compilador,
  flags e carga antes/depois da bateria.
- [Relatório consolidado](resultados_hype.md) e gráficos em [graficos/](graficos/).
- Tentativa de VTune em
  [vtune/resultados/20260917_150435_grande_p8_g500/](vtune/resultados/20260917_150435_grande_p8_g500/).

## Validade da rodada

| Critério | Evidência | Avaliação |
| --- | --- | --- |
| Nó-alvo | Host hype2, 20 núcleos físicos e 40 CPUs lógicas. | Coleta na Hype. |
| Cobertura | 3 conjuntos × 10 execuções sequenciais + 3 conjuntos × 6 contagens de threads × 10 execuções paralelas = 210 linhas. | Correta. |
| Amostras | Cada ponto tem 10 amostras sequenciais e 10 paralelas. | Correta. |
| Correção funcional | O melhor fitness permaneceu em 847, 1522 e 1575 para pequeno, médio e grande, respectivamente. | Correta. |
| Métrica de escalabilidade | S(1) = 1 e E(1) = 1 em todos os conjuntos. | Correta. |
| Carga externa inicial | Média de carga 0,05 / 0,54 / 0,81; a lista de processos não mostra outra carga relevante. | Adequada. |
| Carga externa final | Média de 1 minuto em 3,91, logo após a própria bateria paralela; a lista de processos ainda não mostra concorrência relevante. | Não invalida a rodada. |
| VTune | Hotspots foi iniciado, mas falhou antes de executar o AG e não gerou resumo.txt nem hotspots_por_funcao.txt. | Pendente. |

O registro existente não salvou as variáveis de partição e de nós do Slurm, mas
o host hype2 coincide com a alocação Hype validada no terminal. Para futuras
coletas, o script coletar_ambiente.sh passou a registrar também esses campos.

## Tempo e tamanho do problema

O trabalho nominal, aproximado por população × bits, vale 1, 4 e 8 para os
conjuntos pequeno, médio e grande. Os tempos sequenciais medianos seguem essa
progressão de modo próximo:

| Conjunto | Trabalho relativo | Tempo sequencial mediano | Fator sobre pequeno |
| --- | ---: | ---: | ---: |
| pequeno | 1 | 0,462991 s | 1,00× |
| médio | 4 | 1,792537 s | 3,87× |
| grande | 8 | 3,568084 s | 7,71× |

O crescimento ligeiramente menor que o nominal pode resultar de custos fixos
amortizados em problemas maiores e de efeitos de cache. Como a tendência é
monótona e próxima do trabalho relativo, os três conjuntos são adequados para
medir escalabilidade.

## Speedup e eficiência

S(p) = Tpar(1) / Tpar(p) mede a escalabilidade da própria implementação
paralela. E(p) = S(p) / p mostra quanto do ideal linear foi obtido. Os valores
abaixo vêm das medianas de dez execuções por ponto.

| Threads | Pequeno: S(p) / E(p) | Médio: S(p) / E(p) | Grande: S(p) / E(p) |
| ---: | ---: | ---: | ---: |
| 2 | 1,954× / 97,7% | 1,959× / 98,0% | 1,968× / 98,4% |
| 4 | 3,462× / 86,5% | 3,491× / 87,3% | 3,498× / 87,5% |
| 8 | 6,457× / 80,7% | 6,506× / 81,3% | 6,543× / 81,8% |
| 16 | 11,244× / 70,3% | 11,908× / 74,4% | 12,115× / 75,7% |
| 20 | **13,361× / 66,8%** | **14,352× / 71,8%** | **14,636× / 73,2%** |

- Duas threads entregam 97,7%–98,4% de eficiência, muito próximo do ideal.
- A eficiência diminui gradualmente à medida que aumentam sincronização,
  coordenação de regiões paralelas e competição por recursos compartilhados.
- O conjunto grande mantém a melhor eficiência em 20 threads, enquanto o
  pequeno sofre mais com custos fixos relativos de paralelismo.
- De 16 para 20 threads, o tempo cai 15,85% no pequeno, 17,02% no médio e
  17,22% no grande. O ganho adicional é útil, mas menor que os 25% ideais.

Os 20 threads testados ocupam os 20 núcleos físicos, não os 40 lógicos. Isso é
uma escolha metodológica adequada para a curva principal, pois evita confundir
escalabilidade OpenMP com hyperthreading. Um ponto em 40 threads pode ser
incluído somente como experimento complementar, claramente identificado como
teste de hyperthreading, caso o professor o solicite.

Uma leitura pela lei de Amdahl produz frações seriais efetivas de 2,62%, 2,07%
e 1,93% nos conjuntos pequeno, médio e grande, respectivamente, usando os
speedups em 20 threads. Essas frações agregam código serial, sincronização,
desequilíbrio e limites de memória. Elas ajudam a explicar por que o ganho
adicional diminui conforme p aumenta.

## Comparação com a versão sequencial

O indicador separado Tseq / Tpar(p) compara executáveis distintos. Em uma
thread, ele é 1,035×, 1,011× e 1,006× para pequeno, médio e grande. Portanto,
a versão paralela com uma thread não apresenta penalidade relevante frente à
sequencial; no conjunto pequeno a diferença de 3,5% também pode refletir
variação normal e pequenas diferenças entre os executáveis. Para discutir
escalabilidade, a referência mais apropriada continua sendo S(p), que usa a
mesma versão paralela em uma thread.

## Estabilidade das medições

As repetições são estáveis. O coeficiente de variação é inferior a 1% em 15 dos
21 grupos de medições; os maiores casos são:

| Configuração | Mediana | Maior tempo | Coeficiente de variação | Leitura |
| --- | ---: | ---: | ---: | --- |
| pequeno, 4 threads | 0,129264 s | 0,143469 s | 3,44% | Uma execução isolada mais lenta. |
| médio, 8 threads | 0,272584 s | 0,299891 s | 3,15% | Uma execução isolada mais lenta. |
| grande, 20 threads | 0,242369 s | 0,256304 s | 2,17% | Variação moderada em um ponto de alta concorrência. |

Não há justificativa para excluir essas amostras. A mediana, já usada nos CSVs
e gráficos, reduz corretamente a influência de episódios isolados sem ocultar
os dados brutos. Para os slides, apresente a mediana como métrica central e
cite que há dez repetições por configuração.

## Situação do Intel VTune Profiler

A tentativa de Hotspots usou o conjunto grande, oito threads e 500 gerações
apenas para prolongar a execução perfilada. O ambiente e os parâmetros foram
registrados, mas o VTune 2021.1.1 falhou no mecanismo Pin ao ler a seção
.relr.dyn de /lib64/ld-linux-x86-64.so.2. O arquivo
[pinerr.tpsslog](vtune/resultados/20260917_150435_grande_p8_g500/hotspots-bad/data.0/pinerr.tpsslog)
confirma que a falha ocorreu antes do AG; por isso não existem resultados de
hotspots, snapshot ou HPC Performance utilizáveis.

Esta falha não afeta os tempos sem instrumentação. Para cumprir a parte do
VTune do enunciado, é necessário obter da administração/professor uma versão
mais recente do VTune ou um procedimento compatível com o Debian 12 da Hype e
repetir uma coleta. Até lá, não atribua a queda de eficiência a uma função
específica ou a uma limitação de memória com base nesses arquivos incompletos.

## Texto defensável para o relatório ou apresentação

> Na Hype (hype2, 20 núcleos físicos), a implementação OpenMP apresentou
> speedup de 13,36× a 14,64× em 20 threads, com eficiência entre 66,8% e
> 73,2%. A eficiência foi próxima de 98% em duas threads e diminuiu
> gradualmente ao aumentar o paralelismo, comportamento compatível com custos
> de sincronização e recursos compartilhados. Os resultados usam a mediana de
> dez repetições e mantiveram o mesmo fitness em todas as execuções. A análise
> detalhada por VTune permanece pendente por incompatibilidade da instalação
> 2021.1.1 com o ambiente do nó.

## Próximos passos

1. Use os CSVs e gráficos atuais como resultados finais do item de desempenho.
2. Preserve o diretório hotspots-bad como evidência da falha, mas não o use
   como perfil de desempenho.
3. Solicite uma instalação ou módulo de VTune compatível e repita Hotspots,
   Snapshot ou HPC Performance na Hype, sem substituir os tempos da bateria.
4. Após uma coleta bem-sucedida, gere novamente resultados_hype.md e atualize
   apenas a seção de VTune desta análise.
