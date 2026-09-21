# Ambiente de execução dos experimentos

## Registro: antes da coleta VTune

- Data e hora: `2026-09-17T15:04:36-03:00`
- Host: `hype2`
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

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 15:04:36 up 138 days, 14:21,  1 user,  load average: 0.53, 1.10, 1.03`
- `/proc/loadavg`: `0.53 1.10 1.03 1/477 1125962`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       3.1Gi        41Gi       4.7Mi        81Gi       122Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
3611202 node-exp node_exporter    1.6  0.0
1410107 cgroup-+ cgroup_exporter  0.3  0.0
   1057 message+ dbus-daemon      0.0  0.0
    265 root     kcompactd0       0.0  0.0
   1238 root     fail2ban-server  0.0  0.0
1086706 root     kworker/3:0-eve  0.0  0.0
 847665 root     systemd-journal  0.0  0.1
      1 root     systemd          0.0  0.0
1121969 root     kworker/u81:5-r  0.0  0.0
    266 root     kcompactd1       0.0  0.0
```
