"""
Módulo com uma implementação do projeto padrão Prototype

Autor: Sergio P.
Data: 20/11/2024
"""

from abc import ABCMeta

class Prototype(metaclass=ABCMeta):
    
    def copy(self):
        object = eval(type(self).__name__)
        newInstance = object.__new__(object)
        newInstance.__dict__ = self.__dict__.copy()
        return newInstance
    
# Testes
if __name__ == "__main__":
    
       
    class Product(Prototype):
        ''' Recebe o método copy via herança '''
        
        def __init__(self):
            self.foo = 1
            self.bar = 2
            
    protoproduct = Product()
    products = [protoproduct.copy() for _ in range(5)]    
    assert all([type(p) == Product for p in products])    
    for i, p1 in enumerate(products):
        for j, p2 in enumerate(products):
            if i != j:
                assert id(p1) != id(p2)
        
    