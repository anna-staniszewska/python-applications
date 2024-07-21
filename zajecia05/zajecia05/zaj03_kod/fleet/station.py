from zajecia05.utils.get_logger import get_logger

logger = get_logger("StationLogger")

class Station:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        if not self.validate_coordinates(location):
            logger.error(f"Invalid coordinates: {location}")
            raise ValueError("Invalid coordinates for location")
        
        self.id = Station.__max_id
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1

        logger.info(f"Station created: {self}")

    @staticmethod
    def validate_coordinates(location):
        lat, lon = location
        return -90 <= lat <= 90 and -180 <= lon <= 180

    def check_location(self):
        frontText = f"Stacja nr {self.id}: Karetka nr {self.ambulance.id}"
        if (self.location == self.ambulance.location):
            return  frontText + f" jest już na miejscu."
        else:
            return frontText + f" jeszcze nie dotarła."
        
    def __repr__(self):
        return (f"Station: id={self.id!r}")

    def __str__(self):
        return (f"Station: id={self.id!r}")