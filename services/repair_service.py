from repositories.repair_repository import RepairRepository


class RepairService:

    def __init__(self):
        self.repository = RepairRepository()

    def create_repair(self, repair):

        if not repair.get("device"):
            raise ValueError("Missing required field: device. Please provide the device name.")

        if repair.get("status") not in ["Pending", "In Progress", "Completed"]:
            raise ValueError(f"Invalid repair status: {repair.get('status')}. Allowed statuses are: Pending, In Progress, Completed.")

        return self.repository.create(repair)

    def get_all_repairs(self):
        return self.repository.get_all()

    def get_repair(self, repair_id):
        return self.repository.read(repair_id)
