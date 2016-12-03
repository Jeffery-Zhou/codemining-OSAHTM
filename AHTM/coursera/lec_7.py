import math
print math.e**1

W_xh = 0.5
W_hh = -1.0
W_hy = -0.7
h_bias = -1.0
y_bias = 0.0


def theta_k(k):
    return 1.0/(1+math.e**(-k))

print theta_k(0)

x0 = 9
x1 = 4
x2 = -2
# y1?


z0 = W_xh*x0 + h_bias
h0 = theta_k(z0)
z1 = W_xh*x1 + W_hh*h0 + h_bias
h1 = theta_k(z1)
y1 = W_hy*h1 + y_bias
print y1