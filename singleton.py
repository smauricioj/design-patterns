"""
Módulo com diversas implementações do projeto padrão do tipo Singleton

Autor: Sergio P.
Data: 10/11/2024
"""

class SingletonLazy:
    '''
    SingletonLazy: construtor não cria uma instancia. Ao invés disso,
    um método de classe é usado como forma global de acesso à instância.    
    '''
    
    __instance = None
            
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance
    
# Teste SingletonLazy
def singleton_lazy_tests() -> bool:   
    print('SingletonLazy tests: --------------------------------------------------') 
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
    
    __estado : dict = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(SingletonMonostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
    
# Testes SingletonMonostate

def singleton_monostate_tests() -> bool:
    print('SingletonMonostate tests: --------------------------------------------------')
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
    __instances = {}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwds)
        return cls.__instances[cls]
    
    
class Logger(metaclass=SingletonMetaclass):
    pass

# Testes SingletonMetaclass
def singleton_metaclass_tests() -> bool:
    print('SingletonMetaclass tests: --------------------------------------------------')
    l1, l2 = Logger(), Logger()
    assert(id(l1) == id(l2))
    return True
    
# Main
def main() -> None:
    assert(singleton_lazy_tests())
    assert(singleton_monostate_tests())
    assert(singleton_metaclass_tests())
    
if __name__ == "__main__":
    main()