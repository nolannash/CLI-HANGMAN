# PYTHON HANGMAN
<sub>A Game By: @nolannash (Nolan Nash) and @klums24 (Kevin Luauig) </sub>

# Project Overview:
Welcome to our Hang-man game. A python CLI application that allows a player to play hang-man at several levels of difficulty. The application allows a user to create a "profile" which saves the results from games the player has played. When starting a new game a user is able to select a difficulty for the game: "**Easy**","**Medium**" and "**Hard**". 
After selecting a difficulty a word is then chosen from a list and the game is begun. Once the game is over a player is returned to the start menu where they can either login again to play a new game, make a new profile or choose to leave the game.
# Installation and usage:
## Installation
To install and use our game:
1. Fork and clone to your local environment. 
2. Run `pipenv install` to install dependencies
3. Run cli.py to bein playing!

## Usage
To use our program all that is needed after adding it to your local environment, installing the environment and grabbing your pocket dictionary is to run the cli.py file.
### Notable/Important Features
There are a wide variety of useful and important features, however the main notable features can be found in:
-**cli.py**
    - This is the "play button" when you run this file you are able to experience the full game
- **helpers.py**
  - The helpers file contains all of the methods and logic for navigating the various menus of the game as well as the methods to change the text color 
- **game.py**
  - The game file contains all of the logic for the game class. Each instance of a game is initialized with a difficulty, starting score of 0 and a player. After the game ends the score is saved to a result, tying the game and the games score to whoever played the game.
- **player.py**
  - The player class is initialized with a name, username and password. A player is able to play as many games as they want at whatever difficulty they want and the result of their games are saved to a personal results column in the database.
  - The player class also contains methods for finding players by id, name and username allowing users to find their account if they forgot username 
  - (due to issues with password security and password validation if a user has forgotten their password they must make a new profile)
- **result.py**
  - The result class acts as the bridge between a player and a game. Each time a player finishes a game, an instance of the result class is created with a player_id pointing to the player who played the game and a game_id pointing to the actual game, allowing players to see how many points they scored in each game they played.
---
# References, Acknowledgements and Other Misc.
## References and Acknowledgements
- The list of words for each difficulty as well as the parameters to choose the words was done using CHAT GPT

--------------------------
## [Licensing](/LICENSE)
-------------
## Other Misc.
----------
### Check Out Our Blog Posts
* [Nolan's Blog]()

* [Kevin's Blog]()