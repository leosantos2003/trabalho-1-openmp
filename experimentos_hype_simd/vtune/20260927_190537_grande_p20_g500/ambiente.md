# Ambiente de execução dos experimentos

## Registro: antes da coleta VTune

- Data e hora: `2026-09-27T19:05:37-03:00`
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

### Alocação Slurm

- Job ID: `825314`
- Partição: `hype`
- Nós alocados: `hype2`
- CPUs solicitadas no nó: `40`

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 19:05:37 up 148 days, 18:22,  1 user,  load average: 0.11, 0.26, 0.43`
- `/proc/loadavg`: `0.11 0.26 0.43 1/489 1885376`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       3.6Gi        30Gi       4.7Mi        92Gi       122Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
1885324 phffleck bash             6.2  0.0
3611202 node-exp node_exporter    1.6  0.0
1410107 cgroup-+ cgroup_exporter  0.3  0.0
   1057 message+ dbus-daemon      0.0  0.0
      1 root     systemd          0.0  0.0
 847665 root     systemd-journal  0.0  0.0
   1238 root     fail2ban-server  0.0  0.0
    265 root     kcompactd0       0.0  0.0
1884513 root     kworker/u81:4-n  0.0  0.0
1883918 phffleck bash             0.0  0.0
```

---


## Registro: depois da coleta VTune

- Data e hora: `2026-09-27T19:05:54-03:00`
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

### Alocação Slurm

- Job ID: `825314`
- Partição: `hype`
- Nós alocados: `hype2`
- CPUs solicitadas no nó: `40`

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 19:05:54 up 148 days, 18:23,  1 user,  load average: 0.91, 0.44, 0.49`
- `/proc/loadavg`: `0.91 0.44 0.49 1/490 1885696`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:           125Gi       3.6Gi        30Gi       4.7Mi        92Gi       121Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
3611202 node-exp node_exporter    1.6  0.0
1410107 cgroup-+ cgroup_exporter  0.3  0.0
   1057 message+ dbus-daemon      0.0  0.0
1885308 phffleck bash             0.0  0.0
1884514 root     kworker/u81:6-r  0.0  0.0
1884513 root     kworker/u81:4-r  0.0  0.0
      1 root     systemd          0.0  0.0
 847665 root     systemd-journal  0.0  0.0
   1238 root     fail2ban-server  0.0  0.0
    265 root     kcompactd0       0.0  0.0
```
