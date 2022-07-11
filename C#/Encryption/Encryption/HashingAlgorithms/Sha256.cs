using System;
using System.Security.Cryptography;
using System.Text;

public class HashPass(string password)
{
  using(var sha256 = SHA256.Create())
  {
    var hashBytes = sha256.ComputeHash(Encoding.UTF8.GerBytes(password));
    var hash = BitConvert.ToString(hasheBytes).Replace("-", "").ToLower();
    
    return hash;
  }
}
