#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long amount = 1;

    while (true)
    {
        char c = get_char("Here's $%li. Double it and give it to the next person? ", amount);

        if (c == 'y' || c == 'Y')
        {
            amount *= 2;
        }
        else
        {
            break;
        }
    }

    printf("Here's $%li.\n", amount);
}
