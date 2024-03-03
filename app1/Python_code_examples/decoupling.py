#feet_inches = input("Enter feet and inches: ")

def convert(feet_int, inches_int):
    
    #parts = parts.split(" ")
    feet = float(feet_int)
    inches = float(inches_int)

    meters = feet * 0.3048 + inches * 0.0254
    #return f"{feet} feet and {inches} inches is equal to {meters} meters."
    return round(meters, 3)

#Commented out to only run convert function

# result = (convert(feet_inches))
# if result < 1:
#     print("kid is too small.")
# else:
#     print("Kid can use the slide.")