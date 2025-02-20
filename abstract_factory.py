"""
Módulo com exemplo do projeto padrão do tipo Abstract Factory

Autor: Sergio P.
Data: 19/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    '''
    A interface de fábrica abstrata declara um conjunto de métodos
    que retornam diferentes produtos. Esse conjunto de produtos é
    chamado de família e estão relacionados por algum conceito de
    alto nível.
    '''
    
    @abstractmethod
    def createProductA(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def createProductB(self) -> AbstractProductB:
        pass
    
    
class Factory1(AbstractFactory):
    '''
    A fábrica concreta produz uma família específica de produtos,
    garantindo consistência e compatibilidade entre produtos.
    '''
    
    def createProductA(self) -> AbstractProductA:
        return ProductA1()
    
    def createProductB(self) -> AbstractProductB:
        return ProductB1()
    
    
class Factory2(AbstractFactory):
    '''
    Essa é outra família de produtos.
    '''
    
    def createProductA(self) -> AbstractProductA:
        return ProductA2()
    
    def createProductB(self) -> AbstractProductB:
        return ProductB2()
    

class AbstractProductA(ABC):
    '''
    Cada possível produto requer uma interface prória
    As diferentes famílias irão concretizar essa interface
    '''
    
    @abstractmethod
    def use_a(self) -> None:
        pass


class AbstractProductB(ABC):
    '''
    Esse é outro produto. Ele é diferente pois tem também
    um método de interação.
    '''
    
    @abstractmethod
    def use_b(self) -> None:
        pass
    
    @abstractmethod
    def interact(self, other: AbstractProductA) -> None:
        '''
        Um produto pode interagir com outro, da mesma família,
        para realizar tarefas mais complexas.
        '''
        pass
    
# Cada família deve ter a sua versão concreta dos produtos!
# Família 1


class ProductA1(AbstractProductA):
    
    def use_a(self) -> None:
        print("Realiza tarefa 'a' com características da família 1")


class ProductB1(AbstractProductB):
    
    def use_b(self) -> None:
        print("Realiza tarefa 'b' com características da família 1")
        
    def interact(self, other: AbstractProductA):
        '''
        Esse produto B é da família 1, então "other" deve ser também.
        Ainda assim, o argumento é genérico.
        '''
        print("Produto B interage com produto A")
        other.use_a()

# Família 2


class ProductA2(AbstractProductA):
    
    def use_a(self) -> None:
        print("Realiza tarefa 'a' com características da família 2")


class ProductB2(AbstractProductB):
    
    def use_b(self) -> None:
        print("Realiza tarefa 'b' com características da família 2")
        
    def interact(self, other: AbstractProductA):
        print("Produto B interage com produto A")
        other.use_a()
    
    
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