# python 3
"""
move-non-selected-images.py

Moves any image file-sets that are NOT named like x.y.jpg.

The files (JPEG and any matching raw files) are moved to a subdirectory 'not-selected'.

USAGE: move-non-selected-images.py <path to directory>
"""
from optparse import OptionParser
import os
from pathlib import Path
import sys


###############################################################
# usage() - prints out the usage text, from the top of this file :-)
def usage():
    print(__doc__)


###############################################################
# optparse - parse the args
parser = OptionParser(usage='%prog <directory> [options]')
parser.add_option('-d', '--dryrun', dest='is_dry_run', action="store_true",
                  default=False,
                  help='Dry run - no files will be moved')

(options, args) = parser.parse_args()
if(len(args) != 1):
    usage()
    sys.exit(2)
sourceDirPath = args[0]


def has_multiple_dots(filename):
    return filename.count('.') > 1


def move_file_do(filepath, target_dir_path):
    if options.is_dry_run:
        print(f"[dry run] Moving file {filepath} -> {target_dir_path}")
        return
    print(f"Moving file {filepath} -> {target_dir_path}")
    Path(target_dir_path).mkdir(parents=True, exist_ok=True)
    filename = os.path.basename(filepath)
    target_file_path = os.path.join(target_dir_path, filename)
    os.rename(filepath, target_file_path)


def move_file(filename, dir_path):
    source_file_path = os.path.join(dir_path, filename)
    if os.path.isfile(source_file_path):
        move_file_do(source_file_path, os.path.join(dir_path, "not-selected"))


def is_selected(filename):
    ok_tags = ['ok', 'good', 'edit', 'liked']
    for ok in ok_tags:
        if ok in filename:
            return True
    return False


def is_extension_ok(filename):
    extensions = ['jpg', 'jpeg', 'heic']
    for ext in extensions:
        if filename.endswith(ext) or filename.endswith(ext.lower()):
            return True
    return False


def filter_to_selected(filenames, include_filenames_multiple_dots):
    return list(filter(lambda f:
                       is_extension_ok(f)
                       and (not is_selected(f))
                       and (include_filenames_multiple_dots or not has_multiple_dots(f)),
                       filenames))


def move_files(dir_path):
    filenames_all = os.listdir(dir_path)

    filenames = filter_to_selected(filenames_all, False)

    # handle iphone folder
    if len(filenames) == 0:
        filenames = filter_to_selected(filenames_all, True)

    for filename in filenames:
        move_file(filename, dir_path)
        # Sony, RAW, Panasonic
        raw_file_extensions = ['.ARW', '.RAW', '.RW2', '.CRW', '.NEF']
        for raw_ext in raw_file_extensions:
            raw_file_path = Path(filename).stem + raw_ext
            move_file(raw_file_path, dir_path)
    print(f"{len(filenames)} file sets found (JPG + raw file(s))")


move_files(sourceDirPath)
