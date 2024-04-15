car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

color_of_car_before = car.setdefault("color", "white")
color_of_car_after = car.setdefault("brand", "Acura")

print(car)
print(color_of_car_before, color_of_car_after)