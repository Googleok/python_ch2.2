seq = range(10)
print(seq, type(seq))

print(list(seq))
print(list(seq[5:]))
print(len(seq))

for i in seq:
    print(i, end=" ")
else: # for문이 정상적으로 종료되면 else문 실행
    print()

for i in range(0, -10, -1):
    print(i, end=" ")
else:
    print()

for i in range(-10, 0, 1):
    print(i, end=" ")
print()

for i in range(0,10,2):
    print(i, ens=' ')
else:
    print()

print('ok')
