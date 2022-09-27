import random

CLEAN = "clean"
DIRTY = "dirty"
TIME_STEPS = 100000

class Square:
    state = CLEAN

def generate_random():
    return random.randint(0, 100)/100

# Function calculate_cost() accepts R, CS, CM, P, Q
def calculate_cost(r, cs, cm, p, q):
    A = Square()
    B = Square()
    current_state = A
    vacuum_state = A
    cost = 0
    reward = 0
    for i in range(0, TIME_STEPS):
        # print(i, " A: ", A.state)
        # print(i, " B: ", B.state)
        
        # Check square state
        for i in range(0, 2):
            if (current_state.state == CLEAN):
                random = generate_random()
                if (random < p):
                    current_state.state = DIRTY
            if (current_state == A):
                current_state = B
            elif (current_state == B):
                current_state = A
        
        # Check vacuum position
        if (vacuum_state.state == DIRTY):
            cost += cs
            vacuum_state.state = CLEAN
        else: 
            random = generate_random()
            if (random < q):
                cost += cm
                if (vacuum_state == A):
                    vacuum_state = B
                elif (vacuum_state == B):
                    vacuum_state = A

        # Calculate rewards
        if (A.state == CLEAN and B.state == CLEAN):
            reward += 2*r
        elif ((A.state == CLEAN and B.state == DIRTY) or (A.state == DIRTY and B.state == CLEAN)):
            reward += r

    score = (reward - cost)/TIME_STEPS
    print("R: ", r, ", CS: ", cs, ", CM: ", cm, ", P: ", p, ", Q: ", q, ", final score: ", score)

def main():
    #Round 1
    print("---- Row 1 ----")
    calculate_cost(10, 4, 8, 0.2, 0.0) 
    calculate_cost(10, 4, 8, 0.2, 0.2)
    calculate_cost(10, 4, 8, 0.2, 0.4) 
    calculate_cost(10, 4, 8, 0.2, 0.6) 
    calculate_cost(10, 4, 8, 0.2, 0.8) 
    calculate_cost(10, 4, 8, 0.2, 1.0) 

    #Row 2
    print("---- Row 2 ----")
    calculate_cost(10, 4, 8, 0.8, 0.0) 
    calculate_cost(10, 4, 8, 0.8, 0.2)
    calculate_cost(10, 4, 8, 0.8, 0.4) 
    calculate_cost(10, 4, 8, 0.8, 0.6) 
    calculate_cost(10, 4, 8, 0.8, 0.8) 
    calculate_cost(10, 4, 8, 0.8, 1.0) 

    #Row 3
    print("---- Row 3 ----")
    calculate_cost(10, 4, 20, 0.1, 0.0) 
    calculate_cost(10, 4, 20, 0.1, 0.2)
    calculate_cost(10, 4, 20, 0.1, 0.4) 
    calculate_cost(10, 4, 20, 0.1, 0.6) 
    calculate_cost(10, 4, 20, 0.1, 0.8) 
    calculate_cost(10, 4, 20, 0.1, 1.0) 

    #Row 4
    print("---- Row 4 ----")
    calculate_cost(10, 4, 20, 0.0, 0.0) 
    calculate_cost(10, 4, 20, 0.0, 0.2)
    calculate_cost(10, 4, 20, 0.0, 0.4) 
    calculate_cost(10, 4, 20, 0.0, 0.6) 
    calculate_cost(10, 4, 20, 0.0, 0.8) 
    calculate_cost(10, 4, 20, 0.0, 1.0) 

    #Row 5
    print("---- Row 5 ----")
    calculate_cost(10, 8, 4, 0.2, 0.0) 
    calculate_cost(10, 8, 4, 0.2, 0.2)
    calculate_cost(10, 8, 4, 0.2, 0.4) 
    calculate_cost(10, 8, 4, 0.2, 0.6) 
    calculate_cost(10, 8, 4, 0.2, 0.8) 
    calculate_cost(10, 8, 4, 0.2, 1.0) 

    #Row 6
    print("---- Row 6 ----")
    calculate_cost(10, 8, 2, 0.2, 0.0) 
    calculate_cost(10, 8, 2, 0.2, 0.2)
    calculate_cost(10, 8, 2, 0.2, 0.4) 
    calculate_cost(10, 8, 2, 0.2, 0.6) 
    calculate_cost(10, 8, 2, 0.2, 0.8) 
    calculate_cost(10, 8, 2, 0.2, 1.0) 

if __name__ == "__main__":
    main()
