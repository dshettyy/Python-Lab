num = [ 1, 2, 3 , 4 ,5 ,6]

def squared(x):
    return x * x

squared_numbers = list(map (squared ,num))
print(squared_numbers)