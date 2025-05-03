import csv

def convert_logs(input_path, output_path):
    try:
        with open(input_path) as infile, open(output_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Timestamp", "Level", "Message"])
            for line in infile:
                if line.strip():
                    parts = line.split(" ", 2)
                    writer.writerow(parts)
        return True
    except Exception as e:
        print(f"Conversion failed: {e}")
        return False
