"""
Modelo de controle do tráfego

Autor: Sergio P.
Data: 10/11/2024
"""

from abc import ABC, abstractmethod
from datetime import datetime
from singleton import SingletonMetaclass


# Sensor Abstrato
class TrafficSensor(ABC):
    
    __kind = None
    
    def __init__(self, kind:str):
        self.__kind = kind
        
    @abstractmethod
    def collectData(self):
        pass
    

# Sensor concreto, família urbana
class UrbanTrafficSensor(TrafficSensor):
    
    def __init__(self):
        super().__init__('urban')
        
    def collectData(self) -> dict:
        print('Rotina de coleção de dados de um sensor urbano')
        return {}
    

# Sensor concreto, família rodoviária
class HighwayTrafficSensor(TrafficSensor):
    
    def __init__(self):
        super().__init__('highway')
        
    def collectData(self) -> dict:
        print('Rotina de coleção de dados de um sensor rodoviário')
        return {}
        

# Atuador abstrato
class TrafficActuator(ABC):
    
    __kind : str = None
    
    def __init__(self, kind:str):
        self.__kind = kind
        
    @abstractmethod
    def performAction(self):
        pass


# Atuador concreto, família urbana
class UrbanTrafficActuator(TrafficActuator):
    
    def __init__(self):
        super().__init__('urban')
        
    def performAction(self):
        print('Rotina de atuação em um atuador urbano')
        return None
        

# Atuador concreto, família rodoviária
class HighwayTrafficActuator(TrafficActuator):
    
    def __init__(self):
        super().__init__('highway')
        
    def performAction(self):
        print('Rotina de atuação em um atuador rodoviário')
        return None

    
# Fábrica abstrata
class DeviceFactory(ABC):
    
    @abstractmethod
    def createSensor(self) -> TrafficSensor:
        pass
    
    @abstractmethod
    def createActuator(self) -> TrafficActuator:
        pass


# Fábrica concreta, família urbana
class UrbanDeviceFactory(DeviceFactory):
    
    def createSensor(self):
        return UrbanTrafficSensor()
    
    def createActuator(self):
        return UrbanTrafficActuator()


# Fabrica concreta, família rodoviária
class HighwayDeviceFactory(DeviceFactory):
    
    def createSensor(self):
        return HighwayTrafficSensor()
    
    def createActuator(self):
        return HighwayTrafficActuator()
    

# Estado do tráfego
class TrafficStatus:
    
    congestionLevel : int
    incidents : list[str]
    __observers : list
    
    def __init__(self):
        self.congestionLevel = 0
        self.incidents = []
        self.__observers = []
        
    @property
    def observers(self):
        return [o.id for o in self.__observers]
    
    def addObserver(self, observer) -> None:
        self.__observers.append(observer)
        
    def removeObserver(self, observer) -> None:
        self.__observers.remove(observer)
        
    def notifyObservers(self) -> None:
        for o in self.__observers:
            o.notify()
            
    def updateStatus(self, sensorData) -> None:
        self.congestionLevel = sensorData['congestionLevel']
        self.incidents.append(sensorData['incident'])


# Singleton Administrador e Controle de Tráfego
class TrafficControlManager(metaclass=SingletonMetaclass):
    
    __metrics : dict
    __log : str
    __stat : TrafficStatus
    
    def __init__(self):
        self.__metrics = {}
        self.__log = ''
        self.__stat = TrafficStatus()
        
    @property
    def metrics(self):
        return self.__metrics
    
    @property
    def stat(self):
        return self.__stat
        
    def adjustMetric(self, key:str, value) -> None:
        self.__metrics[key] = value
    
    def logAction(self, action:str) -> None:
        self.__log += f'{datetime.now()}: Performed {action} \n'
            

# Observador Abstrato
class TrafficObserver(ABC):
    
    def __init__(self, stat : TrafficStatus):
        self.stat = stat
        self.stat.addObserver(self)
    
    @abstractmethod
    def notify(self):
        pass
    
    
# Observador concreto, tipo motorista
class DriverNotifier(TrafficObserver):
    
    __currentCL : int
    
    def __init__(self, stat : TrafficStatus):
        super().__init__(stat)
        self.__currentCL = 0
    
    def notify(self) -> None:
        self.__currentCL = self.stat.congestionLevel
        
    @property
    def currentCL(self):
        return self.__currentCL
        

# Observador concreto, tipo autoridade    
class AuthorityNotifier(TrafficObserver):
    
    __lastIncident : str
    
    def __init__(self, stat : TrafficActuator):
        super().__init__(stat)
        self.__lastIncident = 'Nenhum incidente... ainda'
        
    def notify(self) -> None:
        self.__lastIncident = self.stat.incidents[-1]
        
    @property
    def lastIncident(self):
        return self.__lastIncident
        
# Testes modelo de tráfego
if __name__ == '__main__':
    # Instancia singleton do sistema de controle
    manager = TrafficControlManager()
    
    # Família de produtos
    factory = UrbanDeviceFactory()
    
    # Ajuste de métricas de forma global
    manager.adjustMetric(key='maxCongestionLevel', value=8)
    manager.adjustMetric(key='API_key', value='xHrxa34GhmmJ9')
    
    # Acesso ao status interno via método getter
    status = manager.stat
    
    # Instancias dos clientes, motoristas e autoridades
    driver = DriverNotifier(stat=status)
    authority = AuthorityNotifier(stat=status)
    
    # Acessa os múltiplos sensores e atuadores
    sensores = [factory.createSensor() for _ in range(5)]
    atuadores = [factory.createActuator() for _ in range(2)]
    
    # Sensores podem atualizar o estado de tráfego através de seus dados
    sensorData = sensores[0].collectData()
    sensorData['congestionLevel'] = 9
    sensorData['incident'] = 'Colisão entre veículos na esquina da rua foo com avenida bar'
    status.updateStatus(sensorData)
    
    # Após todas as atualizações dos sensores, informa as mudanças aos notificadores
    status.notifyObservers()
    print(f'Motorista informado sobre o atual congestionamento de nível: {driver.currentCL}')
    print(f'Autoridade informada sobre o último acidente: "{authority.lastIncident}"')
    
    # Como fazer a relação entre estado e atuadores? Controle?
    if status.congestionLevel > manager.metrics['maxCongestionLevel']:
        atuadores[0].performAction()
    
    # Registra a atuação no log centralizado
    manager.logAction('Atuador acionado para controlar tráfego')
        