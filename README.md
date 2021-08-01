# Python RPG-DiceRoller

This is a CLI python dice roller

## Basic use:

For using you need to enter, the number of dices you want to roll, like on the rpgs books
Example: `1d20` *this will roll one dice of 20sides.*, if you want to roll 5 dices with 100 sides
you just need to run `5d100` that work for "unconventional" dices, like the d13, d9, d5, and so on.

```
$ Enter the dices you want to roll!
$ For help and manual instructions, type: "h" #This help message will only show on the first time running.
$ 1d20
$ You runned:
$ 1d20: 3
```
That's a example of how to use the dice roller, but you have other options, like:

* Modfiers
* Multiple Rools
* Log

## Modfiers:

For using Modfiers you just need to type the dices and following with a "," you desired modfier, here's
a example on how it works:

```
$ Enter the dices you want to roll!
$ 1d20,2 3d100,30
$ you runned:
$ 1d20+3: 18 #The original roll was 15
$ 3d100+3: 130 55 86 #Original rolls: 100 25 56
```
