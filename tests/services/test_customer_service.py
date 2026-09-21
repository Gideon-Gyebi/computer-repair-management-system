import pytest

from services.customer_service import CustomerService


def test_create_customer():
    service = CustomerService()

    customer = {
        "customer_id": "C001",
        "name": "Wendy",
        "email": "wendy@gmail.com"
    }

    result = service.create_customer(customer)

    assert result["name"] == "Wendy"


# Test to trigger a ValueError for missing email,
# Verify that a customer cannot be created without an email.
def test_create_customer_requires_email():
    service = CustomerService()
    customer_missing_email = {
        "customer_id": "C002",
        "name": "Wendy"
    }
   # Capture and verify the exact message raised by the customer service.
    with pytest.raises(ValueError, match="^Customer email is required$") as error:
        service.create_customer(customer_missing_email)

    print(error.value)
    assert str(error.value) == "Customer email is required"
