#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

// Перед этим все равно, с помощью https://serblog.ru/demo/format-html/ форматируем html код и пихаем в file.txt
// Всего нужно будет нажать 4 раза Enter
// После 2 Enter, нужно зайти в файла и снова отформатировать его на сайте (все лишние пробелы в начале тоже нужно убрать)
// И обязательно в main указать количество подписчиков (подписок) -> count

// 1 - сначала ищем и записываем в файл в таком виде
// <div class = "d7ByH"><span class = "Jv7Aj mArmR MqpiF  "><a class = "FPmhX notranslate  _0imsa " title = "sonchhouss" href = "/sonchhouss/" tabindex = "0">sonchhouss< / a>< / span> < / div>
// <div class = "d7ByH"><span class = "Jv7Aj mArmR MqpiF  "><a class = "FPmhX notranslate  _0imsa " title = "reshenie_zadach_po_matematike" href = "/reshenie_zadach_po_matematike/" tabindex = "0">reshenie_zadach_po_matematike< / a>< / span> < / div>

void task1(int count)
{
	string localData, podStroka = "<div class=\"d7ByH\"><span class=\"Jv7Aj mArmR MqpiF  \"><a class=\"FPmhX notranslate  _0imsa \"";

	fstream fin;
	try
	{
		fin.open("file.txt", fstream::in);
	}
	catch (const exception& ex)
	{
		cout << "Ошибка открытия файла\nДанные ошибки : " << ex.what();
	}

	string* arr = new string[count];

	int i = 0, k = 0;
	while (!fin.eof())
	{
		getline(fin, localData);
		k = localData.find(podStroka);
		if (k != -1)
		{
			arr[i] = localData;
			cout << "i = " << i << endl << arr[i] << endl;
			i++;
		}
	}

	fin.close();

	system("pause");

	try
	{
		fin.open("file.txt", fstream::out);
	}
	catch (const exception& ex)
	{
		cout << "Ошибка открытия файла\nДанные ошибки : " << ex.what();
	}

	for (int i = 0; i < count; i++)
	{
		fin << arr[i];
	}

	fin.close();
	system("pause");
	delete[] arr;
}

// 2 - потом уже в более менее виде удаляем сначала и с конца лишнее(чтобы остались только ники)

void task2(int count)
{
	string localData, podStroka = "title=", podStroka2 = "\"";

	fstream fin;
	try
	{
		fin.open("file.txt", fstream::in);
	}
	catch (const exception& ex)
	{
		cout << "Ошибка открытия файла\nДанные ошибки : " << ex.what();
	}

	string* arr = new string[count];

	int i = 0, k = 0;
	while (!fin.eof())
	{
		getline(fin, localData);
		k = localData.find(podStroka);
		localData.erase(0, 98);
		k = localData.find(podStroka2);
		localData.erase(k);
		arr[i] = localData;
		cout << "i = " << i << endl << arr[i] << endl;
		i++;
	}

	fin.close();

	system("pause");

	try
	{
		fin.open("accounts.txt", fstream::out);
	}
	catch (const exception& ex)
	{
		cout << "Ошибка открытия файла\nДанные ошибки : " << ex.what();
	}

	for (int i = 0; i < count; i++)
	{
		fin << arr[i] << endl;
	}

	fin.close();
	system("pause");
	delete[] arr;
}

int main()
{
	setlocale(LC_ALL, "ru");

	// Перезапишет только ники в файл accounts.txt (из file.txt)
	int count = 164;
	task1(count);
	task2(count);

	return 0;
}