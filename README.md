## Deck Problem.

#### **Problem Statement:**

###### **Part 1:**

You are given a deck containing N cards. While holding the deck:

1. Take the top card off the deck and set it on the table
2. Take the next off the top and put it on the bottom of the deck in your hand.
3. Continue steps 1 and 2 until all cards are on the table. This is a round.
4. Pick up the deck from the table and repeat steps 1-3 until the deck is in original order.

Write a program to determine how many rounds it will take to put a deck back into the original order. This will involve creating a data structure to represent the order of the cards. Do not use an array.

The program should take the number of cards in the deck as a command line argument and write results to standard output.

Please ensure the program compiles and runs correctly (no pseudo-code). You can use any programming language of your choice (eg. C, Java, Python etc.).


###### **Part 2:**

Once the program for the above has been written please write a program that runs unit test cases to validate the program. Please write unit tests for all the various test case scenarios for this.
Please provide clear instructions on how to run program and unit tests.


---

#### **Usage:**

##### Requirements:
- deck_problem.zip ([Download Link](https://github.com/JoseLGonza/DeckProblem/raw/main-problem-functionality/deck_problem.zip))
- Python 3
- A Terminal



After downloading the deck_problem.zip you simply have to run it on your terminal with one of the three available commands:
- `solve -s (-v)`
- `unit-tests`
- `test-cases`

`-s / --size` is a mandatory argument and represents the deck size when solving the problem.

##### Examples:

Solve problem with a 10 card deck size:

`python deck_problem.zip solve -s 10`

Solve problem with a 4 card deck size, and output problem progress:

`python deck_problem.zip solve -s 4 -v`

Run unit tests:

`python deck_problem.zip unit-tests`

Run a set of test cases:

`python deck_problem.zip test-cases`


---

#### **How to Build:**

##### Requirements:
- Bazel


##### Build:
Using [Bazel](https://github.com/bazelbuild/bazel) as the build tool for this small project.

To create a new python zip after making changes to the project, you need to run the following command:

`bazel build //src/... --build_python_zip`

This will generate a new `deck_problem.zip` under `DeckProblem/bazel-bin/src/`.