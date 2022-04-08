using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Net.Sockets;
using System.Security.Cryptography;

namespace MyList_
{
    public class MyList<T> : IEnumerable<T>
    {
        #region Fields

        private T[] _array = Array.Empty<T>(); // Once create array and return link to array

        public int Length { get; set; }

        #endregion

        #region Methods

        /// <summary>
        /// To []
        /// </summary>
        /// <param name="index"></param>
        /// <exception cref="IndexOutOfRangeException"></exception>
        private void CheckIndex(int index)
        {
            if (index < 0 || index >= Length)
            {
                throw new IndexOutOfRangeException(nameof(index)); // nameof - return class name (int)
            }
        }

        /// <summary>
        /// Add object to array
        /// </summary>
        /// <param name="value"></param>
        public void Add(T value)
        {
            Length = _array.Length + 1;
            var newArray = new T[Length];

            for (int i = 0; i < _array.Length; i++)
                newArray[i] = _array[i];

            newArray[_array.Length] = value;
            _array = newArray;
        }

        /// <summary>
        /// Remove object from array for object
        /// </summary>
        public void Remove(T item)
        {
            int index = IndexOf(item);

            if (index >= 0)
                RemoveAt(index);
        }

        /// <summary>
        /// Remove object from array for index
        /// </summary>
        /// <param name="index"></param>
        public void RemoveAt(int index)
        {
            if (index < 0 || index >= Length)
                throw new ArgumentOutOfRangeException();

            Length = _array.Length - 1;
            var newArray = new T[Length];
            Console.WriteLine($"Length: {Length}\nIndex = {index}");

            for (int i = 0; i < index; i++)
                newArray[i] = _array[i];

            for (int i = index; i < Length; i++)
                newArray[i] = _array[i + 1];

            _array = new T[Length];

            for (int i = 0; i < Length; i++)
                _array[i] = newArray[i];
        }

        /// <summary>
        /// Get index for object
        /// </summary>
        /// <param name="item"></param>
        public int IndexOf(T item)
        {
            for (int i = 0; i < _array.Length; i++)
                if (Equals(_array[i], item))
                    return i;

            return -1;
        }

        #endregion

        #region Operator

        /// <summary>
        /// []
        /// </summary>
        /// <param name="index"></param>
        public T this[int index]
        {
            get
            {
                CheckIndex(index);
                return _array[index];
            }
            set
            {
                CheckIndex(index);
                _array[index] = value;
            }
        }

        #endregion

        #region IEnumerable

        public IEnumerator<T> GetEnumerator()
        {
            return ((IEnumerable<T>) _array).GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return _array.GetEnumerator();
        }

        #endregion

        public override string ToString()
        {
            string strToOutput = "[";

            for (int i = 0; i < Length; i++)
            {
                strToOutput += _array[i].ToString();

                if (i < Length - 1)
                    strToOutput += ", ";
            }

            strToOutput += "]";

            return strToOutput;
        }
    }

    #region Person

    public class Person
    {
        private int Id { get; set; }
        private long ChatId { get; set; }
        private string UserName { get; set; }
        private string Phone { get; set; }
        private string Address { get; set; }
        private int OrderId { get; set; }

        public Person()
        {
            Id = 0;
            ChatId = 0;
            UserName = "";
            Phone = "";
            Address = "";
            OrderId = 0;
        }

        public int GetId()
        {
            return Id;
        }

        public void SetId(int id)
        {
            Id = id;
        }

        public long GetChatId()
        {
            return ChatId;
        }

        public void SetChatId(long chatId)
        {
            ChatId = chatId;
        }

        public string GetUserName()
        {
            return UserName;
        }

        public void SetUserName(string userName)
        {
            UserName = userName;
        }

        public string GetPhone()
        {
            return Phone;
        }

        public void SetPhone(string phone)
        {
            Phone = phone;
        }

        public string GetAddress()
        {
            return Address;
        }

        public void SetAddress(string adderess)
        {
            Address = adderess;
        }

        public int GetOrderId()
        {
            return OrderId;
        }

        public void SetOrderId(int orderId)
        {
            OrderId = orderId;
        }
    }

    public class BasePerson
    {
        public static MyList<Person> persons = new MyList<Person>();
    }

    #endregion

    #region Product

    public class Product
    {
        private int Id { get; set; }
        private string Name { get; set; }
        private string Description { get; set; }
        private int Prise { get; set; }
        private string PhotoId { get; set; }

        public Product(int id, string name, string description, int prise, string photoId)
        {
            Id = id;
            Name = name;
            Description = description;
            Prise = prise;
            PhotoId = photoId;
        }

        public Product()
        {
            Id = 0;
            Name = "";
            Description = "";
            Prise = 0;
            PhotoId = "";
        }

        public void SetName(string name)
        {
            Name = name;
        }

        public string GetName()
        {
            return Name;
        }

        public void SetDescription(string description)
        {
            Description = description;
        }

        public string GetDescription()
        {
            return Description;
        }

        public void SetPrise(int prise)
        {
            Prise = prise;
        }

        public int GetPrise()
        {
            return Prise;
        }

        public void SetPhotoId(string photoId)
        {
            PhotoId = photoId;
        }

        public string GetPhotoId()
        {
            return PhotoId;
        }

        public int GetId()
        {
            return Id;
        }

        public void SetId(int id)
        {
            Id = id;
        }
    }

    public class BaseProduct
    {
        public static MyList<Product> products = new MyList<Product>();

        public static Product GetProductForId(int id)
        {
            Product localProduct = new Product();
            
            foreach (var product in products)
                if (product.GetId() == id)
                    localProduct = product;

            return localProduct;
        }
    }

    #endregion

    #region Order

    public class Order
    {
        private int Id { get; }
        private int Prise { get; set; }
        
        private static int Profit { get; set; }

        public Order(int id, int prise)
        {
            Id = id;
            Prise = prise;
            Profit += prise;
        }

        public int GetPrise()
        {
            return Prise;
        }

        public int GetProfit()
        {
            return Profit;
        }
    }

    public class BaseOrder
    {
        public static MyList<Order> orders = new MyList<Order>();
    }

    #endregion
}