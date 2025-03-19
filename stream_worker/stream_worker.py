import threading
import time
from information_collector.com_port_worker import*
from information_sender.mqtt_sender import MqttSender

class ComPortReader(threading.Thread):
    def __init__(self, com: ComPortWorker, sender: MqttSender):
        super().__init__()
        self.com = com
        self.sender = sender
        self._stop_event = threading.Event()  # Событие для остановки потока

    def run(self):
        """Основные метод, который выполняется в потоке."""
        while not self._stop_event.is_set():
            try:
                self.sender.conect_to_broker()
                data = self.com.get_data()
                if data:
                   self.sender.publish_in_topik(data)
                   print(data)
                else:
                   print("Ожидание данных...")
                print(f"Data from {self.com.com}: {data}")
            except KeyboardInterrupt:
                self.com.close_com_port()
                self.sender.close_broker()
                print("Программа остановлена пользователем.")

    def stop(self):
        """Останавливает поток."""
        self._stop_event.set()
