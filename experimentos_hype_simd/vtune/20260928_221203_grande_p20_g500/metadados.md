# Coleta Intel VTune Profiler

- Data: `2026-09-28T22:12:03-03:00`
- Análise solicitada: `hpc`
- Conjunto base: `grande`
- População: `4000`
- Bits por indivíduo: `2000`
- Gerações do experimento de desempenho: `100`
- Gerações perfiladas: `500`
- Taxa de mutação: `0.0005`
- Seed: `42`
- Threads: `20`
- Variáveis OpenMP: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`
- VTune: `Intel(R) oneAPI VTune(TM) Profiler 2021.1.1 Gold (build 613804) Command Line Tool`

A multiplicação de gerações existe apenas para obter uma duração adequada de amostragem. Estes resultados não devem substituir os tempos usados nos gráficos de speedup.

## Comando: hpc

```bash
OMP_NUM_THREADS=20 OMP_DYNAMIC=FALSE OMP_PROC_BIND=true OMP_PLACES=cores vtune -collect hpc-performance -result-dir /home/users/phffleck/trabalho-1-openmp/experimentos_hype/vtune/resultados/20260928_221203_grande_p20_g500/hpc -- /home/users/phffleck/trabalho-1-openmp/ga_seq_paralelizado/ga_seq_paralelizado 4000 2000 500 0.0005 42 
```
