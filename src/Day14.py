from collections import Counter
def step(polymer, rules):
    new_polymer = []

    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        rule_found = False
        # Search pair in rule
        for rule in rules:
            if pair == rule[0]:
                new_polymer.append(pair[0])
                new_polymer.append(rule[1])
                rule_found = True
                break
        # Else add only one
        if not rule_found:
            new_polymer.append(pair[0])

    #Add last letter 
    new_polymer.append(polymer[-1])
    strr = ''.join(new_polymer)
    return strr

if __name__ == '__main__':
    lines = []
    #Read data
    with open('input14.txt', 'r') as file:
        lines = file.read().splitlines()

    polymer = lines[0]
    rules = [] 
    for line in lines[2:]:
        line = line.split(' ')
        rule = (line[0], line[2])
        rules.append(rule)
    # Step
    for i in range(10):
        print("Step " + str(i))
        polymer = step(polymer, rules)
    # Get most frequent letter with the help from collections lib
    c = Counter(polymer)
    frequencies = [b for a, b in c.most_common()]
    common = max(frequencies)
    uncommon = min(frequencies)

    #Task 1
    print(common - uncommon)
 

    
    
