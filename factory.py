"""
Módulo com exemplo do projeto padrão tipo Factory Method

Autor: Sergio P.
Data: 18/11/2024
"""

from abc import ABC, abstractmethod
from typing import Dict
from typing_extensions import Self

class AbstractProduct(ABC):
    '''
    Uma interface comum para diferentes tipos de produtos define uma
    propriedade abstrata 'foo'
    
    Por minha sanidade, eu usei prototype para geração dos múltiplos
    produtos... mas não é necessário.
    '''
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
    '''
    Um tipo A de produto concreto a ser produzido na fábrica
    '''
        
    @property
    def foo(self) -> str:
        return 'foo'

  
class ProductB(AbstractProduct):
    '''
    Outro tipo B de produto concreto a ser produzido na fábrica
    '''
        
    @property
    def foo(self) -> str:
        return 'bar'


class AbstractCreator(ABC):
    '''
    A entidade criadora de produtos define uma interface com um método
    abstrado de criação. Importante que o retorno do método é definido
    como um produto abstrato também.
    '''
    
    @abstractmethod
    def factoryMethod(self) -> AbstractProduct:
        pass
     

class Creator(AbstractCreator):
    '''
    O criador concreto define como o método de fabricação é responsável
    por instanciar os produtos corretos. Aqui, eu usei o padrão protóti-
    po para instanciar os produtos partir de uma tabela hash... mas não
    é necessário
    '''
    
    __prototypes : Dict[str, AbstractProduct] = {}
    
    def __init__(self) -> None:
        self.__prototypes['A'] = ProductA()
        self.__prototypes['B'] = ProductB()

    def factoryMethod(self, product:str) -> AbstractProduct:
        return self.__prototypes[product].copy()

    
# Teste
def factory_method_tests() -> bool:
    c = Creator()
    pa1 = c.factoryMethod(product='A')
    pa2 = c.factoryMethod(product='A')
    pb1 = c.factoryMethod(product='B')
    assert id(pa1) != id(pa2)
    assert type(pa1) != type(pb1)
    return True
    
# Main
def main() -> None:
    assert(factory_method_tests())
    
if __name__ == "__main__":
    main()