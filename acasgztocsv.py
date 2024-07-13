import gzip
import json
import csv

def convert_json_to_csv(input_file, output_file):
    records = []

    try:
        # read as gzipped json file
        with gzip.open(input_file, 'rt', encoding='utf-8') as infile:
            for line in infile:
                try:
                    data = json.loads(line)
                    records.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
    except gzip.BadGzipFile:
        # read as reg JSON file
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                try:
                    data = json.loads(line)
                    records.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")

    # get fieldnames from the keys of the first record
    if records:
        fieldnames = set()
        for record in records:
            fieldnames.update(record.keys())
            if 'acas_ra' in record and isinstance(record['acas_ra'], dict):
                fieldnames.update({f'acas_ra_{k}' for k in record['acas_ra'].keys()})
        fieldnames = sorted(fieldnames)

        # write CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for record in records:
                flat_record = record.copy()
                if 'acas_ra' in flat_record and isinstance(flat_record['acas_ra'], dict):
                    for key, value in flat_record['acas_ra'].items():
                        flat_record[f'acas_ra_{key}'] = value
                    del flat_record['acas_ra']
                writer.writerow(flat_record)

    print(f"Conversion complete. The final CSV file is located at: {output_file}")

# update paths
input_json_file = '/path/to/acas.json.gz'
output_csv_file = '/path/to/acas.csv'


convert_json_to_csv(input_json_file, output_csv_file)