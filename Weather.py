# The weather info

from pyowm import OWM

owm = OWM('your-API-key')

place = input("Enter your city: ")
city = place[0].upper() + place[1:] # Делаем первую букву введенного города заглавной
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

print("It's " + str.lower(w.status) + " in " + city + " now." )
print("Average temperature " + str(round(w.temperature('celsius')["temp"]))+ ", feels like " + str(round(w.temperature('celsius')["feels_like"])))