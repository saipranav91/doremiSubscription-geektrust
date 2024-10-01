class Customer:
    def __init__(self):
        self._services = {}
        self._date = None
        self._topup = {}

    def addServices(self, service):
        self._services[service.getName()] = service

    def checkService(self, service):
        name = service.getName()
        if name in self._services:
            previous = self._services[name]
            if previous.getSubscription() != service.getSubscription():
                return False
        return True

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date = date

    def checkTopUp(self):
        minimum=0
        if len(self._topup) > minimum:

            return False
        return True

    def addTopUp(self, number_of_devices, number_of_months):

        self._topup[number_of_devices] = number_of_months

    def getTopUp(self):
        return self._topup

    def getServices(self):
        return self._services
    def hasServices(self):
        minimum=0
        if len(self._services)>minimum:
            return True 
        else:
            return False


class CustomerBuilder:

    def __init__(self):
        self.customer = Customer()  # customer has to be public

    def addDate(self, date):
        self.customer.setDate(date)

        return self

    def addService(self, service):
        if not self.customer.checkService(service):
            raise Exception("DUPLICATE SERVICE")
        service.setDate(self.customer.getDate())  # calling the self.customer instance in CustomerBuilder not customer
        self.customer.addServices(service)
        return self

    def checkBeforeAddTopUp(self):
        return self.customer.hasServices()

    def addTopUp(self, number_of_devices, number_of_months):

        if self.customer.checkTopUp():

            self.customer.addTopUp(number_of_devices, number_of_months)
            return self
        else:

            raise Exception("DUPLICATE TOPUP")

    def build(self):
        return self.customer
