
file = open("day1_input.txt", "r")
column1 = []
column2 = []
total = 0

for line in file:
  thingy1 = line[0:5]
  thingy2 = line[8:14]

  column1.append(int(thingy1))
  column2.append(int(thingy2))

column1.sort()
column2.sort()

for x in range(0, len(column1)):
  d = column1[x] - column2[x]

  if d < 0:
    d = d * -1

  total += d

print(total)
