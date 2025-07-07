# This is the bonus program, where I have to make a mini quiz game where there is a correct question and answer.
# However, all of the code is already given. What am I supposed to do here???
def ask_question(question, correct_answer):
   answer = input(question + " ")
   if answer.lower() == correct_answer.lower():
    print("Correct!")
   else:
    print("Oops! The right answer was", correct_answer)

ask_question("What is the capital of France?\n", "Paris")
# Okay, so this code works.
# Now I will explain how this works.
# First, the "what is the capital of france" part is defined in the function as "question",
# and the correct answer is defined as "Paris" in the correct_answer variable.
# Inside the function, it will ask the user to input an answer, and if the lowercase form of that matches the lowercase form of the correct answer (in string form), then they are correct.
# Otherwise, it will print that they are wrong, and that the correct answer was etc.etc.
# That's all.
# -N1Rv@n  