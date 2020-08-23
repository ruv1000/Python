# The weather info

from pyowm import OWM

owm = OWM('your-API-key')


def input_place():
    place = input("Enter your city: ").capitalize()
    return place


def forecast():
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    answer = "It's " + str.lower(w.status) + " in " + city + " now." + "\n"
    answer += "Average temperature " + str(round(w.temperature('celsius')["temp"])) + ", feels like " + str(
        round(w.temperature('celsius')["feels_like"]))
    return answer


city = input_place()
i = city.isalpha() and not city.isspace()
# need to add a check for the correctness of the entered city

while not i:
    print("Incorrect value, use alphabetic characters without spaces and other special characters")
    city = input_place()
    i = city.isalpha() and not city.isspace()

print(forecast())
