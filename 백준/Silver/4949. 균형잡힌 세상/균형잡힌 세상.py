import sys
while 1:
    sentence = sys.stdin.readline().rstrip()
    if len(sentence) == 1 and sentence[0] =='.':
        print
        break
    dict_bracket = {']':'[', ')':'('}
    stack_bracket = []
    for letter in sentence:
        if letter=='[' or letter=='(':
            stack_bracket.append(letter)
        elif letter==']' or letter==')':
            if len(stack_bracket)==0:
                print('no')
                break
            elif dict_bracket[letter] == stack_bracket[-1]:
                stack_bracket.pop()
            else:
                print('no')
                break
        elif letter=='.':
            # . = 문장 마지막
            if len(stack_bracket) == 0:
                print('yes')
            else:
                print('no')
            break