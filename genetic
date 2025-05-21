import random

def solve_n_queens_genetic(n, population_size=100, generations=100, mutation_rate=0.1):
    def fitness(chromosome):
        conflicts = 0
        for i in range(n):
            for j in range(i + 1, n):
                if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                    conflicts += 1
        return -conflicts

    def crossover(p1, p2):
        start, end = sorted(random.sample(range(n), 2))
        child = [-1] * n
        child[start:end] = p1[start:end]
        p2_index = 0
        for i in range(n):
            if start <= i < end:
                continue
            while p2[p2_index] in child[start:end]:
                p2_index += 1
            child[i] = p2[p2_index]
            p2_index += 1
        return child

    def mutate(chromosome):
        if random.random() < mutation_rate:
            i, j = random.sample(range(n), 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

    population = [random.sample(range(n), n) for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == 0:
            return population[0]

        next_gen = population[:10]
        while len(next_gen) < population_size:
            parent1 = max(random.sample(population[:50], 5), key=fitness)
            parent2 = max(random.sample(population[:50], 5), key=fitness)
            child = crossover(parent1, parent2)
            next_gen.append(mutate(child))

        population = next_gen

    return []
