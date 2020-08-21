# The weather info

from pyowm import OWM

owm = OWM('75dfc1b48b085784afb332045aa1341f')

place = input("Enter your city: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

print("It's " + w.status + " in " + place + " now." ) # сделать проверку на регистр
print("Average temperature " + str(round(w.temperature('celsius')["temp"]))+ ", feels like " + str(round(w.temperature('celsius')["feels_like"])))