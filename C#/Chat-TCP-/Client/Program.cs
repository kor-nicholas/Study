using System;
using System.IO;
using System.Net;
using System.Net.Sockets;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            ClientObject client = new ClientObject();
            client.Run(); 
            client.Finish();
        }
    }
}