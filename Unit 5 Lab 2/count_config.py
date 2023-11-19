# Read the contents of the INI file 'r' is read only 
with open('./mydefaults.ini.txt', 'r') as ini_file:
    ini_content = ini_file.read()

# I searched stackoverflow to identify new methods the number of letters (A-Z, a-z) and numbers (0-9)
letter_count = sum(char.isalpha() for char in ini_content)
number_count = sum(char.isdigit() for char in ini_content)

# this will create an "outputs.txt" file 'w' as in write and writes the numbers counted
with open('outputs.txt', 'w') as output_file:
    output_file.write(f'Letter Count: {letter_count}\n')
    output_file.write(f'Number Count: {number_count}\n')

print(f'Letter Count: {letter_count}')
print(f'Number Count: {number_count}')