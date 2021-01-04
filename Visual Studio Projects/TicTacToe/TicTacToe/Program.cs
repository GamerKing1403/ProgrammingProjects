using System;
using System.Collections.Generic;

namespace TicTacToe
{
    class Program
    {
        static char[,] gameBoard = new char[5, 5] { {' ','|',' ','|',' '},
            {'-', '+', '-', '+', '-'},
            {' ', '|', ' ', '|', ' '},
            {'-', '+', '-', '+', '-'},
            {' ', '|', ' ', '|', ' '}};

        static void Main(string[] args)
        {

            while (true)
            {

                DrawBoard();
                int pos;
                try
                {
                    Console.WriteLine("Please Enter a Number between 1-9 :- ");
                    pos = Int32.Parse(Console.ReadLine());
                    if (pos > 9 || pos < 0)
                    {
                        Console.WriteLine("Please Enter a Number between 1-9 :- ");
                        pos = Int32.Parse(Console.ReadLine());
                    }
                }
                catch (FormatException)
                {
                    Console.WriteLine("Please Enter a Number between 1-9 :- ");
                    pos = Int32.Parse(Console.ReadLine());
                }
                changeBoard(pos, 'X');
            }

        }

        static void changeBoard(int pos, char xOro)
        {

            switch (pos)
            {
                case 1:
                    gameBoard[4, 0] = xOro;
                    break;
                case 2:
                    gameBoard[4, 2] = xOro;
                    break;
                case 3:
                    gameBoard[4, 4] = xOro;
                    break;
                case 4:
                    gameBoard[2, 0] = xOro;
                    break;
                case 5:
                    gameBoard[2, 2] = xOro;
                    break;
                case 6:
                    gameBoard[2, 4] = xOro;
                    break;
                case 7:
                    gameBoard[0, 0] = xOro;
                    break;
                case 8:
                    gameBoard[0, 2] = xOro;
                    break;
                case 9:
                    gameBoard[0, 4] = xOro;
                    break;
                default:
                    break;
            }
        }

        static void DrawBoard()
        {
            Console.Clear();

            for (int i = 0; i < 5; i++)
            {
                Console.Write(" ");
                for (int j = 0; j < 5; j++)
                {
                    Console.Write(gameBoard[i, j] + " ");
                }
                Console.WriteLine();  
            }
        }

    }
}
