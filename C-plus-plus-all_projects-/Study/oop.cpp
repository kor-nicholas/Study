#include <iostream>
#include <string>
#include <memory>

using namespace std;

//-------------------------------------------------------- Основы классов -----------------------------------------------------------------

// Прототипы классов
class Point;
class Point2;

// a = this; b = other; a - первый объект; b - второй объект;
class Point
{
private:
	int x;
	int y;

public:

	static int Count; // static поле - поле одинаковое для всех объектов (если один меняет его, оно меняется и дл всех)
	// Присваивается значение static полю вне класса (int Point::Count = 0)

	// Конструктор
	Point()
	{
		cout << "Конструктор -> " << this << endl;
		srand(time(nullptr));
		x = rand() % 10;
		y = rand() % 10;
	}

	Point(int valueX, int valueY)
	{
		cout << "Конструктор -> " << this << endl;
		x = valueX;
		y = valueY;
	}

	Point(const Point& other)
	{
		cout << "Конструктор копирования " << this << endl;
		this->x = other.x;
		this->y = other.y;
	}

	// Операторы
	Point& operator = (const Point& other)
	{
		this->x = other.x;
		this->y = other.y;

		return *this;
	}

	Point operator + (const Point& other)
	{
		Point temp;

		temp.x = this->x + other.x;
		temp.y = this->y + other.y;

		return temp;
	}

	Point operator - (const Point& other)
	{
		Point temp;

		temp.x = this->x - other.x;
		temp.y = this->y - other.y;

		return temp;
	}

	bool operator == (const Point& other)
	{
		return this->x == other.x && this->y == other.y;
	}

	bool operator != (const Point& other)
	{
		return this->x != other.x && this->y != other.y;
	}

	Point& operator ++ ()
	{
		this->x++;
		this->y++;

		return *this;
	}

	Point& operator ++ (int value)
	{
		Point temp;

		this->x++;
		this->y++;

		return temp;
	}

	Point& operator -- ()
	{
		this->x--;
		this->y--;

		return *this;
	}

	Point& operator -- (int value)
	{
		Point temp;

		this->x--;
		this->y--;

		return temp;
	}

	void Print();

	// Деструктор
	~Point()
	{
		cout << "Деструктор -> " << this << endl;
	}

	friend void printMessage(const Point& point);
};

int Point::Count = 0; // присваивание значения static полю

// Вынос вне класса
void Point::Print()
{
	cout << "X = " << Point::x << "\tY = " << Point::y << endl;
}

Point::Point()
{
	// Конструктор вне класа
}
Point::~Point()
{
	// Деструктор вне класса
}

// Дружественная функция класса Point
void printMessage(const Point& point)
{
	cout << "X = " << point.x << "\nY = " << point.y << endl;
}

// Дружественные методы класса
class Human
{
public:
	void TakeApple(Apple& apple);
	void EatApple(Apple& apple);
};

class Apple
{
private:
	int weight;
	string color;

	friend void Human::TakeApple(Apple& apple);

public:
	Apple(int weight, string color)
	{
		this->weight = weight;
		this->color = color;
	}
};

void Human::TakeApple(Apple& apple)
{
	// В apple есть доступ к private полям, так как это дружественный метод Apple класа
	apple.weight;
	apple.color;
}

void Human::EatApple(Apple& apple)
{
	// В apple нету доступ к private полям, так как это не дружественный метод Apple класа
}

// Дружественные классы (класс Human1 может получить доступ к любому полю и методу класса Apple1)
class Human1
{
public:
	void TakeApple1(Apple1& apple1);
	void EatApple1(Apple1& apple1);
};

class Apple1
{
	friend Human1;

private:
	int weight;
	string color;

public:
	Apple1(int weight, string color)
	{
		this->weight = weight;
		this->color = color;
	}
};

void Human1::TakeApple1(Apple1& apple1)
{
	// В apple1 есть доступ к private полям, так как это дружественный метод Apple1 класа
	apple1.weight;
	apple1.color;
}

void Human1::EatApple1(Apple1& apple1)
{
	// В apple1 есть доступ к private полям, так как это дружественный метод Apple1 класа
	apple1.weight;
	apple1.color;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Генератор ID на тему static полей и static методов
// В static методах нельзя использовать this, так как static - отдельно один для всех + можно работать только с static полями
class GenerateID
{
private:
	int ID;
	static int Count;

public:
	GenerateID()
	{
		Count++;
		ID = Count;
	}

	int GetID()
	{
		return ID;
	}

	static int GetCount()
	{
		return Count;
	}

	// Для того чтобы работать с не static полями в static методах, нужно просто передать в метод ссылку на объект с которым хотим работать
	static void ChangeCount(GenerateID& generateId, int newCount)
	{
		generateId.Count = newCount;
	}
};

int GenerateID::Count = 0;

// Вложенные классы
class Image
{
public:

	void GetImageInfo()
	{
		cout << "ImageInfo (r,g,b) : " << endl;
		for (int i = 0; i < LENGTH; i++)
		{
			cout << "№ " << i + 1 << " " << pixelsArr[i].GetInfo() << endl;
		}
	}

private:

	class Pixel
	{
	public:
		Pixel(int r, int g, int b)
		{
			this->r = r;
			this->g = g;
			this->b = b;
		}

		string GetInfo()
		{
			return "Pixel: r = " + to_string(r) + " g = " + to_string(g) + " b = " + to_string(b);
		}

	private:
		int r;
		int g;
		int b;
	};

	static const int LENGTH = 3;

	Pixel pixelsArr[LENGTH]
	{
		Pixel(rand() % 255,rand() % 255,rand() % 255),
		Pixel(rand() % 255, rand() % 255, rand() % 255),
		Pixel(rand() % 255, rand() % 255, rand() % 255)
	};
};

//-----------------------------------------------------------------------------------------------------------------------------------------

// Статический массив объектов (для передачи в функцию -> Image & arr)
Image imagesarr[length];

// Динамический массив объектов (для передачи в функцию -> Image * arr)
Image* imagearr = new Image[length];
delete[] imagearr;

//-----------------------------------------------------------------------------------------------------------------------------------------

// Агрегация и композиция (отношения между классами)
// Агрегация - объект класса, можно использовать в любом другом классе
// Композиция - объект класса, можно использовать только внутри определенного класса

// Композиция (человека без мозга не существует и он не может думать без него)
class Human
{
public:
	void Think()
	{
		brain.Think();
	}

private:
	class Brain
	{
	public:
		void Think()
		{
			cout << "Я думаю (мозг) " << endl;
		}
	};
	Brain brain;
};

// Агрегация (класс Cap можно использовать через объект в любом классе : Human либо Maniken)

class Cap
{
public:
	string GetColor()
	{
		return color;
	}

private:
	string color = "green";
};

class Human
{
public:
	void Think()
	{
		brain.Think();
	}

	// inspect - посмотреть
	void InspectCapOnHuman()
	{
		cout << "Кепка на человеке " << cap.GetColor() << " цвета" << endl;
	}

private:
	class Brain
	{
	public:
		void Think()
		{
			cout << "Я думаю (мозг) " << endl;
		}
	};
	Brain brain;
	Cap cap;
};

class Maniken
{
public:
	void InspectCapOnManiken()
	{
		cout << "Кепка на маникене " << cap.GetColor() << " цвета" << endl;
	}

private:
	Cap cap;
};

//----------------------------------------------------- Наследование ----------------------------------------------------------------------

// Базовый(родительський) класс - класс, от которого наследуем свойства и методы 
// Производный(дочерний) класс - класс, который мы унаследовали от родительського (в который мы можем что-то добавлять)

// Родительський класс - Human (так как студенты и профессора - все люди)
// Дочерные классы - Student и Professor (они унаследовали себе качества человека, то есть стали людьми :) )

class Human
{
public:
	string GetName()
	{
		return name;
	}

	void SetName(string name)
	{
		this->name = name;
	}

private:
	string name;
};

class Student : public Human
{
private:
	string group;
};

class Professor : public Human
{
	string object; // предмет, который ведет профессор
};

//-----------------------------------------------------------------------------------------------------------------------------------------

// Модификаторы доступа при наследовании (спецификаторы)
// Таблица изминения модификаторов доступа при наследовании -> https://yapx.ru/v/KkOXJ (чаще всего используют public)
// Методы так же наследуются как и свойства, чтобы было меньше кода, пример будет показан ток на свойствах

class A
{
	// доступные всем (и следующему классу при наследовании и объекту через точку)
public:
	string msgOne = "Сообщкние один";

	// не доступны никому (ни следующему классу, ни объекту через точку), доступен только в классе А
private:
	string msgTwo = "Сообщение два";

	// доступен следующему классу, но не доступен объекту через точку
protected:
	string msgThree = "Сообщение три";
};

// При изминение модефикатора доступа пр  наследовании, все работает за таблицей (public - ничего не меняет)
class B : public A
{
	void print()
	{
		cout << msgOne << endl << msgThree << endl; // только 1 и 3 доступные
	}
};

//-----------------------------------------------------------------------------------------------------------------------------------------

// Порядок вызова конструкторов классов при наследовании
class A
{
public:
	A()
	{
		cout << "Вызвался конструктор класса А" << endl;
	}
};

class B : public A
{
public:
	B()
	{
		cout << "Вызвался конструктор класса B" << endl;
	}
};

class C : public B
{
public:
	C()
	{
		cout << "Вызвался конструктор класса C" << endl;
	}
};
// main : C value; - объект класса С
// Так как класс, унаследует класс B, то он не может создаться, пока не сделается класс B (так же класс B без класса A)
// По-этому сначала вызывается конструктор класса A, потом класса B, потом класса C

// Порядок вызова деструкторов классов при наследовании
class A
{
public:
	~A()
	{
		cout << "Вызвался деструктор класса А" << endl;
	}
};

class B : public A
{
public:
	~B()
	{
		cout << "Вызвался деструктор класса B" << endl;
	}
};

class C : public B
{
public:
	~C()
	{
		cout << "Вызвался деструктор класса C" << endl;
	}
};
// Деструкторы вызываются всегда в обратном порядке, по-этому сначала вызывается деструктор класса C, потом B, потом A и объект удаляется

//-----------------------------------------------------------------------------------------------------------------------------------------

// Порядок вызова конструкторов базового (родительського) класса
class A
{
public:
	A()
	{
		cout << "Вызваля конструктор по-умолчанию класса А" << endl;
	}
	A(string msg)
	{
		cout << "Вызвался перегружен конструктор с сообщением : " << msg << " , класса А" << endl;
	}
};

class B : public A
{
public:
	B() :A("сообщение") // тут можно выбирать конструктор базового (родительського) класса
	{
		cout << "Вызвался конструктор по-умолчанию класса B" << endl;
	}
};

//-----------------------------------------------------------------------------------------------------------------------------------------

// Полиморфизм + виртуальные функции (virtual, override) -> переопределение метода в классе наследнике (дочерном) классе + 
// по ссылке от базового (родительського) класса можно в объекте вызывать любой переопределенный метод дочерного класса

// virtual - делает метод виртуальным, чтобы можно было переопределять в дочерном классе
// override - проверяет чтобы сигнатура метода была одинакова (тип значения, имя, параметры были такими же как у базового(родительського) класса)

class Gun
{
public:
	virtual void Shoot()
	{
		cout << "Bang!" << endl;
	}
};

class SubmachineGun : public Gun // SubmachineGun - пулемет
{
public:
	void Shoot() override
	{
		cout << "Bang! Bang! Bang!" << endl;
	}
};

class Bazuka : public Gun
{
	void Shoot() override
	{
		cout << "Babax" << endl;
	}
};

class Player
{
public:
	void Shoot(Gun * gun)
	{
		gun->Shoot();
	}
};

int main()
{
	setlocale(LC_ALL, "ru");

	Gun gun;
	SubmachineGun machineGun;
	Bazuka bazuka;

	Player player;
	player.Shoot(&gun); // -> Bang!
	player.Shoot(&machineGun); // -> Bang! Bang! B1ng!
	player.Shoot(&bazuka); // -> Babax!

	return 0;
}

// Абстрактные классы - класс с чисто виртуальными функциями (виртуальные функции без реализации, объекты таких классов не создаются)
// в основном для прототипов виртуальных функций в следующих дочерных классов
// Абстактные классы создаются для работы с их наследниками

class Weapon // weapon - оружие
{
public:
	virtual void Shoot() = 0; // чисто виртуальный метод
	void Foo() // так же могут быть свои методы, которыми смогут пользоваться другие классы, а объект нельзя создать если есть чисто виртуальный метод
	{
		cout << "Foo()" << endl;
	}
};

class Gun : public Weapon
{
public:
	void Shoot()
	{
		cout << "Bang!" << endl;
	}
};

class SubmachineGun : public Gun // SubmachineGun - пулемет
{
public:
	void Shoot() override
	{
		cout << "Bang! Bang! Bang!" << endl;
	}
};

class Bazuka : public Weapon
{
	void Shoot() override
	{
		cout << "Babax" << endl;
	}
};

class Knife : public Weapon
{
	void Shoot() override
	{
		cout << "Удар ножом" << endl;
	}
};

class Player
{
public:
	void Shoot(Weapon* weapon)
	{
		weapon->Shoot();
	}
};

// Виртуальный деструктор класса - для правильного удаления динамической памяти при наследовании

class A
{
	A()
	{
		cout << "Выделилась динамическая память объекта А" << endl;
	}
	virtual ~A()
	{
		cout << "Динамическая память очистилась объекта A" << endl;
	}
};

class B : public A
{
	B()
	{
		cout << "Выделилась динамическая память объекта B" << endl;
	}
	~B() override
	{
		cout << "Динамическая память очистилась объекта B" << endl;
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	A* ptr = new B;

	delete ptr; // для удаления всей памяти 

	return 0;
}

// Чисто виртуальный деструктор - все тоже самое что и функции (абстрактный класс)

class A
{
	A()
	{

	}
	virtual ~A() = 0;
};

A::~A() {}; // делает чисто виртуальный деструктор

class B : public A
{
	B()
	{
		
	}
	~B() override
	{
		
	}
};

//-----------------------------------------------------------------------------------------------------------------------------------------

// Делегирующий конструктор - удобное использование конструктора (чтобы писать меньше кода), при вызове одного конструктора, он делегирует 
// его на другой конструктор (то есть перед выполнением одного конструктора, сначала выполняется другой)

// некрасивый вариант
class Human
{
public:

	Human(string name)
	{
		this->name = name;
		this->age = 0;
		this->weight = 0;
	}

	Human(string name, int age)
	{
		this->name = name;
		this->age = age;
		this->weight = 0;
	}

	Human(string name, int age, int weight)
	{
		this->name = name;
		this->age = age;
		this->weight = weight;
	}

	string name;
	int age;
	int weight;
};

// более красивый вариант
class Human
{
public:

	Human(string name)
	{
		this->name = name;
		this->age = 0;
		this->weight = 0;
	}

	Human(string name, int age) : Human(name)
	{
		this->age = age;
	}

	Human(string name, int age, int weight) : Human(name,age)
	{
		this->weight = weight;
	}

	string name;
	int age;
	int weight;
};

// Вызов виртуального метода базового (родительського) класса

class Msg
{
public:

	Msg(string msg)
	{
		this->msg = msg;
	}

	virtual string GetMsg()
	{
		return msg;
	}

private:
	string msg;
};

class BraketsMsg : public Msg
{
public:
	BraketsMsg(string msg) :Msg(msg)
	{
	}
	string GetMsg() override
	{
		return '[' + ::Msg::GetMsg() + ']'; // указание на родительский класс, а не тот в котором мы сейчас находимся
	}
};

class Printer
{
public:
	void Print(Msg* msg)
	{
		cout << msg->GetMsg() << endl;
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	Msg m("Qq");
	BraketsMsg b("Qq2");

	Printer p;
	p.Print(&m);// -> Qq
	p.Print(&b);// -> Qq2

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Множественное наследование - наследование больше одного класса (через запятую), FlyingCar - наследник с двумя классами

class Car
{
public:
	void Drive()
	{
		cout << "Я еду" << endl;
	}
};

class Airplane
{
public:
	void Fly()
	{
		cout << "Я лечу" << endl;
	}
};

class FlyingCar : public Car, public Airplane
{

};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	FlyingCar fc;
	fc.Drive();
	fc.Fly();

	return 0;
}

// Порядок вызова конструкторов при множественном наследовании - так как мы наследовали

class FlyingCar : public Car, public Airplane 
{
	// вызов конструкторов -> Car, Airplane, FlyingCar (так как, чтобы сделать объект FlyingCar, ему нужны уже созданы Car и Airplane)
};

// Порядок вызова деструкторов при множественном наследовании - наоборот от вызова конструкторов

class FlyingCar : public Car, public Airplane
{
	// вызов деструкторов -> FlyingCar, Airplane, Car 
};

// Одинаковые методы при множественном наследовании - решаются с помощью привидения типов

class Car
{
	void Use()
	{
		cout << "Я еду" << endl;
	}
};

class Airplane
{
	void Use()
	{
		cout << "Я лечу" << endl;
	}
};

class FlyingCar : public Car, publica Airplane
{

};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	FlyingCar fc;

	((Car)fc).Use(); // -> Я еду (метод класса Car)

	((Airplane)fc).Use(); // -> Я лечу (метод класса Airplane)

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Интерфейс - абстрактный класс (у которого все методы чисто виртуальные), для которых потом описывается реализация

class IBicycle // I - interface , Bicycle - велосипед -> интрефейс ведосипеда
{
public:
	void virtual Ride() = 0;
};

class SimpleBicycle : public IBicycle
{
public:
	void Ride() override
	{
		cout << "Simple(обычный) велосипед едет" << endl;
	}
};

class SportBicycle : public IBicycle
{
public:
	void Ride() override
	{
		cout << "Sport(спортивный) ведосипед едет" << endl;
	}
};

class Human
{
public:
	void RideOn(IBicycle& bicycle) // ссылка на любой объект, который реализовывает интерфейс ведосипеда
	{
		bicycle.Ride();
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	SimpleBicycle simpleb;
	SportBicycle sportb;

	Human h;

	h.RideOn(simpleb); // -> Simple(обычный) велосипед едет
	h.RideOn(sportb); // -> Sport(спортивный) велосипед едет

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Виртуальное наследование либо же ромбовидное наследование - создано для того, чтобы объект класса не создавался 2 раза
// В примере : Character (компонент ПК и персонаж в игре)
// В игре : orc - человек; warrior - воин

//---------------------------------------------------------ПК------------------------------------------------------------------------------

// В ПК нам нужно чтобы информация раздваивалась (каждому свое значение)

class Component
{
public:
	Component(string companyName)
	{
		cout << "конструктор Component" << endl;
		this->companyName = companyName;
	}
	string companyName;
};

class GPU : public Component
{
public:
	GPU(string companyName) : Component(companyName)
	{
		cout << "конструктор GPU" << endl;
	}
};

class Memory : public Component
{
public:
	Memory(string companyName) : Component(companyName)
	{
		cout << "конструктор Memory" << endl;
	}
};

class GraphicCard : public GPU, public Memory
{
public:
	GraphicCard(string GPUCompanyName, string MemoryCompanyName) : GPU(GPUCompanyName), Memory(MemoryCompanyName)
	{
		cout << "конструктор GraphicCard" << endl;
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	GraphicCard gp("GPU","Memory"); // -> Component, GPU, Component, Memory, GraphicCard

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

//---------------------------------------------------------Игра----------------------------------------------------------------------------

// В игре раздваение информации не нужно

class Character
{
public:
	Character()
	{
		cout << "конструктор Character" << endl;
	}
	int HP; // HP (жизни) персонажа
};

class Orc : public virtual Character
{
public:
	Orc()
	{
		cout << "конструктор Orc" << endl;
	}
};

class Warrior : public virtual Character
{
	Warrior()
	{
		cout << "конструктор Warrior" << endl;
	}
};

class OrcWarrior : public Orc, public Warrior
{
	OrcWarrior()
	{
		cout << "конструктор OrcWarrior" << endl;
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	OrcWarrior orcWar; // -> Character, Orc, Warrior, OrcWarrior

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Схема виртуального (ромбовидного) наследования ->
//                           -----------
//                           |Сharacter|
//                           -----------
//                         /            \
//                        /              \
//                     -----            ---------
//                     |Orc|            |Warrior|
//                     -----            ---------
//                         \             /
//                          \           /
//                          ------------
//                          |OrcWarrior|
//                          ------------

//-----------------------------------------------------------------------------------------------------------------------------------------

// enum - перечисляемый тип - набор констант для удобства программистам (можно использовать как текстом - цифры, и цифры - текстом)

class PC
{
public:

	enum PCState // состояние ПК
	{
		OFF, // -> 0   -|
		IN, // -> 1     | -> константы 
		SLEEP // -> 2  _|
	};

	PCState GetState()
	{
		return State;
	}

	void SetState(PCState State)
	{
		this->State = State;
	}

private:
	PCState State;
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	PC pc;

	pc.GetState(); // PC::PCState::OFF -> 0
	pc.GetState(); // PC::PCState::IN -> 1
	pc.GetState(); // PC::PCState::SLEEP -> 2

	if (pc.GetState() == PC::PCState::IN)
	{
		cout << "Пк включили (либо был включен)" << endl;
	}

	switch (pc.GetState())
	{
	case PC::PCState::OFF:
		cout << "ПК выключен" << endl;
		break;
	case PC::PCState::IN:
		cout << "ПК включен" << endl;
		break;
	case PC::PCState::SLEEP:
		cout << "Пк спит" << endl;
		break;
	}

	return 0;
}

enum Speed // скорость самолета
{
	MIN = 150,
	RECOMMEND = 600,
	MAX = 800
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	Speed speed = Speed::RECOMMEND;
	cout << speed << endl; // -> 600

	return 0;
}

// Пространство имен (namespace) -> using namespace -> не придется писать с какого пространства имен мы пользуемся (std - стандартные С++)

namespace firstNS
{
	void Foo()
	{
		cout << "Foo firstNS" << endl;
	}

	int a = 0;

	class Point
	{
	public:
		int x;
	};
}

namespace secondNS
{
	void Foo()
	{
		cout << "Foo secondNS" << endl;
	}

	int b = 0;

	class Point
	{
	public:
		int y;
	};
}

// Названия классов, переменных и т.д. может быть одинаковым, главное вначале указывать пространство имен (namespace - фамилия, Foo - имя)

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	firstNS::Foo();
	firstNS::a;
	firstNS::Point x;
	x.x; // -> поле Х у класса Point (namespace - firstNS)

	secondNS::Foo();
	secondNS::b;
	secondNS::Point y;
	y.y; // -> поле У у класса Point (namespace - secondNS)

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Шаблоны классов - шаблонные классы нужны для того, чтобы работать с разными типами данных

class Point
{
public:
	Point()
	{
		this->x = 0;
		this->y = 0;
		this->z = 0;
	}

	Point(int x, int y, int z)
	{
		this->x = x;
		this->y = y;
		this->z = z;
	}

private:
	int x;
	int y;
	int z;
};

template<typename T>
class TypeSize
{
public:

	TypeSize(T value)
	{
		this->value = value;
	}

	void DataTypeSize()
	{
		cout << "sizeof value : " << sizeof(value) << endl;
	}

private:
	T value;
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	int a = 0;
	Point b;

	TypeSize<int> c(a); // -> 4 (sizeof(int) = 4)
	TypeSize<Point> d(b); // -> 12 (sizeof(Point) = 12 (3 переменные типа int = 4*3 = 12))

	return 0;
}

// Наследование шаблонных классов

template<typename T>
class TypeSize
{
public:

	TypeSize(T value)
	{
		this->value = value;
	}

	void DataTypeSize()
	{
		cout << "sizeof value : " << sizeof(value) << endl;
	}

protected:
	T value;
};

template<typename T>
class TypeInfo : public TypeSize<T>
{
	TypeInfo(T value):TypeSize(value)
	{

	}

	void ShowTypeName()
	{
		cout << "Тип переменной value : " << typeid(value).name() << endl;
	}

};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	int a = 0;
	Point b;

	TypeInfo<int> ti(a); // -> тип переменной : int + sizeof
	TypeInfo<Point> ti2(b); // -> тип переменной class Point + sizeof

	return 0;
}

// Специализация шаблонов класса - особенна реализация для определенного типа данных

template <typename T>
class Printer
{
public:
	void Print(T value)
	{
		cout << value << endl;
	}
};

template<>
class Printer<string>
{
public:
	void Print(string value)
	{
		cout << "____ " << value << " ____" << endl;
	}
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	int a = 0;

	Printer<int> pr;
	pr.Print(45); // -> 45

	Printer<string> pr2;
	pr2.Print("stroka"); // -> ____ stroka ____

	return 0;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

// Smart pointer - самий примитивный умный указатель (который сам автоматом чистит память при выходе из функции, написаный руками)

template<typename T>
class SmartPointer
{
public:
	SmartPointer(T *ptr)
	{
		this->ptr = ptr;
	}

	~SmartPointer()
	{
		delete ptr;
	}

	T& operator* ()
	{
		return *ptr;
	}

private:
	T* ptr;
};

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	SmartPointer<int> pointer = new int(5); // -> new int() возвращает указатель, который принимается в конструктор

	*pointer = 2345; // -> можно заменить значение

	cout << *pointer << endl; // -> 2345 (так как мы перегрузили оператор разименовывание *)

	return 0;
}

// Smart pointers (стандартные в С++) : auto_ptr, unique_ptr, shared_ptr ; нужно подключить либу #include <memory>
// Чаще всего юзают shared_ptr, так как в нем обошли проблему при удалении указателей на одни и те же данные

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	shared_ptr<int> p1(new int(3));

	shared_ptr<int> p2(p1);

	return 0;
}

// Умные указатели на динамические массивы

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	// Все тоже самое, ток ставим что это массив

	int Size = 0;
	cin >> Size;

	shared_ptr<int[]> ptr(new int[Size]);
	for (int i = 0; i < Size; i++)
	{
		ptr[i] = rand() % 10;
		cout << ptr[i] << endl;
	}

	return 0;
}

int main()
{
	setlocale(LC_ALL, "ru");
	srand(time(NULL));



	return 0;
}