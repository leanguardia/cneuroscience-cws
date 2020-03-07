#for the submission uncomment the submission statements
#so submission.README

from math import *
# from submission import *

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

def learn_pattern(pattern, weight_matrix, n):
    pattern_size = len(pattern)
    for i in range(pattern_size):
        for j in range(i + 1, pattern_size): # print(i, j)
            weight_matrix[i][j] += (1/n) * pattern[i] * pattern[j]
            weight_matrix[j][i] = weight_matrix[i][j]
    return weight_matrix

def energy_of(pattern, weight_matrix):
    energy = 0
    pattern_size = len(pattern)
    for i in range(pattern_size):
        for j in range(i + 1, pattern_size):
            energy += pattern[i] * weight_matrix[i][j] * pattern[j]
    return -0.5 * energy
    

# === MAIN PROGRAM === #

one   = [-1,-1, 1,-1,-1, 1,-1, 1,-1,-1,-1]
three = [ 1,-1, 1, 1,-1 ,1 ,1 ,1, 1,-1,-1]
six   = [ 1, 1,-1, 1, 1, 1, 1,-1, 1, 1,-1]
n = 3

weight_matrix = initialize_weigth_matrix()

weight_matrix = learn_pattern(one, weight_matrix, n)
weight_matrix = learn_pattern(three, weight_matrix, n)
weight_matrix = learn_pattern(six, weight_matrix, n)
# print(weight_matrix)
        
#submission=Submission("Denis Leandro Guardia Vaca")
#submission.header("Denis Leandro Guardia Vaca")

seven_segment(one)
print(energy_of(one, weight_matrix))
seven_segment(three)
print(energy_of(three, weight_matrix))
seven_segment(six)
print(energy_of(six, weight_matrix))

##this assumes you have called your weight matrix "weight_matrix"
# submission.section("Weight matrix")
# submission.matrix_print("W",weight_matrix)

print("test1")
#submission.section("Test 1")

test = [ 1,-1, 1, 1,-1, 1, 1,-1,-1,-1,-1 ]

seven_segment(test)
print(energy_of(test, weight_matrix))
#submission.seven_segment(test)
##for COMSM0027

##where energy is the energy of test
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
#submission.section("Test 1")

seven_segment(test)
print(energy_of(test, weight_matrix))

#submission.seven_segment(test)

##for COMSM0027
##where energy is the energy of test
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step


#submission.bottomer()



