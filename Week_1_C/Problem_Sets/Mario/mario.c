#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Keep asking until the user enters a positive integer
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0);

    // Build the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print leading spaces
        for (int s = 0; s < height - i; s++)
        {
            printf(" ");
        }

        // Print hashes
        for (int h = 0; h < i; h++)
        {
            printf("#");
        }

        // New line after each row
        printf("\n");
    }
}