import argparse
p = argparse.ArgumentParser()
p.add_argument('inp')
p.add_argument('--upper', action="store_true")
p.add_argument('--lines', type=int, default=0)
p.add_argument('outp')
ar = p.parse_args()
stroka = open(ar.inp).read().split('\n')
if ar.upper:
    stroka = list(map(lambda x: x.upper(), stroka))
newstroka = ''
for i in range(ar.lines):
    newstroka.append(stroka[i])
open(ar.outp, mode='w').write(newstroka.join('\n'))