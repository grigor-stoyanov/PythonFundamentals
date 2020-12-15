# n = 2*(i+1)**2 + ....
def el_distr(layer, electrons):
    shell = 2 * (layer ** 2)
    electrons -= shell
    if electrons < 0:
        shell += electrons
    return shell


n = int(input())
atom = []
for i in range(0, n):
    atom.append(el_distr(i+1, n))
    n -= atom[i]
    if n <= 0:
        break
print(atom)