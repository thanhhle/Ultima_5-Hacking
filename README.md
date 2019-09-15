# Ultima_5-Hacking
An application written in Python

## Prerequisites
- The game will probably not run directly on modern operating systems, but it will run just fine under DOSBox (a DOS environment designed to play older games). Grab DOSBox from https://www.dosbox.com. DOSBox will require a bit of setup, but the game should run under DOSBox without any additional tweaking of the game itself.
- Completing this assignment will require you to use a binary hex editor.

## Description:
- This assignment is designed to introduce to you how malware can infect compiled programs, give you exposure to using a hex editor to understand computer code at a machine level, and how security researchers inspect binary code to understand software at a low level.
- First, play the game enough to establish a character and get a feel for how the game is played. If you have experience playing CRPGs, then this game will be at least somewhat familiar to you. Then, you will save the game by pressing ’Q’ and then alter the game’s files to give your character maximum stats and gold. You can check the character’s stats by pressing ’Z’ and then selecting the highlighted character on the right. It will be up to you to locate which file(s) are necessary to modify and what values to place into those file(s) at specific locations.

## Assignment
- Hack the game by pres-setting the following values of all characters in the game:
  - Str = 99
  - Int = 99
  - Dex = 99
  - HP = 999
  - Max HP = 999 
  - Exp = 9999
  - Gold = 9999
  - Keys = 100
  - Skull keys = 100
  - Gems = 100
  - Black badge = 1
  - Magic carpets = 2
  - Magic Axes = 1
- Write an interactive program which allows the user to change the above values to whatever they want (not just a pre-set value structure).
