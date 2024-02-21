import zipfile
import pathlib


def zip_it(filepath_input, destination_directory_input):
    # define name of the output archive (here it's hardcoded)
    final_filename = "test_11.zip"
    # define destination folder and connect it with output archive's name
    # using pathlib.Path() makes the output destination better to handle
# it is possible to not use pathlib.Path() although it is not recommended:
# it would look like this:
# with zipfile.ZipFile(destination_directory_input + "/" + "test_11.zip", 'w') as zip_file:
    final_destination_directory = pathlib.Path(destination_directory_input,
                                               final_filename)
    # zipfile.ZipFile is a function that actually converts the file
    # it requires appropriate folder directory combined with expected archive's name
    # it requires 'w' mode, as it is expected to write a file
    with zipfile.ZipFile(final_destination_directory, 'w') as zip_file:
        # for-loop ensures that program performs a conversion for each file (filepath)
        # that has been provided with into function (filepath_input)
                # filepath_input is expected to not be a string at this point
                # therefore .split(";") function is used in the main code
                # before creating actual "filepath_input" variable
        for filepath in filepath_input:
            # here using pathlib converts original filepath into a form that
            # the program can interact and modify.
            # that step is necessary for using 'arcname='
            filepath = pathlib.Path(filepath)
            # .write() function writes (saves) the converted file as archive
            # "filepath" points to a "filepath" value converted via pathlib.Path()
            # "arcname=" extracts a name of the file, to use it for saving the
            # newly created archive in a proper way. It is so due to filepath.name method
            # using it is possible due to converting the "filepath" within pathlib.Path()
            zip_file.write(filepath, arcname=filepath.name)
