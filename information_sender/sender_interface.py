from abc import ABC, abstractmethod


# возможное улучшение с помощью шаблона "Стратегия" (Strategy Pattern) для обработки данных.
class SenderIntrface(ABC):
    """
    в наследнике обязательно поле _data
    и функции chack_data и send_data
    """

    _is_connected: bool = False  # Поле для полученной данных

    @property
    @abstractmethod
    def is_connected(self):
        return self._is_connected


    @abstractmethod  # декоратор который обязывает наследников реализовать метод получения данных
    def connection_to_server(self) -> str:
        """
        вызываем через созданный экземпляр класса наследника интерфейса InformationCollectorIntrface
        :return: данные полученные внутри класса наследника
        """
        pass


    @abstractmethod  #декоратор который обязывает наследников реализовать метод получения данных
    def send_to_server(self)->str:
        """
        вызываем через созданный экземпляр класса наследника интерфейса InformationCollectorIntrface
        :return: данные полученные внутри класса наследника
        """
        pass

    @abstractmethod  # декоратор который обязывает наследников реализовать метод получения данных
    def end_connection_to_server(self)->str:
        """
        вызываем через созданный экземпляр класса наследника интерфейса InformationCollectorIntrface
        :return: данные полученные внутри класса наследника
        """
        pass
