# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Exercise:
# Given: A UML Class Diagram below:
# Required: Create a Pyhton Code for creating the Class named TV and a 
# Test Driver program named TestTV that will create two objects from Class TV.

class TV_channel():
    # constructor
    def __init__(self, power=False, channel=1, volume=1):
        self.power = power
        self.channel = channel
        self.volume = volume
    
    # turning the TV on
    def turn_on(self):
        if self.power:
            self.power = True
            
    # turning the TV off
    def turn_off (self):
        if self.power:
            self.power = False
            
    # getting the channel
    def get_channel (self, channel):
        if channel >=1 and channel <=120:
            self.channel = channel

    # setting the channel      
    def set_channel (self, channel):

    


            


        

   
