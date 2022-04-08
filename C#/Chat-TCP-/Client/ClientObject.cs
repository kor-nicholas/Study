using System;
using System.IO;
using System.Net.Sockets;
using System.Threading;
using System.Threading.Tasks;

namespace Client
{
    public class ClientObject
    {
        #region Fields

        private string _userName;
        private TcpClient _client;
        private NetworkStream _stream;
        private StreamReader _reader;
        private StreamWriter _writer;

        #endregion
        
        private static void ClearCurrentConsoleLine()
        {
            Console.SetCursorPosition(0, Console.CursorTop - 1);
            int currentLineCursor = Console.CursorTop;
            Console.SetCursorPosition(0, Console.CursorTop);
            Console.Write(new string(' ', Console.WindowWidth)); 
            Console.SetCursorPosition(0, currentLineCursor);
        }
        
        public void Run()
        {
            Connect();
            Task.Run(ReadMessage);
            SendMessage();
        }
        
        private void Connect()
        {
            Console.Write("Enter your name: ");
            _userName = Console.ReadLine();
            
            _client = new TcpClient();
            _client.Connect("127.0.0.1", 8888);
            
            _stream = _client.GetStream();
            _writer = new StreamWriter(_stream);
            _reader = new StreamReader(_stream);
            Console.WriteLine("Connection to server is successful");

            _writer.AutoFlush = true;
            _writer.WriteLine($"{_userName}");

        }

        private void ReadMessage()
        {
            while (_client.Connected)
            {
                string msg = _reader.ReadLine();
                Console.WriteLine(msg);
            }
        }

        private void SendMessage()
        {
            while (_client.Connected)
            {
                string msg = Console.ReadLine();
                ClearCurrentConsoleLine();
            
                if (msg.Contains("exit"))
                {
                    msg = "exit" + _userName;
                    _writer.WriteLine(msg);
                    Thread.Sleep(2000);
                    Finish();
                }
            
                _writer.WriteLine($"{_userName}: " + msg);
            }
        }

        public void Finish()
        {
            Console.WriteLine("Finish");
            if (_stream != null)
            {
                _stream.Close();
            }

            if (_client != null)
            {
                _client.Close();
            }
        }
    }
}