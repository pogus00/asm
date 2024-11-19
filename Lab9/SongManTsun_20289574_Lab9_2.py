import os.path
def main():
    i = 0
    while i == 0:
        file_name = input("Enter the file name to read (e.g., studentRecord.txt): ")
        if os.path.exists(file_name):
            print("exists in the current directory.")
            readData(file_name)
            i += 1
        else:
            print("DOES NOT exist in the current directory. Please retry.")
            continue

def readData(fname):
    with open(fname, 'r') as file:
        lines = file.readlines()
        total_marks = 0
        count = 0
        for i in range(0, len(lines), 2):
            name = lines[i].strip()
            marks = int(lines[i + 1].strip())
            print(f'name: {name}')
            print(f'marks: {marks}')
            total_marks += marks
            count += 1

    average = total_marks / count
    print(f"Average Mark: {average:.2f}")

if __name__ == '__main__':
    main()