import pytest

from services.repair_service import RepairService


def test_create_repair():
    service = RepairService()

    repair = {
        "repair_id": "R001",
        "device": "HP Laptop",
        "status": "Pending"
    }

    result = service.create_repair(repair)

    assert result["status"] == "Pending"

# Test to trigger a ValueError for missing device and missing status,
# ensuring the service raises the correct exception with the expected message.
# Verify that a repair cannot be created without a device.
def test_create_repair_requires_device():
    service = RepairService()
    repair_missing_device = {
        "status": "Pending"
    }

    # Capture and verify the exact message raised by the service.
    with pytest.raises(ValueError, match="^Missing required field: device. Please provide the device name.$") as error:
        service.create_repair(repair_missing_device)

    print(error.value)
    assert str(error.value) == "Missing required field: device. Please provide the device name."

# Verify that unsupported repair statuses are rejected.
def test_create_repair_rejects_invalid_status():
    service = RepairService()
    repair_invalid_status = {
        "repair_id": "R002",
        "device": "HP Laptop",
        "status": "Unknown"
    }

    # Capture and verify the exact message raised by the service.
    with pytest.raises(ValueError, match=f"^Invalid repair status: {repair_invalid_status.get('status')}. Allowed statuses are: Pending, In Progress, Completed.$") as error:
        service.create_repair(repair_invalid_status)

    print(error.value)
    assert str(error.value) == f"Invalid repair status: {repair_invalid_status.get('status')}. Allowed statuses are: Pending, In Progress, Completed."