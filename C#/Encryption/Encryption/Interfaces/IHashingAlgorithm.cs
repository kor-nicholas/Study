namespace Encryption.Interfaces
{
    /// <summary>
    /// Interface to hashing algorithm (Base64, Base85, ... ). Default: Base64
    /// </summary>
    public interface IHashingAlgorithm
    {
        string Encode(string msg);
        string Decode(string encryptedMessage);
    }
}