from adapters.processor_adapter import PaymentProcessor


class PhysicalProductPaymentHandler(PaymentProcessor):
    def run(self):
        self.generate_shipping_label()
        self.generate_commission_payment()
