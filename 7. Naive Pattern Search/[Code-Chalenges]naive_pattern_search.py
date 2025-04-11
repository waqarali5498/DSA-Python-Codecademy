# # Extend our naive pattern search algorithm functionality to not just find patterns, but replace them as well! This will be done through the following steps:

# # Find patterns more easily by making the search case-insensitive.
# # Build and maintain a separate copy of the introduction to insert replacements.
# # Skip newly-replaced characters.

# def pattern_search(text, pattern,case_sensitive=True):
#   for index in range(len(text)):
#     match_count = 0
#     for char in range(len(pattern)): 
#       if case_sensitive and pattern[char] == text[index + char]:
#         match_count += 1
#       elif not case_sensitive and pattern[char].lower()== text[index+char].lower():
#         match_count+=1
#       else:
#         break
#     if match_count == len(pattern):
#       print(pattern, "found at index", index)

# friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
# pattern_search(friends_intro, "Language")
# pattern_search(friends_intro, "pylhon", False)
# pattern_search(friends_intro, "idil", False)



# -----------------------------------------------------------------------------------------------------------------------------------

def pattern_search(text, pattern, replacement_text,case_sensitive=True):
  fixed_text=''
  num_skips=0
  for index in range(len(text)):
    match_count = 0
    if num_skips>0:
        num_skips-=1
        continue
    for char in range(len(pattern)): 
      
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

      fixed_text+=replacement_text
      num_skips=len(pattern)-1
    else:
       fixed_text+=text[index]
  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")
print(pattern_search(friends_intro, "languuUuage", "language"))



# ------------------------------------------------------------------------------------------


# def pattern_search(text, pattern, replacement_text, case_sensitive=True):
#     fixed_text = ""
#     num_skips = 0  # Track characters to skip

#     for index in range(len(text)):
#         if num_skips > 0:
#             num_skips -= 1  # Skip characters that are part of a replaced pattern
#             continue

#         # Check if the pattern matches at the current index
#         if text[index: index + len(pattern)] == pattern if case_sensitive else text[index: index + len(pattern)].lower() == pattern.lower():
#             print(f'"{pattern}" found at index {index}')
#             fixed_text += replacement_text
#             num_skips = len(pattern) - 1  # Skip the characters that were just replaced
#         else:
#             fixed_text += text[index]  # Keep the original character if no match found

#     return fixed_text  # Return the modified text

# # Original text
# friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."

# # Apply multiple replacements step by step
# friends_intro = pattern_search(friends_intro, "Language", "language")
# friends_intro = pattern_search(friends_intro, "pylhon", "Python", False)
# friends_intro = pattern_search(friends_intro, "idil", "ideal", False)
# friends_intro = pattern_search(friends_intro, "zzz ", "")
# friends_intro = pattern_search(friends_intro, "syntacs", "syntax")
# friends_intro = pattern_search(friends_intro, "languuUuage", "language")

# # Print final corrected text
# print("\nFinal corrected text:\n", friends_intro)
