rows = 3
cols = 12

space = 1
left = 150

for i in range(12):
    top = 240
    left += 102
    for j in range(3):
        print('#spc_' + str(space) + ' {')
        print('    position: absolute;')
        print('    top:' + str(top) + 'px;')
        print('    left:' + str(left) + 'px;')
        print('}') 
        space = space + 1
        top = top - 70

