A = [x**2 for x in range(0,7)]
print(A)

B = [(x,x**2) for x in range(7)]
print(B)

C = [x**2 for x in range(15) if x%2==0]
print(C)

D = [3 for i in range(5)]
print(D)

E = [[0 for j in range(3) ] for i in range(3)]
print(E)

F = [[1 if j ==1 else 0 for j in range (3)] for i in range(3)]
print(F)

d = "Yogyakarta dan Surakarta"
G = [x for x in d if x in "aiueoAIUEO"]
print(G)
