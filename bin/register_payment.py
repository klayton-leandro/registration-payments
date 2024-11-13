from handlers.physical_product_handler import PhysicalProductPaymentHandler
from handlers.book_handler import BookHandler
from handlers.membership_handler import MembershipHandler
from handlers.membership_upgrade_handler import MembershipUpgradeHandler
from handlers.skiing_video_handler import SkiingVideoHandler


def register_payment(config, log):
    """
    Entry point for Payment Registration.
    """
    payment_processors = {
        'physical_product': PhysicalProductPaymentHandler,
        'book': BookHandler,
        'membership': MembershipHandler,
        'membership_upgrade': MembershipUpgradeHandler,
        'skiing_video': SkiingVideoHandler,
    }

    payment_type = config['configuration']['type']

    processor_class = payment_processors.get(payment_type)
    if not processor_class:
        log.error(f"Payment type '{payment_type}' is not supported.")
        return

    try:
        processor = processor_class(config, log)
        processor.run()
    except Exception as exp:
        log.error(f"Error: {repr(exp)}")
        quit()
