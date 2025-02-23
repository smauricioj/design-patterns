"""
Módulo com exemplo do projeto padrão do tipo Command

Autor: Sergio P.
Data: 19/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class AbstractCommand(ABC):
    '''
    Interface de comando abstrato que declara um método de execução
    '''
    
    @abstractmethod
    def execute(self) -> None:
        pass
    

class SimpleCommand(AbstractCommand):
    '''
    Comandos simples podem implementar o código associado à uma tarefa
    sozinhos
    '''
            
    def execute(self) -> None:
        print(f"Fazendo algo simples, com foo = {self._foo}")
        
class ComplexCommand(AbstractCommand):
    '''
    Tarefas mais complexas são delegadas para outras classes, chamadas
    receivers, onde a operação lógica fica implementada
    '''
    
    def __init__(self, receiver: Receiver) -> None:
        self._receiver : Receiver = receiver
        self._params : list = [1, 2, 3]
        
    def execute(self) -> None:
        print("Fazendo algo complexo, com auxílio de um receiver!")
        self._receiver.task(self._params)
        

class Receiver:
    '''
    Receivers implementam as operações lógicas associadas aos comandos.
    '''
    
    def task(self, params: list) -> None:
        print(f"Receiver faz algo com params = {params}")
        

class Invoker:
    '''
    Invokers agem como um intermédio entre comandos e receivers, sem de-
    pender diretamente das suas versões concretas. Eles repassa um coma-
    ndo ao receiver de forma indireta, através da execução!
    
    Aqui, esse é um exemplo de invoker que "protege" uma tarefa de outr-
    as, que devem vir antes e depois.
    '''
    
    def __init__(self) -> None:
        self._before: List[AbstractCommand] = []
        self._after: List[AbstractCommand] = []
        
    def append_command_before(self, cmd: AbstractCommand) -> None:
        self._before.append(cmd)
        
    def append_command_after(self, cmd: AbstractCommand) -> None:
        self._after.append(cmd)
        
    def do_something_important(self) -> bool:
        if self._before:
            for cmd in self._before:
                cmd.execute()
            self._before.clear()
        print('-- Invoker fazendo algo "protegido" --')
        if self._after:
            for cmd in self._after:
                cmd.execute()
            self._after.clear()
        return True

# Testes
def command_tests() -> bool:    
    ivk, rcv = Invoker(), Receiver()
    ivk.append_command_before(SimpleCommand())
    ivk.append_command_after(ComplexCommand(receiver=rcv))                             
    return ivk.do_something_important()
    
# Main
def main() -> None:
    assert(command_tests())
    
if __name__ == "__main__":
    main()
    