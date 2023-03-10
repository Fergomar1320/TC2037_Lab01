import graphviz
from collections import deque

dot = graphviz.Digraph(comment = 'Lab 01 Fernando Gomez Martinez')
dot
key_stack = deque()
alphabet_stack = deque()
node_stack = deque()
set = []
grid = []
   

def main ():
    reflexive = True
    symetric = True
    transitive = True
    print('Enter your string: ')
    set = input()

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

        #Creating a 2D table for the domain of the fucntion
        grid = [[0 for i in range (len(alphabet_stack))]for j in range(len(alphabet_stack))]


    #Creating the nodes 
    for index in alphabet_stack:
        dot.node(index)

    #Adding the corresponding edges
    for i in range (0,len(node_stack),2):
        x = int(node_stack[i])
        y = int(node_stack[i+1])
        dot.edge(node_stack[i], node_stack[i+1])
        grid[x][y] = 1
    
    print(grid)

    #Check if the set is reflexive
    for i in range(0,len(alphabet_stack)):
        if grid[i][i] != 1:
            reflexive = False
            break

    #Check if the set is symetric
    for i in range(0,len(alphabet_stack)):
        for j in range(0,len(alphabet_stack)):
            print(i)
            print(j)
            print(grid[i][j])
            print(grid[j][i])
            print('___')
            if grid[i][j] == 1 and grid[j][i] != 1 or grid[i][j] != 1 and grid[j][i] == 1:
                symetric = False
                break

    print(dot.source)
    print(reflexive)
    print(symetric)
    #dot.render("Lab01.pdf", view=True)

main()

#TEST CASE { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }