from __future__ import annotations


class Facade:
    '''
    A Facade forcene uma interface simplificada para um conjunto comple-
    to de subsistemas. Isso barra o acesso do cliente aos subsistemas e
    simplifica o seu entendimento
    '''
    
    def __init__(self) -> None:
        '''
        Os subsistemas estão aqui instanciados na inicialização, mas
        também podem ser passados como argumentos na construção se ne-
        cessário
        '''
        self._subsystemA: SubsystemA = SubsystemA()
        self._subsystemB: SubsystemB = SubsystemB()
        
    def operation(self) -> bool:
        '''
        Uma operação complexa que o cliente fica abstraído e separado
        '''
        results: list = []
        results.append(self._subsystemA.operation1())
        results.append(self._subsystemA.operation2())
        results.append(self._subsystemB.operation3())
        results.append(self._subsystemB.operation4())
        return all(results)


class SubsystemA:
    '''
    Um subsistema com diversas operações
    '''
    
    def operation1(self) -> bool:
        return True
    
    def operation2(self) -> bool:
        return True


class SubsystemB:
    '''
    Outro subsistema, que organização complexa!
    '''
    
    def operation3(self) -> bool:
        return True
    
    def operation4(self) -> bool:
        return True
    
# Testes
def facade_test() -> bool:
    '''
    O código do cliente é super simples
    '''
    facade = Facade()
    assert(facade.operation())
    
# Main
def main() -> None:
    assert(facade_test())
    
if __name__ == "__main__":
    main()
        