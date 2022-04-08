using System;
using Encryption.Interfaces;

namespace Encryption.HashingAlgorithms
{
    /// <summary>
    /// Class with methods to Encode and Decode messages use Base64
    /// </summary>
    public class Base64HashingAlgorithm : IHashingAlgorithm
    {
        public string Encode(string msg)
        {
            byte[] bytes = System.Text.ASCIIEncoding.ASCII.GetBytes(msg);

            return Convert.ToBase64String(bytes);
        }
        
        public string Decode(string encodedMessage)
        {
            byte[] bytes = Convert.FromBase64String(encodedMessage);

            return System.Text.ASCIIEncoding.ASCII.GetString(bytes);
        }
    }
}