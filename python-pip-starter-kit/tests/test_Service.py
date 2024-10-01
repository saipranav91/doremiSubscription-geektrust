import unittest 
from src.Service import ServiceFactory

class test_Service(unittest.TestCase):
    def setUp(self):
        self.name="MUSIC"
        self.date="12-09-2022"
        self.subscription_type="PREMIUM"
        self.service_factory=ServiceFactory()
    def test_Service(self):
        service=self.service_factory.create_service(self.name,self.subscription_type)
        self.assertEqual(service.getSubscription(),"PREMIUM")
        self.assertEqual(service.getName(),"MUSIC")
        
if __name__=="__main__":
    unittest.main(buffer=False)
        
        
        
    