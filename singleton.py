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
    
# Testes SingletonLazy

if __name__ == "__main__":    
    print('SingletonLazy tests: --------------------------------------------------') 
    s1 = SingletonLazy()
    print('Objeto não instanciado')
    ins = SingletonLazy.get_instance()
    print('Objeto criado agora!')
    print(id(s1))
    print(id(ins))


class SingletonMonostate:
    '''
    SingletonMonostate: múltiplas instâncias são permitidas,
    mas elas compartilham o mesmo estado dos atributos
    '''
    
    __estado = {}
    
    def __new__(cls, *args, **kwargs):
        obj = super(SingletonMonostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj
    
# Testes SingletonMonostate

if __name__ == "__main__":
    print('SingletonMonostate tests: --------------------------------------------------')
    m1 = SingletonMonostate()
    print(f'M1 ID: {id(m1)}')
    print(m1.__dict__)
    m2 = SingletonMonostate()
    print(f'M2 ID: {id(m2)}')
    print(m2.__dict__)
    m1.nome = 'Felicity'
    print(m1.__dict__)
    print(m2.__dict__)


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


# Testes SingletonMetaclass
if __name__ == "__main__":
    print('SingletonMetaclass tests: --------------------------------------------------')
    
    
    class Logger(metaclass=SingletonMetaclass):
        pass

    l1 = Logger()
    l2 = Logger()
    print(f'l1: {id(l1)}')
    print(f'l2: {id(l2)}')
    
    
    class ConfigData(metaclass=SingletonMetaclass):
        pass
    
    c1 = ConfigData()
    c2 = ConfigData()
    print(f'c1: {id(c1)}')
    print(f'c2: {id(c2)}')
    