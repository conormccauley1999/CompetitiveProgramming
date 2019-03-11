// Problem 301

using System;

namespace Nim
{

    class Program
    {

        static void Main(string[] args)
        {

            int total = 0;

            int max = Convert.ToInt32(Math.Pow(2.0, 30.0));

            for (int i = 1; i <= max; i++)
            {
                if (((i ^ 2 * i) ^ 3 * i) == 0) total += 1;
                if (i % 10000000 == 0) Console.WriteLine(i);
            }

            Console.WriteLine(total);
            Console.Read();

        }

    }

}
