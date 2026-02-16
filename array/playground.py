test = {1:2, 3:5, 5:2}
element_counter = sorted(test.items(), key=lambda x: (x[1], x[0]), reverse = True)
print(dict(element_counter))