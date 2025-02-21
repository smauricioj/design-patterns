"""
Módulo com exemplo de implementação do projeto padrão Observer

Autor: Sergio P.
Data: 18/11/2024
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class AbstractSubject(ABC):
    '''
    A interface de sujeito define os três métodos do padrão. Os observa-
    dores podem observar um sujeito (attach) e deixar de observar (det-
    tach). Além disso, é necessário um método para notificar (notify)
    todos os observadores quando há mudança no estado do sujeito.
    '''
    
    @abstractmethod
    def attach(self, obs: AbstractObserver) -> None:
        pass
    
    @abstractmethod
    def dettach(self, obs: AbstractObserver) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass    


class Subject(AbstractSubject):
    '''
    A versão concreta de um sujeito deve definir como os métodos funcio-
    nam. Aqui, os observadores são armazenados em uma lista, e o estado
    do sujeito é apenas um número.
    '''
    
    __observers : List[AbstractObserver]
    __state : int
    
    def __init__(self) -> None:
        self.__observers = []
        self.__state = 0
        
    def attach(self, obs: AbstractObserver) -> None:
        self.__observers.append(obs)
        
    def dettach(self, obs):
        return self.__observers.remove(obs)
    
    def notify(self) -> None:
        for obs in self.__observers:
            obs.update(self)
            
    def task(self) -> None:
        '''
        Dificilmente o padrão Observer é a totalidade da classe sujeito.
        Na prática, ela também realiza tarefas, integrada ao software
        completo, e quando seu estado é modificado ela notifica os ob-
        servadores (sistema push)
        '''
        self.__state = randrange(0, 10)
        self.notify()
        
    @property
    def state(self) -> int:
        return self.__state
 

class AbstractObserver(ABC):
    '''
    A interface de observadores requer apenas a declaração de uma reação
    à atualização do sujeito observado
    '''
        
    @abstractmethod
    def update(self, sbj: AbstractSubject):
        pass


class ObserverA(AbstractObserver):
    '''
    Diferentes observadores concretos, por sua vez, realizam reações di-
    ferentes ao estado atual do sujeito observado.
    '''
        
    def update(self, sbj: AbstractSubject) -> None:
        print(f'Reação do observador A ao estado atual: {sbj.state}')


class ObserverB(AbstractObserver):
    '''
    Esse é outro observador
    '''
        
    def update(self, sbj: AbstractSubject) -> None:
        print(f'Reação do observador B ao estado atual: {sbj.state}')
        
        
# Testes
def observer_tests() -> bool:
    sbj = Subject()    
    obs_a = ObserverA()
    sbj.attach(obs_a)
    obs_b = ObserverB()
    sbj.attach(obs_b)
    sbj.task()
    sbj.dettach(obs_b)
    sbj.task()
    return True
    
# Main
def main() -> None:
    assert(observer_tests())
    
if __name__ == "__main__":
    main()