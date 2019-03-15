// Problem 587

using System;

namespace _587
{
    class Program
    {

        static double epsilon = 0.000000000000001;
        static int integralSteps = 50000000;

        static void Main(string[] args)
        {

            double lp = 1.0;
            double l = (4.0 - Math.PI) / 4.0;

            int n = 2230; // got to this starting point via a lot of trial-and-error

            double p, al, ar, at;

            while (lp >= 0.001)
            {

                p = getP(n);
                al = 0.5 * n * p * p;
                ar = getRightArea(p, 1.0);
                at = al + ar;

                lp = 1.0 - (at / l);
                Console.WriteLine("{0}, {1}", n, lp);

                n++;

            }

            Console.WriteLine(n - 1);
            Console.ReadLine();

        }

        private static double getP(int n)
        {

            double d = 1.0;
            double x = 0.5;
            double s = 0.1;

            double v1, v2;

            while (true)
            {

                v1 = n * x;
                v2 = 1.0 - Math.Sqrt(1.0 - ((x - 1.0) * (x - 1.0)));
                d = (v1 - v2);
                if (d < 0) d *= -1.0;

                if (d < epsilon) return x;

                if (v1 > v2) x -= s;
                else x += s;

                s *= 0.99;

            }

        }

        private static double getRightArea(double xs, double xe)
        {

            double a = 0.0;
            double s = (xe - xs) / integralSteps;

            double x = xs;

            while (x < xe)
            {
                a += s * (1.0 - Math.Sqrt((x * 2.0) - (x * x)));
                x += s;
            }

            return a;

        }

    }
}
