# Ambiente de execução dos experimentos

## Registro: antes da coleta VTune

- Data e hora: `2026-09-27T18:56:52-03:00`
- Host: `hype5`
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

- Job ID: `825309`
- Partição: `hype`
- Nós alocados: `hype5`
- CPUs solicitadas no nó: `40`

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 18:56:52 up 148 days, 18:14,  1 user,  load average: 0.36, 0.66, 0.41`
- `/proc/loadavg`: `0.36 0.66 0.41 1/540 576807`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       3.4Gi        54Gi       4.8Mi        69Gi       122Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
 576809 phffleck ps               100  0.0
1204885 node-exp node_exporter    1.8  0.0
 576730 phffleck bash             1.4  0.0
1885733 cgroup-+ cgroup_exporter  0.3  0.0
1204932 nvidia-+ nvidia_gpu_expo  0.1  0.0
   1130 message+ dbus-daemon      0.0  0.0
   1196 root     irq/204-nvidia   0.0  0.0
   1593 root     irq/205-nvidia   0.0  0.0
   1132 root     fail2ban-server  0.0  0.0
      1 root     systemd          0.0  0.0
```
