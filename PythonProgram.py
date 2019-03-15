class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._mileage = mileage

    def getMake(self):
        return self._make
    def getModel(self):
        return self._model
    def getColor(self):
        return self._color
    def getYear(self):
        return self._year
    def getMileage(self):
        return self._mileage
    def setMake(self, m):
        self._make = m
    def setModel(self, m):
        self._model = m
    def setColor(self, m):
        self._color = m
    def setYear(self, m):
        self._year = m
    def setMileage(self, m):
        self._mileage = m

# method to add new vehicle to the list
def addVehicle(lstVehicle, vehicle):
    lstVehicle.append(vehicle)
    return lstVehicle

# method to remove vehicle from the list
def removeVehicle(lstVehicle, vehicle):
    lstVehicle.remove(vehicle)
    return lstVehicle

# method to update the vehicle in the list
def updateVehicle(lstVehicle, vehicle):
    for obj in lstVehicle:
        if obj.getMake() == vehicle.getMake():
            obj.setColor("Red")
            return lstVehicle

def createAutomobileFromUser():
    print("Enter automobile details")
    make = input("Make\n")
    model = input("Model\n")
    color = input("Color\n")
    year = input("Year\n")
    mileage = input("Mileage\n")
    vehicle = Automobile(make, model,color,year,mileage) # create new vehicle
    return vehicle
    pass

def main():
    vehicle = createAutomobileFromUser() # create new vehicle
    vehicle1 = createAutomobileFromUser() # create new vehicle
    vehicle2 = createAutomobileFromUser() # create new vehicle

def main():
    lstVehicles = [] # declare a list for vehicles
    addVehicle(lstVehicles, vehicle)
    addVehicle(lstVehicles, vehicle1)
    addVehicle(lstVehicles, vehicle2)

  # remove the vehicle
removeVehicle(lstVehicles, vehicle)
vehicle2 = Automobile("Test1", "Black", "", 2018, 23)

  # update the vehicle in list
updateVehicle(lstVehicles, vehicle2)

  # open a new file to write
thefile = open('test.txt', 'w')

for item in lstVehicles: # print the output to console
    print(item.getMake() + " " + item.getColor())

  # write the list items to the file
thefile.write(item.getMake() + " " + item.getColor()+"\n")

main()