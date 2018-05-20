import urllib.request
import re

def main():
    next_nothing("12345")
    next_nothing(str(16044/2))

def next_nothing(nothing):
    counter = 1
    pattern = re.compile(r"and the next nothing is (\d+)")

    while True:
        content = urllib.request.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}").read().decode()
        match = pattern.search(content)

        if match is None:
            print(content)
            break

        print(f"{counter}: " + match.group(1))
        nothing = match.group(1)
        counter += 1


if __name__ == "__main__":
    main()
