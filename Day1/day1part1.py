dial = 50
combo = 0

#if the number is > 198, loop around again 

def goRight(number):
    global dial 
    dial += number
    
    if (dial > 99):
        dial = abs(100 - dial)
    return dial

def goLeft(number):
    global dial
    dial -= number
    if(dial < 0):
        dial = abs(abs(dial) - 100) 
    return dial

file_path = "input.txt"

try:
    with open(file_path, 'r') as file:
        for line in file:
            direction = line[:1]
            number = int(line[1:])
            if(number > 99): number %= 100
            if (line[:1] == "L"):
                goLeft(number)
                if(dial == 0): combo += 1
            if (line[:1] == 'R'):
                goRight(number)
                if(dial == 0): combo += 1

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(combo)