import math

def to_rad(degrees):
    radians = math.radians(degrees)

    return radians


to_convert = to_rad(30)

print("30 degrees is {} radians".format(to_convert))