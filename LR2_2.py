def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
        return None

def main():
    filename = input("Enter filename: ")

    lines = read_file(filename)

    if lines is not None:
        num_lines = len(lines)

        while True:
            print(f"\nNumber of lines in the file: {num_lines}")
            line_number = int(input("Enter line number (1 to number of lines, 0 to quit): "))

            if line_number == 0:
                print("Exiting the program. Goodbye!")
                break
            elif 1 <= line_number <= num_lines:
                print(f"Line {line_number}: {lines[line_number - 1]}")
            else:
                print("Invalid input. Please enter a valid line number.")

if __name__ == "__main__":
    main()
