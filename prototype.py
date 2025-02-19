"""
Módulo com exemplo de implementação do projeto padrão Prototype

Autor: Sergio P.
Data: 20/11/2024
"""

from abc import ABC
from typing_extensions import Self

class Prototype(ABC):
    
    def __init__(self) -> None:
        pass
    
    def copy(self) -> Self:
        object = eval(type(self).__name__)
        newInstance = object.__new__(object)
        newInstance.__dict__ = self.__dict__.copy()
        return newInstance


class Product(Prototype):
        
    def __init__(self) -> None:
        super().__init__()
        self.foo = 1
        self.bar = 2


# Testes
def prototype_tests() -> bool:            
    protoproduct = Product()
    products = [protoproduct.copy() for _ in range(5)]    
    assert all([type(p) == Product for p in products])    
    for i, p1 in enumerate(products):
        for j, p2 in enumerate(products):
            if i != j:
                assert id(p1) != id(p2)
    return True
                
# Main
def main() -> None:
    assert(prototype_tests())
    
if __name__ == "__main__":
    main()