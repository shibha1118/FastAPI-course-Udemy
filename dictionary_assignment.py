my_vehicle = {
"model": "Ford",
"make": "Explorer",
"year": 2018,
"mileage": 40000
}
for x,y in my_vehicle.items():
    print(x,y)
print("_______")
vehicle2 = my_vehicle.copy()
vehicle2 ['number of tires']= 4
vehicle2.pop("mileage")
for g in vehicle2:
    print(g)