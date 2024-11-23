"""
Módulo com uma implementação do projeto padrão Observer

Autor: Sergio P.
Data: 18/11/2024
"""

from abc import ABCMeta, abstractmethod


class AbstractObject(metaclass=ABCMeta):
    
    __observers : list
    
    def __init__(self):
        self.__observers = []
    
    @property
    def observers(self):
        return [type(valor).__name__ for valor in self.__observers]
    
    def register(self, observer) -> None:
        self.__observers.append(observer)
        return None
        
    def unregister(self, observer) -> None:
        return self.__observers.remove(observer)
        
    def notify(self) -> None:
        assert [o.notify() for o in self.__observers]
        return None

class Object(AbstractObject):
    
    __state : int
    
    def __init__(self):
        super().__init__()
        self.__state = 0

    @property
    def state(self) -> int:
        return int(self.__state)
    
    @state.setter
    def state(self, value : int) -> None:
        self.__state = int(value)
        return None
 

class Observer(metaclass=ABCMeta):
    
    def __init__(self, object : Object):
        self.object = object
        self.object.register(self)
        
    @abstractmethod
    def notify(self):
        pass


class ObserverA(Observer):
        
    def notify(self):
        print(f'Reação (tipo A) à notificação que o estado atual é: {self.object.state}')
        return True


class ObserverB(Observer):
        
    def notify(self):
        print(f'Reação (tipo B) à notificação que o estado atual é: {self.object.state}')
        return True
        
# Testes
if __name__ == '__main__':
    obj = Object()    
    ObserverA(obj)
    ObserverB(obj)
    obj.state = 3
    obj.notify()