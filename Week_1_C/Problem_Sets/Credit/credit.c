#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get card number from user
    long number = get_long("Number: ");

    // Luhn’s Algorithm checksum
    int sum = 0;
    bool second = false;
    long temp = number;

    while (temp > 0)
    {
        int digit = temp % 10;

        if (second)
        {
            int product = digit * 2;
            sum += product / 10;  // add tens digit (0 or 1)
            sum += product % 10;  // add ones digit
        }
        else
        {
            sum += digit;
        }

        second = !second;
        temp /= 10;
    }

    // If checksum fails, it's invalid
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // Determine length and starting digits
    int length = 0;
    int first_digit = 0;
    int first_two_digits = 0;
    temp = number;

    while (temp > 0)
    {
        if (temp < 10)
        {
            first_digit = temp;
        }
        if (temp >= 10 && temp < 100)
        {
            first_two_digits = temp;
        }

        temp /= 10;
        length++;
    }

    // Check card type
    if (length == 15 && (first_two_digits == 34 || first_two_digits == 37))
    {
        printf("AMEX\n");
    }
    else if (length == 16 && (first_two_digits >= 51 && first_two_digits <= 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((length == 13 || length == 16) && first_digit == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
