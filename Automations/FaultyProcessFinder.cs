using System;
using System.Diagnostics;
using System.Linq;

namespace ProcessMonitor
{
    class Program
    {
        static void Main(string[] args)
        {
            var lastPros = Process.GetProcesses().Select((x) => x.Id).ToList();
            var oldProcessList = Process.GetProcesses();
            while (true)
            {
                var processlist = Process.GetProcesses();

                var currentPros = processlist.Select(x => x.Id).ToList();
                var diff = lastPros.Except(currentPros).ToList();
                Console.ForegroundColor = ConsoleColor.Red;

                var pro = oldProcessList.Where(x => diff.Contains(x.Id)).ToList();

                if (diff.Count == 0)
                {
                    pro = processlist.Where((x) => diff.Contains(x.Id)).ToList();
                    diff = currentPros.Except(lastPros).ToList();
                    Console.ForegroundColor = ConsoleColor.Green;
                    pro = processlist.Where((x) => diff.Contains(x.Id)).ToList();
                }
                foreach (var oldPid in diff)
                {
                    Console.Write("PID {0}", oldPid);
                    try
                    {
                        Console.WriteLine(" name {0}", pro.Where((x) => x.Id == oldPid).ToList()[0].ProcessName);
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine($" Hit exception {e}");
                    }
                }
                if (diff.Count > 0)
                {
                    lastPros = currentPros;
                    oldProcessList = processlist;
                }
                System.Threading.Thread.Sleep(100);
            }
        }
    }
}