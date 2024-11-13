from adapters.processor_adapter import PaymentProcessor


class MembershipUpgradeHandler(PaymentProcessor):
    def run(self):
        self.activate_membership(upgrade=True)
