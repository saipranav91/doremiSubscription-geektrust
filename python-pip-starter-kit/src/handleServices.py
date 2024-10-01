from datetime import datetime
class handleServices:
    def check_date(self,date_str):
        try:
            date=datetime.strptime(date_str,"%d-%m-%Y")
            return date
        except ValueError:
            raise Exception("INVALID DATE INPUT")
    def handleStartSubscription(self,start_date,subscription_context):
        try:
            start_date=start_date.strip() #make sure to strip the date before processing further
            date=self.check_date(start_date)
            subscription_context.customer_builder.addDate(date)
        except:
            subscription_context.subscription_manager.handleInvalidDate()
            
            
    def handleAddService(self,service_name,subscription_type,subscription_context):
        if not subscription_context.subscription_manager.invalid_date:
            service=subscription_context.service_factory.create_service(service_name,subscription_type)

            try:
                subscription_context.customer_builder.addService(service)
            except:
                subscription_context.subscription_manager.handleDuplicateSubscription()
        else:
            subscription_context.subscription_manager.handleSubscriptionAfterInvalidDate()

    def handleAddTopup(self, number_of_devices, number_of_months,subscription_context):
        if subscription_context.subscription_manager.invalid_date:
            subscription_context.subscription_manager.handleTopUpAfterInvalidDate()
            return

        FOUR_DEVICE_COUNT = 4
        TEN_DEVICE_COUNT = 10
        device_map = {"FOUR_DEVICE": FOUR_DEVICE_COUNT, "TEN_DEVICE": TEN_DEVICE_COUNT}

        if number_of_devices in device_map:
            number_of_devices = device_map[number_of_devices]
        else:
            raise ValueError("Invalid device count")

        if not subscription_context.customer_builder.checkBeforeAddTopUp():
            subscription_context.subscription_manager.handleTopUpWithOutSubscription()
            return
    
        try:
            subscription_context.customer_builder.addTopUp(number_of_devices, number_of_months)
        except:
            subscription_context.subscription_manager.handleDuplicateTopup()

