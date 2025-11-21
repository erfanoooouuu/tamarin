
import math
# x = float(input("adad1 "))
# y = float(input("adad2 "))
# z = (x * (-1.30)) + (y * 2.28) - 0.58
# print(f'z= {z} ===================')
# result = math.log(1+math.e**z)
# print(f'ln = {result}  ===================')


w1,w2,w3,w4 = -34.4, -2.52, -1.30, 2.28
b1,b2,b3 = 2.14, 1.29, -0.58

x_LowDose = [0, 0.01, 0.1]
x_MidDose = [0.4, 0.5, 0.6]
x_HighDose = [0.85, 0.9, 1]

x = [0, 0.01, 0.1, 0.4, 0.5, 0.6, 0.85, 0.9, 1]
y = [0,0,0,1,1,1,0,0,0]
z = lambda w,x,b:(w*x )+ b
soft_plus_formula = lambda z : math.log(1+math.e**z)

#a layer1
a0_l1 = []
a1_l1 = []
for i in x:
    out_z_a0 = z(w1, i, b1)
    out_z_a1 = z(w2, i, b2)
    a0_l1.append(soft_plus_formula(out_z_a0))
    a1_l1.append(soft_plus_formula(out_z_a1))

def a_l2(a0_l1, a1_l1,w3,w4,b3):
    a_l2_formula = lambda a10,a11,w3,w4,b3: (a10*w3) + (a11*w4) + b3 
    a20 = []
    z_ha = []
    for j in range(0,len(a0_l1)):
        z = a_l2_formula(a0_l1[j], a1_l1[j], w3,w4, b3)
        z_ha.append(z)
        a20.append(soft_plus_formula(z))
    return {'a20':a20,'z':z_ha}
# ##############################################################

def formul_gd_W(w,y,a20,z,x):
    sigmaha = -2 *(y-a20)
    df_dw = sigmaha * ((math.e**z) * (1 / (1+math.e**z)) )* x

    new_W = w - 0.1 * df_dw

    return new_W


def formul_gd_B(b,y,a20,z):
    sigmaha = -2 *(y-a20)
    df_db = sigmaha * ((math.e**z) * (1 / (1+math.e**z)) ) * 1

    new_B = b - 0.1 * df_db

    return new_B



out_a_l2 = a_l2(a0_l1, a1_l1,w3,w4,b3)

for i in range(1000):
    new_w3 = formul_gd_W(w3,y[2],out_a_l2['a20'][2], out_a_l2['z'][2],x[2])
    new_w4 = formul_gd_W(w4,y[2],out_a_l2['a20'][2], out_a_l2['z'][2],x[2])
    new_b3 = formul_gd_B(b3,y[2],out_a_l2['a20'][2], out_a_l2['z'][2],)
    out_a_l2 = a_l2(a0_l1, a1_l1,new_w3,new_w4,new_b3)

    w3 = new_w3
    w4 = new_w4
    b3 = new_b3
    print(out_a_l2['a20'])
    print('-=--------------------------------------')


#CHATGPT
import matplotlib.pyplot as plt

# دیتاهای شما

# ایجاد نمودار
plt.figure(figsize=(10, 6))
plt.scatter(out_a_l2['a20'], y, color='red', s=100, alpha=0.7, label='دیتاهای من')
# [1,2,3,4,5,6,7,8,9]
# تنظیمات نمودار
plt.title('نمایش دیتاهای X و Y', fontsize=14)
plt.xlabel('مقادیر X', fontsize=12)
plt.ylabel('مقادیر Y', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# نمایش نمودار
plt.tight_layout()
plt.show()