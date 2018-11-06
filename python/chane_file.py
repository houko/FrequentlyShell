import os
import sys


def scan_dir(path):
    listdir = os.listdir(path)
    for list_item in listdir:
        old_file = path + "/" + list_item
        new_file = path + "/" + str.split(old_file, ".")[0] + ".png"
        if os.path.isfile(old_file):
            change_file_name(old_file, new_file)
        else:
            scan_dir(old_file)


def change_file_name(old_file, new_file):
    os.rename(old_file, new_file)


def main():
    path = sys.argv[1]
    scan_dir(path)


if __name__ == '__main__':
    main()
