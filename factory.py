"""
Módulo com diversas implementações do projeto padrão do tipo Factory

Autor: Sergio P.
Data: 18/11/2024
"""

from abc import ABCMeta, abstractmethod

# Factory Method #########################################

class AbstractProduct(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def foo(self):
        pass
    
    def copy(self):
        ''' Projeto padrão Prototype'''
        object = eval(type(self).__name__)
        copy = object.__new__(object)
        copy.__dict__ = self.__dict__
        return copy


class ProductA(AbstractProduct):
        
    @property
    def foo(self):
        return 'foo'

  
class ProductB(AbstractProduct):
        
    @property
    def foo(self):
        return 'bar'


class AbstractCreator(metaclass=ABCMeta):
    
    @abstractmethod
    def factoryMethod(self) -> AbstractProduct:
        raise NotImplementedError()
     

class Creator(AbstractCreator):
    
    __prototypes : dict = {}
    
    def __init__(self):
        self.__prototypes['ProductA'] = ProductA()
        self.__prototypes['ProductB'] = ProductB()

    def factoryMethod(self, product:str) -> AbstractProduct:
        return self.__prototypes[product].copy()

    
# Testes de Factory Method

if __name__ == '__main__':
    print('Testes Factory Method --------------------------')
    c = Creator()
    pa1 = c.factoryMethod(product='ProductA')
    pa2 = c.factoryMethod(product='ProductA')
    pb = c.factoryMethod(product='ProductB')
    assert id(pa1) != id(pa2)
    assert type(pa1) != type(pb)

# Abstract Factory #########################################

class AbstractProductA(metaclass=ABCMeta):
    pass


class ProductA1(AbstractProductA):
    
    def __repr__(self):
        return 'Product of type A, family 1'


class ProductA2(AbstractProductA):
    
    def __repr__(self):
        return 'Product of type A, family 2'


class AbstractProductB(metaclass=ABCMeta):
    pass


class ProductB1(AbstractProductB):
    
    def __repr__(self):
        return 'Product of type B, family 1'


class ProductB2(AbstractProductB):
    
    def __repr__(self):
        return 'Product of type B, family 2'
    

class AbstractFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def createProductA(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def createProductB(self) -> AbstractProductB:
        pass
    
    
class Factory1(AbstractFactory):
    
    def createProductA(self):
        return ProductA1()
    
    def createProductB(self):
        return ProductB1()
    
    
class Factory2(AbstractFactory):
    
    def createProductA(self):
        return ProductA2()
    
    def createProductB(self):
        return ProductB2()
    
# Testes Abstract Factory
if __name__ == '__main__':
    print("Testes Abstract Factory -------------------------")
    f1 = Factory1()    
    pa1 = f1.createProductA()
    f2 = Factory2()
    pa2 = f2.createProductA()    
    print(pa1)
    print(pa2)