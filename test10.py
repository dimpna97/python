class FourCal:
   def __init__(self,first,second):
       self.first = first
       self.second = second
   
   def setdata(self, first, second):
       self.first = first
       self.second = second

   def add(self):
       result = self.first + self.second
       return result 
    
   def mul(self):
       result = self.first * self.second
       return result
   
   def div(self):
       result = self.first / self.second
       return result
    
    
a = FourCal(4,2)
#b = FourCal()
#a.setdata(4,2)
#b.setdata(3,7)
#print(id(a.first))
#print(id(b.first))
#print(a.add())       
print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
    def div(self):
        if self.second ==0:
            return 0
        else:
            return self.first/self.second

a = MoreFourCal(4,2)
print(a.pow())
a = MoreFourCal(4,0)
print(a.div())