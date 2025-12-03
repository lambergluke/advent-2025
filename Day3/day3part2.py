def find_joltage(str_n):
    chars = list(str_n)
    to_remove = len(chars) - 12
    i = 0
    while to_remove > 0 and i < len(chars):
        # We remove if: there's a larger digit within the next 'to_remove' positions
        if i < len(chars) - 1:  # Not at the end
            # Look ahead at most 'to_remove' positions (we need at least that many to potentially swap)
            lookahead = chars[i+1:min(i+1+to_remove, len(chars))]
            if lookahead and chars[i] < max(lookahead):
                chars.pop(i)
                to_remove -= 1 
                # This bug was a tough find: Don't increment i because we need to recheck this position with new char. Its like we move it to us
                # instead of us moving to it
            else:
                i += 1
        else:
            i += 1
    
    # Remove from end if needed
    while to_remove > 0:
        chars.pop()
        to_remove -= 1
    
    return ''.join(chars)
    

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
