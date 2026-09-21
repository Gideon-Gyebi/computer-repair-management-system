import pytest   
from services.technician_service import TechnicianService


def test_create_technician():

    service = TechnicianService()

    technician = {
        "technician_id": "T001",
        "name": "John",
        "specialization": "Laptop Repair"
    }

    result = service.create_technician(technician)

    assert result["specialization"] == "Laptop Repair"


def test_create_technician_requires_specialization():

    service = TechnicianService()

    technician_2 = {
        "technician_id": "T001",
        "name": "John"
    }

    with pytest.raises(ValueError, match="^Specialization is required$") as error:
        service.create_technician(technician_2)
    
    print(error.value)
    assert str(error.value) == "Specialization is required"
    