file = open("day1_input.txt", "r")
column1 = []
column2 = []
total = 0
counter = 0

for line in file:
  thingy1 = line[0:5]
  thingy2 = line[8:14]

  column1.append(int(thingy1))
  column2.append(int(thingy2))

for x1 in column1:
  for x2 in column2:
    if x1 == x2:
      counter += 1
  total += x1 * counter
  counter = 0

print(total)
