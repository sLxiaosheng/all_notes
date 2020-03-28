

class tree_two:
    def __init__(self, val, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right
    

A, B, C, D, E = [tree_two(x) for x in '12345']
A.left = 2
A.right = 3
B.left = 4
B.right = 5
C.right = None
C.left = None
D.right = None
D.left = None
add = {1:A,2:B,3:C,4:D,5:E}

#创建一个列表存储已经查看过的节点

covered = []
i = 0
def find_longest(node):
if add[node].left:
    covered.append(add[node.left])
    i += 1
    node = node.left
    find_longest(add[node])
if add[node].right:
    covered.append(add[node.right])
    find_longest.i += 1
    node = node.right
    find_longest(add[node])   
return i


def scan_code(code):
    long = []
    while code.right | code.left:
        if code not in covered:
            long = long.append(find_longest(code))
        code = add[code.right | code.left]
    long = long.sort()
    return long[0]

print(scan_code(A))
