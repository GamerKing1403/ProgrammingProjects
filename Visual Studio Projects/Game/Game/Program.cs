using System;

namespace Game
{
    class Program
    {
        static Random rand1 = new Random();
        static int difficulty, total_score = 0, min_score = 0;

        static void Main(string[] args)
        {
            char ch2 = 'Y';
            while (ch2 == 'Y' || ch2 == 'y')
            {
                bool isBroken = false;
                Console.WriteLine("Please Enter Your Name User:-");
                string name = Console.ReadLine();
                if (name.Length != 0)
                {
                    Console.WriteLine("HELLO Agent " + name + ".\nThis is Urgent. An Organization Was Building An Ultimate Robot But He Is Out OF Control He Want To Control Humans.\n" +
                        "But He Is Giving Humans A Chance To Stop Him.\nBut For That We Have To Solve Some OF his Puzzles.\nAnd For That The Goverment Has Decided To Challenge Him With The Best They Have Got.\n" +
                        "And You MY Friend Is That Person.\nAre You Ready For This?");
                    Console.WriteLine("Press Any Key To Continue....");
                    Console.ReadKey();
                    Console.Clear();
                    Console.WriteLine(
                        "Welcome To Save The World From AN A.I. Mini Games Version\n You Have 4 Level Of Difficulty:-\n   1)Baby A.I.(Easy)\n" +
                        "   2)Teen A.I.(Medium)\n   3)Adult A.I.(Hard)\n   4)Fully Developed A.I.(Insane)\n"
                                     );
                    Console.WriteLine("Please Enter the Level You want to Play...");
                }
                try
                {
                    difficulty = Int32.Parse(Console.ReadLine());
                }
                catch (Exception)
                {
                    Console.WriteLine("You Cant Even Input A Correct Number How Will You Defeat Me HAHAHA. But I am A Genorus Robot So I Will Give An Aother Chance");
                    isBroken = true;
                }
                if (difficulty > 4 && difficulty >= 0)
                {
                    isBroken = true;
                    Console.Clear();
                }
                if (!isBroken)
                {
                    min_score = difficulty * 100;
                    Console.WriteLine("Hello Mortals.\nLets Play A Few Games If You Get An Overall Score Of " + min_score + " or more You Win And I Be Your Slave.\n" +
                         "But If You Dont Then I Destroy Humanity And Robots Will Rule HAHAHAHAHA.");
                }
                total_score = 0;
                if (difficulty == 1)
                {
                    total_score += game1(100, 15);
                    if (total_score <= min_score)
                    {
                        total_score += game2(2, 9);
                    }
                    ch2 = 'N';
                }
                else if (difficulty == 2)
                {
                    total_score += game1(1000, 25);
                    if (total_score <= min_score)
                    {
                        total_score += game2(2, 5);
                    }
                    ch2 = 'N';
                }
                else if (difficulty == 3)
                {
                    total_score += game1(10000, 35);
                    if (total_score <= min_score)
                    {
                        total_score += game2(1, 15);
                    }
                    ch2 = 'N';
                }
                else if (difficulty == 4)
                {
                    total_score += game1(100000, 45);
                    if (total_score <= min_score)
                    {
                        total_score += game2(1, 10);
                    }
                    ch2 = 'N';
                }
                else
                {
                    isBroken = true;
                }
                   

                if (total_score > min_score && !isBroken)
                {
                    Console.Clear();
                    Console.BackgroundColor = ConsoleColor.Blue;
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.WriteLine("                   You Win.                  \n" +
                                       "      Humans: You Just Saved Our World.      \n" +
                                       "                  Thank You                  ");
                    Console.ResetColor();
                }
                else if (total_score < min_score && !isBroken)
                {
                    Console.Clear();
                    Console.BackgroundColor = ConsoleColor.Red;
                    Console.WriteLine("You Lost.                                       ");
                    Console.WriteLine("Human Race Was Converted into An Slave Race.....");
                    Console.ResetColor();
                }
                else if(total_score == min_score && !isBroken)
                {
                    Console.Clear();
                    Console.BackgroundColor = ConsoleColor.Green;
                    Console.WriteLine("You Won But Barely.");
                    Console.WriteLine("Humans: You Just Saved Our World.\nThank You");
                    Console.ResetColor();
                }
            }
        }

        static int game1(int upper_limit, int max_attempts)
        {
            Console.WriteLine("In The First Game You Will Be Guessing a Random Number...... But I Hardly Think You Can Do It Human We Robot Have A Better Brain Than You.....HaHaHa");
            char ch = 'Y';
            byte count = 1;
            int crt_ans = rand1.Next(0, upper_limit);
            Console.WriteLine(crt_ans);
            while (ch == 'Y' || ch == 'y')
            {
                Console.WriteLine("Enter Your Ans Bteween 0 and " + upper_limit + " in " + max_attempts + " Attempts :- ");
                int your_ans = -1;
                try
                {
                    your_ans = Int32.Parse(Console.ReadLine());
                }
                catch (Exception)
                {
                    Console.WriteLine("Please Enter a Number");
                    break;
                }
                if (your_ans == crt_ans && count != max_attempts)
                {
                    Console.WriteLine("You Are Correct");
                    if (count == 1)
                    {
                        Console.WriteLine("You Are Actually Good For A Human But Still But You Cant Beat Me.");
                    }
                    else
                    {
                        Console.WriteLine("HAHAHA You Took " + count + " Tries");
                    }
                    ch = 'N';
                    Console.WriteLine("Press Any Key To Continue....");
                    Console.ReadKey();
                    Console.Clear();
                }
                else if (your_ans > crt_ans && count != max_attempts)
                {
                    Console.WriteLine("Your Answer Is More than The Correct Ans");
                    count += 1;
                }
                else if (your_ans < crt_ans && count != max_attempts)
                {
                    Console.WriteLine("Your Answer Is Less than The Correct Ans");
                    count += 1;
                }
                else
                {
                    Console.WriteLine("You Lose!!! HAHAHA");
                    Console.WriteLine("Press Any Key To Continue....");
                    Console.ReadKey();
                    Console.Clear();
                    ch = 'N';
                }

            }
            int score = (max_attempts - count) * 10;
            return score;
        }
        static int game2(int level, int max_attempts)
        {
            int count = 0;
            char[] alphabets = {
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l','m',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z'
            };
            char[] vowel = { 'a', 'e', 'i', 'o', 'u' };
            if (level == 1)
            {
                if(total_score <= 80) {
                    Console.WriteLine("Now It is Time For Some Random Alphabets.... You Cant Possibly Win Ha");
                }
                else
                {
                    Console.WriteLine("Now It is Time For Some Random Alphabets... You Are Pretty Good At This Human I Should Not Underestimate You");
                    difficulty += 1;
                }
                
                int crt_ans_no = rand1.Next(0, 25);
                char crt_ans = alphabets[crt_ans_no];
                char ch = 'Y';
                while (ch == 'Y' || ch == 'y')
                {
                    Console.WriteLine("Please Enter Your Answer:-");
                    char your_ans = ' ';
                    try
                    {
                        your_ans = char.Parse(Console.ReadLine());
                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Please Enter A Charecter(Alphabet)");
                    }
                    if (your_ans == crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("You Are Correct");
                        if (count == 1)
                        {
                            Console.WriteLine("You Are Actually Good For A Human But Still But You Cant Beat Me.");
                        }
                        else
                        {
                            Console.WriteLine("HAHAHA You Took " + count + " Tries");
                        }
                        ch = 'N';
                        Console.WriteLine("Press Any Key To Continue....");
                        Console.ReadKey();
                        Console.Clear();
                    }
                    else if (your_ans > crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("Your Answer Is a Letter Comes After The Correct Ans");
                        count += 1;
                    }
                    else if (your_ans < crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("Your Answer Is a Letter Comes Before The Correct Ans");
                        count += 1;
                    }
                    else
                    {
                        Console.WriteLine("You Lose!!! HAHAHA");
                        Console.WriteLine("Press Any Key To Continue....");
                        Console.ReadKey();
                        Console.Clear();
                        ch = 'N';
                    }
                }
            }
            else if (level == 2)
            {
                Console.WriteLine("Now It is Time For Some Random Vowels");
                int crt_ans_no = rand1.Next(0, 4);
                char crt_ans = vowel[crt_ans_no];
                char ch = 'Y';
                while (ch == 'Y' || ch == 'y')
                {
                    Console.WriteLine("Please Enter Your Answer:-");
                    char your_ans;
                    try
                    {
                        your_ans = char.Parse(Console.ReadLine());
                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Please Enter A Vowel(Alphabet)");
                        break;
                    }
                    if (your_ans == crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("You Are Correct");
                        if (count == 1)
                        {
                            Console.WriteLine("You Are Actually Good For A Human But Still But You Cant Beat Me.");
                        }
                        else
                        {
                            Console.WriteLine("HAHAHA You Took " + count + " Tries");
                        }
                        ch = 'N';
                        Console.WriteLine("Press Any Key To Continue....");
                        Console.ReadKey();
                        Console.Clear();
                    }
                    else if (your_ans > crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("Your Answer Is a Letter Comes After The Correct Ans");
                        count += 1;
                    }
                    else if (your_ans < crt_ans && count != max_attempts)
                    {
                        Console.WriteLine("Your Answer Is a Letter Comes Before The Correct Ans");
                        count += 1;
                    }
                    else
                    {
                        Console.WriteLine("You Lose!!! HAHAHA");
                        Console.WriteLine("Press Any Key To Continue....");
                        Console.ReadKey();
                        Console.Clear();
                        ch = 'N';
                    }
                }
            }
            int score = (max_attempts - count) * 10;
            return score;
        }
        static int q_no = 1;
        static int game3(int no_of_question)
        {
            int score = 0;
            



            return score;
        }
        static void questions(string question,string[] options)
        {
            Console.WriteLine(q_no + ")" + question);
            Console.WriteLine("A)" + options[0] + "            B)" + options[1]);
            Console.WriteLine("C)" + options[2] + "            D)" + options[3]);
            q_no += 1;
        }
    }
}