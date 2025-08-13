# Text File Processor

input_file = "task1.txt"
output_file = "report.txt"

line_count = 0
word_count = 0
char_count = 0

try:
    with open(input_file, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)

    with open(output_file, 'w') as f:
        f.write(f"Lines: {line_count}\n")
        f.write(f"Words: {word_count}\n")
        f.write(f"Characters: {char_count}\n")

    print("Report generated successfully!")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
