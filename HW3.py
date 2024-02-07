# HW3

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        if self.top == None:                # Checks if the head is empyty
            return True
        else:
            return False

    def __len__(self): 
        current = self.top                  # Sets current equal to the head
        count = 0
        while current is not None:
            count += 1                      # Iterates through the stack and adds one for every character
            current = current.next
        return count

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node                 # Sets the new node put into the stack as the head of the stack

     
    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            if len(self) == 1: 
                remove_node = self.top.value
                self.top = self.top.next             
                self.head = None
                self.tail = None

            else:
                remove_node = self.top.value        # Makes the node that wants to be removed as the head's value
                self.top = self.top.next            # Sets the head equal to the next node
            return remove_node


    def peek(self):
        if self.isEmpty() == True:
            return None
        else:
            top_node = self.top.value               # Gets the value of the head of the stack
            return top_node



#=============================================== Part II ==============================================

class Calculator:
    '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        try:
            x = float(txt)
            return True
        except:
            return False




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3  ) ^ 2 + (1 +4 ))    ))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        priority = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
        postfix_lst = []
        clean_lst = []
        digit = ''
        for i in range(len(txt)):
            if txt[i] == '-' and txt[i-1] in priority:      # Checks for a negative operator followed by a number
                digit += txt[i]
            if txt[i] == '-' and txt[i-1] == ' ':
                clean_lst += [digit.strip()]
                clean_lst += [txt[i]]
                digit = ''
            elif txt[i] in priority:
                clean_lst += [digit.strip()]
                clean_lst += [txt[i]]                           # Adds what is in the digit to clean list and removes the spaces                                # Adds the operand to the list
                digit = ''                                            # resets the string to 0
            else:
                digit += txt[i]                                # If its not an operator or a negative it will just add it to digit and remove spaces
        clean_lst += [digit.strip()]

        for i in clean_lst:
            if i != '':
                if self._isNumber(i) == True:
                    postfix_lst.append(str(float(i)))               # If its a number covert it to a float and then a string and append it to my list
                elif postfixStack.isEmpty() == True:
                    postfixStack.push(i)                            # If the stack is empty just push it in
                elif i == '(':
                    postfixStack.push(i)
                elif i == ')':
                    while postfixStack.peek() != '(':
                        postfix_lst.append(postfixStack.pop())          # Pop all the items and append them to my list
                    postfixStack.pop()                                  # Then remove the '(' from the stack
                elif priority[i] > priority[postfixStack.peek()]:       # If its greater just push to the stack
                    postfixStack.push(i)
                elif priority[i] <= priority[postfixStack.peek()]:
                    while postfixStack.isEmpty() == False and priority[i] <= priority[postfixStack.peek()]:     # Continues to run until the stack is empty or priority of i is higher
                        postfix_lst.append(postfixStack.pop())                
                    postfixStack.push(i)
        if postfixStack.isEmpty() == False:                 # After all the examples if the stack still has operators pop them
            while postfixStack.isEmpty() != True:
                postfix_lst.append(postfixStack.pop())
        return ' '.join(postfix_lst)




    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        postfix_lst = []
        postfix_lst.append(self._getPostfix(self.getExpr))                          # Not sure how to make the list iterate over the whole number including decimal within the string
        for i in postfix_lst:
            if self._isNumber(i):
                calcStack.push(float(i))
            else:
                second_num = calcStack.pop()                                    # If you come across an operator pop twice
                first_num = calcStack.pop()
                if i == '+':                                                    # Do the corresponding operations depending on the operator in the list
                    answer = second_num + first_num
                elif i == '-':
                    answer = second_num - first_num
                elif i == '*':
                    answer = second_num * first_num
                elif i == '/' and first_num != 0:
                    answer = second_num / first_num
                else:
                    return None
        return answer                                                           # Return the calculation





#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states = {'x1': 23.0, 'x2': 28.0}
        >>> C._replaceVariables('1')
        '1'
        >>> C._replaceVariables('105 + x')
        >>> C._replaceVariables('7 * ( x1 - 1 )')
        '7 * ( 23.0 - 1 )'
        >>> C._replaceVariables('x2 - x1')
        '28.0 - 23.0'
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        if word[0].isalpha() and word.isalnum():
            return True
        else:
            return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        new_lst = expr.split()                              
        for item in range(len(new_lst)):                                # iterates through and splits expression
            if self._isVariable(new_lst[item]):                         # Checks if element is a variable
                if new_lst[item] in self.states:                        # Checks if the variable is in self.states
                    new_lst[item] = str(self.states[new_lst[item]])
                else:
                    return None
        return ' '.join(new_lst)

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        pass

if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(AdvancedCalculator, globals(), name='LAB4',verbose=True)
