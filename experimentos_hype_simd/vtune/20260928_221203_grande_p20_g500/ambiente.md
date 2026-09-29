# Ambiente de execução dos experimentos

## Registro: antes da coleta VTune

- Data e hora: `2026-09-28T22:12:03-03:00`
- Host: `hype1`
- Sistema operacional: Debian GNU/Linux 12 (bookworm)
- Kernel: `Linux 6.1.0-45-amd64 x86_64 GNU/Linux`

### Processador

- Modelo: Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz
- Núcleos físicos: 20
- CPUs lógicas totais: 40
- CPUs lógicas disponíveis ao processo: 40
- Soquetes: 2
- Núcleos por soquete: 10
- Threads por núcleo: 2

### Alocação Slurm

- Job ID: `825511`
- Partição: `hype`
- Nós alocados: `hype1`
- CPUs solicitadas no nó: `40`

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp -fopt-info-vec`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 22:12:03 up 149 days, 21:29,  1 user,  load average: 0.10, 0.04, 0.56`
- `/proc/loadavg`: `0.10 0.04 0.56 1/461 1022858`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       2.7Gi        12Gi       4.8Mi       111Gi       123Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
1022806 phffleck bash             5.0  0.0
 656125 node-exp node_exporter    1.7  0.0
3700828 cgroup-+ cgroup_exporter  0.3  0.0
1022636 root     slurmstepd       0.0  0.0
   1118 message+ dbus-daemon      0.0  0.0
1022641 phffleck bash             0.0  0.0
2643993 root     systemd-journal  0.0  0.0
1022190 phffleck systemd          0.0  0.0
      1 root     systemd          0.0  0.0
   1308 root     fail2ban-server  0.0  0.0
```

---


## Registro: depois da coleta VTune

- Data e hora: `2026-09-28T22:12:21-03:00`
- Host: `hype1`
- Sistema operacional: Debian GNU/Linux 12 (bookworm)
- Kernel: `Linux 6.1.0-45-amd64 x86_64 GNU/Linux`

### Processador

- Modelo: Intel(R) Xeon(R) CPU E5-2650 v3 @ 2.30GHz
- Núcleos físicos: 20
- CPUs lógicas totais: 40
- CPUs lógicas disponíveis ao processo: 40
- Soquetes: 2
- Núcleos por soquete: 10
- Threads por núcleo: 2

### Alocação Slurm

- Job ID: `825511`
- Partição: `hype`
- Nós alocados: `hype1`
- CPUs solicitadas no nó: `40`

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp -fopt-info-vec`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 22:12:21 up 149 days, 21:30,  1 user,  load average: 0.42, 0.12, 0.58`
- `/proc/loadavg`: `0.42 0.12 0.58 1/463 1023175`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       2.7Gi        12Gi       4.8Mi       112Gi       123Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
 656125 node-exp node_exporter    1.7  0.0
3700828 cgroup-+ cgroup_exporter  0.3  0.0
1022780 root     kworker/u81:4-r  0.0  0.0
   1118 message+ dbus-daemon      0.0  0.0
1022636 root     slurmstepd       0.0  0.0
1022790 phffleck bash             0.0  0.0
1022641 phffleck bash             0.0  0.0
2643993 root     systemd-journal  0.0  0.0
      1 root     systemd          0.0  0.0
1022190 phffleck systemd          0.0  0.0
```
