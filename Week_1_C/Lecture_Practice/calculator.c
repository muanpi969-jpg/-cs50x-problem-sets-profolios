// calculator_int.c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a = get_int("First integer: ");
    char op = get_char("Operator (+ - * / %%): ");
    int b = get_int("Second integer: ");

    if (op == '+')
    {
        printf("%d\n", a + b);
    }
    else if (op == '-')
    {
        printf("%d\n", a - b);
    }
    else if (op == '*')
    {
        printf("%d\n", a * b);
    }
    else if (op == '/')
    {
        if (b == 0)
        {
            printf("Error: division by zero\n");
            return 1;
        }
        printf("%d\n", a / b);            // integer division
    }
    else if (op == '%')
    {
        if (b == 0)
        {
            printf("Error: modulo by zero\n");
            return 1;
        }
        printf("%d\n", a % b);
    }
    else
    {
        printf("Unknown operator: %c\n", op);
        return 2;
    }

    return 0;
}
