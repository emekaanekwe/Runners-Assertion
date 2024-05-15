# get values of all vars
v_1 = dir()
v_d_1 = {}
count = 0
for v in v_1:
    if not v.startswith('__'):
        value = eval(v)
        v_d_1[v] = value
        count += 1
#print(v_d_1)
