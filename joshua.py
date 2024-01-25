import random
from population import *


# Choose Country

target = ""
launch_attack = ""
country = ""
print("1: United States")
print("2: Soviet Union")

country = input("Which side do you choose, 1 or 2?: ")
if country == "1":
  choice = input("Would you like to play as the United States, Y or N:")
if country == "2":
  choice = input("Would you like to play as the Soviet Union, Y or N:")

if country == "1" or country == "2":
  target = input("List your target city: ")
  launch_attack = input("Would you like to target " + target + ", Y or N?: ")
else:
  print("Error")


# Weather Conditons in (city)
  
random_weather = random.randint(1, 10)
weather_penalty = 0.0

random_casualties = (random.randint(10, 99) / 10)

weather_yesno = input("Would you like to check weather conditions in " + target + ", Y or N?: ")

if random_weather == 1:
  random_weather = "Blizzard"
  print("Visibility is near-zero with high winds and snow.")
elif random_weather == 2:
  random_weather = "Rain"
  print("Hard rain is impeding visibilty, but not enough to divert our forces.")
elif random_weather == 3:
  random_weather = "Snow"
  print("Snowfall is hindering our forces, but they can still move.")
elif random_weather == 4:
  random_weather = "Storm"
  print("Conditions are not ideal for combat with heavy rain and frequent cloud-to-ground lighting.")
else:
  random_weather = "Clear"
  print("Our forces can move and strike with perfect visabilty.")

if random_weather == 1:
  weather_penalty = 0.2
elif random_weather == 2:
  weather_penalty = 0.1
elif random_weather == 3:
  weather_penalty = 0.1
elif random_weather == 4:
  weather_penalty = 0.2
else:
  weather_penalty = 0.0

success_prob = 1.0 - weather_penalty

confirm_attack = input("Would you like to strike now at " + target + "?: ")

if confirm_attack == "Y":
  if success_prob >= 0.7:
    print(target + " has been successfully hit, causing " + str(random_casualties) + " million casualties. Great work commander!")
  elif success_prob < 0.7:
    print(target + " has not been hit successfully due to bad weather conditions. I apologize, commander.")
  else:
    print("The outcome of the battle is unknown at this time.")

exit()