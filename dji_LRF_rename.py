import os


# check if Windows OS

def separator():
    if os.name == 'nt':
        return '\\'
    else:
        return '/'


count = 0
current_dir = os.getcwd()
print(f"Current dir: {current_dir}")


def rename_files_in_dir(subdir=''):
    global count
    # iterate all files from a directory
    for file_name in os.listdir(current_dir + subdir):
        # Construct old file name
        source = current_dir + subdir + separator() + file_name
        if os.path.isdir(source):
            print(f">> Subdirectory: {source}")
            rename_files_in_dir(separator() + file_name)
        if os.path.isfile(source) and file_name.find(".LRF") != -1:
            new_name = file_name.split('.')[0] + "_proxy.mp4"
            destination = current_dir + subdir + separator() + new_name
            os.rename(source, destination)
            # print(f"os.rename({source}, {destination})")
            count += 1
            print(F"{file_name} ==> {new_name}")


rename_files_in_dir()
print(f"{count} files renamed")
