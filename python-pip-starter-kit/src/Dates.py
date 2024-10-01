from datetime import datetime, timedelta

class Dates:
    def calDates(self, storage_factory, customer):
        cal_dates = {}
        all_services = customer.getServices()
        for service_name in all_services:
            if service_name == "MUSIC":
                cal_dates["MUSIC"] = self.calMusicDate(storage_factory, customer.getDate(), all_services[service_name])
            elif service_name == "VIDEO":
                cal_dates["VIDEO"] = self.calVideoDate(storage_factory, customer.getDate(), all_services[service_name])
            elif service_name == "PODCAST":
                cal_dates["PODCAST"] = self.calPodCastDate(storage_factory, customer.getDate(), all_services[service_name])
        return cal_dates

    def calMusicDate(self, storage_factory, starting_date, service):
        music_storage = storage_factory.createStorage("MUSIC")
        subscription_type = service.getSubscription()
        months = self.helper(music_storage, subscription_type)
        notification_date = self.calDate(starting_date, months)
        return notification_date.strftime("%d-%m-%Y")
    
    def calVideoDate(self, storage_factory, starting_date, service):
        video_storage = storage_factory.createStorage("VIDEO")
        subscription_type = service.getSubscription()
        months = self.helper(video_storage, subscription_type)
        notification_date = self.calDate(starting_date, months)
        return notification_date.strftime("%d-%m-%Y")
    
    def calPodCastDate(self, storage_factory, starting_date, service):
        podcast_storage = storage_factory.createStorage("PODCAST")
        subscription_type = service.getSubscription()
        months = self.helper(podcast_storage, subscription_type)
        notification_date = self.calDate(starting_date, months)
        return notification_date.strftime("%d-%m-%Y")
        
    def helper(self, storage, subscription_type):
        subscription_type=subscription_type.strip()
        if subscription_type == "FREE":
            return storage.getTimeFree()
        elif subscription_type == "PERSONAL":
      
            return storage.getTimePersonal()
        elif subscription_type == "PREMIUM":
          
            return storage.getTimePremium()
    
    def calDate(self, starting_date, months):
        if months is None:
    
            return None  # Handle this situation appropriately

    # Proceed with calculations if months is valid
        year = starting_date.year
        month = starting_date.month + months

    # If months overflow, adjust the year and month accordingly
        MONTHS_IN_YEAR = 12
        while month > MONTHS_IN_YEAR:
            year += 1
            month -= MONTHS_IN_YEAR


        day = starting_date.day
        try:
            expiration_date = datetime(year, month, day)  # Try same day in the new month
        except ValueError:
        # Handle end-of-month overflow
            expiration_date = datetime(year, month + 1, 1) - timedelta(days=1)

        NOTIFICATION_DAYS_BEFORE = 10
        notification_date = expiration_date - timedelta(days=NOTIFICATION_DAYS_BEFORE)

        return notification_date


