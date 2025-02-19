"""
Módulo com exemplo do projeto padrão do tipo Abstract Factory

Autor: Sergio P.
Data: 19/02/2025
"""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    
    @abstractmethod
    def use_a(self) -> None:
        pass


class AbstractProductB(ABC):
    
    @abstractmethod
    def use_b(self) -> None:
        pass


class ProductA1(AbstractProductA):
    
    def use_a(self) -> None:
        print("Realiza tarefa 'a', mas com características da família 1")


class ProductA2(AbstractProductA):
    
    def use_a(self) -> None:
        print("Realiza tarefa 'a', mas com características da família 2")


class ProductB1(AbstractProductB):
    
    def use_b(self) -> None:
        print("Realiza tarefa 'b', mas com características da família 1")


class ProductB2(AbstractProductB):
    
    def use_b(self) -> None:
        print("Realiza tarefa 'b', mas com características da família 2")
    

class AbstractFactory(ABC):
    
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
    
# Teste
def abstract_factory_tests() -> bool:
    f1 = Factory1()    
    pa1 = f1.createProductA()
    f2 = Factory2()
    pa2 = f2.createProductA()
    assert(issubclass(type(pa1), AbstractProductA))
    assert(issubclass(type(pa2), AbstractProductA))
    pb = f1.createProductB()
    assert(issubclass(type(pb), AbstractProductB))
    return True

# Main
def main() -> None:
    assert(abstract_factory_tests()) 
    
if __name__ == "__main__":
    main()