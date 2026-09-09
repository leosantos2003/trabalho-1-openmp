#include "include/ga.h"

#include <stdio.h>
#include <stdlib.h>

static int config_is_valid(const GAConfig *config) {
    return config->population_size >= 2 &&
           config->bits_per_individual >= 2 &&
           config->generations >= 1 &&
           config->mutation_rate >= 0.0 &&
           config->mutation_rate <= 1.0 &&
           config->seed != 0;
}

int main(int argc, char **argv) {
    GAConfig config = {
        .population_size = 1000,
        .bits_per_individual = 1000,
        .generations = 200,
        .mutation_rate = 0.0,
        .seed = 42,
    };

    if (argc > 1) config.population_size = strtoull(argv[1], NULL, 10);
    if (argc > 2) config.bits_per_individual = strtoull(argv[2], NULL, 10);
    config.mutation_rate = 1.0 / config.bits_per_individual;
    if (argc > 3) config.generations = atoi(argv[3]);
    if (argc > 4) config.mutation_rate = atof(argv[4]);
    if (argc > 5) config.seed = strtoull(argv[5], NULL, 10);

    if (!config_is_valid(&config)) {
        fprintf(stderr, "Uso: %s [populacao] [bits] [geracoes] [mutacao] [seed]\n", argv[0]);
        return 1;
    }

    int global_best;
    double elapsed_seconds;
    if (ga_run(&config, &global_best, &elapsed_seconds) != 0) return 1;

    printf("Melhor fitness: %d/%zu\n", global_best, config.bits_per_individual);
    printf("Tempo: %.6f s\n", elapsed_seconds);
    return 0;
}
