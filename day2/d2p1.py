file = open("d2i.txt", "r")
safeCounter = 0
moreOrLess = ""

def convert_strings_to_ints(arrayA):
  arrayB = []
  for theString in arrayA:
    theInt = int(theString)
    arrayB.append(theInt)
  return arrayB

for line in file:
  array_of_strings = line.split(" ")
  # array_of_int = convert_strings_to_ints(array_of_strings)
  array_of_int = list(map(int, array_of_strings))
  previous = array_of_int[0]

  difference = array_of_int[1] - array_of_int[0]
  if difference > 0:
    moreOrLess = "increase"
  elif difference < 0:
    moreOrLess = "decrease"

  safe = True

  for x1 in array_of_int[1:]:
    difference = x1 - previous

    if difference == 0 or difference > 3 or difference < -3:
      safe = False
      break

    if difference > 0 and moreOrLess == "decrease":
      safe = False
      break

    if difference < 0 and moreOrLess == "increase":
      safe = False
      break

    previous = x1

  if safe:
    safeCounter += 1

print(safeCounter)
