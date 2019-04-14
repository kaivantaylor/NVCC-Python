
string = '(()' 

def recur(string):

    length = len(string)
    
    #Base Case
    if length == 1:
        return False
    
    elif length == 0:
        return True
    
    else:
           
        stack = []
        case_1 = ['(',')']

        for text in string:
            stack.append(text)
        
        
        if stack[-2:] == ['(', ')']:
            stack.pop()
            stack.pop()
            new_str = ''.join(stack)
            return recur(new_str)
        
