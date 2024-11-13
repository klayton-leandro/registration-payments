from adapters.processor_adapter import PaymentProcessor


class MembershipHandler(PaymentProcessor):
    def run(self):
        self.activate_membership()
