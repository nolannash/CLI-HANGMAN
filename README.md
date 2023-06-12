# Dev Dot Exe(cute)
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

## References and Acknowledgements
Created by Nolan Nash and Kevin Lumauig


--------------------------
## [Licensing](/LICENSE)
MIT License

Copyright (c) [2023] [Nolan Nash, Kevin Lumauig]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------
## Other Misc.
----------
### Check Out Our Blog Posts
* [Nolan's Blog]()

* [Kevin's Blog]()