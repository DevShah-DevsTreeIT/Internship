from collections import defaultdict

def analyze_log_file(file_path):
    total_lines = 0
    error_count = 0
    error_messages = []
    error_summary = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line:
                error_count += 1
                error_messages.append(line.strip())
                
                # Optional: Extract type of error if available
                parts = line.strip().split(" - ")
                if len(parts) == 2:
                    error_type = parts[1].split()[0]  # e.g., "Failed", "Timeout"
                    error_summary[error_type] += 1

    print("Log Summary:")
    print("------------")
    print(f"Total lines      : {total_lines}")
    print(f"Error count      : {error_count}")
    print("Error breakdown  :")
    for err_type, count in error_summary.items():
        print(f"  {err_type}: {count} time(s)")

    print("\nError Messages:")
    for msg in error_messages:
        print(f"- {msg}")
    
    # Optional: Save to a report file
    with open("log_report.txt", "w") as report:
        report.write("Log Summary Report\n")
        report.write("------------------\n")
        report.write(f"Total lines      : {total_lines}\n")
        report.write(f"Error count      : {error_count}\n")
        report.write("Error breakdown  :\n")
        for err_type, count in error_summary.items():
            report.write(f"  {err_type}: {count} time(s)\n")
        report.write("\nError Messages:\n")
        for msg in error_messages:
            report.write(f"- {msg}\n")

# Usage
analyze_log_file("sample.log")
