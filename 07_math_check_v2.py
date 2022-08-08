import math

def to_rad(degrees):
    radians = math.radians(degrees)

    return radians

def to_deg(radians):
    degrees = math.degrees(radians)

    return degrees

# hard coding

bc_length = 3
bca_size = 53.13



if bc_length >= 1 and bca_size >= 1:
    # Solves triangle using trigonometry
    # Converts bca size to radians
    
    # angle using trigonometry
    bac_size = 90 - bca_size
    abc_size = 90
    bca_size = to_rad(bca_size)
    hypotenuse_length = (bc_length / math.cos(bca_size))
    ab_length = math.sqrt((hypotenuse_length * hypotenuse_length) - (bc_length * bc_length))
    bca_size = to_deg(bca_size)
   
print(hypotenuse_length)
print(ab_length)
print(bc_length)
print(bca_size)
print(bac_size)
print(abc_size)