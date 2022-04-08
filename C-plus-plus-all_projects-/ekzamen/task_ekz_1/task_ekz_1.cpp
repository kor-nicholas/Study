﻿#include <iostream>
#include <windows.h>
#include<fstream>

using namespace std;

void printMatrix(int** matrix, int row, int column);
int** initMatrix(int row, int column);
int countOddElements(int** matrix, int row, int column);
int* processMatrix(int** matrix, int row, int column, int countVector);
void fileMatrix(int** matrix, int row, int column);
void delMatrix(int** matrix, int row, int column);
void restartAplication(char return_y_n, int row, int column);


int main() {
	setlocale(0, "ukr");
	cout << "Екзаменацiйне завдання №1" << endl << "Виконав : Коровченко Микола" << endl << endl;

	int row = 0, column = 0;
	cout << "Введiть кiлькiсть рядкiв матрицi : ";
	cin >> row;
	cout << "Введiть кiлькiсть стовпцiв матрицi : ";
	cin >> column;

	int** matrix = initMatrix(row, column);

	char return_y_n = 'y';
	restartAplication(return_y_n, row, column);

	delMatrix(matrix, row, column);

	system("pause");
}

void printMatrix(int** matrix, int row, int column)
{
	// cout.precision(3) - Вывод числа до определенного количества знаков после запятой (3)
	// cout << x;

	cout << "Матриця -> \n";
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < column; j++)
		{
			cout.width(5); // Ширина поля вывода (для красивого оформления матрицы)
			cout << matrix[i][j] << "\t";
		}
		cout << endl;
	}
}

int** initMatrix(int row, int column)
{
	int** matrix = new int* [row];
	for (int i = 0; i < row; matrix[i] = new int[column], i++);

	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < column; j++)
		{
			matrix[i][j] = rand() % 10;
		}
	}

	return matrix;
}

// Нечетные елементы в четных рядах
int countOddElements(int** matrix, int row, int column)
{
	int countVector = 0;
	for (int i = 1; i < row; i += 2)
	{
		for (int j = 0; j < column; j++)
		{
			if (matrix[i][j] % 2 != 0)
			{
				countVector++;
			}
		}
	}
	return countVector;
}

int* processMatrix(int** matrix, int row, int column, int countVector)
{
	int sum = 0;
	int* vector = new int[countVector];

	for (int i = 1; i < row; i += 2)
	{
		for (int j = 0; j < column; j++)
		{
			if (matrix[i][j] % 2 != 0)
			{
				sum += matrix[i][j];
			}
		}
		vector[i - 1] = sum;
		sum = 0;
	}

	/*if (a % 2)
		cout << "чет";
	else
		cout << "нечет";*/

	return vector;
}

void fileMatrix(int** matrix, int row, int column)
{
	fstream fout;
	try
	{
		fout.open("file.txt", fstream::out);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	fout << "Матриця -> \n";
	for (int i = 0; i < row; i++)
	{
		for (int j = 0; j < column; j++)
		{
			fout.width(5); // Ширина поля вывода (для красивого оформления матрицы)
			fout << matrix[i][j] << "\t";
		}
		fout << endl;
	}

	fout.close();
}

void printVector(int* vector, int countVector)
{
	cout << "\nВектор непарних елементiв, парних рядкiв матрицi : " << endl;
	for (int i = 0; i < countVector; i++)
	{
		if (vector[i] > 0)
		{
			cout << vector[i] << endl;
		}
	}
}

void fileVector(int* vector, int countVector)
{
	fstream fapp;
	try
	{
		fapp.open("file.txt", fstream::app);
	}
	catch (const exception& ex)
	{
		cout << "Помилка вiдкриття файлу";
		cout << ex.what();
	}

	fapp << "\nВектор непарних елементiв, парних рядкiв матрицi : " << endl;
	for (int i = 0; i < countVector; i++)
	{
		if (vector[i] > 0)
		{
			fapp << vector[i] << endl;
		}
	}
	fapp.close();
}

void delMatrix(int** matrix, int row, int column)
{
	for (int i = 0; i < row; i++)
	{
		delete[] matrix[i];
	}
	delete[] matrix;
}

void restartAplication(char return_y_n, int row, int column)
{
	setlocale(0, "ukr");
	do {
		int** matrix = initMatrix(row, column);

		int countVector = countOddElements(matrix, row, column);
		int* vector = processMatrix(matrix, row, column, countVector);

		printMatrix(matrix, row, column);
		fileMatrix(matrix, row, column);

		printVector(vector, countVector);
		fileVector(vector, countVector);

		delMatrix(matrix, row, column);
		delete[] vector;

		cout << "\nReturn ? y/n : ";
		cin >> return_y_n;

		while (true) {
			if (return_y_n == 'n')
				break;
			if (return_y_n == 'y')
			{
				cout << "Введiть кiлькiсть рядкiв матрицi : ";
				cin >> row;
				cout << "Введiть кiлькiсть стовпцiв матрицi : ";
				cin >> column;
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