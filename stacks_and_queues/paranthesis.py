from Stack import MyStack


def balance(str):
    stack = MyStack()
    for c in str:
        if c == "{" or c == "(" or c == "[":
            stack.push(c)
        elif c == "}" and stack.peek() == "{":
            stack.pop()
        elif c == "]" and stack.peek() == "[":
            stack.pop()
        elif c == ")" and stack.peek() == "(":
            stack.pop()
    print(stack.stack_list)
    if stack.is_empty():
        return True
    return False


if __name__ == "__main__":
    exp = "{[()}"
    print(balance(exp))
