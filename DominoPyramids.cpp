#include <iostream>
using namespace std;
	
	// function declaration 
	bool IsDominoPyramidValid(int values[]);
	bool CheckValuesOnRowAgainstRowBelow(int values[], int startOfCurrentRow, int currentRowLength);
	

int main()
{
	    		int values[] =  { 3, 4, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6,9,1,2,3,4,5,6,8 };
                bool result = IsDominoPyramidValid(values);
            
                cout <<endl<< result? "Yes" : "No";
				return 0;
}



   
                 
       bool IsDominoPyramidValid(int values[])
        {
            int arrayLength = sizeof(values); // returns length 
			int DominoLength = 2;
            int offset = 0;
            int currentRow = 1; // Start of row
            bool result = true;
            while (result)
            {
                int currentRowLength = currentRow * DominoLength; //2

                // Avoid checking final row: there is no row below it
                if (offset + currentRowLength >= arrayLength)
                {
                	// loop terminate
                    break;
                }

                result = CheckValuesOnRowAgainstRowBelow(values, offset, currentRowLength);
                offset += currentRowLength;
                currentRow++;
            }

            return result;
        }
       bool CheckValuesOnRowAgainstRowBelow(int values[], int startOfCurrentRow, int currentRowLength)
        {
            int startOfNextRow = startOfCurrentRow + currentRowLength;
            int comparablePointOnNextRow = startOfNextRow + 1;
            for (int i = 0; i < currentRowLength; i++)
            {
                if (values[startOfCurrentRow + i] != values[comparablePointOnNextRow + i])
                {
                    return false;
                }

              
            }

            return true;
        }
         
