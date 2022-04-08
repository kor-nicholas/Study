class PC:
    RAM = int
    disk_memory = int
    model = ''
    CPU = ''

class TablePC(PC):
    screen = ''
    keyboard = ''
    mouse = ''
    size = ''

    def getInfo(self):
        print(f"\nИнформация о настольном ПК {self.model}\nОперативная память : {self.RAM}\nОбъем памяти на диске : {self.disk_memory}\n"
              f"Процессор : {self.CPU}\nМонитор : {self.screen}\nКлавиатура : {self.keyboard}\nМишь : {self.mouse}\nГабариты : {self.size}")

class Laptop(PC):
    size = ''
    size_of = int

    def getInfo(self):
        print(
            f"\nИнформация о ноутбуке {self.model}\nОперативная память : {self.RAM}\nОбъем памяти на диске : {self.disk_memory}\n"
            f'Процессор : {self.CPU}\nГабариты ноутбука : {self.size}\nДиагональ экрана : {self.size_of}"')

if __name__ == '__main__':
    