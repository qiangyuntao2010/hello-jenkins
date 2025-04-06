# test.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(2, 3)
    with open("result.txt", "w") as f:
        f.write(f"Test result: add(2, 3) = {result}\n")
    print("Test executed successfully. Output written to result.txt")

