# iterate through string, find the biggest number and save its position
# if the biggest number is in the last position, find second biggest number, combo = second biggest, first biggest
# if the biggest number is not in the last position only iterate right and find the biggest number to the right of the biggest number
# save the biggest index, need to compare. split the list into everything after the biggest number, find biggest number again




def find_joltage(str_n):
    max_battery = ""
    chars = list(str_n)
    biggest = max(chars)
    biggest_index = [i for i, value in enumerate(chars) if value == biggest]
    # quick solve for where the biggest number is repeated, easily makes it big+big
    if(len(biggest_index) > 1): 
        max_battery = biggest + biggest
        return max_battery
    # solving for where the biggest number is last, we don't care where it is just need the second biggest number
    for i in biggest_index:
        if(i == len(chars)-1):
            chars.sort()
            second_biggest = chars[-2]
            max_battery = second_biggest + biggest
            return max_battery
    # solving for normal case where biggest number is anywhere else in the string. split after and just run it back
    new_list = chars[biggest_index[0] + 1:]
    second_biggest = max(new_list)
    max_battery = biggest + second_biggest
    return max_battery


def read_file(file_path):
    total = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                total += int(find_joltage(line.strip()))
        return total
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "input.txt"

if __name__ == "__main__":
    total = read_file(file_path)
    print(total)