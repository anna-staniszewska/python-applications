from zajecia05.utils.get_logger import get_logger

logger = get_logger("AmbulanceLogger")

class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment']
    __max_id = 0

    def __init__(self, vehicle_type, status, location, medical_equipment):
        if not self.validate_coordinates(location):
            logger.error(f"Invalid coordinates: {location}")
            raise ValueError("Invalid coordinates for location")

        self.vehicle_type = vehicle_type
        self.status = status  # e.g., "available", "on_mission", "servicing"
        self.location = location # as (latitude, longitude)
        self.medical_equipment = medical_equipment  # List of medical equipment names
        self.id = Ambulance.__max_id
        Ambulance.__max_id += 1

        logger.info(f"Ambulance created: {self}")

    def update_location(self, new_location):
        if not self.validate_coordinates(new_location):
            logger.error(f"Invalid coordinates: {new_location}")
            raise ValueError("Invalid coordinates for location")
        self.location = new_location
        logger.info(f"Ambulance {self.id} location updated to {new_location}")

    @staticmethod
    def validate_coordinates(location):
        lat, lon = location
        return -90 <= lat <= 90 and -180 <= lon <= 180

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type

    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")

    @staticmethod
    def validate_id(ambulance_id):
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__max_id}"

if __name__ == "__main__":
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())
