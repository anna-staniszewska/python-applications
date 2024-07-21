def check_location(location):   
    if (location[0] >= -90 and location[0] <= 90 and location[1] >= -180 and location[1] <= 180):
        return True
    else:
        return False

