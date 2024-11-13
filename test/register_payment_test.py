from handlers.book_handler import BookHandler
from handlers.membership_handler import MembershipHandler
from handlers.physical_product_handler import PhysicalProductPaymentHandler
from handlers.membership_upgrade_handler import MembershipUpgradeHandler
from handlers.skiing_video_handler import SkiingVideoHandler

import pytest
import os
import sys
from unittest.mock import MagicMock
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def mock_log():
    """Creates a mock for the logger."""
    return MagicMock()


@pytest.fixture
def mock_config():
    """Creates a mock for the configuration."""
    return {"configuration": {"type": "dummy"}}


def test_physical_product_payment(mock_config, mock_log):
    """Test to verify if the physical product payment processing works correctly."""
    processor = PhysicalProductPaymentHandler(mock_config, mock_log)
    processor.run()

    # Verifies if the appropriate methods were called
    mock_log.info.assert_any_call("Generating shipping label.")
    mock_log.info.assert_any_call("Generating agent commission payment.")


def test_book_payment(mock_config, mock_log):
    """Test to verify if the book payment processing works correctly."""
    processor = BookHandler(mock_config, mock_log)
    processor.run()

    # Verifies if the appropriate methods were called, including the duplicate label
    mock_log.info.assert_any_call("Generating shipping label.")
    mock_log.info.assert_any_call("Generating duplicate label for royalties.")
    mock_log.info.assert_any_call("Generating agent commission payment.")


def test_membership_payment(mock_config, mock_log):
    """Test to verify if the membership payment processing works correctly."""
    processor = MembershipHandler(mock_config, mock_log)
    processor.run()

    # Verifies if the membership activation method was called
    mock_log.info.assert_any_call("Membership activated.")
    mock_log.info.assert_any_call("Sending email: Membership activated")


def test_membership_upgrade_payment(mock_config, mock_log):
    """Test to verify if the membership upgrade processing works correctly."""
    processor = MembershipUpgradeHandler(mock_config, mock_log)
    processor.run()

    # Verifies if the membership upgrade method was called
    mock_log.info.assert_any_call("Membership upgraded.")
    mock_log.info.assert_any_call("Sending email: Membership upgraded")


def test_skiing_video_payment(mock_config, mock_log):
    """Test to verify if the skiing video payment processing works correctly."""
    processor = SkiingVideoHandler(mock_config, mock_log)
    processor.run()

    # Verifies if the method for adding the free video was called
    mock_log.info.assert_any_call("Generating shipping label.")
    mock_log.info.assert_any_call("Adding free 'First Aid' video.")
