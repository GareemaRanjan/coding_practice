from Stack import MyStack

def find_next(l):
    res = [-1]*len(l)
    mystack = MyStack()
    for i in range(0,len(l)):
        if mystack.is_empty():
            mystack.push(l[i])
        elif mystack.peek()<=l[i]:
            res[i] = l[i]
            mystack.push(l[i])
        else:
            res[i] = res[i-1]
            mystack.push(l[i])

    print(res)

if __name__ == "__main__":
    find_next([4,6,3,2,8,1])