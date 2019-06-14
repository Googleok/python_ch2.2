
index = 0
for color in ['yellow', 'blue', 'black', 'white']:
    print("{0}:{1}".format(index, color))
    index += 1

for index, color in enumerate(['yellow', 'blue', 'black', 'white']):
    print("{0}:{1}".format(index, color))


seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))

for t in z:
    print(t, type(t))

tl = [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
seq1, seq2 = zip(*tl)
print(seq1)