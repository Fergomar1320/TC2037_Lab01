import graphviz
from collections import deque

dot = graphviz.Digraph(comment = 'Lab 01 Fernando Gomez Martinez')
dot
key_stack = deque()
alphabet_stack = deque()
node_stack = deque()
set = []
    

def main ():
    print('Enter your string: ')
    set = input()
    print('You entered: ' + set)

    #Reading, storing and validating the input syntax
    if set[0] != '{':
        print('Syntax Error')
    else:
        key_stack.append(set[0])
        for element in set:
            if element == '(':
                if element not in key_stack:
                    key_stack.append(element)
                else:
                    print('ERROR: Misplaced ' + element)

            elif element == ')':
                last_key = key_stack.pop()
                if last_key != '(':
                    print('ERROR: Misplaced ' + element)
                    break

            elif element == '}':
                last_key = key_stack.pop()
                if last_key != '{':
                    print('ERROR: Misplaced ' + element)
                    break
                
            elif element != ',' and element != ' ' and element != '{':
                node_stack.append(element)
                if element not in alphabet_stack:
                    alphabet_stack.append(element)

    print(node_stack)
    print(alphabet_stack)

    #Creating the nodes 
    for index in alphabet_stack:
        dot.node(index)

    print(dot.source)

main()

#TEST CASE { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }