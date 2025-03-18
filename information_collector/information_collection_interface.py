from abc import ABC, abstractmethod


class InformationCollectorIntrface(ABC):
    """
    в наследнике обязательно поле _data
    и функции chack_data и send_data
    """

    _data: str = None  # Поле для полученной данных

    def chack_data(self):
        if self._data==None:
             return False
        else: return True

    @abstractmethod  #декоратор который обязывает наследников реализовать метод получения данных
    def get_data(self)->str:
        """
        вызываем через созданный экземпляр класса наследника интерфейса InformationCollectorIntrface
        :return: данные полученные внутри класса наследника
        """
        pass

