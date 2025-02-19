"""
Módulo com exemplo do projeto padrão do tipo Abstract Factory

Autor: Sergio P.
Data: 19/02/2025
"""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    pass


class ProductA1(AbstractProductA):
    
    def __repr__(self):
        return 'Product of type A, family 1'


class ProductA2(AbstractProductA):
    
    def __repr__(self):
        return 'Product of type A, family 2'


class AbstractProductB(ABC):
    pass


class ProductB1(AbstractProductB):
    
    def __repr__(self):
        return 'Product of type B, family 1'


class ProductB2(AbstractProductB):
    
    def __repr__(self):
        return 'Product of type B, family 2'
    

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
    
# Testes Abstract Factory
def abstract_factory_tests() -> bool:
    print("Testes Abstract Factory -------------------------")
    f1 = Factory1()    
    pa1 = f1.createProductA()
    f2 = Factory2()
    pa2 = f2.createProductA()
    assert(issubclass(type(pa1), AbstractProductA))
    assert(issubclass(type(pa2), AbstractProductA))
    return True

# Main #################################################

def main() -> None:
    assert(abstract_factory_tests()) 
    
if __name__ == "__main__":
    main()