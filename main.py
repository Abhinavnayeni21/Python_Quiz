print("Hello, Welcome to Abhinav's Quiz. Please feel to take this quiz to know me better!") ## This greets the user when first prompted to the game 

print("Also, please notice that I made this game quite interesting buy not saying whether you are right or wrong :)") ## This is some additional information given to the user 

answer_to_the_questions = input("Are you ready to the play game? (yes/no): ") ## This ensures that user is ready to play the game 
amount_of_scores = 0 
amount_of_questions = 10

if answer_to_the_questions.lower () == "yes": ## Notice that if the answer is yes to the question above the user, will be prompted to the game
  print("1. What's been my greatest accomplishment?") ## This allow the User to see the first set of question (We will repeat this process at least 10 times)
  print("options:") ## guide
  print("driving the car") ## option one 
  print("attending university") ## second option 
  print("coding") ## third option 
  print("playing games") ## fourth option 
answer_to_the_questions = input("what is your answer?") 
if answer_to_the_questions.lower () == "attending university": ## If the answer to the question is this answer
   amount_of_scores += 1 ## Then we add one to the score 

print("2. Base: 32.3, Height= 98.3, find the area of this triangle?") ## This allow the User to see the second set of question (We will repeat this process at least 10 times)
print("Note this formula: Base * Height / 2") ## Hint for the next question 
print("options:") ## guide 
print("1587.593") ## option one
print("3231.32") ## option two
print("1587.545") ## option three
print("32342.43") ## option four
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "1587.545": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("3. Name at least one of my ice cream flavour I like?") ##This allow the User to see the third set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("oreo") ## option one 
print("strawberry") ## option two 
print("chocolate") ## option three 
print("cookies and dough") ## option four 
answer_to_the_questions = input("What is your answer?")
if answer_to_the_questions.lower () == "strawberry" or answer_to_the_questions.lower () == "chocolate" or answer_to_the_questions.lower () == "cookies and dough": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score 

print("4. What is your favourite programming language?") ## This allow the User to see the fourth set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("c++") ## option one 
print("racket") ## option two 
print("java") ## option three 
print("python") ## option four 
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "python" or answer_to_the_questions.lower () == "racket": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("5. If I had to pack up and move to another country tomorrow, where would I go?") ## This allow the User to see the fifth set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("hawaii") ## option one 
print("duabi") ## option two 
print("bora bora") ## option three 
print("los angeles") ## option four 
answer_to_the_questions = input("What is your answer") 
if answer_to_the_questions.lower () == "bora bora" or answer_to_the_questions.lower () == "duabi": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("6. What career path do you see me doing in the future?") ## This allow the User to see the sixth set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("software developer") ## option one 
print("back/front end developer") ## option two 
print("web developer") ## option three 
print("computer research scientist") ## option four 
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "software developer" or answer_to_the_questions.lower () == "back/front end developer": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("7. If I could have dinner with anyone dead or alive, who would it be?") ## This allow the User to see the seventh set of question (We will repeat this process at least 10 times)
print("options:")
print("the weeknd") ## option one
print("kanye west") ## option two 
print("drake") ## option three 
print("jay-z") ## option four 
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "drake": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("8. If I can give my parents one thing in the world, what would it be:)?") ## This allow the User to see the eight set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("take them out for a nice dinner") ## option one 
print("spend quality time") ## option two 
print("buy a car") ## option three 
print("a family vacation") ## option four 
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "a family vacation": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("9. What game was I was playing during the pandemic?") ## This allow the User to see the ninth set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("fortnite") ## option one 
print("warzone") ## option two 
print("fifa") ## option three 
print("nba") ## option four 
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "warzone": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("10. Did you enjoy yourslef when you played this game?") ## This allow the User to see the tenth set of question (We will repeat this process at least 10 times)
print("options:") ## guide 
print("yes yes yes") ## option one 
print("yes") ## option two 
print("no no no") ## option three 
print("no") ## option four
answer_to_the_questions = input("What is your answer?") 
if answer_to_the_questions.lower () == "yes yes yes": ## If the answer to the question is this answer 
 amount_of_scores += 1 ## Then we add one to the score

print("Thank you for playing, your result will be printed. Please give me a moment") ## This will just guide the user to the end of the game, with a message 

your_mark = (amount_of_scores/amount_of_questions) *100 ## We will do this by a simple formula given above 

print("Mark Earned: ", your_mark) ## Now the program will simply present the final value 
print("See you again") ## Last promt the to the user 