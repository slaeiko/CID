# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 14:50:21 2025

@author: Leonardo Sebastian Loza Sandoval - 222790633
"""
#year, sales, advertising
benetton = [[1, 651, 23],
            [2, 762, 26],
            [3, 856, 30],
            [4, 1063, 34],
            [5, 1190, 43],
            [6, 1298, 48],
            [7, 1421, 52],
            [8, 1440, 57],
            [9, 1518, 58]]
#advertising is the predictor variable, so the array goes -, Y, X...

#by this way, the array goes X,Y (we need modify indexes)
example = [[1,2],
           [2,4],
           [3,6],
           [4,8],
           [5,10]]
            
class SLR ():
    def __init__(self, arr):
        self.data = arr #Arreglo [X,Y]
        self.b0 = None
        self.b1 = None
        self.sumXi2 = 0
        self.sumYi = 0  
        self.sumXi = 0
        self.sumXiYi = 0
        
        for row in self.data:
            self.sumXi2  =  self.sumXi2 + (row[2]*row[2])  
        for row in self.data:
            self.sumYi  =  self.sumYi + row[1]  
        for row in self.data:
            self.sumXi  =  self.sumXi + row[2]
        for row in self.data:
             self.sumXiYi  =  self.sumXiYi + (row[2]*row[1])
        
    def calculateB0(self):
        self.b0 = ( ((self.sumXi2*self.sumYi) - (self.sumXi*self.sumXiYi)) / 
                    (len(self.data)*self.sumXi2 - (self.sumXi*self.sumXi)) ) 
    
    def calculateB1(self):
        self.b1 = ( ((len(self.data)*self.sumXiYi) - (self.sumXi*self.sumYi)) /
                    (len(self.data)*self.sumXi2 - (self.sumXi*self.sumXi)) )
    
    def predict(self, x):
        return self.b0 + (self.b1 * (x))
    
    def getB0(self):
        if not self.b0:
            self.calculateB0()
        return self.b0
        
    def getB1(self):
        if not self.b1:
            self.calculateB1()
        return self.b1
        
        
ex = SLR(benetton)
print("b0 coefficient: " + str(ex.getB0()))
print("b1 coefficient: " + str(ex.getB1()))
print("y = %.4f + %.4f(x)" %  (ex.getB0(), ex.getB1()))
print()    

advertising_values = [24, 28, 38, 45, 60]

# table headers
print("%-15s %-15s" % ("Advertising", "Sales"))
print("-" * 30)

for adv in advertising_values:
    sales = ex.predict(adv)
    print("%-15.0f %-15.4f" % (adv, sales))


        