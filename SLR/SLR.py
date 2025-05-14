# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 14:50:21 2025

@author: Leonardo Sebastian Loza Sandoval - 222790633
"""

class Dataset:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    # Independent variable
    def get_X(self):
        return [row[2] for row in self.data]

    # Dependent variable
    def get_Y(self):
        return [row[1] for row in self.data]

    def get_len(self):
        return len(self.data)

class SLR:
    def __init__(self, dataset):
        # Initialize the data
        self.data = dataset.get_data() 
        self.X = dataset.get_X()
        self.Y = dataset.get_Y()

        self.b0 = None
        self.b1 = None

        self.n = dataset.get_len()

        self.sumXi2 = 0
        self.sumYi = 0  
        self.sumXi = 0
        self.sumXiYi = 0
        
        # Calculate sums
        for i, _ in enumerate(self.data):
            self.sumXi2  =  self.sumXi2 + (self.X[i]**2)  
            self.sumYi  =  self.sumYi + self.Y[i] 
            self.sumXi  =  self.sumXi + self.X[i] 
            self.sumXiYi  =  self.sumXiYi + (self.X[i]*self.Y[i])

    # Calculate coefficients   
    def calculateB0(self):
        self.b0 = ( ((self.sumXi2*self.sumYi) - (self.sumXi*self.sumXiYi)) / 
                    (self.n*self.sumXi2 - (self.sumXi*self.sumXi)) ) 
    
    def calculateB1(self):
        self.b1 = ( ((self.n*self.sumXiYi) - (self.sumXi*self.sumYi)) /
                    (self.n*self.sumXi2 - (self.sumXi*self.sumXi)) )
    
    def predict(self, x):
        return self.b0 + (self.b1 * (x))
    
    def getB0(self):
        if self.b0 is None:
            self.calculateB0()
        return self.b0
        
    def getB1(self):
        if self.b1 is None:
            self.calculateB1()
        return self.b1

class Predictor:
    def __init__(self, model):
        self.model = model

    def call_predictions(self, x_values):
        print("%-15s %-15s" % ("Advertising", "Sales"))
        print("-" * 30)
        for adv in x_values:
            sales = self.model.predict(adv)
            print("%-15.0f %-15.4f" % (adv, sales))

# year, sales, advertising
benetton = [
    [1, 651, 23],
    [2, 762, 26],
    [3, 856, 30],
    [4, 1063, 34],
    [5, 1190, 43],
    [6, 1298, 48],
    [7, 1421, 52],
    [8, 1440, 57],
    [9, 1518, 58]
]

dataset = Dataset(benetton)
slr_model = SLR(dataset)

print("b0 coefficient: " + str(slr_model.getB0()))
print("b1 coefficient: " + str(slr_model.getB1()))
print("y = %.4f + %.4f(x)" %  (slr_model.getB0(), slr_model.getB1()))
print()    

advertising_values = [24, 28, 38, 45, 60]
predictor = Predictor(slr_model)
predictor.call_predictions(advertising_values)