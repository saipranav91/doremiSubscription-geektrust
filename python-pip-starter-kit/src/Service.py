from src.SubscriptionType import SubscriptionType 


class Service:
    def __init__(self,name):
        self.__name=name 
        self.__date=None
        # self._free=False
        # self._personal=False 
        # self._premium=False
        self.__subscription=None
        
    
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name 
    def getDate(self):
        return self.__date
    def setDate(self,date):
        self.__date=date
    
    def setSubscriptionState(self,subscription_type):
          # Check if subscription_type is a valid SubscriptionType
        if isinstance(subscription_type, SubscriptionType):
            self.__subscription = subscription_type
        else:
            raise ValueError("Invalid subscription type")
        
    def getSubscription(self):
        return self.__subscription.value if self.__subscription else None
            
        
        

class ServiceFactory:
    def create_service(self,name,subscription_type):
        service=Service(name)
         # Convert string to enum (if valid) and set the subscription state
        try:
            subscription_type = SubscriptionType(subscription_type)
            service.setSubscriptionState(subscription_type)
        except ValueError:
            raise Exception("Not a Valid subscription state")
        
        return service
    
    
    
    
    
    
    
    
    
    
    