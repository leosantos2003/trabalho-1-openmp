# Ambiente de execução dos experimentos

## Registro: antes da coleta

- Data e hora: `2026-09-17T09:00:13-03:00`
- Host: `bali2`
- Sistema operacional: Debian GNU/Linux 12 (bookworm)
- Kernel: `Linux 6.1.0-45-amd64 x86_64 GNU/Linux`

### Processador

- Modelo: Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz
- Núcleos físicos: 16
- CPUs lógicas totais: 32
- CPUs lógicas disponíveis ao processo: 32
- Soquetes: 2
- Núcleos por soquete: 8
- Threads por núcleo: 2

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 09:00:13 up 138 days,  8:19,  4 users,  load average: 0.12, 0.08, 0.03`
- `/proc/loadavg`: `0.12 0.08 0.03 1/456 3137089`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:            31Gi       1.3Gi        12Gi       5.0Mi        17Gi        30Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
3137091 lrsantos ps               100  0.0
1957513 node-exp node_exporter    1.6  0.2
2677333 cgroup-+ cgroup_exporter  0.6  0.1
    225 root     kswapd1          0.0  0.0
    999 message+ dbus-daemon      0.0  0.0
    224 root     kswapd0          0.0  0.0
   1001 root     fail2ban-server  0.0  0.1
      1 root     systemd          0.0  0.0
     16 root     rcu_preempt      0.0  0.0
3048213 root     kworker/20:0-ev  0.0  0.0
```

---


## Registro: depois da coleta

- Data e hora: `2026-09-17T09:04:34-03:00`
- Host: `bali2`
- Sistema operacional: Debian GNU/Linux 12 (bookworm)
- Kernel: `Linux 6.1.0-45-amd64 x86_64 GNU/Linux`

### Processador

- Modelo: Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz
- Núcleos físicos: 16
- CPUs lógicas totais: 32
- CPUs lógicas disponíveis ao processo: 32
- Soquetes: 2
- Núcleos por soquete: 8
- Threads por núcleo: 2

### Compilação

- Compilador: `gcc (Debian 12.2.0-14+deb12u1) 12.2.0`
- Flags sequenciais: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -Iinclude`
- Flags paralelas: `-O2 -g -std=c11 -Wall -Wextra -Wpedantic -fopenmp -Iinclude`
- Flags de ligação OpenMP: `-fopenmp`
- Afinidade usada pelo coletor: `OMP_DYNAMIC=FALSE`, `OMP_PROC_BIND=true`, `OMP_PLACES=cores`

### Carga no momento do registro

- Uptime e média de carga: ` 09:04:34 up 138 days,  8:23,  4 users,  load average: 4.28, 1.49, 0.58`
- `/proc/loadavg`: `4.28 1.49 0.58 1/452 3140436`

Memória:

```text
               total        used        free      shared  buff/cache   available
Mem:            31Gi       1.3Gi        12Gi       5.0Mi        17Gi        30Gi
Swap:             0B          0B          0B
```

Processos com maior uso de CPU no instante do registro:

```text
PID      USUÁRIO         PROCESSO                 %CPU   %MEM
3140438 lrsantos ps               100  0.0
1957513 node-exp node_exporter    1.6  0.2
2677333 cgroup-+ cgroup_exporter  0.6  0.1
3137030 lrsantos bash             0.1  0.0
    225 root     kswapd1          0.0  0.0
    999 message+ dbus-daemon      0.0  0.0
    224 root     kswapd0          0.0  0.0
   1001 root     fail2ban-server  0.0  0.1
      1 root     systemd          0.0  0.0
     16 root     rcu_preempt      0.0  0.0
```
