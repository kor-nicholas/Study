using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace Server
{
    class Program
    {
        static void Main(string[] args)
        {
            AllServerTasks server = new AllServerTasks();
            server.Start();
            server.Finish();

            
        }
    }
}