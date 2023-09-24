@ECHO OFF

ECHO Moves ALL non-selected JPG and ARW files to a sub-folder 'non-selected'

ECHO Press CTRL+C to cancel...

pause
python %PATH_TO_RAW_IMAGE_FILE_TOOLS%\move-non-selected-images.py .
