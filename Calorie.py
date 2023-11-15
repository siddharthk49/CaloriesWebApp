from Temperature import Temperature
class Calorie:
    """
    Represent the amount of calories with
    BMR = 10 * weight + 6.25 * height - 5* age + 5 - 10 * temperature
    """
    def __init__(self,height,weight, age,temperature):
        self.height = height
        self.weight = weight
        self.age = age
        self.temperature = temperature


    def calculate(self):
        result =  10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return  result

if __name__ =='__main__':
    temperature = Temperature(country="Italy", city= "Rome").get()
    cals = Calorie(weight=70, height=170, age= 26, temperature=temperature)

    print(cals.calculate())
