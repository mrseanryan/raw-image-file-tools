# raw-image-file-tools README

Simple tools for moving and copying selected RAW image files and their associated JPG

## Dependencies

- [Python 3.x](https://www.python.org/downloads/)
- [Image Magick](https://imagemagick.org/script/download.php)

## Setup

- install [Python 3.x](https://www.python.org/downloads/)
- ensure `python` is available via the PATH environment variable
- install [Image Magick](https://imagemagick.org/script/download.php)
- ensure `magick` is available via the PATH environment variable

To use the BAT scripts, you need to create an environment variable `PATH_TO_RAW_IMAGE_FILE_TOOLS` that points to the local copy of this repository.

Then, you can copy the BAT scripts to a convenient location, for example `c:\`.


## Usage

| Script                         | To see usage                         | To use                                                                                                                                | Description                                                                                                                                        |
| ------------------------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| copyright-images-here.bat      | -                                    | Edit the script to use your name. Then CD to the directory with images to add a copyright watermark. Then `copyright-images-here.bat` | Adds a copyright watermark to the images in the current directory.                                                                                 |
| copy-selected.bat              | -                                    | `copy-selected.bat`                                                                                                                   | See copy-selected-images.py                                                                                                                        |
| copy-selected-images.py        | `python copy-selected-images.py`     | `python copy-selected-images.py <path to directory>`                                                                                  | Copies any image file-sets that ARE named like x.y.jpg. The files (JPEG and any matching raw files) are copied to a subdirectory 'selected'.       |
| move-non-selected.bat          | -                                    | CD to directory of images. Name selected images like x.y.jpg. Then `move-non-selected.bat`                                            | See move-non-selected-images.py                                                                                                                    |
| move-non-selected-images.py    | `python move-non-selected-images.py` | `python move-non-selected-images.py <path to directory>`                                                                              | Moves any image file-sets that are NOT named like x.y.jpg. The files (JPEG and any matching raw files) are moved to a subdirectory 'not-selected'. |
| resize-images-here-large.bat   | -                                    | CD to directory containing a copy of images to resize. Then `resize-images-here-large.bat`                                            | Resizes images in the current directory to smaller 'large' size.                                                                                   |
| resize-images-here-smaller.bat | -                                    | CD to directory containing a copy of images to resize. Then `resize-images-here-smaller.bat`                                          | Resizes images in the current directory to smaller 'smaller' size.                                                                                 |
| resize-images-here.bat         | -                                    | CD to directory containing a copy of images to resize. Then `resize-images-here.bat`                                                  | Resizes images in the current directory to smaller size.                                                                                           |
| resize-single-image-here.bat   | -                                    | Make a copy of an image to resize. Then `resize-single-image-here.bat <path to image file>`                                           | Resizes one image to smaller size.                                                                                                                 |

## RAW files supported

The following RAW file formats are supported:

- CRW (Canon)
- NEF (Nikon)
- RAW (?)
- ARW (Sony)
- RW2 (Panasonic)

### Usage - process and examples

1. First 'mark' an image file (RAW or JPG) by renaming it to have a middle part, separated by `.`.

Examples:

- from `x.JPG` -> x`.ok`.JPG
- from `SA12345.JPG` -> SA12345`.ok`.JPG
- from `SA12345.ARW` -> SA12345`.good`.ARW

2. Then you can automatically move all NON selected images to a sub-folder 'not-selected'

Example:

```
python move-non-selected-images.py C:\myImages\pics1
```

3. OR you can copy all the _selected_ images to sub-folder 'selected'

Example:

```
python copy-non-selected-images.py C:\myImages\pics1
```

#### Benefits

- Helps speed up the curation process, when you have a lot of images to deal with.
- When a RAW file is processed, any associated JPG file will also be moved or copied.
- Quickly resize and watermark images.

## License

- MIT - copyright Sean Ryan 2022
