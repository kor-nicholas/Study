# Наследование - создание новых классов, на основе других (+ добавление нового функционала)
# Полиморфизм - возможность вызова методово базового класса из нового
# Инкапсуляция - вся работа происходит под капотом

# Класс - шаблон, екземпляр - объект (имя с большой буквы)

#--------------------------------------------------- Атрибуты ----------------------------------------------------------

class Point:
    "Описание класса : класс для указания x,y координат точки" # будет доступно в Point.__doc__
    x = 1 # атрибуты (свойства)
    y = 1 # атрибуты (свойства)

pt = Point()
Point.x = 100 # динамически меняет класс - автоматом меняет и экземпляры этого класса (похоже на статические переменные на С++)
print(pt.x, pt.y) # 100, 1

pt.x = 5 # меняет значение только у екземпляра pt
print(pt.x, Point.x) # 5, 1

pt.z = 10 # Если атрибута нету в классе, то он динамически будет добавлен (но если атрибута нету, то прочитать его не получится)
print(pt.z, pt.a) # 10, AtributError
getattr(pt, 'a', False) # Обращение к атрибуту, если нету атрибута, то вернет False
setattr(pt,'a',100) # Установка значения атрибуту
delattr(pt,'a') # Удаление атрибута
del pt.z # Удаление атрибута
hasattr(pt,'a') # Есть ли такой атрибут
isinstance(pt,Point) # Является ли екземпляр pt екземпляром класса Point

#-----------------------------------------------------------------------------------------------------------------------

#--------------------------------- Встроенные переменные классов -------------------------------------------------------

# Екземпляров :
print(pt.__doc__) # строка с описанием класса
print(pt.__dict__) # набор локальных атрибутов екземпляра класса (именно которые прописываются pt.x = 5)

# Классов :
print(Point.__doc__) # строка с описанием класса
print(Point.__name__) # строка с именем класса
print(Point.__dict__) # набор локальных атриботов класса (именно которые прописываются Point.x = 3)

#-----------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------- Методы (self) -----------------------------------------------------

# self - this на C++ (обращение именно к этому екземпляру), каждый метод должен иметь первый параметр self (так прописано в Python)

class Point:
    def __init__(self, x = 0, y = 0): # конструктор
        self.x = x
        self.y = y

    def __del__(self): # деструктор
        print("Деструктор")

    x = 1; y = 1
    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt = Point()
pt1 = Point()
pt.setCoords(5,1)
print(pt.__dict__) # a = 5, b = 1
Point.setCoords(pt1, 100, 5) # указываем именно к какому екземпляру обращаемся

pt = Point() # x = 0, y = 0
pt1 = Point(5) # x = 5, y = 0
pt2 = Point(5,10) # x = 5, y = 10

pt = 0 # После этого, переменная pt не будет ссылаться на екземпляр класса Point (проще говоря, удаляет екземпляр как я понял)

#-----------------------------------------------------------------------------------------------------------------------

#----------------------------- Геттеры и сеттеры + режимы доступа (public, private, protected) -------------------------

# <имя класса> (без подчеркиваний вначале) - public (обращение везде и в екземплярах)
# _<имя класса> (с 1 подчеркиванием вначале) - protected (обращение только внутри либо дочерных классах)
# __<имя класса> (с 2 подчеркиваниями вначале) - private (обращение только внутри класса)

class Point:
    WIDTH = 5 # константа, должна быть всегда одинаковой

    __slots__ = ['__x', '__y'] # разрешенные дополнтельные (локальные) свойства екземпляров класса
    # то есть при Point.z - приозойдет исключение, так как оно не прописано в __slots__
    # но в тоже время, нельзя указывать атрибуты, которые уже есть в классе до __slots__ (в нашем случае WIDTH)

    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __checkValue(value): # закрытый метод на проверку значений
        if (isinstance(value, int) or isinstance(value, float)):
            return True
        return False

    def setCoords(self, x, y): # сеттер - устанавливает значения атрибутам
        if Point.__checkValue(x) and Point.__checkValue(y): # проверка на тип (\ - перенос команды)
            self.__x = x; self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self): # геттер - возвращает кортеж значений екземпляра
        return self.__x, self.__y

    def __getattribute__(self, item): # перегрузка метода, чтобы не было доступа по _Point__x
        if item == "_Point__x":
            return "Закрытая переменная"
        else:
            return object.__getattribute__(self,item)

    def __setattr__(self, key, value): # перегрузка метода, чтобы не изменялась константа (WIDTH)
        if key == "WIDTH":
            raise AttributeError # генерируем исключение
        else:
            self.__dict__[key] = value # если не константа, то сохраняем значение

    def __getattr__(self, item):
        print(f"__getattr__:{item}") # если не существует атрибута в классе

    def __delattr__(self, item):
        print(f"__delattr: {item}") # перегрузка оператора del (для удаления атрибута)

pt = Point(1,2)
pt.getCoords() # 1,2
pt.setCoords(10,20)
pt.getCoords() # 10,20

pt5 = Point()
print(pt5._Point__x) # обращение к закрытому атрибут из екземпляра
Point._Point__checkValue(4) # обращение к закрытому методу из екземпляра

pt.WIDTH = 100 # AtributError

pt.zzz # вызовется __getattr__
pt.z = 1 # вылетит ошибка, так как мы 'z' не прописали в __slots__
del pt.z # вызовется __delattr__

#-----------------------------------------------------------------------------------------------------------------------

#-------------------------------- Объекты свойства (property) и дескрипторы классов ------------------------------------

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __setCoordX(self, x):
        self.__x = x

    def __getCoordX(self):
        return self.__x

    def __delCoordX(self):
        print("Удаление свойства")
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __delCoordX)

pt = Point(1,2)
pt.coordX = 100 # вызовится сеттер
x = pt.coordX # вызовится геттер'
del pt.coordX # вызовится __delCoordX (либо же удалится атрибут и выведит на экран об удалении)

# С использованием декораторов

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        self.__x = x

    @coordX.deleter
    def coordX(self):
        print("Удаление свойства")
        del self.__x

    #coordX = property(__getCoordX, __setCoordX, __delCoordX)

pt = Point(1,2)
pt.coordX = 100 # вызовится сеттер
x = pt.coordX # вызовится геттер'
del pt.coordX # вызовится __delCoordX (либо же удалится атрибут и выведит на экран об удалении)

# С использованием дескрипторов

class CoordValue: # класс дескриптора
    def __init__(self, name):
        self.__name = name # имя локального свойства

    def __set_name__(self, owner, name): # можно юзать вместо конструктора и не придется передавать строчки с именем
        print(name) # сначала coordX; потом coordY
        self.__name = name # Но доступно после Python 3.6+

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name] # для работы с определенным екземпляром

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value # для работы именно с определенным екземпляром (+ сами создаем локальную переменную)

class Point:
    coordX = CoordValue("coordX") # создают в каждом екземпляре свои локальные переменные
    coordY = CoordValue("coordY") # создают в каждом екземпляре свои локальные переменные
    coordX = CoordValue() # если без конструктора, а с __set_name__, то не обязательно передавать имя в качестве параметра
    coordY = CoordValue() # если без конструктора, а с __set_name__, то не обязательно передавать имя в качестве параметра

    def __init__(self, x = 0, y = 0):
        self.coordX = x; self.coordY = y

pt = Point(1,2)
pt.coordX = 5
# pt.coordX = Point.coordX

#-----------------------------------------------------------------------------------------------------------------------

#----------------------- Статические свойства и методы класса, декоратор @staticmethod, синглетон ----------------------

class Point:
    count = 0
    __count = 0

    def __init__(self, x = 0, y = 0):
        Point.__count += 1
        self.coordX = x; self.coordY = y # тоже создает локальные переменные в каждои екземпляре

    @staticmethod # декоратор, который указывает что метод статический и self передавать не обязательно
    def getCount():
        return Point.__count

pt = Point()
pt1 = Point()
pt2 = Point()
print(pt.count, pt1.count, pt2.count) # 0,0,0
Point.count = 10
print(pt.count, pt1.count, pt2.count) # 10,10,10
pt.count = 5 # создает локальную переменную в екземпляре (pt.count != Point.count)
print(pt.count, pt1.count, pt2.count) # 5,10,10
print(pt.getCount(), Point.getCount()) # 3 3 (так как создавалось 3 екземпляра)

def getCount():
    return 346

pt.getCount = getCount # переопределение метода в екземпляре, а основной класса - остается на месте
print(pt.getCount(), Point.getCount()) # 346 3

# Класс синглетон - класс, которого можна создать только 1 объект (екземпляр)
class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs): # перед созданием екземпляра класса
        # cls - ссылка на класс Point
        if not isinstance(cls.__instance, cls): # если это не наш класс
            cls.__instance = super(Point, cls).__new__(cls) # то мы создаем екземпляр нашего класса
        else:
            print("Екземпляр класса Point уже создан")

    def __init__(self, x = 0, y = 0):
        Point.__count += 1
        self.coordX = x; self.coordY = y # тоже создает локальные переменные в каждои екземпляре

    @staticmethod # декоратор, который указывает что метод статический и self передавать не обязательно
    def getCount():
        return Point.__count

pt = Point()
pt1 = Point()
pt2 = Point()
print(id(pt), id(pt1), id(pt2)) # Екземпляр класса уже создан 2 раза вызовется (при создании pt1 и pt2)
# id(pt) = id(pt1) = id(pt2) - потому что этот класс, создает только 1 екземпляр

#-----------------------------------------------------------------------------------------------------------------------

#-------------------------------------- Наследование классов (protected) -----------------------------------------------

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __str__(self): # переопределяем класс Line в str
        return f"({self.__x}, {self.__y})"

class Line:
    def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1):
        # : - нотация - ничего не дает на код, просто показывает программисту, какой класс ждет в параметры
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def drawLine(self):
        print(f"Рисование линии : {self._sp}, {self._ep}, {self._color}, {self._width}")

class Rect:
    def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1):
        # : - нотация - ничего не дает на код, просто показывает программисту, какой класс ждет в параметры
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def drawRect(self):
        print(f"Рисование прямоугольника : {self._sp}, {self._ep}, {self._color}, {self._width}")

l = Line(Point(1,2), Point(10,20))
l.drawLine()
r = Rect(Point(1,2), Point(10,20))
r.drawRect()

# Чтобы не было DRY (не повторяйся) - юзаем наследование

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str = "red", width:int = 1):
        # : - нотация - ничего не дает на код, просто показывает программисту, какой класс ждет в параметры
        self._sp = sp # _sp - protected, но из екземпляра все равно доступно (работает на совесть програмиста)
        self._ep = ep
        self._color = color
        self.__width = width # private - можно юзать только в Prop (либо геттер width)

    def getWidth(self):
        return self.__width

class Line (Prop): # наследуемся из класса Prop
    def drawLine(self):
        # Тут юзается конструктор по-умолчанию
        print(f"Рисование линии : {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")

class Rect (Prop): # наследуемся от класса Prop
    def __init__(self, *args):
        print("Новый конструктор класса Rect")
        super().__init__(*args) # явно запускаем конструктор Point, так как в конструкторе по-умолчанию он сам это делает

    def drawRect(self):
        print(f"Рисование прямоугольника : {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")

l = Line(Point(1,2), Point(10,20))
# Сначала вызовется конструктор Line, а потом уже конструктор Prop (дочерный, потом базовый)

#-----------------------------------------------------------------------------------------------------------------------

#---------------------------------- Переопределение и перегрузка методов, абстрактные методы ---------------------------



#-----------------------------------------------------------------------------------------------------------------------