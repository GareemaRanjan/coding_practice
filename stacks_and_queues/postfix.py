"""
Problem Statement
The usual convention followed in mathematics is the infix expression. Operators like + and * appear between the two
numbers involved in the calculation:

6 + 3 * 8 - 4

Another convention is the postfix expression where the operators appear after the two numbers involved in the
expression. In postfix, the expression written above will be presented as:

6 3 8 * + 4 -

The two digits preceding an operator will be used with that operator

1. From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
2. Reading the operators from left to right, the first one is *. The expression now becomes 3 * 8
3. The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
4. The value of this expression is followed by 4, which is right before -. Hence we have 6 + 8 * 3 - 4.

Implement a function called evaluatePostFix() that will compute a postfix expression given to it as a string.

Input
A string containing a postfix mathematic expression. Each digit is considered to be a separate number, i.e., there are
no double digit numbers.

Output
A result of the given postfix expression.

Sample Input#
exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4
Sample Output
3

------------------------------------------------------------------------------------------------------------------------

Solution: Numbers as Stack Elements

We check each character of the string from left to right. If we find a digit, it is pushed into the stack.

If we find an operand, we pop two elements from the stack (there have to be at least two present or else this postfix
expression is invalid) and solve the expression. The resulting value is pushed back into the stack.

The process continues until we reach the end of the string.
------------------------------------------------------------------------------------------------------------------------

####
------------------------------------------------------------------------------------------------------------------------

Time complexity:

Since we traverse the string of n characters once, the time complexity for this algorithm is O(n).
"""
from Stack import MyStack


def eval_postfix(expression):
    mystack = MyStack()

    for char in expression:
        if char.isdigit():
            mystack.push(char)
        else:
            right = mystack.pop()
            left = mystack.pop()
            result = str(eval(left + char + right))
            mystack.push(result)

    return int(float(mystack.pop()))


if __name__ == "__main__":
    print("Result of expression (921*-8-4+) : " + str(eval_postfix("921*-8-4+")))
