using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;

namespace Server
{
    public class AllServerTasks
    {
        #region Fields

        private static int _port = 8888;
        private bool _statusServer;
        private TcpListener _server;
        private List<ClientObject> _clients = new List<ClientObject>();

        #endregion

        public void Start()
        {
            _server = new TcpListener(IPAddress.Any, 8888);
            _server.Start();
            _statusServer = true;
            Console.WriteLine("Server is start. Wait connections ... ");

            Task.Run(ReadKeyToStopServer);
            Listen();
        }
        
        private void ReadKeyToStopServer()
        {
            Console.WriteLine("If you want stop server, just press Enter");

            while (_statusServer)
            {
                ConsoleKey key = Console.ReadKey().Key;
                if (key == ConsoleKey.Enter)
                {
                    Finish();
                }
            }
        }

        private void Listen()
        {
            while (_statusServer)
            {
                TcpClient client = _server.AcceptTcpClient();
                NetworkStream stream = client.GetStream();
                
                StreamReader reader = new StreamReader(stream);
                string userName = reader.ReadLine();
                
                ClientObject clientObject = new ClientObject(userName, client, stream);
                _clients.Add(clientObject);
                
                Console.WriteLine($"{userName} entered in chat");
                BroadcastMessaging($"{userName} entered in chat");

                Task.Run(() => ReadMessages(clientObject));
            }
        }
        
        private void ReadMessages(ClientObject clientObject)
        {
            while (clientObject.Client.Connected)
            {
                StreamReader reader = new StreamReader(clientObject.Stream);
                string msg = reader.ReadLine();
                
                if (msg.Contains("exit"))
                {
                    string userName = msg.Substring(msg.IndexOf("exit") + 4);
                    DisconnectClientForUserName(userName);
                }
                else
                {
                    Console.WriteLine(msg);
                    BroadcastMessaging(msg);
                }
            }
        }

        private void BroadcastMessaging(string msg)
        {
            foreach (var client in _clients)
            {
                StreamWriter writer = new StreamWriter(client.Stream);
                writer.WriteLine(msg);
                writer.Flush();
            }
        }

        private void DisconnectClientForUserName(string userName)
        {
            Console.WriteLine($"{userName}: left the chat");
            BroadcastMessaging($"{userName}: left the chat");
            
            foreach (var client in _clients)
            {
                
                if (client.UserName == userName)
                {
                    client.Stream.Close();
                    client.Client.Close();
                    _clients.Remove(client);
                }
            }
        }

        public void Finish()
        {
            Console.WriteLine("Finis");
            BroadcastMessaging("Server is stop");
            
            foreach (var client in _clients)
            {
                if (client.Stream != null)
                {
                    client.Stream.Close();
                }

                if (client.Client != null)
                {
                    client.Client.Close();
                }
            }
            
            _server.Stop();
            _statusServer = false;
            Console.WriteLine("Server is stop");
            
        }
        
    }
}