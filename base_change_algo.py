def convert_to_base(base,number):
    if number == 0:
        return '0'
    else:
        return convert_to_base(base,number//base) + str(number%base)

converted_representation = convert_to_base(231,232)
print(converted_representation)