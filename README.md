## Deck Problem.

#### **Problem Statement:**

**Part 1:**

You are given a deck containing N cards. While holding the deck:

1. Take the top card off the deck and set it on the table
2. Take the next off the top and put it on the bottom of the deck in your hand.
3. Continue steps 1 and 2 until all cards are on the table. This is a round.
4. Pick up the deck from the table and repeat steps 1-3 until the deck is in original order.

Write a program to determine how many rounds it will take to put a deck back into the original order. This will involve creating a data structure to represent the order of the cards. Do not use an array.

The program should take the number of cards in the deck as a command line argument and write results to standard output.

Please ensure the program compiles and runs correctly (no pseudo-code). You can use any programming language of your choice (eg. C, Java, Python etc.).


**Part 2:**

Once the program for the above has been written please write a program that runs unit test cases to validate the program. Please write unit tests for all the various test case scenarios for this.
Please provide clear instructions on how to run program and unit tests.


Example:


Cards   Rounds
   2        2
   3        3
   4        2
   5        5
   6        6
   7        5
   8        4
   9        6
  10        6
  11       15
  12       12
  13       12
  14       30
  15       15
  16        4
  20       20
  30       12
  31      210
  32       12
  50       50
  51       42
  52      510