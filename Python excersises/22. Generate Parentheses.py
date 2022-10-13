# n is number of parenthesis
# if n= 3 I need 3 open and 3 close
import random
def generateParenthesis(n: int):
    cont = '(' * n + ')' * n
    cont = [i for i in cont]
    open_brackets =[]
    res = ''
    for i in cont:
        if i == '(':
            open_brackets.append(i)
            res += i
        else:
            if open_brackets:
                res+= i


    random.shuffle(cont)


    # if cont not in options:
    #     options.add(cont)

    return cont

 #["((()))","(()())","(())()","()(())","()()()"]
n = 5
print(generateParenthesis(n))