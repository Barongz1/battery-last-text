"""The Battery's Last Text to Its Charger — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The last text: the battery held on at 1% for hours, then left with regrets.
TEXT = "You took all day. I held on at 1% for hours, and now I am leaving this phone with nothing but regrets and a dead screen."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
