using System;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Выберите действие:");
        Console.WriteLine("1. +");
        Console.WriteLine("2. -");
        Console.WriteLine("3. /");
        Console.WriteLine("4. *");
        string math = Console.ReadLine();

        Console.WriteLine("Введите первое число:");
        int first =  Convert.ToInt32(Console.ReadLine());

         Console.WriteLine("Введите второе число:");
        int second =  Convert.ToInt32(Console.ReadLine());

        if (math == "+")
        {
            int answer = first + second;
            Console.WriteLine("Ответ:" + answer);
        }

        if (math == "-")
        {
            int answer = first - second;
            Console.WriteLine("Ответ:" + answer);
        }

        if (math == "/")
        {
            int answer = first / second;
            Console.WriteLine("Ответ:" + answer);
        }

        if (math == "*")
        {
            int answer = first * second;
            Console.WriteLine("Ответ:" + answer);
        }

    }
}
