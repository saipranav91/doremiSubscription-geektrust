import unittest 
from src.Dates import Dates 
from src.Storage import StorageFactory 
from src.Customer import CustomerBuilder 
from src.Service import ServiceFactory
from src.TopUp import TopUpBuilder
from datetime import datetime

class test_Date(unittest.TestCase):
    def setUp(self):
        self.customer_builder=CustomerBuilder()
        self.storage_builder=StorageFactory() 
        self.dates=Dates()
        self.service_factory=ServiceFactory()
        self.topup_builder=TopUpBuilder()
        self.number_of_devices=4
        self.date_string="20-02-2022"
        self.months=3
    def test_Date(self):
        service1=self.service_factory.create_service("MUSIC","PERSONAL")
        service2=self.service_factory.create_service("VIDEO","PREMIUM")
        service3=self.service_factory.create_service("PODCAST","FREE")
        starting_date = datetime.strptime(self.date_string, "%d-%m-%Y")
        self.customer_builder.addDate(starting_date)
        self.customer_builder.addService(service1)
        self.customer_builder.addService(service2)
        self.customer_builder.addService(service3)
        customer=self.customer_builder.build()
        all_notification_dates=self.dates.calDates(self.storage_builder,customer)
        self.assertEqual(all_notification_dates["MUSIC"],"10-03-2022")
        self.assertEqual(all_notification_dates["VIDEO"],"10-05-2022")
        self.assertEqual(all_notification_dates["PODCAST"],"10-03-2022")

    
    

if __name__=="__main__":
    unittest.main(buffer=False)