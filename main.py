import argparse
from utils import set_config_yaml
from package import __version__ as VERSION
from package import __describe__ as DESCRIBE
from package import __help_payment__ as HELP_PAYMENT
from package import __default_config__ as DEFAULT_CONFIG

from bin.register_payment import register_payment


def main():
    """
    Entry Point
    """
    parser = argparse.ArgumentParser(description=DESCRIBE)
    parser.add_argument('-c', '--configuration', help=HELP_PAYMENT,
                        required=False, default=DEFAULT_CONFIG)
    args = parser.parse_args()

    config_file, log = set_config_yaml(
        f'Register v-{VERSION}', 'Actions', args.configuration)

    register_payment(config_file, log)


if __name__ == '__main__':
    main()
