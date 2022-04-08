#include <iostream>
#include <windows.h>
#include <string>
#include <fstream>
#include <sstream>
#include <typeinfo>

using namespace std;

void foutInFile(string* arr, int n)
{
    string localData;
    ofstream fout;

    try
    {
        fout.open("file1.txt");
    }
    catch (const exception& ex)
    {
        cout << "Помилка вiдкриття файлу : " << endl;
        ex.what();
    }

    for (int i = 0; i < n; i++)
    {
        localData += arr[i];
        localData += '\n';
        cout << "Довжина " << i + 1 << " рядку : " << arr[i].size() << endl;
    }

    fout << localData;

    fout.close();
}

double** init(int a, int b) 
{
    double** arr2 = new double* [a]; // a - ряды ; b - столбцы
    for (int i = 0; i < a; i++)
        arr2[i] = new double[b];

    for (int i = 0; i < a; i++)
        for (int j = 0; j < b; j++)
            arr2[i][j] = 0;
    return arr2;
}

void deleteInit(double** arr2, int a, int b)
{
    for (int i = 0; i < a; i++)
        delete[] arr2[i];
    delete[] arr2;
}

void finInFile(int a, int b)
{
    double** arr2 = init(a, b);

    string localData;
    double miinusModule = 0;
    ifstream fin;

    try
    {
        fin.open("file2.txt");
    }
    catch (const exception& ex)
    {
        cout << "Помилка вiдкриття файлу" << endl;
        ex.what();
    }

    cout << "Данi з файлу : " << endl;
    for (int i = 0, j = 0; !fin.eof(); i++)
    {
        getline(fin, localData, '\n');
        cout << localData << endl;

        double temp = 0;

        istringstream ist(localData);
        for (i, j;ist >> temp; j++)
        {
            if (j % 4 == 3)
            {
                arr2[i][j] = temp;
                j = -1;
            }
            else
                arr2[i][j] = temp;
        }
    }

    for (int i = 0; i < a; i++)
        for (int j = 0; j < b; j++)
            if (arr2[i][j] < 0)
                miinusModule += abs(arr2[i][j]);

    cout << "Сумма модулiв всiх вiд'емних елементiв матрицi : " << miinusModule << endl;
    
    deleteInit(arr2, a, b);
}

int main()
{
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);

    cout << "Завдання №1" << endl << endl;

    int n = 0;

    cout << "Введiть кiлькiсть рядкiв : ";
    cin >> n;

    string* arr = new string[n];

    for (int i = 0; i < n; i++)
    {
        cout << "\nВведiть " << i + 1 << " слово рядку : ";
        cin >> arr[i];
    }

    foutInFile(arr, n);

    delete[] arr;

    cout << "\nЗавдання №2" << endl << endl;

    int a = 3, b = 4;

    finInFile(a, b);

    return 0;
}