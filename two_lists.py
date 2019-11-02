m1 = [1, 3, 5, 10]
m2 = [3, 8, 4, 5]

ans = []

for a in m1:
  if a in m2:
    ans.append(a)

print(ans)