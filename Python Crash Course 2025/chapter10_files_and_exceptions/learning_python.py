from pathlib import Path

print("--- Reading in the entire file:")
path = Path('/Users/jamesmacbook/Desktop/Python Crash Course 2025/Chapter 10. Files and Exceptions/10.1 learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)