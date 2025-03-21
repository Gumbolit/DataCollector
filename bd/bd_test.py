from information_collector.com_port_worker import*
from information_sender.mqtt_sender import *
from stream_worker.stream_worker import StreamWorker
import sqlite3

class Sqllite_worker:

    def __init__(self, bd_name: str):
        """ Инициализация подключения к бд, надо ввести имя бд"""
        self._bd_name = bd_name
        self._conection = None
