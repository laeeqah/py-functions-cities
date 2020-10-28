# Task 1
def hotel_cost(nights):
    return 140 * nights

user_nights= int(input("Put in amount of nights: "))
print(hotel_cost(user_nights))


def plane_ride_cost(city):

    if city == "Cape Town":
        return 2500

    elif city == "Durban":
        return 2300

    elif city == "JHN":
        return 2000
    
    elif city == "BFN":
        return 1800
    else:
        return ("Flight not available")

print("Put in the city: ")
cities=input("")
print(plane_ride_cost(cities))
