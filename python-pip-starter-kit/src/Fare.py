class Fare:

    def totalFare(self, customer,storage_factory,topup_builder):
        total_fare = 0

        all_services = customer.getServices()

        for service_name in all_services:

            sub_type = storage_factory.createStorage(service_name)


            total_fare =total_fare+ self.calSubTypeFare(sub_type, all_services[service_name])


        # Calculate top-up fare
        try:
            all_topup = customer.getTopUp()
        except:
            raise Exception("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")


        for number_of_devices in all_topup:
            number_of_months=all_topup[number_of_devices] 
            total_fare=total_fare+self.calTopUpFare(number_of_devices,topup_builder,number_of_months)
        return total_fare

    def calTopUpFare(self, number_of_devices,topup_builder,number_of_months):
        topup=topup_builder.createTopUp(number_of_devices)
        return (topup.getPrice())*number_of_months


    def calSubTypeFare(self, sub_type, service):
        out_of_bound=0
        free="FREE"
        personal="PERSONAL"
        premium="PREMIUM"

        subscription_type = service.getSubscription()
        subscription_type=subscription_type.strip()

        if subscription_type == free:
            return sub_type.getFree()
        elif subscription_type == personal:
            return sub_type.getPersonal()  
        elif subscription_type == premium:
            return sub_type.getPremium()
        else:
            return out_of_bound


