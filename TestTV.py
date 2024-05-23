# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Test Driver

from TV import TV_channel

# TV1
tv1 = TV_channel(30, 3, True)
tv1.set_channel(30)
tv1.set_volume(3) 

# TV2
tv2 = TV_channel(3, 2, True)
tv2.set_channel(3)
tv2.set_volume(2) 

# display tv1
print (f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")

# display tv2
print (f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")