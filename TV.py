# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Exercise:
# Given: A UML Class Diagram below:
# Required: Create a Pyhton Code for creating the Class named TV and a 
# Test Driver program named TestTV that will create two objects from Class TV.

class TV_channel:
    # constructor
    def __init__(self, power=False, channel=1, volume=1):
        self.power = power
        self.channel = channel
        self.volume = volume
    
    # turning the TV on
    def turn_on(self) -> None:
        self.power = True
            
    # turning the TV off
    def turn_off (self) -> None:
        self.power = False
            
    # getting the channel
    def get_channel (self) -> int :
        return self.channel

    # setting the channel      
    def set_channel (self, channel: int) -> None:
        if channel >=1 and channel <=120:
            self.channel = channel

    # getting the volume
    def get_volume (self) -> int:
        return self.volume
    
    # setting the volume
    def set_volume (self, volume: int) -> None:
        if volume >=1 and volume <=7:
            self.volume = volume

    # increasing the channel number
    def increase_channel_up (self) -> None:
        if self.channel < 120:
            self.channel += 1
        else:
            self.channel = 1

    # decreasing the channel number
    def decrease_channel_up (self) -> None:
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120

    # turning the volume up
    def volume_up (self) -> None:
        if self.volume < 7:
            self.volume +=1
        else:
            self.volume = 7

    # turning the volume down
    def volume_down (self) -> None:
        if self.volume > 1:
            self.volume -= 1
        else:
            self.volume = 1



            


        

   
