from abc import ABC ,abstractmethod 

class TopUp:
    @abstractmethod
    def getPrice(self):
        pass
    @abstractmethod
    def getTime(self):
        pass 

class TopUp_4(TopUp):
    def __init__(self) -> None:
        super().__init__() 
        self._price=50 
        self._time=1 

    def getPrice(self):
        return self._price 
    def getTime(self):
        return self._time

class TopUp_10(TopUp):
    def __init__(self) -> None:
        super().__init__() 
        self._price=100 
        self._time=1 
    def getPrice(self):
        return self._price 
    def getTime(self):
        return self._time

class TopUpBuilder:
    def __init__(self):
        self.topup_list={
            4:TopUp_4(),
            10:TopUp_10()
        }
    def createTopUp(self,number_of_devices):
        if number_of_devices in self.topup_list:
            return self.topup_list[number_of_devices]



