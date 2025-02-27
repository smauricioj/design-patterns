"""
Módulo com exemplo do projeto padrão tipo Builder

Autor: Sergio P.
Data: 21/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, List


class AbstractBuilder(ABC):
    '''
    A interface Builder declara os métodos para criação de diferentes
    partes de um produto
    '''
    
    @property
    @abstractmethod
    def product(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_a(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_b(self) -> None:
        pass
    
    @abstractmethod
    def produce_part_c(self) -> None:
        pass
    
    
class Builder1(AbstractBuilder):
    '''
    Um Builder concreto implementa os passos de construção de um produto
    Diferentes Builders podem construir diferentes produtos, por isso
    não existe uma interface abstrata de produtos
    
    Tipicamente, Builders automaticamente resetam seu produto após ex-
    portarem o seu resultado para o cliente, como implementado nesse có-
    digo.
    '''
    
    def __init__(self) -> None:
        '''
        Cada instância de um builder deve começar um produto do zero
        '''
        self.reset()
        
    def reset(self) -> None:
        self._product = Product1()
        
    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product
    
    def produce_part_a(self) -> None:
        self._product.add("part_a")
    
    def produce_part_b(self) -> None:
        self._product.add("part_b")
    
    def produce_part_c(self) -> None:
        self._product.add("part_c")
       

class Product1():
    '''
    Produtos no padrão Builder são geralmente extensos e complexos, com
    diversas etapas e partes. Além disso, diferentes builders constroem
    diferentes e não relacionados produtos (sem interface comum)
    '''
    
    Part = TypeVar("Part")
    _parts: List[Part]
    
    def __init__(self) -> None:
        self._parts = []
        
    def add(self, part: Part) -> None:
        self._parts.append(part)
        
    def list_parts(self) -> None:
        print(f'Partes do produto: {', '.join(self._parts)}')
        
class Director:
    '''
    (opcional, mas util)
    O diretor é um objeto responsável por dirigir o builder e realizar
    construções que seguem um padrão, sequência ou diretriz
    '''
    
    def __init__(self) -> None:
        self._builder = None
        
    @property
    def builder(self) -> AbstractBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: AbstractBuilder) -> None:
        '''
        Um diretor pode trabalhar com diferentes builders, flexibilizan-
        do a operação
        '''
        
        self._builder = builder
        
    def build(self, kind:str = 'small') -> None:
        if kind == 'small':
            self.builder.produce_part_a()
        else:
            self.builder.produce_part_a()
            self.builder.produce_part_b()
            self.builder.produce_part_c()
        
# Teste
def builder_test() -> bool:
    director = Director()
    builder = Builder1()
    director.builder = builder
    
    # Faz um produto pequeno
    director.build(kind='small')
    builder.product.list_parts()
    
    # Faz um produto grande
    director.build(kind='large')
    builder.product.list_parts()
    
    # Deu tudo certo!
    return True

def main() -> None:
    assert(builder_test())
    
if __name__ == "__main__":
    main()