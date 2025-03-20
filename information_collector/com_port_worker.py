import serial
from information_collector.collection_interface import *


#абстрактный класс который содержит общие поляя и методы
#для различных видов подключаемых устройств перифирии с разными датчиками
class ComPortWorker(InformationCollectorIntrface):
    def __init__(self, com: str, baudrate: int = 9600):
        self._com = com
        self._baudrate = baudrate
        self.ser = None  # Инициализируем атрибут для хранения объекта serial.Serial

    @property # декоратор который делает геттер вызвав ComPortWorker.com веренет какой у нас com
    def com(self):
        return self._com
    @property
    def baudrate(self):
        return self._baudrate

    # Открытие COM-порта
    def __open_com_port(self):
        print('открытие ком порта')
        try:
            self.ser = serial.Serial(self._com, self._baudrate, timeout=1)
            print(f"Подключено к {self._com}")
        except serial.SerialException as e:
            print(f"Ошибка подключения к {self._com}: {e}")

    #чтение из порта
    def __read_data(self):
        """
         Читает данные из последовательного порта.
        """
        print('читаем')

        if not self.ser or not self.ser.is_open: # Проверяем, открыт ли порт если нет открываем
            self.__open_com_port()  # открываем порт

        if self.ser and self.ser.is_open:  # Проверяем, открыт ли порт
            try:
                self._data = self.ser.readline().decode('utf-8').strip()  # Чтение строки данных

                if self.chack_data():
                    print(f"Получены данные: {self._data}")
                else:
                    print("Нет данных для чтения.")
            except Exception as e:
                print(f"Ошибка при чтении данных: {e}")
        else:
            print("Порт не открыт. Сначала откройте порт.")
            self.__open_com_port()

    def get_data(self) -> str:
        """
        возвращает данные полученные из копорта с помощью метода __read_data(self)
        :return: данные прочитанные из компорта
        """
        self.__read_data()
        try:
            if self.chack_data():
                return self._data
        except Exception as e:
            print(f"Ошибка при отправки данных в функции send_data() интерфейса InformationCollectorIntrface : {e}")


    #закрытие порта
    def close_com_port(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Порт закрыт.")
        else:
            print("Порт уже закрыт или не был открыт.")