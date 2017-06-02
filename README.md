# AEQ Technical Assignment

## Part 1: The Castle Company

### castle.py

The `castle.py` has a function that accepts an input array of integers from which
it determines how many castles should be built based on the following criteria:

`A castle will only be built in a valley or on a peak.`

`A peak is an integer or series of integers that is above the immediately preceding
and following ints. I.E: [5,7,7,6,2] the sequence of 2 7s is a peak.`

`A valley is an integer or series of integers that is below the immediately preceding
and following ints. I.E: [5,3,2,2,5] the sequence of 2 2s is a valley.`

#### How to use:
From command line within the Castles directory call:

`$ python3 castle.py`

The input array can be changed inside of the file to be a specific input array,
 for now it passes in a randomly generated array of integers.

## Part 2: The Transformation Company

The `run.py` and `transformer.py` files are used in conjuction to determine whether the autobots
or decepticons, from an input array, are the victors after a series of battles.

The victor of each battle is determine by comparing the battling transformers' stats.

The `transformer.py` file holds the class definition for a transformer. This class
definition contains name, allegiance, strength, intelligence, speed, endurance, rank,
courage, firepower, skill, calculated rating, and whether they are alive, for each
transformer.

#### How to use:
From command line within the Transfomers directory call:

`$ python3 run.py`

The input array can be changed inside of the `run.py` file to add or remove
autobots and decepticons for the battles to come.


## License

This software is free to use under the MIT license. See the [LICENSE][] file for more details.

  [License]: https://github.com/greg-petersen/AEQTakeHome/blob/master/LICENSE.txt