#for the submission uncomment the submission statements
#so submission.README

from math import *
from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""
        if d1:
            word="|"
        else:
            word=" "
        if d3:
            word+="_"
        else:
            word+=" "
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))

# === MY PROCEDURES === #

def initialize_weigth_matrix():
    return [[0.0 for col in range(11)] for row in range(11)]

def report_pattern(pattern, weight_matrix):
    submission.seven_segment(pattern)
    submission.print_number(energy_of(pattern, weight_matrix))
    submission.qquad()

def learn_pattern(pattern, weight_matrix, n):
    pattern_size = len(pattern)
    for i in range(pattern_size):
        for j in range(i + 1, pattern_size): # print(i, j)
            weight_matrix[i][j] += (1/n) * pattern[i] * pattern[j]
            weight_matrix[j][i] = weight_matrix[i][j]
    return weight_matrix

def recall_step(pattern, weight_matrix):
    pattern_size = len(pattern)
    for i in range(pattern_size):
        sum = 0
        for j in range(pattern_size):
            sum += weight_matrix[i][j]
        if sum >= 0: 
            pattern[i] = 1
        else:
            pattern[i] = -1
    return pattern

def energy_of(pattern, weight_matrix):
    energy = 0
    pattern_size = len(pattern)
    for i in range(pattern_size):
        for j in range(pattern_size):
            energy += pattern[i] * weight_matrix[i][j] * pattern[j]
    energy = -0.5 * energy
    print(energy)
    return energy

def recall(pattern, weight_matrix, convergence_steps):
    previous_pattern = pattern
    repetitions = 0
    while (repetitions <= convergence_steps):
        pattern = recall_step(pattern, weight_matrix)
        seven_segment(three)
        energy_of(pattern, weight_matrix)
        if (pattern == previous_pattern):
            repetitions += 1
        else: 
            repetitions = 0
            previous_pattern = pattern
        report_pattern(pattern, weight_matrix)

# === MAIN PROGRAM === #

submission=Submission("denis_leandro_guardia_vaca")
submission.header("Denis Leandro Guardia Vaca")

one   = [-1,-1, 1,-1,-1, 1,-1, 1,-1,-1,-1]
three = [ 1,-1, 1, 1,-1 ,1 ,1 ,1, 1,-1,-1]
six   = [ 1, 1,-1, 1, 1, 1, 1,-1, 1, 1,-1]
n = 3

weight_matrix = initialize_weigth_matrix()

weight_matrix = learn_pattern(three, weight_matrix, n)
weight_matrix = learn_pattern(six, weight_matrix, n)
weight_matrix = learn_pattern(one, weight_matrix, n)

submission.section("Patterns")
report_pattern(one, weight_matrix)
report_pattern(three, weight_matrix)
report_pattern(six, weight_matrix)
        
submission.section("Weight matrix")
submission.matrix_print("W",weight_matrix)

print("Test 1")
submission.section("Test 1")

test1 = [ 1,-1, 1, 1,-1, 1, 1,-1,-1,-1,-1 ]
report_pattern(test1, weight_matrix)
recall(test1, weight_matrix, 2)

print("Test 2")
submission.section("Test 2")

test2 =[1, 1, 1, 1, 1, 1, 1,-1,-1,-1,-1]
report_pattern(test2, weight_matrix)
recall(test2, weight_matrix, 2)

submission.bottomer()
