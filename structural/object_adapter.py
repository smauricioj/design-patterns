"""
Módulo com exemplo do projeto padrão tipo Object Adapter

Autor: Sergio P.
Data: 27/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Target(ABC):
    
    @abstractmethod
    def task(self) -> None:
        pass    
        
    
class Adaptee:
    
    def unusable_task(self) -> str:
        return 'levázilitu oãn sam ,etnatropmi ogla oçaF'
    

class Adapter(Target):
    
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee
        
    def task(self) -> None:        
        print(f'{self._adaptee.unusable_task()[::-1]}')
    

def object_adapter_test() -> None:
    adaptee = Adaptee()
    print(adaptee.unusable_task())
    adapter = Adapter(adaptee=adaptee)
    adapter.task()
    return True

# Main
def main() -> None:
    assert(object_adapter_test())
    
if __name__ == "__main__":
    main()