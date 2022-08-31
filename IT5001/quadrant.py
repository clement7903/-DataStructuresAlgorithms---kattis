x_coordinate = int(input())
y_coordinate = int(input())

if x_coordinate > 0 and y_coordinate > 0:
  print(1)
elif x_coordinate > 0 and y_coordinate < 0:
  print(4)
elif x_coordinate < 0 and y_coordinate < 0:
  print(3)
else:
  print(2)
