#include <iostream>
#include <windows.h>
#include <string>

using namespace std;

struct Car
{
    string model;
    int year;
    double price;
    string color;
};

Car* inputCar(int N)
{
    Car* arrCar = new Car[N];

    for (int i = 0; i < N; i++)
    {
        cout << "\nВведiть данi " << i + 1 << " структуры : \nМодель ->";
        cin >> arrCar[i].model;
        cout << "Рiк випуску -> ";
        cin >> arrCar[i].year;
        cout << "Цiна -> ";
        cin >> arrCar[i].price;
        cout << "Колiр -> ";
        cin >> arrCar[i].color;
    }

    return arrCar;
}

void outputCar(Car* arrCar, int N)
{
    cout << "\n\nМассив структур : " << endl << endl;
    for (int i = 0; i < N; i++)
    {
        cout << i + 1 << ". " << "структура : \nМодель -> " << arrCar[i].model << endl <<
            "Рiк випуску -> " << arrCar[i].year << endl << "Цiна -> " << arrCar[i].price << endl <<
            "Колiр -> " << arrCar[i].color << endl << endl;
    }
}

int countCar(Car* arrCar, int N, string color, int year)
{
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        if (arrCar[i].color == color)
        {
            if (arrCar[i].year == year)
            {
                count++;
            }
        }
    }

    return count;
}

Car* processCar(Car* arrCar, int N, string color, int year)
{
    Car* arrCar2 = new Car[countCar(arrCar, N, color, year)];

    for (int i = 0,j = 0; i < N; i++)
    {
        if (arrCar[i].color == color)
        {
            if (arrCar[i].year == year)
            {
                arrCar2[j].color = arrCar[i].color;
                arrCar2[j].model = arrCar[i].model;
                arrCar2[j].price = arrCar[i].price;
                arrCar2[j].year == arrCar[i].year;
                j++;
            }
        }
    }

    return arrCar2;
}

int main()
{
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);

    string color = "Червоний";
    int N = 0, year = 2001;
    cout << "Введiть кiлькiсть структур : ";
    cin >> N;

    Car* arrCar = inputCar(N);

    outputCar(arrCar, N);

    cout << "За сюжетом : " << endl;

    Car* arrCar2 = processCar(arrCar, N, color, year);
    outputCar(arrCar2, countCar(arrCar, N, color, year));

    delete[] arrCar;
    delete[] arrCar2;

    return 0;
}
