from information_collector.com_port_worker import*
from information_sender.mqtt_sender import *
from stream_worker.stream_worker import ComPortReader

com3 = ComPortWorker('COM3')
sender3 = MqttSender('test/topic190A','mqtt.eclipseprojects.io',1883)

com4 = ComPortWorker('COM5')
sender4 = MqttSender('test/topic190A2','mqtt.eclipseprojects.io',1883)

thread1 = ComPortReader(com3, sender3)
thread1.start()

thread2 = ComPortReader(com4, sender4)
thread2.start()



"""
try:

        sender3.conect_to_broker()
        while True:
            data = com3.get_data()
            if data:
                sender3.publish_in_topik(data)
                print(data)

            else:
                print("Ожидание данных...")
except KeyboardInterrupt:
        com3.close_com_port()
        sender3.close_broker()
        print("Программа остановлена пользователем.")
"""