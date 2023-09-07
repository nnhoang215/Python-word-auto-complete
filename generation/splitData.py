import random

def select_random_entries(input_file, output_file, x):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    random_entries = random.sample(lines, x)
    
    with open(output_file, 'w') as f:
        f.writelines(random_entries)

x = 5000  # Number of entries to randomly select
y = 'data5k.txt'  # Name of the output file
file_name = 'sampleData200k.txt'  # Name of the input file

select_random_entries(file_name, y, x)
print(f"Randomly selected {x} entries written to {y}")

