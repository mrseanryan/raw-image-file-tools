@ECHO OFF

ECHO Copies ALL selected JPG and ARW files from '.' to a subdirectory 'selected'

ECHO Press CTRL+C to cancel...

pause
python %PATH_TO_RAW_IMAGE_FILE_TOOLS%\copy-selected-images.py  .
