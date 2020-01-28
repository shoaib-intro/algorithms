static int Main(string[] args)
        {

            Console.WriteLine("Domino's Pyramids!");

            int[] Values = new int[] { 3, 4, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5, 6, 8 };
            bool result = DomonoContruction(Values); // Checks Pyramids Contruction
            Console.WriteLine(result ? "YES" : "NO");
            Console.ReadLine();

            return 0;
        }

        private const int DominoLength = 2;

        public static bool DomonoContruction(int[] Values)
        {
            int currentRow = 1; // Starting row 
            int offset = 0; // Values Offset in array
            bool result = true;
            while (result)
            {
                int currentRowLength = currentRow * DominoLength; // calculates length by row * 2
                if (offset + currentRowLength >= Values.Length)
                {
                    break;
                }
                result = CompareValues(Values, offset, currentRowLength);
                offset += currentRowLength;
                currentRow++;
            }
            return result;
        }
        public static bool CompareValues(int[] Values, int offset, int currentRowLength)
        {
            int startofNextRow = offset + currentRowLength;
            int ComparePointofNextRow = startofNextRow + 1;
            for (int i = 0; i < currentRowLength; i++)
            {
                if (Values[offset + i] != Values[ComparePointofNextRow + i])
                {
                    return false;
                }
            }
            
            return true;
        }
