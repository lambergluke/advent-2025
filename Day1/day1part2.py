dial = 50
combo = 0
size = 100


def goRight(number):
    global dial 
    global combo
    old_dial = dial
    
    dial += number
    if (dial > 99):
        dial = dial % size
    
    if old_dial == 0:
        combo += number // size
        return dial
    
    combo += (old_dial + number) // size
    
    return dial

def goLeft(number):
    global dial
    global combo
    old_dial = dial
    
    dial -= number
    if(dial < 0):
        dial = dial % size
    
    if old_dial == 0:
        combo += number // size
        return dial
    
    if old_dial <= number:
        combo += ((number - old_dial) // size) + 1
    
    return dial

file_path = "input.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            direction = line[:1]
            number = int(line[1:].strip())

            if direction == "L":
                goLeft(number)
            elif direction == 'R':
                goRight(number)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(combo)