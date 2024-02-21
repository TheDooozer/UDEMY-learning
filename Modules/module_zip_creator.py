import zipfile
import pathlib


def zip_it(filepath_input, destination_directory_input):
    final_filename = "test_11.zip"
    final_destination_directory = pathlib.Path(destination_directory_input, final_filename)

    with zipfile.ZipFile(final_destination_directory, 'w') as zip_file:
        for filepath in filepath_input:
            filepath = pathlib.Path(filepath)
            zip_file.write(filepath, arcname=filepath.name)
