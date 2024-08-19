# python 3
"""
move-non-selected-images.py

Moves any image file-sets that are NOT named like x.y.jpg.

The files (JPEG and any matching raw files) are moved to a subdirectory 'not-selected'.

Files named like x.y.almost.jpg are move to a subdirectory 'almost'.

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


def _move_not_wanted_file(filename, dir_path, subdir_name):
    source_file_path = os.path.join(dir_path, filename)
    if os.path.isfile(source_file_path):
        move_file_do(source_file_path, os.path.join(dir_path, subdir_name))


def is_selected(filename):
    ok_tags = ['ok', 'good', 'edit', 'liked', 'crop']
    for ok in ok_tags:
        if ok in filename:
            return (not is_almost(filename))
    return False


def is_almost(filename):
    tags = ['almost']
    for ok in tags:
        if ok in filename:
            return True
    return False

def is_extension_ok(filename):
    extensions = ['jpg', 'jpeg', 'heic']
    for ext in extensions:
        if filename.lower().endswith(ext):
            return True
    return False


def filter_to_not_selected(filenames, include_filenames_multiple_dots=False):
    return list(filter(lambda f:
                       is_extension_ok(f)
                       and (not is_selected(f)) and (not is_almost(f))
                       and (include_filenames_multiple_dots or not has_multiple_dots(f)),
                       filenames))


def filter_to_not_selected__iphone(filenames_all):
    return filter_to_not_selected(filenames_all, True)


def filter_to_almost(filenames):
    return list(filter(lambda f:
                       is_extension_ok(f)
                       and (is_almost(f)),
                       filenames))

def filter_to_selected(filenames):
    return list(filter(lambda f:
                       is_extension_ok(f)
                       and is_selected(f) and (not is_almost(f)),
                       filenames))

def _move_files_to_subdir(filenames_not_wanted, dir_path, subdir):
    for filename in filenames_not_wanted:
        _move_not_wanted_file(filename, dir_path, subdir)
        # Sony, RAW, Panasonic
        raw_file_extensions = ['.ARW', '.CRW', '.DNG', '.NEF', '.RAW', '.RW2']
        for raw_ext in raw_file_extensions:
            # handle x.jpg -> x.arw
            raw_file_path = Path(filename).stem + raw_ext
            _move_not_wanted_file(raw_file_path, dir_path, subdir)
            if "almost" in filename:
                # handle x.almost.jpg -> x.arw
                raw_file_path = filename.split(".")[0] + raw_ext
                _move_not_wanted_file(raw_file_path, dir_path, subdir)

def print_section(title):
    print(f"=== === === {title} === === ===")

def handle_not_selected(filenames_all, dir_path):
    filenames_not_selected = filter_to_not_selected(filenames_all)
    # handle iphone folder
    if len(filenames_not_selected) == 0:
        filenames_not_selected = filter_to_not_selected__iphone(filenames_all)
    _move_files_to_subdir(filenames_not_selected, dir_path, "not-selected")
    print(f"not-selected: {len(filenames_not_selected)} file sets found (JPG + raw file(s))")
    return filenames_not_selected

def handle_almost(filenames_all, dir_path):
    filenames_almost = filter_to_almost(filenames_all)
    _move_files_to_subdir(filenames_almost, dir_path, "almost")
    print(f"almost: {len(filenames_almost)} file sets found (JPG + raw file(s))")
    return filenames_almost

def move_files(dir_path):
    filenames_all = os.listdir(dir_path)
    filenames_all = list(filter(lambda f:
                       os.path.isfile(f),
                       filenames_all))

    print_section("not-selected")
    handle_not_selected(filenames_all, dir_path)

    print_section("almost")
    handle_almost(filenames_all, dir_path)

    print_section("selected")
    filenames_selected = filter_to_selected(filenames_all)
    print(f"selected: {len(filenames_selected)} file sets remaining (JPG + raw file(s))")

move_files(sourceDirPath)
