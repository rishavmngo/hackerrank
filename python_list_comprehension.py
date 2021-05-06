x = int(input())
y = int(input())
z = int(input())
n = int(input())
z = [[a,b,c]  for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
z = [ q for q in z if sum(q) != n]
print(z)
