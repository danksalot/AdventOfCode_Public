using System.IO;
using System;

class Program
{
    static void Main()
    {
        const int GRID_SIZE = 400;
        bool[,] Grid = new bool[GRID_SIZE, GRID_SIZE];
        int SantaX = GRID_SIZE / 2;
        int SantaY = GRID_SIZE / 2;
        int RobotX = GRID_SIZE / 2;
        int RobotY = GRID_SIZE / 2;
        int Year1Total = 1;
        int Year2Total = 1;
        
        // Record that the initial house has a present already
        Grid[SantaX, SantaY] = true;
        
        using (StreamReader reader = new StreamReader("Input"))
        {
            do
            {
                // Make the move to a new house
                char ch = (char)reader.Read();
                switch(ch)
                {
                    case '^' : SantaY++; break;
                    case 'v' : SantaY--; break;
                    case '>' : SantaX++; break;
                    case '<' : SantaX--; break;
                }
                
                // Only record a new house if it hasn't received a present yet
                if (Grid[SantaX, SantaY] == false)
                {
                    Grid[SantaX, SantaY] = true;
                    Year1Total++;
                }
                
            } while (!reader.EndOfStream);
        }
        
        // Reset values for the next year
        Grid = new bool[GRID_SIZE, GRID_SIZE];
        SantaX = GRID_SIZE / 2;
        SantaY = GRID_SIZE / 2;
        Grid[SantaX, SantaY] = true;
        
        using (StreamReader reader = new StreamReader("Input"))
        {
            do
            {
                // First calculate and record Santa's position
                char SantaChar = (char)reader.Read();
                switch(SantaChar)
                {
                    case '^' : SantaY++; break;
                    case 'v' : SantaY--; break;
                    case '>' : SantaX++; break;
                    case '<' : SantaX--; break;
                }
                
                if (Grid[SantaX, SantaY] == false)
                {
                    Grid[SantaX, SantaY] = true;
                    Year2Total++;
                }
                
                // Then calculate and record the Robot's position
                char RobotChar = (char)reader.Read();
                switch(RobotChar)
                {
                    case '^' : RobotY++; break;
                    case 'v' : RobotY--; break;
                    case '>' : RobotX++; break;
                    case '<' : RobotX--; break;
                }
                
                if (Grid[RobotX, RobotY] == false)
                {
                    Grid[RobotX, RobotY] = true;
                    Year2Total++;
                }
                
            } while (!reader.EndOfStream);
        }
        
        Console.WriteLine("Year 1 houses visited: " + Year1Total);
        Console.WriteLine("Year 2 houses visited: " + Year2Total);
    }
}
