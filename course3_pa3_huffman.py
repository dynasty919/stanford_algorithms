# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 0:30
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa3_huffman.py
# @Software: PyCharm

class binarytree(object):
    '''定义一个二叉树，用来作为霍夫曼树'''
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = None
    def insertleft(self, node):
        self.left = node
    def insertright(self, node):
        self.right = node
    def getvalue(self):
        return self.value
    def setvalue(self, value):
        self.value = value
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def __str__(self):
        return str(self.value)

def heapmin_insert(heapmin, xobj):
    '''对一个min堆做插入，堆里储存的是二叉树结点。这东西是用之前MedianMaintenance里写好的模块改的。
    幸好当时手动实现了这玩意，要不然又不知道要写多久'''
    def pop_up(heapmin, n):
        if n == 1:
            return heapmin
        else:
            if n % 2:
                if heapmin[n - 1].value > heapmin[n // 2 - 1].value:
                    return heapmin
                else:
                    heapmin[n - 1], heapmin[n // 2 - 1] = heapmin[n // 2 - 1], heapmin[n - 1]
                    return pop_up(heapmin, n // 2)
            else:
                if heapmin[n - 1].value > heapmin[(n - 1) // 2].value:
                    return heapmin
                else:
                    heapmin[n - 1], heapmin[(n - 1) // 2] = heapmin[(n - 1) // 2], heapmin[n - 1]
                    return pop_up(heapmin, (n + 1) // 2)
    if not heapmin:
        heapmin.append(xobj)
        return heapmin
    else:
        heapmin.append(xobj)
        heapmin = pop_up(heapmin, len(heapmin))
        return heapmin

def heapmin_extract(heapmin):
    '''对min堆释放拥有最小值的二叉树结点，同上'''
    def pop_down(heapmin, n):
        if 2*n > len(heapmin):
            return heapmin
        elif 2*n == len(heapmin):
            if heapmin[n-1].value > heapmin[2*n-1].value:
                heapmin[n-1], heapmin[2*n-1] = heapmin[2*n-1], heapmin[n-1]
                return pop_down(heapmin, 2*n)
            else:
                return heapmin
        else:
            if heapmin[n-1].value < heapmin[2*n-1].value and heapmin[n-1].value < heapmin[2*n].value:
                return heapmin
            elif heapmin[n-1].value > heapmin[2*n-1].value and heapmin[n-1].value < heapmin[2*n].value:
                heapmin[n - 1], heapmin[2 * n - 1] = heapmin[2 * n - 1], heapmin[n - 1]
                return pop_down(heapmin, 2 * n)
            elif heapmin[n-1].value > heapmin[2*n].value and heapmin[n-1].value < heapmin[2*n-1].value:
                heapmin[n - 1], heapmin[2 * n] = heapmin[2 * n], heapmin[n - 1]
                return pop_down(heapmin, 2*n+1)
            else:
                if heapmin[2*n-1].value < heapmin[2*n].value:
                    heapmin[n - 1], heapmin[2 * n - 1] = heapmin[2 * n - 1], heapmin[n - 1]
                    return pop_down(heapmin, 2 * n)
                else:
                    heapmin[n - 1], heapmin[2 * n] = heapmin[2 * n], heapmin[n - 1]
                    return pop_down(heapmin, 2 * n + 1)
    result = heapmin[0]
    heapmin[0] = heapmin[-1]
    heapmin.pop()
    heapmin = pop_down(heapmin, 1)
    return result

def readfile():
    '''读文件，得到一个排好的int list（同时也是一个heap）'''
    with open('huffman.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(int(c.strip()))
        d = sorted(b)
        return d

def initheap():
    '''把读出的int list 变成二叉树结点的list'''
    intlist = readfile()
    objlist = []
    for someint in intlist:
        objlist.append(binarytree(someint))
    return objlist

def huffman():
    '''主程序，基本就是一直释放最小的两个结点，把他们合并再插入回去，最后只剩一个结点了，就是最后完整霍夫曼树的根节点'''
    heap = initheap()
    while len(heap) > 1:
        z = binarytree()
        x = heapmin_extract(heap)
        y = heapmin_extract(heap)
        z.left = x
        z.right = y
        z.value = x.value + y.value
        heapmin_insert(heap, z)
    return heap

def leaf_height(tree,alist=None):
    '''用来求霍夫曼树的每个叶子的高度'''
    if alist is None:
        alist = []
        tree.height = 0
    if not (tree.left and tree.right):
        alist.append(tree.height)
    else:
        tree.left.height = tree.height + 1
        tree.right.height = tree.height + 1
        leaf_height(tree.left, alist)
        leaf_height(tree.right, alist)
    return alist

def main():
    '''得到霍夫曼树，求出各叶子高度'''
    tree = huffman()[0]
    heightlist = leaf_height(tree)
    print(min(heightlist), max(heightlist))

main()