# Python RPG-DiceRoller

This is a CLI python dice roller

## Basic use:

For using you need to enter, the number of dices you want to roll, like on the rpgs books
Example: `1d20` *this will roll* **one** *dice of* **20sides.**, if you want to roll 5 dices with 100 sides
you just need to enter: `5d100` this works for "unconventional" dices, like the d13, d9, d5, and so on.

```
$ Enter the dices you want to roll!
$ 1d20
$ You rolled:
$ 1d20: 3
```
That's a example of how to use the dice roller, but you have other options, like:

* Modfiers
* Multiple Rools
* Log

## Modfiers:

For using Modfiers you just need to type the dices and following with a "," you desired modfier, here's
a example on how it works, and a quick example on Multiple Rools:

```
$ Enter the dices you want to roll!
$ 1d20-2 3d100+30
$ you rolled:
$ 1d20-2: 12 #The original roll was 14
$ 3d100+30: 130 55 86 #Original rolls: 100 25 56
```

## Log

The log will be send to a file called `mylog.txt` all the output of the program will be stored inside that file
and everytime that you run the program, a new log will be appended to that file. If the file does not exist, it'll
be created on the run.
