x = (3,5)
y = (4,7)

def addfrac(tuple1,tuple2):
        xnum = tuple1[0]
        ynum = tuple2[0]
        xdenom = tuple1[1]
        ydenom = tuple2[1]

        new_denom = xdenom * ydenom
        xnum *= ydenom
        ynum *= xdenom

        new_num = xnum + ynum

        if new_num % new_denom == 0:
                fraction = new_num / new_denom
        else:
                fraction = (new_num,new_denom)

        return fraction

print(addfrac((3,5),(4,7)))