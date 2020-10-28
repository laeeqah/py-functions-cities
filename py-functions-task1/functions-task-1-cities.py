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


user_days = int(input("How many days you will rent the car: "))
car_cost = 40 #per day
def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50

    elif days >= 3:
        return days * 40 - 20

    else:
        return "Not Renting"


print(rental_car_cost(user_days))

spend_money =int(input("Put in spending money: "))
def trip_cost(city, days, spend_money):
    return city + days + spend_money

costs =((hotel_cost(user_nights))+(plane_ride_cost(cities))+(rental_car_cost(user_days)+ (spend_money)))

print(costs)



