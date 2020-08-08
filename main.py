def stringcleaner(dirty_str):
  lowercased_str = dirty_str.lower()
  cleaned_str = ""
  for element in lowercased_str:
    if element.isalpha():
      cleaned_str = cleaned_str + element
  return cleaned_str
  

def isPalindrome(input_str):
  cleaned_str = stringcleaner(input_str)
  if cleaned_str == cleaned_str[::-1]:
    return 1
  return 0
  
#print(isPalindrome("Otto"))
#print(isPalindrome("abc"))