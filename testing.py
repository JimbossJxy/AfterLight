import os
import random
import string
import time
import tempfile

# Create a temporary directory
temp_dir = tempfile.mkdtemp()
print(f'Temporary directory created: {temp_dir}')

# Generate random characters for the text file
random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Create a text file with random characters
file_path = os.path.join(temp_dir, 'random_file.txt')
with open(file_path, 'w') as file:
    file.write(random_chars)

# Sleep for 60 seconds
time.sleep(60)
print('Finished sleeping for 60 seconds')