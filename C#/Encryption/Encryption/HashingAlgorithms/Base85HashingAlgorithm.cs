using Encryption.Interfaces;
using SimpleBase;

namespace Encryption.HashingAlgorithms
{
    /// <summary>
    /// Class with methods to Encode and Decode messages use Base85
    /// </summary>
    public class Base85HashingAlgorithm : IHashingAlgorithm
    {
        public string Encode(string msg)
        {
            byte[] bytes = System.Text.ASCIIEncoding.ASCII.GetBytes(msg);

            return Base85.Ascii85.Encode(bytes);
        }

        public string Decode(string encodedMessage)
        {
            var bytes = Base85.Ascii85.Decode(encodedMessage);

            return System.Text.ASCIIEncoding.ASCII.GetString(bytes);
        }
    }
}