import unittest 
from src.TopUp import TopUpBuilder

class test_TopUp(unittest.TestCase):
    
    def setUp(self):
        self.topup_builder=TopUpBuilder() 
        self.number_of_devices=10
    
    def test_TopUp(self):
        topup=self.topup_builder.createTopUp(self.number_of_devices)
        
        self.assertEqual(topup.getPrice(),100)
        self.assertEqual(topup.getTime(),1)
        
    


if  __name__=="__main__":
    unittest.main(buffer=False)
    