expression = list(input())

alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
values = {char: 0 for char in alphabets}
max_result = -float('inf')

def calculate():
    res = values[expression[0]]
    
    for i in range(1, len(expression), 2):
        op = expression[i]
        next_val = values[expression[i+1]]
        
        if op == '+':
            res += next_val
        elif op == '-':
            res -= next_val
        elif op == '*':
            res *= next_val
    return res

def backtrack(idx):
    global max_result
    
    if idx == 6:
        current_res = calculate()
        if current_res > max_result:
            max_result = current_res
        return
    
    for val in range(1, 5):
        values[alphabets[idx]] = val
        backtrack(idx + 1)

backtrack(0)
print(max_result)