class CarDriving():

    def fuel_left(self, gallonsfilled, milespergallon, totalmilescandroven):
        self.gallonsfilled = gallonsfilled
        self.milespergallon = milespergallon
        self.totalmilescandroven = totalmilescandroven

        self.remaingdistance = (self.gallonsfilled * self.milespergallon) - self.totalmilescandroven
        self.remainggallon = self.remaingdistance / self.milespergallon

    def returnf(self):
        return self.remainggallon


obj = CarDriving()
obj.fuel_left(10, 30, 100)
print(obj.returnf())