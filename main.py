while numTravelers = int(numTravelers):
  numTravelers = True
  if numTravelers > 0 and numTravelers <= 48:
    break
  elif numTravelers <= 0 and numTravelers > 48:
    numTravelers = input("Please enter a two digit whole number between 1 and 48: ")
    numTravelers = int(numTravelers)
  else:
    numTravelers = input("Please enter a two digit whole number between 1 and 48: ")
    numTravelers = int(numTravelers)

  if type(numTravelers) == str:
    numTravelers = int(input("Please enter a two digit whole number between 1 and 48: "))