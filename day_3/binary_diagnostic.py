def analyze_from_matrix(path:str):
    with open(path) as file:
        # read matrix and rotate by 90 degree
        error_matrix = zip(*reversed([line.strip() for line in file.readlines()]))

    gamma = ""
    epsilon = ""

    for bit in error_matrix:
        # determine common bit
        if bit.count('1') > len(bit)/2:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    # multiply epsilon and gamma (as decimal) to gain data about power consumption
    power_consumption = int(gamma, 2) * int(epsilon, 2)

    # format result
    param_results = f"Gamma: {gamma} | Epsilon: {epsilon}"
    divider = len(param_results)*'-'
    consumption_result = f"Power Consumption: {power_consumption}"
    # print result
    print(param_results + "\n" + divider + "\n" + (abs(len(divider)-len(consumption_result)))*" " + consumption_result)


if __name__ == '__main__':
    analyze_from_matrix("input.txt")






