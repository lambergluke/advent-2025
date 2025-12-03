###
# we have a few cases: 
# Case 1:number is even and split down middle is same ex: 123123
# Case 2: number is even and split down middle is not same, but has repeating ex: 565656
# Case 3: number is odd and is completely repeating ex: 111,222,333
# Case 4: number is odd and has tuplets? would have to be a multiple of 3, then check for 
###
import re

def check_id(start, finish):
    total = 0
    for i in range(start, finish + 1):
        string_i = str(i)
        if re.search(r'^(\d+)\1+$', string_i):
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