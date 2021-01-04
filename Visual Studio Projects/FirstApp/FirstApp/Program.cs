using System;

namespace FirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello Mortals!Here Is A Challenge For You All Mortals Guess The Number From 0 to 100. I choose");
            Console.WriteLine("Enter Your Answer");
            int first = 0;
            Random rand1 = new Random();
            try
            {
                first = Int32.Parse(Console.ReadLine());
            }
            catch(Exception)
            {
                Console.WriteLine("Please Enter A Number");
            }
            int ran = rand1.Next(0, 100);
            if(first != ran)
            {
                Console.WriteLine("Baam You Are Wrong." +
                    "Press Any Button To Continue...");
                Console.ReadKey();
                Console.Clear();
            }
            else
            {
                Console.WriteLine("Press Any Button To Continue...");
                Console.ReadKey();
                Console.WriteLine("You Just Got Lucky");
            }
            
        }
    }
}
