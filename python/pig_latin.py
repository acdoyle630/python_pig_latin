def pigLatin(word):
  vowels = ["a", "e", "i", "o", "u"]
  word_list_vowels = []
  word_list = list(word)
  for letters in vowels:
    if letters not in word_list:
      print "cannot find"
    elif word_list.index(letters) >= 0:
      first_vowel = word_list.index(letters)
      word_list_vowels.extend([first_vowel])
  endLetter = word_list[min(word_list_vowels) - 1]
  word_list.remove(word_list[min(word_list_vowels) - 1])
  word_list.extend(endLetter + "ay")
  return "".join(word_list)
print pigLatin('football')