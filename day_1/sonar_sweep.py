def read_depth_logs(path):
    """Read the depth log file of the AOC submarine"""
    with open(path) as log_file:
        return [int(log) for log in log_file.readlines()]


def get_gradient(l: list[int]):
    """Calculate gradient for AOC submarine's sonar"""
    return sum([1 for index, elem in enumerate(l) if (index < (len(l)-1) and elem < l[index+1])])


def get_denoised_log(l: list[int], window_size):
    """Calculate denoised gradient for AOC submarine's sonar"""
    offset = window_size - 1    # offset for iteration
    return [sum(l[i:i+window_size]) for i in range(len(l)-offset)]


if __name__ == '__main__':
    logs = read_depth_logs("input.txt")
    print("Gradient: " + str(get_gradient(logs)))
    print("Denoised Gradient: " + str(get_gradient(get_denoised_log(logs, 3))))
