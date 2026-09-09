# Algoritmo Genético OneMax

O projeto contém duas implementações modulares do Algoritmo Genético para o problema OneMax:

- `ga_seq/`: implementação sequencial;
- `ga_seq_paralelizado/`: implementação com OpenMP na avaliação e na reprodução.

Em ambas, `main.c` é o ponto de entrada. `ga.c` coordena a execução, `population.c` concentra inicialização e fitness, `reproduction.c` implementa seleção, crossover e mutação, e `rng.c` encapsula o gerador pseudoaleatório.

## Compilação e execução

```bash
make -C ga_seq
make -C ga_seq_paralelizado

./ga_seq/ga_seq [populacao] [bits] [geracoes] [mutacao] [seed]
OMP_NUM_THREADS=4 ./ga_seq_paralelizado/ga_seq_paralelizado [populacao] [bits] [geracoes] [mutacao] [seed]
```

Todos os argumentos são opcionais. Os valores padrão são população `1000`, `1000` bits por indivíduo, `200` gerações, mutação `1/bits` e seed `42`.

O arquivo `compile_commands.json` e a configuração em `.vscode/` informam ao IntelliSense do VS Code os diretórios de headers corretos de cada versão.
