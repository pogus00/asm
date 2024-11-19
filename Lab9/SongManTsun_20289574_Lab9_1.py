def main():
    file_name = input("Please enter a file name in text format:")
    writedata(file_name)

def writedata(fname):
    with open(fname, 'w') as file:
        for i in range(3):
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            file.write(f"{name}\n")
            file.write(f"{mark}\n")
    print(f"Data written to {fname}")

if __name__ == "__main__":
    main()