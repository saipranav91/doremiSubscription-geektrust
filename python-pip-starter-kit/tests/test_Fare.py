import unittest 
from src.Service import ServiceFactory
from src.Customer import CustomerBuilder
from src.Fare import Fare
from src.Storage import StorageFactory
from src.TopUp import TopUpBuilder

class test_Fare(unittest.TestCase):
    def setUp(self):
        self.service=ServiceFactory().create_service("MUSIC","PERSONAL")
        self.service2=ServiceFactory().create_service("VIDEO","PREMIUM")
        self.service3=ServiceFactory().create_service("PODCAST","FREE")
        
        self.customer_builder=CustomerBuilder()
        self.storage_factory=StorageFactory()
        self.topup_builder=TopUpBuilder()
        self.number_of_devices=4
        self.number_of_months=3
        self.fare=Fare()
    def test_Fare(self):
        self.customer_builder.addService(self.service)
        self.customer_builder.addService(self.service2)
        self.customer_builder.addService(self.service3)
        self.customer_builder.addTopUp(self.number_of_devices,self.number_of_months)
        customer=self.customer_builder.build()
        self.assertEqual(self.fare.totalFare(customer,self.storage_factory,self.topup_builder),750)


if __name__=="__main__":
    unittest.main(buffer=True)        
    