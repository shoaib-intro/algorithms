            int n = 0;
            int len = n < 10 ? 0 : 1;
            while (n >= 10)
            {
                len = len * 10;
                n /= 10;
            }
            Console.WriteLine("Ten multiple is \t"+len);
            Console.ReadLine();
