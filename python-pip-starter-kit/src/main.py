from src.Customer import CustomerBuilder 
from src.Service import ServiceFactory
from src.Storage import StorageFactory 
from src.Fare import Fare
from src.Dates import Dates 
from src.TopUp import TopUpBuilder 
from src.SubscriptionManager import SubscriptionManaager
from sys import argv
from src.handling_input import Input
from src.Subscription_context import SubscriptionContext

def main():
    customer_builder=CustomerBuilder()
    service_factory=ServiceFactory()
    storage_factory=StorageFactory() 
    fare=Fare() 
    date=Dates() 
    topup_builder=TopUpBuilder() 
    subscription_manager=SubscriptionManaager()
    input=Input()
    subscription_context=SubscriptionContext(service_factory,customer_builder,subscription_manager)
    
    filePath=input.validate_args(argv)
    input.process_file(filePath,subscription_context)
    customer=customer_builder.build() 
    if not subscription_manager.invalid_date:
        total_fare=fare.totalFare(customer,storage_factory,topup_builder)
        notification_dates=date.calDates(storage_factory,customer)
    if not subscription_manager.invalid_date:
        printSummary(total_fare,notification_dates)
    min_length=0
    if len(customer.getServices())==min_length:
        print("SUBSCRIPTIONS_NOT_FOUND") 
 
    
    
def printSummary(total_fare,notification_dates):
    if notification_dates:
        for sub_type in notification_dates:
            print(f"RENEWAL_REMINDER {sub_type} {notification_dates[sub_type]}")

    
    if total_fare:
        print(f"RENEWAL_AMOUNT {total_fare}")
    


    
    


        
        
            
        
        
    
    

       
    
        
    
    
    