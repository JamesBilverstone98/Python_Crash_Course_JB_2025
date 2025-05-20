from pathlib import Path
import json

path = Path('/Users/jamesmacbook/Desktop/Python Crash Course 2025/Chapter 10. Files and Exceptions/10.11 favourite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favourite number! It's {number}.")