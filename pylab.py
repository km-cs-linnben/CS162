import pylab

list_of_ints = []
for counter in range(10):
    list_of_ints.append(counter*2)
print(list_of_ints)
print(len(list_of_ints))

# now pl ot th e l i s t
pylab.plot(list_of_ints)
pylab.show()