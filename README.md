# raw-image-file-tools README

Simple tools for moving and copying selected RAW image files and their associated JPG

## Dependencies

Python 3.x

## Usage

| Script                      | To see usage                         | To use                                                   | Description                                                                                                                                        |
| --------------------------- | ------------------------------------ | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| copy-selected-images.py     | `python copy-selected-images.py`     | `python copy-selected-images.py <path to directory>`     | Copies any image file-sets that ARE named like x.y.jpg. The files (JPEG and any matching raw files) are copied to a subdirectory 'selected'.       |
| move-non-selected-images.py | `python move-non-selected-images.py` | `python move-non-selected-images.py <path to directory>` | Moves any image file-sets that are NOT named like x.y.jpg. The files (JPEG and any matching raw files) are moved to a subdirectory 'not-selected'. |

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

#### Benefit: When a RAW file is processed, any associated JPG file will also be moved or copied.

## License

- MIT - copyright Sean Ryan 2022
