
# Console Pentago

## What it is

Console Pentago is Python program that runs from the command line. It's a game modeled after Tic-Tac-Toe and has an incredibly large state space which poses a great challenge for Computer Ai to win against a human player.

## The latest version

The current version of this program is written for Python 3.7 due to the usage of Python's new f-string syntax.

## Installation

To to use this program begin by opening your favorite terminal program or
command prompt on windows machines and navigating to the directory in which
the program resides. Then install any required dependencies.

### Install dependencies

#### Currently numpy and termcolor are the only two dependencies required

`:~$ pip3 install -r requirements.txt`

## To run the program type

  `:~$ python3 pentago.py` into your terminal.

## Navigating the program

### Starting a game of Pentago

#### Enter your players info on one one line separated by a space

**i.e. "name", "color", and "type of player"**

### Example:

`>  Carl W Human`

`>  BotMan B AI`

### Game Play

- Entering moves:

  - Enter moves using the following format

  - "Block Number"/"Block index" "block""Rotation direction"

      i.e. ` > 2/1 2R`

      This would place a marble on the second block and in the first of 9 positions on the block.
        The second argument is the block number and direction of rotation.

  - Directions of rotation are 'r', 'R', 'l', or 'L' for right and left rotatation

### Modifying AI search parameters:
  
- Search depth can be modified by changing the global **SEARCH_DEPTH** variable on line 16 of pentago.py

- Search method can be modified by changing the **SEARCH_METHOD** variable on line 18 of pentago.py

  - i.e. "AlphaBeta" or "MiniMax"

## Licensing

Copyright 2016 Carl Argabright

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Contact

If you have any comments or suggestions please feel free to leave them for me on
GitHub

If you need to say something a little more personal feel free to send me an
email at carl.argbright@gmail.com
