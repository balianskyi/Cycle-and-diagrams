PARKING_PLACE = 7
FREE_PLACE = 3 # №
TOTAL_FREE_PLACE = PARKING_PLACE - 1
print("#"*PARKING_PLACE*5)
for place_index in range(1, TOTAL_FREE_PLACE +1):
    print("| X |", end="")
    if place_index in range(2,FREE_PLACE,4):
       print("|  |" , end="")
print("\n", "#"*PARKING_PLACE*5,sep="")
https://imgsh.net/a/LvWYwoa.png
