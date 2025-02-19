"""
Módulo com diversas implementações do projeto padrão do tipo Factory

Autor: Sergio P.
Data: 18/11/2024
"""

from abc import ABC, abstractmethod
from typing import Dict
from typing_extensions import Self

class AbstractProduct(ABC):
    
    @property
    @abstractmethod
    def foo(self):
        pass
    
    def copy(self) -> Self:
        '''
        Método do Projeto Padrão Prototype
        '''
        object = eval(type(self).__name__)
        newInstance = object.__new__(object)
        newInstance.__dict__ = self.__dict__.copy()
        return newInstance


class ProductA(AbstractProduct):
    
    def __init__(self) -> None:
        pass
        
    @property
    def foo(self) -> str:
        return 'foo'

  
class ProductB(AbstractProduct):
    
    def __init__(self) -> None:
        pass
        
    @property
    def foo(self) -> str:
        return 'bar'


class AbstractCreator(ABC):
    
    @abstractmethod
    def factoryMethod(self) -> AbstractProduct:
        pass
     

class Creator(AbstractCreator):
    
    __prototypes : Dict[str, AbstractProduct] = {}
    
    def __init__(self) -> None:
        self.__prototypes['ProductA'] = ProductA()
        self.__prototypes['ProductB'] = ProductB()

    def factoryMethod(self, product:str) -> AbstractProduct:
        return self.__prototypes[product].copy()

    
# Teste
def factory_method_tests() -> bool:
    c = Creator()
    pa1 = c.factoryMethod(product='ProductA')
    pa2 = c.factoryMethod(product='ProductA')
    pb1 = c.factoryMethod(product='ProductB')
    assert id(pa1) != id(pa2)
    assert type(pa1) != type(pb1)
    return True
    
# Main
def main() -> None:
    assert(factory_method_tests())
    
if __name__ == "__main__":
    main()