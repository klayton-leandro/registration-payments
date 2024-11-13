from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, config, log):
        self.config = config
        self.log = log

    @abstractmethod
    def run(self):
        """Executes the specific payment process."""
        pass

    def generate_shipping_label(self, duplicate=False):
        self.log.info("Generating shipping label.")
        if duplicate:
            self.log.info("Generating duplicate shipping label for royalties.")

    def activate_membership(self, upgrade=False):
        action = "activated" if not upgrade else "upgraded"
        self.log.info(f"Membership {action}.")
        self.send_email(f"Membership {action}")

    def send_email(self, message):
        self.log.info(f"Sending email: {message}")

    def add_free_video(self):
        self.log.info("Adding free 'First Aid' video.")

    def generate_commission_payment(self):
        self.log.info("Generating commission payment to the agent.")
