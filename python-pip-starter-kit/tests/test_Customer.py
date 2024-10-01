import unittest
from src.Service import Service 
from src.Customer import Customer ,CustomerBuilder
 


class test_Customer(unittest.TestCase):
    
    def setUp(self):
        
        self.customer_builder=CustomerBuilder()
        self.name="MUSIC"
        self.service1=Service(self.name)
        self.service2=Service(self.name)
        self.number_of_devices=4 
        self.number_of_months=3
    def test_Customer(self):
        self.customer_builder.addTopUp(self.number_of_devices,self.number_of_months)
        customer=self.customer_builder.build()
        self.assertEqual(customer.getTopUp(),{4:3})
        
        
        

        
        
        
    


if __name__=="__main__":
    unittest.main(buffer=False)
    