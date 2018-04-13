class Incometax:        # define parent class
   def calculatetax(self):
      print("Calling parent method")

class Gst(Incometax): # define child class
   def calculatetax(self):
      print("Calling child method")

c = Gst()          # instance of child
c.calculatetax()         # child calls overridden method