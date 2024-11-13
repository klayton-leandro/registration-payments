from adapters.processor_adapter import PaymentProcessor


class SkiingVideoHandler(PaymentProcessor):
    def run(self):
        self.generate_shipping_label()
        self.add_free_video()
