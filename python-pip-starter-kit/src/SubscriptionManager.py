from datetime import datetime
class SubscriptionManaager:
    def __init__(self):
        self.start_date=None 
        self.subscriptions={}
        self.topup=None 
        self.invalid_date=False
        self.subscription_duplicate=False

    def handleInvalidDate(self):
        self.invalid_date=True
        print("INVALID_DATE")

    def handleSubscriptionAfterInvalidDate(self):
        print("ADD_SUBSCRIPTION_FAILED INVALID_DATE")

    def handleTopUpAfterInvalidDate(self):
        print("ADD_TOPUP_FAILED INVALID_DATE")   

    def handleDuplicateSubscription(self):
        print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")

    def handleDuplicateTopup(self):
        print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")

    def handleTopUpWithOutSubscription(self):
        print("ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND")






