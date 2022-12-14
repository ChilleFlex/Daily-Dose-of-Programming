from collections import Counter

st = 'rafsan_weds_takia'
res = Counter(st)

m = max(res, key=res.get)
print(m)