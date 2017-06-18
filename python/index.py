def pigLatin(string):
  reverseList = []
  for letters in reversed(list(string)):
    reverseList.extend(letters)
  if string == "".join(reverseList):
    return True
  elif string != "".join(reverseList):
    return False

print pigLatin("bob")