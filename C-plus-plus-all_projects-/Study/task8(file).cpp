#include <conio.h>
#include "Windows.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

struct Products
{
	std::string name; // Iм'я товару
	std::string manufacturer; // Виробник
	double price; // Цiна
	int count; // Кiлькiсть
};

void Menu(Products* massiv_structur, std::string path, int maxStructur);
void firstChoice(Products* massiv_structur, std::string path, int max_structur);
void secondChoice(Products* massiv_structur, std::string path, int max_structur);
void thirdChoice(Products* massiv_structur, int maxStructur);
void fourthChoice(Products* massiv_structur, std::string path, int maxStructur);
void fifthChoice(Products* massiv_structur, std::string path, int maxStructur);
void sixthChoice(Products* massiv_structur, int maxStructur);

int main()
{
	setlocale(0, "ukr");
	cout << "Лабораторна робота №8" << endl << "Виконав : Коровченко Микола" << endl;

	int maxStructur = 20;
	string path; // Шлях до файлу

	cout << "\nВведiть шлях до файлу (або назву файлу,якщо файл знаходиться в цiй же папцi) з яким будемо працювати :  \n";
	cin >> path;

	Products* massiv = new Products[maxStructur + 3];

	Menu(massiv, path, maxStructur);

	delete[] massiv;

	return 0;
}

// Читання даних з файлу
void firstChoice(Products* massivStructur, string path, int maxStructur)
{
	string local_data;

	fstream fin; // file in
	try
	{
		fin.open(path, fstream::in);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	for (int i = 0, k = 0; !fin.eof(); i++) // По-строкове читання даних
	{
		getline(fin, local_data, '>'); // Молоко>Ласунка>23>100 в файле

		if (massivStructur[k].name.empty() == true) massivStructur[k].name = local_data; // name - пуста 
		else if (massivStructur[k].manufacturer.empty() == true) massivStructur[k].manufacturer = local_data; // manufacturer - пуста
		else if (massivStructur[k].price < 0)
		{
			double price_data = 0;

			istringstream price(local_data); // Переведення з string в double
			price >> price_data;

			massivStructur[k].price = price_data;
		}
		else if (massivStructur[k].count < 0)
		{
			int count_data;

			istringstream count(local_data); // Переведення з string в int
			count >> count_data;

			massivStructur[k].count = count_data;
		}

		if (i % 4 == 3) k++;
	}

	//cout << "massiv -> " << endl;   // Вивiд массиву структур на экран
	//for (int i = 0; i < maxStructur; i++)
	//{
	//	cout << "[" << i + 1 << "] -> " << endl << massivStructur[i].name << endl << massivStructur[i].manufacturer << endl <<
	//		massivStructur[i].price << endl << massivStructur[i].count << endl << endl;
	//}

	fin.close();
	cout << "\nДанi зчитано" << endl;
}

// Запис даних до файлу (запис даних з пам'ятi комп'ютера до файлу,створення нового файлу)
void secondChoice(Products* massivStructur, string path, int maxStructur)
{
	string local_data, price_str, count_str;

	for (int i = 0, k = 0; k < maxStructur; i++)  // Очистка даних з структури
	{
		if (massivStructur[k].name.empty() == false) massivStructur[k].name.clear(); // name - не пуста
		if (massivStructur[k].manufacturer.empty() == false) massivStructur[k].manufacturer.clear(); // manufacturer - не пуста
		if (massivStructur[k].price > 0) massivStructur[k].price = -1;
		if (massivStructur[k].count > 0) massivStructur[k].count = -1;

		if (i % 4 == 3) k++;
	}

	cout << "\nВведiть данi,якi буде записано до файлу : \n";

	cout << "1. Iм'я товару -> ";
	cin >> massivStructur[0].name;

	cout << "2. Виробник -> ";
	cin >> massivStructur[0].manufacturer;

	cout << "3. Цiна -> ";
	cin >> massivStructur[0].price;

	ostringstream ost; // Переведення з double в string
	ost << massivStructur[0].price;
	price_str = ost.str();

	cout << "4. Кiлькiсть -> ";
	cin >> massivStructur[0].count;

	ostringstream ost1; // Переведення з int в string
	ost1 << massivStructur[0].count;
	count_str = ost1.str();

	local_data = massivStructur[0].name + '>' + massivStructur[0].manufacturer + '>' + price_str + '>' + count_str + '>';

	fstream fout; // file out
	try
	{
		fout.open(path, fstream::out);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	fout << local_data;

	fout.close();
	cout << "\nДанi записано до файлу (або створено новий файл)" << endl;
}

// Переглянути вмiст даних на екранi
void thirdChoice(Products* massivStructur, int maxStructur)
{
	cout << "Всi товари,якi е на складi -> \n\n";
	for (int i = 0; i < maxStructur; i++)
	{
		if (massivStructur[i].name.empty() == false) cout << "Назва товару : " << massivStructur[i].name << endl; // name - не пуста
		if (massivStructur[i].manufacturer.empty() == false) cout << "Виробник : " << massivStructur[i].manufacturer << endl; // manufacturer - не пуста
		if (massivStructur[i].price > 0) cout << "Цiна : " << massivStructur[i].price << endl;
		if (massivStructur[i].count > 0) cout << "Кiлькiсть : " << massivStructur[i].count << endl << endl;
	}
}

// Дописати данi в кiнець файлу
void fourthChoice(Products* massivStructur, string path, int maxStructur)
{
	string local_data, price_str, count_str;

	fstream fout_fapp; // file out + file app
	try
	{
		fout_fapp.open(path, fstream::out | fstream::app);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	int i = 0;
	for (i; i < maxStructur; i++) // проходим по циклу та дiзнаемось iндекс (i) куди можна записати данi
	{
		if (massivStructur[i].name.empty() == false) continue; // name - не пуста
		else break;
	}

	cout << "\nВведiть данi,якi хочете додати в кiнець файлу : \n";

	cout << "1. Iм'я товару -> ";
	cin >> massivStructur[i].name;

	cout << "2. Виробник -> ";
	cin >> massivStructur[i].manufacturer;

	cout << "3. Цiна -> ";
	cin >> massivStructur[i].price;

	ostringstream ost; // Переведення з double в string
	ost << massivStructur[i].price;
	price_str = ost.str();

	cout << "4. Кiлькiсть -> ";
	cin >> massivStructur[i].count;

	ostringstream ost1; // Переведення з int в string
	ost1 << massivStructur[i].count;
	count_str = ost1.str();

	local_data = '\n' + massivStructur[i].name + '>' + massivStructur[i].manufacturer + '>' + price_str + '>' + count_str + '>';

	fout_fapp << local_data;

	fout_fapp.close();
	cout << "\nДанi дописано в кiнець файлу" << endl;
}

// Очистити данi з файлу
void fifthChoice(Products* massivStructur, string path, int maxStructur)
{
	fstream fout; // file out + trunc
	try
	{
		fout.open(path, fstream::out | fstream::trunc);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	for (int i = 0, k = 0; k < maxStructur; i++)  // Очистка даних з структури
	{
		if (massivStructur[k].name.empty() == false) massivStructur[k].name.clear(); // name - не пуста
		if (massivStructur[k].manufacturer.empty() == false) massivStructur[k].manufacturer.clear(); // manufacturer - не пуста
		if (massivStructur[k].price > 0) massivStructur[k].price = -1;
		if (massivStructur[k].count > 0) massivStructur[k].count = -1;

		if (i % 4 == 3) k++;
	}

	fout.close();
	cout << "\nДанi очищено" << endl;
}

// Мое завдання
void sixthChoice(Products* massivStructur, int maxStructur)
{
	int j = 0;
	double nowPrice = 0, max = 0, sum_cost = 1;

	for (int i = 0; i < maxStructur; i++)
	{
		nowPrice = massivStructur[i].price;

		if (nowPrice > max)
		{
			max = nowPrice;
			j = i;
		}
	}

	sum_cost = max * massivStructur[j].count;

	cout << "\nДанi про найдорожчий товар -> " << endl << endl << "Iм'я товару : " << massivStructur[j].name << endl <<
		"Виробник : " << massivStructur[j].manufacturer << endl << "Цiна : " << massivStructur[j].price << endl << "Кiлькiсть : " << massivStructur[j].count << endl << endl;

	cout << "Сумарна вартiсть товару : " << sum_cost << endl;
}

// Menu
void Menu(Products* massivStructur, string path, int maxStructur)
{
	int choise = 0; // Вибiр

	do {
		cout << "\n----------------------------------------------------------Menu----------------------------------------------------------" << endl;
		cout << "Введiть 1 для того,щоб прочитати данi з файлу" << endl;
		cout << "Введiть 2 для того,щоб записати данi до файлу" << endl;
		cout << "Введiть 3 для того,щоб переглянути вмiст даних на экранi" << endl;
		cout << "Введiть 4 для того,щоб дописати данi в кiнець файлу" << endl;
		cout << "Введiть 5 для того,щоб очистити данi з файлу" << endl;
		cout << "Введiть 6 для того,щоб виконати завдання" << endl;
		cout << "Введiть 7 для того,щоб вийти з программи" << endl;
		cout << "------------------------------------------------------------------------------------------------------------------------" << endl;
		cout << "\nВаш вибiр -> ";
		cin >> choise;

		switch (choise)
		{
		case 1:
			firstChoice(massivStructur, path, maxStructur);
			system("cls");
			break;
		case 2:
			secondChoice(massivStructur, path, maxStructur);
			system("cls");
			break;
		case 3:
			thirdChoice(massivStructur, maxStructur);
			system("cls");
			break;
		case 4:
			fourthChoice(massivStructur, path, maxStructur);
			system("cls");
			break;
		case 5:
			fifthChoice(massivStructur, path, maxStructur);
			system("cls");
			break;
		case 6:
			sixthChoice(massivStructur, maxStructur);
			system("cls");
			break;
		}
	} while (choise != 7);
}