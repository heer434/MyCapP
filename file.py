def get_file_extension(filename):
    # Split the filename by dot (.)
    parts = filename.split(".")
    
    # The last part will be the file extension
    extension = parts[-1]
    return extension

filename = input("Input the Filename: ")
extension = get_file_extension(filename)
print(f"The extension of the file is: '{extension}'")
