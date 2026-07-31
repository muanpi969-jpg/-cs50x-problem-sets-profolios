#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GENERATIONS 3
#define INDENT_LENGTH 4

typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

person *create_family(int generations);
void free_family(person *p);
void print_family(person *p, int generation);
char random_allele(void);

int main(void)
{
    srand(time(0));

    person *p = create_family(GENERATIONS);

    print_family(p, 0);

    free_family(p);
}

// Create family recursively
person *create_family(int generations)
{
    person *new_person = malloc(sizeof(person));

    if (generations > 1)
    {
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        new_person->parents[0] = parent0;
        new_person->parents[1] = parent1;

        new_person->alleles[0] = parent0->alleles[rand() % 2];
        new_person->alleles[1] = parent1->alleles[rand() % 2];
    }
    else
    {
        new_person->parents[0] = NULL;
        new_person->parents[1] = NULL;

        new_person->alleles[0] = random_allele();
        new_person->alleles[1] = random_allele();
    }

    return new_person;
}

// Free memory
void free_family(person *p)
{
    if (p == NULL)
        return;

    free_family(p->parents[0]);
    free_family(p->parents[1]);
    free(p);
}

// Print family tree
void print_family(person *p, int generation)
{
    if (p == NULL)
        return;

    for (int i = 0; i < generation * INDENT_LENGTH; i++)
        printf(" ");

    if (generation == 0)
        printf("Child (Gen %i): %c%c\n", generation, p->alleles[0], p->alleles[1]);
    else if (generation == 1)
        printf("Parent (Gen %i): %c%c\n", generation, p->alleles[0], p->alleles[1]);
    else
        printf("Grandparent (Gen %i): %c%c\n", generation, p->alleles[0], p->alleles[1]);

    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Random allele
char random_allele(void)
{
    int r = rand() % 3;
    if (r == 0) return 'A';
    if (r == 1) return 'B';
    return 'O';
}
