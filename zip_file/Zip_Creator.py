import zipfile
import pathlib
#from File_Zipper import filepaths


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)
#
#
#
#
if __name__ == '__main__':
    make_archive(filepaths = ['One.py', 'main.py'], dest_dir = 'dest')

# Zip_Creator.py
# import zipfile
# import os
#
# def make_archive(filepaths, dest_dir):
#     """Compress the provided files into a ZIP archive in the specified destination folder."""
#     archive_name = os.path.join(dest_dir, "compressed_files.zip")
#     with zipfile.ZipFile(archive_name, 'w') as archive:
#         for filepath in filepaths:
#             archive.write(filepath, os.path.basename(filepath))
#     print(f"Files compressed successfully into {archive_name}")
