import re
answer = 
Total_Number_Incorrect_Guesses_Allowed = 5
num_of_incorrect_guesses = 0
guesssed_letters =[]

print()



while 
answer = answer.upper()

for answer_index in range(len(answer)):
  if guessed_answer


print()
print()

letter = input("Enter a Letter: ")
letter = letter.upper()

if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z}$]", letter):
  guessed_letters_insert_index = 0
  for current_guessed_letter in guessed_letters:
    if letter < current_guessed_letter:
      break
    guessed_letters_insert_index += 1
  guessed_letters.insert(guessed_letters_insert_index, letter)

  if letter in answer:
    #The letter guessed is in the puzzle.
    for answer_index in range(len(answer)):
      if letter == answer[answer_index]:
        guesssed_answer[answer_index] = True
  else:
    #letter is incorrect
    num_of_incorrect_guesses += 1
#Post-game Summary
print()

if num_of_incorrect_guesses < Total_Number_Incorrect_Guesses_Allowed:
  print("Congratulations, you win!")
else:
  print("Sorry, you lose...")
print()

print(f"{answer} is the answer to the puzzle!)