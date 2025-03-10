"""
Módulo com exemplo do projeto padrão tipo Bridge

Autor: Sergio P.
Data: 27/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    '''
    A abstração é a parte do código que não realiza trabalho, apenas de-
    fine as estruturas que o cliente pode utilizar. Ela mantem um regis-
    tro da implementação que irá realizar a operação, e pode atualizar 
    esse registro em tempo de execução (agregação).
    '''
    
    def __init__(self, imp: Implementation) -> None:
        self._imp = imp
        
    def set_implementation(self, imp: Implementation) -> None:
        ''' Agregação '''
        self._imp = imp
        
    def operation(self) -> None:
        self._imp.operation_imp()        
        
        
class RefinedAbstraction(Abstraction):
    '''
    Uma versão refinada que extende a abstração. É opcional, mas geral-
    mente utilizada.
    '''
    
    def refined_operation(self) -> None:
        print('Eu faço melhor! Ou diferente?')
        self._imp.operation_imp()
    

class Implementation(ABC):
    '''
    A implementação, nesse padrão, é uma interface que define quais são
    as operações que devem ser implementadas pelas versões concretas. A
    abstração pode fazer uso de qualquer implementação concreta e, in-
    clusive, mudar de implementações em tempo de execução.
    '''
    
    @abstractmethod
    def operation_imp(self) -> None:
        pass
    
    
class ConcreteImpA(Implementation):
    
    def operation_imp(self) -> None:
        print('Implementação da operação no estilo A')
        
    
class ConcreteImpB(Implementation):
    
    def operation_imp(self) -> None:
        print('Implementação da operação no estilo B')        
    

def bridge_test() -> None:
    a = Abstraction(imp=ConcreteImpA())
    a.operation()
    a.set_implementation(imp=ConcreteImpB())
    a.operation()
    a = RefinedAbstraction(imp=ConcreteImpA())
    a.refined_operation()
    return True

# Main
def main() -> None:
    assert(bridge_test())
    
if __name__ == "__main__":
    main()