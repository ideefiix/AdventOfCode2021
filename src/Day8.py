def count_1_4_7_and_8(signal_list):
    count = 0
    for signal in signal_list:
        leng = len(signal)
        if leng == 2 or leng == 3 or leng == 4 or leng == 7:
            count += 1
    return count

def decode_2_3_or_5(encoded_1_4_7, signal):
    # 2 hints == Signal is decoded
    signal_3_hint = 0
    signal_5_hint = 0

    for letter in signal:
        if letter in encoded_1_4_7[0]:
            signal_3_hint += 1
        elif letter in encoded_1_4_7[1]:
            signal_5_hint += 1

    if signal_3_hint == 2:
        return '3'
    elif signal_5_hint == 2:
        return '5'
    else:
        return '2'

def decode_0_6_or_9(encoded_1_4_7, signal):
    # hints
    signal_0_hint = 0
    signal_6_hint = 0
    signal_9_hint = 0

    for letter in signal:
        if letter in encoded_1_4_7[0]:
            signal_0_hint += 1
            signal_9_hint += 1
        elif letter in encoded_1_4_7[1]:
            signal_6_hint += 1
            signal_9_hint += 1

    if signal_0_hint == 2 and signal_6_hint == 2:
        return '9'
    elif signal_0_hint == 2:
        return '0'
    elif signal_6_hint == 2:
        return '6'
    else:
        print("Signal could not be decoded in decode_0_6_or_9")

def decode_output(input_signals, output_signals):
    encoded_1_4_7 = ['', '','']
    decoded_output = []

    # Find the easy 1,4,7 first
    for signal in input_signals:
        if len(signal) == 2:
            encoded_1_4_7[0] = signal
        elif len(signal) == 4:
            encoded_1_4_7[1] = signal
        elif len(signal) == 3:
            encoded_1_4_7[2] = signal
        

    # Remove common signals
    encoded_1_4_7[1].replace(encoded_1_4_7[0][0], '')
    encoded_1_4_7[1].replace(encoded_1_4_7[0][1], '')

    encoded_1_4_7[2].replace(encoded_1_4_7[0][0], '')
    encoded_1_4_7[2].replace(encoded_1_4_7[0][1], '')


    # Use this information to decode signals
    for signal in output_signals:
        lengg = len(signal)
        if lengg == 2:
            decoded_output.append('1')
            continue
        elif lengg == 3:
            decoded_output.append('7')
            continue
        elif lengg == 4:
            decoded_output.append('4')
            continue 
        elif lengg == 5:
            decoded_output.append(decode_2_3_or_5(encoded_1_4_7, signal))
            continue
        elif lengg == 6:
            decoded_output.append(decode_0_6_or_9(encoded_1_4_7, signal))
            continue
        elif lengg == 7:
            decoded_output.append('8')
            continue
    
    return int(''.join(decoded_output))

if __name__ == '__main__':
    # List with a tuple of 2 lists, INPUT and OUTPUT
    signals = []
    decoded_output = []
    with open('input8.txt', 'r') as file:
        for line in file.readlines():
            tmp = line.strip().split(' | ')
            inpul_val = tmp[0].split(' ')
            output_val = tmp[1].split(' ')
            signals.append((inpul_val, output_val))

    task1_num = sum(count_1_4_7_and_8(y) for x, y in signals)


    print("TASK 1:")
    print(task1_num)
    print("------------")
    print("TASK 2:")

    for inputt, outputt in signals:
        decoded_output.append(decode_output(inputt, outputt))

    print(sum(decoded_output))
        