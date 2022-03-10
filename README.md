# cse210-05 Cycle Game

<!-- Design Plan:
-Duplicate and rename control_actions_actor.py to apply to two actors/ players, and update the "I, J, K, L" keys in keyboard_service.py to be arrows - Kosei
-Update Handle_collisions.py to handle snake collisions, the lose game functionality, and how the snakes grow -Camden
-Update main.py and make it control two players -Mary
-Adapt Snake files to cycle game, especially the ReadME, Constants.py, and Director.py files. Jump in where needed to make game functional, and possible collaborate with Mary to make a "game rounds and score" enhancement - Jenny
(Polymorphism is applied in our design by overwriting the execute method in varies files)
-->

# Cycle
Cycle is inspired by the game Tron Cycle. 

Cycles is a two player game where you each control a bicycle and try to make the other play run into your trail by blocking them in with it.

You play the game on a simulated terminal, with a textual interface.

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 snake 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies

* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors

*  Mary Goff
*  Camden Miller
*  Kosie Kameta
*  Jennifer Walton
