import math 
 
# Hard coded dictionaries

ab_length = 35
bc_length = 47
 
    # Solves triangle
if ab_length >= 1 and bc_length >= 1:
    # Solves triangle using pythagoras
    hypotenuse_length = math.sqrt((ab_length * ab_length) + (bc_length * bc_length))
    # need to use tan inverse
    angle_bca = math.degrees(math.atan(ab_length / bc_length))
    angle_bac = math.degrees(math.atan(bc_length / ab_length))
    angle_abc = 90 

print("Ab length: {}".format(ab_length))
print("BC length: {}".format(bc_length))
print("AC Length: {}".format(hypotenuse_length))
print(angle_abc)
print(angle_bac)
print(angle_bca)