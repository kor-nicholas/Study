#include <iostream>
#include <fstream>
#include <windows.h>
#include <string>

using namespace std;

struct teacher
{
    string fio; // ФIО викладача
    string subject; // предмет
};

teacher* inputStructInFile(teacher* local, int n)
{
    string localData = "Данi про викладачiв : \n", name, lastname;

    for (int i = 0; i < n; i++)
    {
        cout << "Введiть данi про " << i + 1 << " викладача -> \nПриiзвище : ";
        cin >> lastname;
        cout << "\nIнiцiали : ";
        cin >> name;
        local[i].fio = lastname + " " + name;
        localData += '\n'; localData += to_string(i + 1);
        localData += ". ФIО - "; localData += local[i].fio;
        cout << "\nПредмет : ";
        cin >> local[i].subject;
        localData += "\nПредмет - "; localData += local[i].subject; localData += '\n';
    }

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

    fout << localData;

    fout.close();

    return local;
}

void outInfo(int n, teacher* local, string subject)
{
    for (int i = 0; i < n; i++)
    {
        if (local[i].subject == subject)
        {
            cout << i + 1 << ". " << local[i].fio << '\n';
        }
    }
}

struct sklad
{
    string name;
    int type; // одиниця вимiру
    int cost; // цiна одиницi товару
    int quantity; // кiлькiсть
};

sklad* inputSklad(sklad* local, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "\nВведiть данi " << i + 1 << " товару -> \nНазва товару : ";
        cin >> local[i].name;
        cout << "\nОдиниця вимiру : ";
        cin >> local[i].type;
        cout << "\nЦiна за одиницю товару : ";
        cin >> local[i].cost;
        cout << "\nКiлькiсть : ";
        cin >> local[i].quantity;
    }

    return local;
}

void outSklad(sklad* local, int n, string name)
{
    int j = 1;
    for (int i = 0; i < n; i++)
    {
        if (local[i].name == name)
        {
            cout << endl << j << ". Назва товару : " << local[i].name << "\nЦiна за одиницю товару : " << local[i].cost
                << "\nКiлькiсть на складi : " << local[i].quantity << "\nЗагальна сума : " << local[i].cost * local[i].quantity; j++;
        }
    }

    if (j == 1)
        cout << "\nТовар не знайдено на складi" << endl;
}

int main()
{
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);

    cout << "Задача №1" << endl;

    int n = 0;
    cout << "Введiть кiлькiсть викладачiв : ";
    cin >> n;

    teacher* teachers = new teacher[n];

    teachers = inputStructInFile(teachers, n);

    string subject;
    cout << "\nВведiть предмет для пошуку : ";
    cin >> subject;

    outInfo(n, teachers, subject);

    delete[] teachers;

    cout << "\nЗадача №2" << endl;

    n = 0;
    cout << "Введiть кiлькiсть товару на складi : ";
    cin >> n;

    sklad* shop = new sklad[n];

    shop = inputSklad(shop, n);

    string name;
    cout << "Введiть назву товару, якого хочете дiзнатись iнформацiю : ";
    cin >> name;

    outSklad(shop, n, name);

    delete[] shop;

    return 0;
}
