﻿#include<iostream>
#include<string>
#include<sstream>
#include<fstream>

using namespace std;

string* inputText(string* text, int countStr);
string* processText(string* text, int countStr);
void fileText(string* text);
void printText(string* text, int countStr);
void delText(string* text);
void restartAplication(char return_y_n, int countStr);

int main() {
	setlocale(0, "ukr");
	cout << "Екзамецiйна робота №2" << endl << "Виконав : Коровченко Микола" << endl << endl;

	int countStr = 0;

	cout << "Введiть кiлькiсть рядкiв : ";
	cin >> countStr;

	char return_y_n = 'y';
	restartAplication(return_y_n, countStr);

	system("pause");

	return 0;
}

string* inputText(string* text, int countStr)
{
	setlocale(0, "ukr");
	cout << "\nВведiть текст -> ";

	for (int i = 0; i < countStr; i++)
	{
		if (!i) { cin.ignore(); cin.clear(); }
		getline(cin, text[i]);
	}

	return text;
}

string* processText(string* text, int countStr)
{
	string word, wordCopy;

	for (int i = 0; i < countStr; i++)
	{
		istringstream strin(text[i]);
		while (strin >> word) // wark = kraw
		{
			int indexWord = text[i].find(word), strlen = word.length();
			for (int j = 0; j < strlen; j++)
			{
				wordCopy += word[strlen - j - 1];
			}
			text[i].replace(indexWord, strlen, wordCopy);
			wordCopy.clear();
		}
	}
	return text;
}

void printText(string* text, int countStr)
{
	cout << "\nText -> \n";

	for (int i = 0; i < countStr; cout << text[i] << endl, i++);
}

void delText(string* text)
{
	delete[] text;
}

void restartAplication(char return_y_n, int countStr)
{
	do {
		string* text = new string[countStr];

		text = inputText(text, countStr);

		text = processText(text, countStr);

		printText(text, countStr);

		delText(text);

		cout << "\nReturn ? y/n : ";
		cin >> return_y_n;

		while (true) {
			if (return_y_n == 'n')
				break;
			if (return_y_n == 'y')
			{
				cout << "Введiть кiлькiсть рядкiв : ";
				cin >> countStr;
				break;
			}
			if (return_y_n != 'n' && return_y_n != 'y')
			{
				cout << "Сталася помилка,повторiть спробу ще раз" << endl << "Return? y/n: ";
				cin >> return_y_n;
			}
		}
	} while (return_y_n == 'y');
}