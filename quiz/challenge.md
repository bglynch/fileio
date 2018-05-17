Planning
We know how to read and write files, let’s use what we’ve learned to create a simple Quiz game.

Overview
This game will store questions and answers in a file. When you run the quiz it will ask the questions, and check your answers against those in the file. At the end of the quiz it will tell you how many you got right.

The game will also allow users to add new questions and answers to the quiz file.

Menu
The game will include a menu with the following options.

1. Ask Questions
2. Add a Question
3. Exit Game

1.  Asking Questions
When the user chooses the Ask Questions option, the game will display each quiz question in turn, asking for the answer to each one. When an answer is given the game will indicate whether the answer is right or wrong before moving to the next question.
- get questions from a text file
-   read each question one line at a time
- user input() answer
-   compare answer to stored answer to question
-   return anwer is correct or incorrect



After all of the questions have been answered the game will display how many out of the total number asked the player got right. The game will then return to the main menu.


2.  Adding A Question
When the user chooses the Add A Question option, the game will prompt the user for the question, and the answer. It will append these to the questions file and return to the main menu.


3.  Exiting
When the user chooses the Exit option, the game will simply shut down.

Getting Started
Create a python file called 'quiz.py'.

Questions will be stored in a file called questions.py. Instead of just putting some questions in the file, we'll write the code for adding questions, and use that to create and populate the file.