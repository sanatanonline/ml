import util

w = [0.2, -0.1, 0.1]
p = [0.4, 0.2, 0.2]
b = 0.1
net = util.activate(w, p, b)
print("The net value is:", net)
a, d_a = util.logsigmoid(net)
print("The output value is:")
print(a)
