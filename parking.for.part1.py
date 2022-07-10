PARKING_PLACE = 7
FREE_PLACE = 3
print("#"*PARKING_PLACE*5)
PLACE_NUMBER = PARKING_PLACE - 1 # №
TOTAL_FREE_PLACE_number= PARKING_PLACE - FREE_PLACE
for place_index in range(1, PARKING_PLACE +1):
    if  place_index == FREE_PLACE:
        print("|  |",end="")
    else:
        print("| X |",end="")
print("\n", "#"*PARKING_PLACE*5,sep="")
