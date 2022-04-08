using System.IO;
using System.Net.Sockets;

namespace Server
{
    public class ClientObject
    {
        #region Fields

        public string UserName { get; }
        public TcpClient Client { get; }
        public NetworkStream Stream { get; }

        #endregion

        #region Constructor

        public ClientObject(string userName, TcpClient client, NetworkStream stream)
        {
            this.UserName = userName;
            this.Client = client;
            this.Stream = stream;
        }

        #endregion
        
    }
}