"""
Módulo com exemplo do projeto padrão tipo Proxy

Autor: Sergio P.
Data: 21/02/2025
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    '''
    A interface do sujeito declara os métodos comuns entre o sujeito re-
    al e a proxy.
    '''
    
    @abstractmethod
    def task(self) -> None:
        pass
    
    
class RealSubject(AbstractSubject):
    '''
    O sujeito real é aquele objeto que realiza tarefas funcionais, gera-
    lmente de lentas, com alta demanda ou sensíveis. O padrão proxy vai
    nos ajudar a resolver esse problema.
    '''
    
    def task(self) -> None:
        print("Subject: Realizando algo super complicado")
        

class ProxySubject(AbstractSubject):
    '''
    A proxy implementa a mesma interface do sujeito
    '''
    
    _real_subject: RealSubject
    
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
        
    def task(self) -> None:
        '''
        A proxy pode modificar a operação do sujeito sem interferir no
        seu código. Por exemplo, autenticar acesso e registrar logs.
        '''
        
        if not self.authentication():
            print("Proxy: Usuário não autenticado! Fechando programa")
            exit()
        else:
            self.log_access()
            self._real_subject.task()
            
    def authentication(self) -> bool:
        print("Proxy: Autenticando acesso...")
        return True
    
    def log_acess(self) -> None:
        print("Proxy: Registrando log de acesso...")
        
def client(sbj: AbstractSubject) -> None:
    '''
    O cliente não sabe se está lidando com o sujeito real ou a proxy
    '''
    sbj.task()
    
# Teste
def proxy_test() -> bool:
    real_subject = RealSubject()
    proxy_subject = ProxySubject(real_subject)
    client(proxy_subject)
    return True
    
def main() -> None:
    assert(proxy_test())
    
if __name__ == "__main__":
    main()
    
    
    