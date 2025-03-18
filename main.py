from information_collector.com_port_worker import*
from information_sender.mqtt_sender import *


com =ComPortWorker('COM3')
sender = MqttSender('test/topic190A','mqtt.eclipseprojects.io',1883)

try:

        sender.conect_to_broker()
        while True:
            data = com.get_data()
            if data:
                sender.publish_in_topik(data)
                print(data)

            else:
                print("Ожидание данных...")
except KeyboardInterrupt:
        com.close_com_port()
        sender.close_broker()
        print("Программа остановлена пользователем.")