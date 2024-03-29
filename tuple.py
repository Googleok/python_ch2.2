# 튜플 생성


t = ()      # 공튜플
t = (1,)    # 항목이 하나일 때는 반드시, (콤마) 사용
t = (1, 2, 3)
print(t, type(t))

#
# sequenece 지원 연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[-0], t[1], t[2])

# 슬라이싱
print(t[1:30])
print(t[::-1])

# 반복
print(t*2)

# 연결
print(t + (4, ))

# 길이
print(len(t))

# 확인
print(4 not in t)

# tuple은 immutable 이다
# t[0] = 100

# 여러개 값의 대입
x, y, z = 10, 20, 30
print(x, y, z)

# swap
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

#
# 객체함수 : 많지 않다 ( immutable 이기 때문에)
#

t = (20, 30, 10, 20)
print(t.index(20))
print(t.count(20))

# 변환
t = (1, 2, 3, 3)
print(t)

# tuple -> set
s = set(t)
print(s, type(s))

# tuple -> list
l = list(t)
print(l, type(l))

# list -> tuple
t = tuple(l)
print(t, type(t))