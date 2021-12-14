
def get_expected_closing(c):
    if c == '(':
        return ')'

    elif c == '[':
        return ']'

    elif c == '{':
        return '}'

    elif c == '<':
        return '>'
    else:
        print("INVALID VALUE IN CHUNK STACK!")

def get_character_score(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137

def corrupted_score(line):
    expected_closing = ''
    chunk_stack = []
    for c in line:
        if c == '(':
            chunk_stack.append(c)
            expected_closing = ')'
        elif c == '[':
            chunk_stack.append(c)
            expected_closing = ']'
        elif c == '{':
            chunk_stack.append(c)
            expected_closing = '}'
        elif c == '<':
            chunk_stack.append(c)
            expected_closing = '>'
        else: #Closing Chunk
            if c != expected_closing:
                return get_character_score(c)
            else:
                chunk_stack.pop()
                if len(chunk_stack) > 0:
                    expected_closing = get_expected_closing(chunk_stack[-1])
                else:
                    expected_closing = ''
    return 0



if __name__ == "__main__":
    inputt = []
    with open('input10.txt', 'r') as file:
        for line in file.readlines():
            inputt.append(line.strip())

    syntax_error_score = 0
    for line in inputt:
        corrupt_score = corrupted_score(line)
        syntax_error_score += corrupt_score
    
    print("Task 1:")
    print(syntax_error_score)
