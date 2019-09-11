#I have string s = 'a3c9b1c1' My expected out is a3b1c10 which has to sort in order of alphabet


import re
from collections import defaultdict

s = 'a3c9b1c1'
data = re.findall(r'([A-Za-z])(\d+)', s)
# [('a', '3'), ('c', '9'), ('b', '1'), ('c', '1')]
counts = defaultdict(int)
for letter, count in data:
    counts[letter] += int(count)
# {'a': 3, 'c': 10, 'b': 1}
print(''.join('{}{}'.format(k, v) for k, v in sorted(counts.items())))

> a3b1c10
from collections import Counter

s = 'aaacccccccccbc'
c = Counter(s)
print(''.join('{}{}'.format(k, v) for k, v in sorted(c.items())))
>a3b1c10


s = 'a3c9b1c1'
t = list(s)
#print (t)
i = iter(t)
m = list(zip(i, i))
print ('tuple :', m)
sums = defaultdict(int)
for i, j in m:
    sums[i] += int(j)
print ('dict:', dict(sums))
print ('joined string:', ''.join('{}{}'.format(key, val) for key, val in sorted(sums.items())))
>tuple : [('a', '3'), ('c', '9'), ('b', '1'), ('c', '1')]
dict: {'a': 3, 'c': 10, 'b': 1}
joined string: a3b1c10
