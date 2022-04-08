#include <iostream>
#include <windows.h>
#include <string>

using namespace std;


int main() {
	setlocale(0, "ukr");

	// \0 - конец строчки(тарминирующий ноль)

	char text[] = "Hello World!";

	strlen(text); // считает количество символов до торменирующего ноля
	cout << "В тексте " << text << " " << strlen(text) << " символов" << endl;

	// Приведение типов в стиле С
	
	double a = 634.324; // а типа double

	cout << (int)a << endl; // a уже типа int

	// Таблица SACII 

	cout << sizeof(char) << endl; // 1 байт,8 бит => 256 комбинаций(кодов),каждый отвечает за свой символ

	//for (int i = 0; i <= 255; i++)
	//{
	//	cout << "numbers_code = " << i << "char = " << char(i) << endl;
	//}

	// До 128 едемента (с индексом 127) все статические символы ; после 128 -> setlocale

	// Указатели строк

	const char* string_1 = "Hello World!";

	cout << string_1 << endl;

	// Конкотенация №1 (меняется првая строчка(str1) - к ней добавляется вторая строчка(str2))

	char str1[255] = "Hello";
	char str2[255] = " World!";

	cout << str1 << endl;

	strcat_s(str1, str2);

	cout << str1 << endl;
}