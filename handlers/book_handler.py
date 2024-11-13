from adapters.processor_adapter import PaymentProcessor


class BookHandler(PaymentProcessor):
    def run(self):
        self.generate_shipping_label(duplicate=True)
        self.generate_commission_payment()
