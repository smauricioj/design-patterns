"""
Módulo com exemplo do projeto padrão do tipo Command

Autor: Sergio P.
Data: 19/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    '''
    Interface de comando abstrato que declara um método de execução
    '''
    
    @abstractmethod
    def execute(self) -> None:
        pass
    

class SimpleCommand(Command):
    '''
    Comandos simples podem implementar o código associado 
    à uma tarefa sozinhos
    '''
    
    def __init__(self, foo: str) -> None:
        self._foo = foo
        
    def execute(self) -> None:
        print(f"Fazendo algo simples, com foo = {self._foo}")
        
class ComplexCommand(Command):
    '''
    Tarefas mais complexas são delegadas para outras classes,
    chamadas receivers, onde a operação lógica fica implementada
    '''
    
    def __init__(self, receiver: Receiver, foo: str, bar: str) -> None:
        self._receiver = receiver
        self._foo = foo
        self._bar = bar
        
    def execute(self) -> None:
        print("Fazendo algo complexo, com auxílio de um receiver!")
        self._receiver.task_a(self._foo)
        self._receiver.task_b(self._bar)
        

class Receiver:
    '''
    Receivers implementam as operações lógicas associadas aos comandos.
    '''
    
    def task_a(self, foo: str) -> None:
        print(f"Receiver faz algo com foo = {foo}")
    
    def task_b(self, bar: str) -> None:
        print(f"Receiver faz outro algo com bar = {bar}")
        

class Invoker:
    '''
    Invokers agem como um intermédio entre comandos e receivers, sem
    depender diretamente das suas versões concretas. Eles repassa um
    comando ao receiver de forma indireta, através da execução!
    
    Aqui, esse é um exemplo de invoker que "protege" uma tarefa de
    outras, que devem vir antes e depois.
    '''
    
    def __init__(self) -> None:
        self._before: list[Command] = []
        self._after: list[Command] = []
        
    def append_command_before(self, cmd: Command) -> None:
        self._before.append(cmd)
        
    def append_command_after(self, cmd: Command) -> None:
        self._after.append(cmd)
        
    def do_something_important(self) -> None:
        if self._before:
            for cmd in self._before:
                cmd.execute()
            self._before.clear()
        print('-- Invoker fazendo algo "protegido" --')
        if self._after:
            for cmd in self._after:
                cmd.execute()
            self._after.clear()

# Testes
def command_tests() -> bool:
    
    ivk = Invoker()
    ivk.append_command_before(SimpleCommand(foo='abc'))
    rcv = Receiver()
    ivk.append_command_after(ComplexCommand(receiver=rcv, foo='abc', bar='123'))
    ivk.do_something_important()
    return True
    
# Main
def main() -> None:
    assert(command_tests())
    
if __name__ == "__main__":
    main()
    