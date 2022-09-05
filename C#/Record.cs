public class Cat
{
	public string Name { get; set; }
	public string Breed { get; set; }
	public string Color { get; set; }

	public Cat(string name, string breed, string color)
	{
		Name = name;
		Breed = breed;
		Color = color;
	}
}

Cat cat1 = new Cat("test", "test", "test");
Cat cat2 = new Cat("test", "test", "test");

Console.WriteLine(cat1 == cat2); // False (because it's reference type, not value)

// ------------------------------------------------------------------------------------------------------------------------------------------------

public class Cat
{
	public string Name { get; set; }
	public string Breed { get; set; }
	public string Color { get; set; }

	public Cat(string name, string breed, string color)
	{
		Name = name;
		Breed = breed;
		Color = color;
	}

	public static Boolean operator ==(Cat firstCat, Cat secondCat)
	{
		return firstCat.Name.Equals(secondCat.Name) && firstCat.Breed.Equals(secondCat.Breed) && firstCat.Color.Equals(secondCat.Color);
	}

	public static Boolean operator !=(Cat firstCat, Cat secondCat)
	{
		return !(firstCat == secondCat);
	}

	// and better to write method Equals(), GetHashCode()
}

Cat cat1 = new Cat("test", "test", "test");
Cat cat2 = new Cat("test", "test", "test");

Console.WriteLine(cat1 == cat2); // True

// ------------------------------------------------------------------------------------------------------------------------------------------------

public record Cat(string Name, string Breed, string Color); // code like up, but fileds 'initonly' and we can't to change field's value

Cat cat3 = new Cat("test", "test", "test");
cat3.Name = "new test2" // we can't
cat3 = cat3 with { Name = "new test2" }; // we can change value, but it's create new object in memory

// ------------------------------------------------------------------------------------------------------------------------------------------------

public record Cat(string Name, string Breed, string Color)
{
	public string Name { get; set; } = Name; // create new record, but field Name like just field(not 'initonly')
}

Cat cat4 = new Cat("test", "test", "test");
cat4.Name = "new test";

// ------------------------------------------------------------------------------------------------------------------------------------------------

public record Pet(int Weight); // records like classes can (наследоваться)

public record Cat(string Name, string Breed, string Color, int Weight) : Pet(Weight)
{
	public string Name { get; set; } = Name; // create new record, but field Name like just field(not 'initonly')
}

// ------------------------------------------------------------------------------------------------------------------------------------------------

public record Cat(string Name, string Breed, string Color, int Weight) : IDisposable
{
	public string Name { get; set; } = Name; // create new record, but field Name like just field(not 'initonly')

	public void Dispose()
	{
		Console.WriteLine($"{Name} disposed");
	}
}

