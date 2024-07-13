#install 'requests' library using 'pip install requests'

import requests

def download_file(url, output_dir):
    local_filename = url.split('/')[-1]
    local_path = f"{output_dir}/{local_filename}"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded {local_filename}")
    return local_path

def download_files(urls_file, output_dir):
    with open(urls_file, 'r') as f:
        urls = f.readlines()
    
    for url in urls:
        url = url.strip()
        if url:
            download_file(url, output_dir)

# adjust paths below
urls_file = 'path/for/list/of/urls.txt'
output_dir = 'output/dir/path'

download_files(urls_file, output_dir)
