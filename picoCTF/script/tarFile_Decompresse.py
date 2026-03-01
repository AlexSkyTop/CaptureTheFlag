import tarfile
import os

def extract_nested_tar(file_path, dest_dir="."):
    while file_path.endswith(".tar"):
        print(f"Extraction de {file_path} ...")
        with tarfile.open(file_path) as tar:
            tar.extractall(dest_dir)
        os.remove(file_path)
        tars = [f for f in os.listdir(dest_dir) if f.endswith(".tar")]
        if not tars:
            break
        file_path = tars[0]

extract_nested_tar("1000.tar")