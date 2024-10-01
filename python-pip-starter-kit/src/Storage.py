from abc import ABC,abstractmethod 

class Storage(ABC):
    def __init__(self):
        self._free=0 
        self._time_free=1 
        self._time_personal=1
        self._time_premium=3
    
    def getFree(self):
        return self._free 
    def getTimeFree(self):
        return self._time_free 
    def getTimePersonal(self):
        return self._time_personal
    def getTimePremium(self):
        return self._time_premium 
    @abstractmethod 
    def getPersonal(self):
        pass 
    @abstractmethod
    def getPremium(self):
        pass
    
class Music(Storage):
    def __init__(self):
        super().__init__() 
        self._personal=100 
        self._premium=250
    
    def getPersonal(self):
        return self._personal
    def getPremium(self):
        return self._premium

class PodCast(Storage):
    def __init__(self):
        super().__init__() 
        self._personal=100 
        self._premium=300
    
    def getPersonal(self):
        return self._personal
    def getPremium(self):
        return self._premium


class VideoStreaming(Storage):
    def __init__(self):
        super().__init__() 
        self._personal=200 
        self._premium=500
    
    def getPersonal(self):
        return self._personal
    def getPremium(self):
        return self._premium

class StorageFactory:
    def __init__(self):
        self.subscription_types={
            "MUSIC":Music(),
            "VIDEO":VideoStreaming(),
            "PODCAST":PodCast()
        }
    def addSubscriptionType(self,key,value):
        self.addSubscriptionType[key]=value 
        
    def createStorage(self,service_type):
        if service_type in self.subscription_types:
            return self.subscription_types[service_type]
        else:
            raise Exception(f"{service_type} not found")
