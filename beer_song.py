#Beer song
#Developed by Allen Klus
#4/9/18
import time
num_beer = 99


def main():


        # The '&' are supposed to mimic a musical note...
    print("& 99 Bottles of beer on the wall, 99 bottles of beer, take one down,\n pass it around, 99 Bottles of beer on the wall &")

   
    for x in range(99,0, -1):
        global num_beer
        num_beer = num_beer - 1
        time.sleep(2)
        print("------------------------------------------")
        print("&", str(num_beer),"Bottles of beer on the wall,", str(num_beer), "Bottles of beer, take one down, \n pass it around,", str(num_beer),"bottles of beer on the wall &")
main()
