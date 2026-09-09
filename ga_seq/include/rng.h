#ifndef RNG_H
#define RNG_H

#include <stddef.h>
#include <stdint.h>

void rng_seed(uint64_t seed);
uint64_t rng64(void);
size_t rng_index(size_t limit);
double rng_unit(void);

#endif
