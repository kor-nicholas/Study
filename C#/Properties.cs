using System;

namespace Property
{
    public class Properties
    {
        // We can just use in object -> object.X = 10; Console.WriteLine(object.X);
        // Not use Get and Set
        private int _x;
        
        public int X
        {
            get
            {
                return _x;
            }
            set
            {
                if ((value < 0) || (value > 5))
                {
                    throw new ArgumentOutOfRangeException();
                }
                _x = value;
            }
        }
        
        public int y { get; set; } // just get and set 
                
        /*
            private int _y;
        
            public int Y
            {
                get
                {
                    return _y;
                }
                set
                {
                    _y = value;
                }
            }
            */
    }
}