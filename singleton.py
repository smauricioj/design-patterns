"""
Módulo com diversas implementações do projeto padrão do tipo Singleton

Autor: Sergio P.
Data: 10/11/2024
"""

from typing import Dict
from typing_extensions import Self
from threading import Lock, Thread

class SingletonLazy:
    '''
    SingletonLazy: construtor não cria uma instancia. Ao invés disso,
    um método de classe é usado como forma global de acesso à instância.    
    '''
    
    __instance: Self = None
            
    @classmethod
    def get_instance(cls) -> Self:
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance
    
# Teste SingletonLazy
def singleton_lazy_tests() -> bool: 
    s = SingletonLazy()
    ins1 = SingletonLazy.get_instance()
    ins2 = SingletonLazy.get_instance()
    assert(id(s) != id(ins1))
    assert(id(ins1) == id(ins2))
    return True


class SingletonMonostate:
    '''
    SingletonMonostate: múltiplas instâncias são permitidas,
    mas elas compartilham o mesmo estado dos atributos
    '''
    
    __estado : Dict = {}
    
    def __new__(cls, *args, **kwargs) -> Self:
        obj = super(SingletonMonostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
    
# Teste SingletonMonostate
def singleton_monostate_tests() -> bool:
    m1 = SingletonMonostate()
    m2 = SingletonMonostate()
    m1.foo = 'bar'
    assert(id(m1) != id(m2))
    assert(m2.foo == 'bar')
    return True


class SingletonMetaclass(type):
    '''
    SingletonMetaclass: Age através da herança,
    permitindo apenas uma instância de cada classe abaixo.
    '''
    
    __instances : Dict = {}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwds)
        return cls.__instances[cls]
    
    
class Logger(metaclass=SingletonMetaclass):
    pass

# Teste SingletonMetaclass
def singleton_metaclass_tests() -> bool:
    l1, l2 = Logger(), Logger()
    assert(id(l1) == id(l2))
    return True


class SingletonMetaclassMultiThread(type):
    '''
    SingletonMetaclassMultiThread: Em situações de várias threads,
    o singleton simples pode falhar. Assim, é necessária precaução
    e o uso do Lock para impedir a falha.
    '''
    
    __instances : Dict = {}
    __lock : Lock = Lock()
    
    def __call__(cls, *args, **kwds):
        with cls.__lock:
            '''
            A primeira thread que passar pela call vai adquirir o
            lock e criar a instância. Todas as outras até podem
            entrar em call e esperar pelo lock, mas quando passarem
            vão descobrir a instância criada e falhar no seguinte if
            '''
            if cls not in cls.__instances:
                cls.__instances[cls] = super(SingletonMetaclassMultiThread, cls).__call__(*args, **kwds)
        return cls.__instances[cls]
    
class LoggerMultiThread(metaclass=SingletonMetaclassMultiThread):
    '''
    Esse logger pode ser operado em multi threads e vai
    ter apenas uma instância, com apenas uma chave
    '''
    key: str = None
    
    def __init__(self, key: str) -> None:
        self.key = key
        
# Teste SingletonMetaclassMultiThread
def process(key: str) -> None:
    logger = LoggerMultiThread(key=key)
    print(logger.key)
    
def singleton_metaclass_multi_thread_test() -> bool:
    process1 = Thread(target=process, args=('foo',))
    process2 = Thread(target=process, args=('bar',))
    process1.start()
    process2.start()
    return True
    
# Main
def main() -> None:
    assert(singleton_lazy_tests())
    assert(singleton_monostate_tests())
    assert(singleton_metaclass_tests())
    assert(singleton_metaclass_multi_thread_test())
    
if __name__ == "__main__":
    main()