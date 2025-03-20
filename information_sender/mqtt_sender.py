import paho.mqtt.client as mqtt
import socket  # Для обработки сетевых ошибок
from information_sender.sender_interface import *

# класс для работы с брокером может быть абстрактным для каких-то наследников
class MqttSender(SenderIntrface):
    def __init__(self, topic: str, broker: str = 'mqtt.eclipseprojects.io', port: int = 1883):
        self._broker = broker
        self._port = port
        self._topic = topic
        self.client = None  # Инициализируем атрибут для хранения объекта mqtt.Client()
        self._is_connected = False  # Флаг для отслеживания состояния подключения

    @property  # декоратор который делает геттер
    def topic(self):
        return self._topic
    @property
    def broker(self):
        return self._broker
    @property
    def port(self):
        return self._port
    @property
    def is_connected(self):
        return self._is_connected

    #Подключение к брокеру
    def connection_to_server(self):
        """
        подключение к брокеру

        """
        #создаем клиента не знаю правильно ли что тут
        self.client = mqtt.Client()
        print("подключаемся к брокеру")

        try:
            self.client.connect(self._broker, self._port, 60)
            print(f"Подключено к {self._broker}")
            self._is_connected = True
        except (socket.error, ConnectionError) as e:
            print(f"Ошибка при подключении к {self._broker}: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка приподключении к {self._broker}: {e}")

    # Публикуем сообщение в топик
    def send_to_server(self, message: str):

        # Проверяем, установлено ли подключение
        if not self._is_connected:
            print("Подключение не установлено. Пытаемся подключиться...")
            self.connection_to_server()  # Вызываем connect, если подключение отсутствует

        if self._is_connected:  #проверяем есть ли подключение
            try:
                self.client.publish(self._topic, message)
                print(f"Сообщение отправлено в топик '{self._topic}': {message}")
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")
        else:
            print("Не удалось подключиться к брокеру. Сообщение не отправлено.")

    def end_connection_to_server(self):
        if self._is_connected:
            try:
                self.client.disconnect(self._broker, self._port)
                print(f"Подключено к {self._broker}")
            except Exception as e:
                print(f"Неизвестная ошибка при отключении от {self._broker}: {e}")
