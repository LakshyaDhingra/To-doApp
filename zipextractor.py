import zipfile


def extract_archive(filepath, folder):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(folder)
