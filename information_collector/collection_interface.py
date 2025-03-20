from abc import ABC, abstractmethod

# возможное улучшение с помощью шаблона "Стратегия" (Strategy Pattern) для обработки данных.
class CollectorIntrface(ABC):
    """
    в наследнике обязательно поле _data
    и функции chack_data и send_data
    """

    _data: str = None  # Поле для полученной данных

    def check_data(self):
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

