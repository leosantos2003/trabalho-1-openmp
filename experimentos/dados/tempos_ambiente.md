# Ambiente de execução dos experimentos

## Registro: antes da coleta

- Data e hora: `2026-09-16T15:49:43-03:00`
- Host: `leonardo-Inspiron-15-3530`
- Sistema operacional: Ubuntu 24.04.4 LTS
- Kernel: `Linux 7.0.0-30-generic x86_64 GNU/Linux`

### Processador

- Modelo: 13th Gen Intel(R) Core(TM) i7-1355U
- Núcleos físicos: 10
- CPUs lógicas totais: 12
- CPUs lógicas disponíveis ao processo: 12
- Soquetes: 1
- Núcleos por soquete: 10
- Threads por núcleo: 2

### Compilação

- Compilador: `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 15:49:43 up 8 min,  1 user,  load average: 0,96, 0,94, 0,54`
- `/proc/loadavg`: `0.96 0.94 0.54 2/1525 11478`

Memória:

```text
               total       usada       livre    compart.  buff/cache  disponível
Mem.:           15Gi       4,5Gi       7,7Gi       761Mi       4,2Gi        10Gi
Swap:          4,0Gi          0B       4,0Gi
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
   5004 leonardo code            22.2  2.6
   4949 leonardo code             9.8  1.2
   2998 leonardo gnome-shell      9.4  2.0
   6715 leonardo code             9.3  2.8
   6736 leonardo code             7.8  2.0
   4907 leonardo code             6.9  1.7
  11411 leonardo bash             6.2  0.0
  10037 leonardo code             5.5  1.1
   7650 leonardo cpptools         5.1  0.1
   4574 leonardo zen              4.3  2.9
```

---


## Registro: depois da coleta

- Data e hora: `2026-09-16T15:52:38-03:00`
- Host: `leonardo-Inspiron-15-3530`
- Sistema operacional: Ubuntu 24.04.4 LTS
- Kernel: `Linux 7.0.0-30-generic x86_64 GNU/Linux`

### Processador

- Modelo: 13th Gen Intel(R) Core(TM) i7-1355U
- Núcleos físicos: 10
- CPUs lógicas totais: 12
- CPUs lógicas disponíveis ao processo: 12
- Soquetes: 1
- Núcleos por soquete: 10
- Threads por núcleo: 2

### Compilação

- Compilador: `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 15:52:38 up 11 min,  1 user,  load average: 2,70, 1,63, 0,88`
- `/proc/loadavg`: `2.70 1.63 0.88 4/1521 14456`

Memória:

```text
               total       usada       livre    compart.  buff/cache  disponível
Mem.:           15Gi       4,6Gi       7,6Gi       751Mi       4,2Gi        10Gi
Swap:          4,0Gi          0B       4,0Gi
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
  14458 leonardo ps               100  0.0
   5004 leonardo code            17.4  2.6
   4949 leonardo code             8.9  1.2
   2998 leonardo gnome-shell      8.5  2.0
  14404 leonardo bash             8.3  0.0
   6715 leonardo code             7.1  3.0
   4907 leonardo code             5.4  1.7
   6736 leonardo code             5.0  2.1
   7650 leonardo cpptools         3.3  0.1
   4574 leonardo zen              3.0  2.9
```
