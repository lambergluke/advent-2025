def check_id(start, finish):
    total = 0
    for i in range(start, finish + 1):
        string_i = str(i)
        if len(string_i) % 2 != 0:
            continue
        mid = len(string_i) // 2
        first, second = string_i[:mid], string_i[mid:]
        if first == second:
            total += i
    return total


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            number_list = []
            content = file.read()
            for line in content.split('\n'):
                number_list += line.split(',')
        return number_list
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def process_ranges(number_list):
    total = 0
    for item in number_list:
        ranges = item.split('-')
        total += check_id(int(ranges[0]), int(ranges[1]))
    return total


if __name__ == "__main__":
    number_list = read_file("input.txt")
    total = process_ranges(number_list)
    print(total)
