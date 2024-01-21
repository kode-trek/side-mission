using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace boy_girl
{
    class Program
    {
        static void Main(string[] args)
        {
            string name;
       

            Console.Write("Enter Name: ");
            name = Console.ReadLine();

            //Print a blank line                          
            Console.WriteLine();

            

            string str;
            str = name;
            int Counter = 0;
            foreach (char myCahr in str)
            {
                
                if (
                       myCahr.ToString().ToUpper() == "A" 
                    || myCahr.ToString().ToUpper() == "E" 
                    || myCahr.ToString().ToUpper() == "I"
                    || myCahr.ToString().ToUpper() == "O"
                    || myCahr.ToString().ToUpper() == "U"
                    )
                    Counter = Counter + 1;
            }

            //Show the details you typed                  
            Console.WriteLine("Name is ** {0}. ** & Counter Is: {1}", name, Counter);

            string BoyOrGirl;
            if (Counter % 2 == 0)
                BoyOrGirl = "Girl";
            else
                BoyOrGirl = "Boy";


            Console.WriteLine(BoyOrGirl);
            //Print a blank line                          
            Console.WriteLine();
            Console.Write("Press Any Key To Exit ");
            Console.ReadLine();
        }
    }
}
