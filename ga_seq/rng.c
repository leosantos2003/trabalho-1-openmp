#include "include/rng.h"

/* A sequential execution has one pseudo-random generator state. */
static uint64_t rng_state = 42;

void rng_seed(uint64_t seed) {
    rng_state = seed;
}

uint64_t rng64(void) {
    uint64_t x = rng_state;

    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;

    rng_state = x;
    return x;
}

size_t rng_index(size_t limit) {
    return (size_t)(rng64() % limit);
}

double rng_unit(void) {
    return (rng64() >> 11) * (1.0 / 9007199254740992.0);
}
