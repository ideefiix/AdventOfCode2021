from statistics import median

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

def get_closing_score(c):
    if c == ')':
        return 1
    elif c == ']':
        return 2
    elif c == '}':
        return 3
    elif c == '>':
        return 4

def incomplete_line_score(line):
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
            chunk_stack.pop()
            if len(chunk_stack) > 0:
                expected_closing = get_expected_closing(chunk_stack[-1])
            else:
                expected_closing = ''
    #Give score
        score = 0
    for i in range(len(chunk_stack)):
        opening = chunk_stack.pop()
        closing = get_expected_closing(opening)
        closing_score = get_closing_score(closing)
        # dis work? O.o
        score *= 5
        score += closing_score

    return score


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

#TASK 2: Remove corrupt lines
    print("Task: 2")
    incomplete_lines = [line for line in inputt if corrupted_score(line) == 0]
    scores = []
    for line in incomplete_lines:
        scores.append(incomplete_line_score(line))
        
    print(median(scores))
