#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"

#define N 10007

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

node *table[N];
unsigned int word_count = 0;

// HASH FUNCTION
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *word++))
    {
        c = tolower(c);
        hash = ((hash << 5) + hash) + c;
    }

    return hash % N;
}

// LOAD DICTIONARY
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (!file) return false;

    char word[LENGTH + 1];

    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (!new_node) return false;

        strcpy(new_node->word, word);

        int index = hash(word);

        new_node->next = table[index];
        table[index] = new_node;

        word_count++;
    }

    fclose(file);
    return true;
}

// CHECK WORD
bool check(const char *word)
{
    char lower[LENGTH + 1];

    for (int i = 0; word[i]; i++)
        lower[i] = tolower(word[i]);
    lower[strlen(word)] = '\0';

    int index = hash(lower);

    node *cursor = table[index];
    while (cursor)
    {
        if (strcasecmp(cursor->word, lower) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// DICTIONARY SIZE
unsigned int size(void)
{
    return word_count;
}

// UNLOAD MEMORY
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
