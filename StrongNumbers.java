public class StrongNumbers
{
    // Function to calculate the factorial of a number
    public static int calculateFactorial(int n)
    {
        int fact = 1;
        for (int i = 1; i <= n; i++)
        {
            fact *= i;
        }
        return fact;
    }

    // Function to check if a number is a strong number
    public static boolean isStrongNumber(int number)
    {
        int originalNumber = number;
        int sumOfFactorials = 0;
        int tempNumber = number;

        while (tempNumber > 0)
        {
            int digit = tempNumber % 10;
            sumOfFactorials += calculateFactorial(digit);
            tempNumber /= 10;
        }

        return sumOfFactorials == originalNumber;
    }

    public static void main(String[] args)
    {
        System.out.println("Strong numbers from 1 to 5000 are:");
        for (int i = 1; i <= 5000; i++)
        {
            if (isStrongNumber(i))
            {
                System.out.println(i);
            }
        }
    }
}