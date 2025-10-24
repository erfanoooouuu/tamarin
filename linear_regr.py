dataset = [(1,3), (3,1)]
w = 0
b = 0

dw = lambda x, y, w, b: (-2*x)*(y-(w*x)-b)
db = lambda x, y, w, b: -2*(y-(w*x)-b)
w_kham = 0
b_kham = 0

alpha = 0.01

new_w = lambda w, alpha, dw: w-(alpha*dw)
new_b = lambda b, alpha, db: b-(alpha*db)

for i in range(5):
    dfw = 0
    dfb = 0
    for x,y in dataset:
        dfw += dw(x, y, w, b)
        dfb += db(x, y, w, b)

    w = new_w(w, alpha, dfw)
    b = new_b(b, alpha, dfb)

    print(f'new_w = {w}')
    print(f'new_b = {b}')
    print('----------------------------')

