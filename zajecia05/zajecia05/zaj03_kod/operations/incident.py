from zajecia05.utils.get_logger import get_logger

logger = get_logger("IncidentLogger")

class Incident:
    __max_id = 0

    def __init__(self, description, priority, time, reporter, location):
        if not self.validate_coordinates(location):
            logger.error(f"Invalid coordinates: {location}")
            raise ValueError("Invalid coordinates for location")

        self.id = Incident.__max_id
        self.description = description
        self.priority = priority
        self.time = time
        self.reporter = reporter
        self.location = location
        self.ambulance = None
        Incident.__max_id += 1

        logger.info(f"Incident created: {self}")

    @staticmethod
    def validate_coordinates(location):
        lat, lon = location
        return -90 <= lat <= 90 and -180 <= lon <= 180

    def __repr__(self):
        return (f"Incident(id={self.id!r}, description={self.description!r}, "
                f"priority={self.priority!r}, time={self.time!r}, reporter={self.reporter!r})")

    def __str__(self):
        return (f"Incident {self.id}: {self.description}, priority={self.priority}, "
                f"{self.time}, reported by: {self.reporter}")

