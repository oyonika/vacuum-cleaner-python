# Vacuum Cleaner

Implement a version of the simple vacuum cleaner agent. It should operate in the following way:

- There are two squares, A and B.
- Initially, both squares are clean. The vacuum cleaner is in square A.
- The program runs through a simulation of 100 000 time steps.
- At the beginning of each time step, for each square:
    - If it was dirty, it remains dirty.
    - If it was clean, it becomes dirty with some probability p. To simulate this, generate a random number between 0 and 1. If it is less than p, then make the square dirty.)
- During each time step,
    - If the square in which the vacuum cleaner is currently located is dirty, then suck up the dirt (with cost cs), which makes the square clean.
    - Otherwise, move (with cost cm) to the other square with some probability q and just stay in the current location with probability 1 - q.
- At the end of the time step, the agent earns a reward of R for each square that is clean. (If both squares are clean, then the reward is 2R. If only one square is clean, the reward is R. If both squares are dirty, the reward is 0.)
- Set up your code so that it runs through 100 000 time steps and prints the average score (rewards minus costs) earned per time step, to 3 decimal places (for example, 7.862).
