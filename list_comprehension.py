# zip
list_1 = [1, 2, 3]
list_2 = ['sugar', 'spice', 'salty', 'everything nice']

# for item in zip(
#     [1, 2, 3], 
#     ['sugar', 'spice', 'salty', 'everything nice'], 
#     ["mild", "medium", "heavy"]):

#     print(item)

print()
seasonning_dict = {list_no:list_item for (list_no, list_item) in zip(list_1, list_2)}
print(seasonning_dict)