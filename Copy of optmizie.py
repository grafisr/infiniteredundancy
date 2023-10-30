import math
import numpy as np
import itertools
import numpy.linalg as la
import scipy.linalg as spla
import pulp


# Define the dimensions
# m, n = 2, 9
# num_ones = 8  # Number of 1s allowed in x

# Fin_2 = -0.32635182+1.85083316j
# Fin_3 = -1.43969262-0.52400526j

v_combinations = list(itertools.product([0, 1], repeat=9))
fourier_coefficients = [np.fft.fft(v) for v in v_combinations]

Fin = -0.17364818+0.98480775j

def expte(x):
    return math.cos(x*np.pi / 180) + math.sin(x*np.pi / 180) * 1j

###############################
# vectro: =  (0, 0, 0, 0, 0, 0, 1, 1, 0)
# Coeeficeint: = [ 2.        +0.j         -0.32635182+1.85083316j -1.43969262-0.52400526j
#   0.5       -0.8660254j   0.26604444+0.22323779j  0.26604444-0.22323779j
#   0.5       +0.8660254j  -1.43969262+0.52400526j -0.32635182-1.85083316j]

# vectro: =  (0, 0, 1, 0, 0, 1, 1, 1, 1)
# Coeeficeint: = [ 5.        +0.j         -0.32635182+1.85083316j -1.43969262-0.52400526j
#  -1.        +1.73205081j  0.26604444+0.22323779j  0.26604444-0.22323779j
#  -1.        -1.73205081j -1.43969262+0.52400526j -0.32635182-1.85083316j]
###############################


# D = np.array([[np.real(Fin)],
#               [np.imag(Fin)]])

# print(D)

c0 = expte(-0)
c1 = expte(-40)
c2 = expte(-80)
c3 = expte(-120)
c4 = expte(-160)
c5 = expte(-200)
c6 = expte(-240)
c7 = expte(-280)
c8 = expte(-320)

c10 = expte(-0)
c11 = expte(-80)
c12 = expte(-160)
c13 = expte(-240)
c14 = expte(-320)
c15 = expte(-400)
c16 = expte(-480)
c17 = expte(-560)
c18 = expte(-640)

c20 = expte(-0)
c21 = expte(-120)
c22 = expte(-240)
c23 = expte(-360)
c24 = expte(-480)
c25 = expte(-600)
c26 = expte(-720)
c27 = expte(-840)
c28 = expte(-960)

c40 = expte(-0)
c41 = expte(-160)
c42 = expte(-320)
c43 = expte(-480)
c44 = expte(-640)
c45 = expte(-800)
c46 = expte(-960)
c47 = expte(-1120)
c48 = expte(-1280)

c80 = expte(-0)
c81 = expte(-320)
c82 = expte(-640)
c83 = expte(-960)
c84 = expte(-1280)
c85 = expte(-1600)
c86 = expte(-1920)
c87 = expte(-2240)
c88 = expte(-2560)

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c40), np.real(c41), np.real(c42), np.real(c43), np.real(c44), np.real(c45), np.real(c46), np.real(c47), np.real(c48)],
#               [np.imag(c40), np.imag(c41), np.imag(c42), np.imag(c43), np.imag(c44), np.imag(c45), np.imag(c46), np.imag(c47), np.imag(c48)]])

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c10), np.real(c11), np.real(c12), np.real(c13), np.real(c14), np.real(c15), np.real(c16), np.real(c17), np.real(c18)],
#               [np.imag(c10), np.imag(c11), np.imag(c12), np.imag(c13), np.imag(c14), np.imag(c15), np.imag(c16), np.imag(c17), np.imag(c18)]])

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c10), np.real(c11), np.real(c12), np.real(c13), np.real(c14), np.real(c15), np.real(c16), np.real(c17), np.real(c18)],
#               [np.imag(c10), np.imag(c11), np.imag(c12), np.imag(c13), np.imag(c14), np.imag(c15), np.imag(c16), np.imag(c17), np.imag(c18)],
#               [np.real(c40), np.real(c41), np.real(c42), np.real(c43), np.real(c44), np.real(c45), np.real(c46), np.real(c47), np.real(c48)],
#               [np.imag(c40), np.imag(c41), np.imag(c42), np.imag(c43), np.imag(c44), np.imag(c45), np.imag(c46), np.imag(c47), np.imag(c48)]])

# A = np.array([[np.real(c20), np.real(c21), np.real(c22), np.real(c23), np.real(c24), np.real(c25), np.real(c26), np.real(c27), np.real(c28)],
#               [np.imag(c20), np.imag(c21), np.imag(c22), np.imag(c23), np.imag(c24), np.imag(c25), np.imag(c26), np.imag(c27), np.imag(c28)]])
A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
              [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
              [np.real(c20), np.real(c21), np.real(c22), np.real(c23), np.real(c24), np.real(c25), np.real(c26), np.real(c27), np.real(c28)],
              [np.imag(c20), np.imag(c21), np.imag(c22), np.imag(c23), np.imag(c24), np.imag(c25), np.imag(c26), np.imag(c27), np.imag(c28)]])

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c10), np.real(c11), np.real(c12), np.real(c13), np.real(c14), np.real(c15), np.real(c16), np.real(c17), np.real(c18)],
#               [np.imag(c10), np.imag(c11), np.imag(c12), np.imag(c13), np.imag(c14), np.imag(c15), np.imag(c16), np.imag(c17), np.imag(c18)],
#               [np.real(c20), np.real(c21), np.real(c22), np.real(c23), np.real(c24), np.real(c25), np.real(c26), np.real(c27), np.real(c28)],
#               [np.imag(c20), np.imag(c21), np.imag(c22), np.imag(c23), np.imag(c24), np.imag(c25), np.imag(c26), np.imag(c27), np.imag(c28)]])

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c80), np.real(c81), np.real(c82), np.real(c83), np.real(c84), np.real(c85), np.real(c86), np.real(c87), np.real(c88)],
#               [np.imag(c80), np.imag(c81), np.imag(c82), np.imag(c83), np.imag(c84), np.imag(c85), np.imag(c86), np.imag(c87), np.imag(c88)]])

# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)],
#               [np.real(c10), np.real(c11), np.real(c12), np.real(c13), np.real(c14), np.real(c15), np.real(c16), np.real(c17), np.real(c18)],
#               [np.imag(c10), np.imag(c11), np.imag(c12), np.imag(c13), np.imag(c14), np.imag(c15), np.imag(c16), np.imag(c17), np.imag(c18)]])



# A = np.array([[np.real(c0), np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#               [np.imag(c0), np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)]])

# A = np.array([[np.real(c10), np.real(c11), np.real(c12), np.real(c13), np.real(c14), np.real(c15), np.real(c16), np.real(c17), np.real(c18)],
#               [np.imag(c10), np.imag(c11), np.imag(c12), np.imag(c13), np.imag(c14), np.imag(c15), np.imag(c16), np.imag(c17), np.imag(c18)]])

# A = np.array([[np.real(c20), np.real(c21), np.real(c22), np.real(c23), np.real(c24), np.real(c25), np.real(c26), np.real(c27), np.real(c28)],
#               [np.imag(c20), np.imag(c21), np.imag(c22), np.imag(c23), np.imag(c24), np.imag(c25), np.imag(c26), np.imag(c27), np.imag(c28)]])

# A = np.array([[np.real(c40), np.real(c41), np.real(c42), np.real(c43), np.real(c44), np.real(c45), np.real(c46), np.real(c47), np.real(c48)],
#               [np.imag(c40), np.imag(c41), np.imag(c42), np.imag(c43), np.imag(c44), np.imag(c45), np.imag(c46), np.imag(c47), np.imag(c48)]])

m = len(A)
n = len(A[0])


# A = np.array([[np.real(c1), np.real(c2), np.real(c3), np.real(c4), np.real(c5), np.real(c6), np.real(c7), np.real(c8)],
#      [np.imag(c1), np.imag(c2), np.imag(c3), np.imag(c4), np.imag(c5), np.imag(c6), np.imag(c7), np.imag(c8)]])

# print(np.shape(A))
# print(np.shape(D))

# x = np.linalg.lstsq(A, D, rcond=None)[0]
#
# print(x)
# Create a linear programming problem
t = 0
zt = 0
for ind, it in enumerate(fourier_coefficients):
    # print(i)
    # print(v_combinations[ind])
    num_ones = int(np.real(it[0]))
    # D = np.array([[np.real(it[3])],
    #               [np.imag(it[3])]])

    D = np.array([[np.real(it[1])],
                  [np.imag(it[1])],
                  [np.real(it[3])],
                  [np.imag(it[3])]])

    # D = np.array([[np.real(it[1])],
    #                             [np.imag(it[1])],
    #                             [np.real(it[2])],
    #                             [np.imag(it[2])],
    #                             [np.real(it[3])],
    #                             [np.imag(it[3])]])

    # D = np.array([[np.real(it[1])],
    #               [np.imag(it[1])],
    #               [np.real(it[2])],
    #               [np.imag(it[2])],
    #               [np.real(it[3])],
    #               [np.imag(it[3])]
    #               [np.real(it[4])],
    #               [np.imag(it[4])]])
    # D = np.array([[np.real(it[1])],
    #               [np.imag(it[1])],
    #               [np.real(it[-1])],
    #               [np.imag(it[-1])]])
    # D = np.array([[np.real(it[4])],
    #               [np.imag(it[4])]])

    # D = np.array([[np.real(it[1])],
    #               [np.imag(it[1])],
    #               [np.real(it[4])],
    #               [np.imag(it[4])]])

    # print(num_ones, D)
    lp_problem = pulp.LpProblem("BinaryLinearSystem", pulp.LpMinimize)
# # # Define binary decision variables for x (8x1)
    x = [pulp.LpVariable(f'x{i}', cat=pulp.LpBinary) for i in range(n)]
# # # Define an additional binary variable for counting the number of 1s in x
#     count_ones = pulp.LpVariable("count_ones", cat=pulp.LpInteger, lowBound=num_ones, upBound=num_ones)
# # # Define the objective function (minimize 0)
    lp_problem += 0
# # # Add the constraints Ax = b
    for i in range(m):
        lp_problem += pulp.lpSum(A[i, j] * x[j] for j in range(n)) == D[i]
# # Add the constraint for counting the number of 1s in x
#     lp_problem += count_ones == pulp.lpSum(x)
# # # Solve the linear programming problem
#     lp_problem.solve()
    lp_problem.solve(pulp.PULP_CBC_CMD(msg=0))

# # print(lp_problem.status)
#     if lp_problem.status == pulp.LpStatusOptimal:
#         print("The constraints are feasible.")
#     else:
#         print("The constraints are infeasible.")
# # # Extract the solution
    solution = [int(pulp.value(x[i])) for i in range(n)]
# # # Print the solution
#     print("Solution:", solution)
#     print(v_combinations[ind])

    if solution == list(v_combinations[ind]):
        # print("The lists are identical")
        t = t +1
        print(np.real(it[1]), np.imag(it[1]), np.real(it[3]), np.imag(it[3]))
    else:
        # print("The lists are not identical")
        # print("Solution:", solution)
        # print("volution:",v_combinations[ind])
        zt = zt +1

    # if ind == 6:
    #     break

print("success", t)
print("failure", zt)
