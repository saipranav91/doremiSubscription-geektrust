class SubscriptionContext:
    def __init__(self,service_factory,customer_builder,subscription_manager):
        self.service_factory=service_factory
        self.customer_builder=customer_builder 
        self.subscription_manager=subscription_manager 
