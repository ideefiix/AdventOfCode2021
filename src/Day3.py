#TASK 1
def gamma_epsilon_rate(listt):
    gammaRate = ""
    epsilonRate = ""
    bit_0_count = 0
    bit_1_count = 0
    for bit_index in range(len(listt[0])):
        for line in listt:
            if line[bit_index] == "0": bit_0_count += 1
            elif line[bit_index] == "1": bit_1_count += 1
        
        if bit_0_count > bit_1_count: 
            gammaRate = gammaRate + "0" 
            epsilonRate =  epsilonRate + "1" 
        elif bit_0_count < bit_1_count: 
            gammaRate =  gammaRate + "1"
            epsilonRate =  epsilonRate + "0" 
    
        bit_0_count = 0
        bit_1_count = 0

    gammaRate = int(gammaRate, 2)
    epsilonRate = int(epsilonRate, 2)
    return gammaRate, epsilonRate

#TASK 2

def common_bit(listt, index):
    bit_0_count = 0
    bit_1_count = 0
    for num in listt:
        if num[index] == "0": bit_0_count += 1
        elif num[index] == "1": bit_1_count += 1

    if bit_0_count == bit_1_count: return "1"

    common_bit = max(bit_0_count, bit_1_count)
    if bit_0_count == common_bit: return "0"
    elif bit_1_count == common_bit: return "1"


def life_support_rating(listt):
    list_oxygen = listt[:]
    list_co2 = listt[:]

    for bit_index in range(len(listt[0])):
        #DETERMINE COMMON BIT
        oxygen_common_bit = common_bit(list_oxygen, bit_index)
        co2_common_bit = common_bit(list_co2, bit_index)

        #REMOVE ELEMENTS
        if len(list_oxygen) > 1:
            list_oxygen = [x for x in list_oxygen if x[bit_index] == oxygen_common_bit]
        if len(list_co2) > 1:
            list_co2 = [x for x in list_co2 if x[bit_index] != co2_common_bit]

        if len(list_oxygen) == 1 and len(list_co2) == 1:
            break

    oxygen_rate = int(list_oxygen[0], 2)
    co2_rate = int(list_co2[0], 2)
    life_support_rating = oxygen_rate * co2_rate

    return life_support_rating






if __name__ == "__main__":
    input_list = []

    with open("input3.txt", "r") as file:
        for line in file.readlines():
            input_list.append(line.replace('\n', ''))

    gamma, epsilon = gamma_epsilon_rate(input_list)
    print("Answer task 1: " + str(gamma * epsilon))
    print("Answer task 2: " + str(life_support_rating(input_list)))