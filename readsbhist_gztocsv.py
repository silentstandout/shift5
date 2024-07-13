import gzip
import json
import os
import csv

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        elif isinstance(x, list):
            i = 0
            for a in x:
                flatten(x[i], name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

def process_aircraft(aircraft_list):
    processed_data = []
    for aircraft in aircraft_list:
        flattened_aircraft = flatten_json(aircraft)
        processed_data.append(flattened_aircraft)
    return processed_data

def convert_gzipped_json_to_csv(input_dir, output_file):
    fieldnames = set()
    records = []
    error_files = []

    for filename in os.listdir(input_dir):
        if filename.endswith('.json.gz'):
            input_file_path = os.path.join(input_dir, filename)
            try:
                with gzip.open(input_file_path, 'rt', encoding='utf-8') as infile:
                    data = json.load(infile)
                    flattened_data = flatten_json({k: v for k, v in data.items() if k != 'aircraft'})
                    fieldnames.update(flattened_data.keys())
                    if 'aircraft' in data:
                        aircraft_records = process_aircraft(data['aircraft'])
                        for aircraft_record in aircraft_records:
                            combined_record = {**flattened_data, **aircraft_record}
                            records.append(combined_record)
                            fieldnames.update(combined_record.keys())
                    else:
                        records.append(flattened_data)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
                error_files.append(filename)

    fieldnames = sorted(fieldnames)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

    if error_files:
        print(f"The following files could not be processed: {error_files}")

input_directory = '/path/to/input/dir'  # update path to your input directory
final_output_file = '/path/to/output/readsb_hist.csv'  # update path to output file

convert_gzipped_json_to_csv(input_directory, final_output_file)

print(f"Conversion complete. The final CSV file is located at: {final_output_file}")