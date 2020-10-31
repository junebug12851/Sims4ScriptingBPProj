from zipfile import PyZipFile, ZIP_STORED


def get_zip_handle(path):
    return PyZipFile(path, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)
