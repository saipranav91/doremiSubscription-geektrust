from src.handleServices import handleServices
from datetime import datetime

class Input:
    def __init__(self):
        self.handleServices=handleServices()
    def validate_args(self,args):
        REQUIRED_ARG_COUNT = 2
        if len(args) != REQUIRED_ARG_COUNT:
            raise Exception("File Path does not exist")
        return args[1]


  

    def process_file(self,filePath,subscription_context):
        
        with open(filePath,'r') as file:
            lines=file.readlines()
        
        for line in lines:
            line.strip()
            if not line:
                break 
            self.process_line(line,subscription_context)

        

    def process_line(self,line,subscription_context):
        line=line.split(" ")
        if line[0]=="START_SUBSCRIPTION":
            self.handleServices.handleStartSubscription(line[1],subscription_context)
        
                
        elif line[0]=="ADD_SUBSCRIPTION":
            service_name=line[1].strip()
            subscription_type=line[2].strip()
            self.handleServices.handleAddService(service_name,subscription_type,subscription_context)
        
        elif line[0]=="ADD_TOPUP":
            number_of_devices=line[1].strip()
            number_of_months=int(line[2].strip())
            self.handleServices.handleAddTopup(number_of_devices,number_of_months,subscription_context)