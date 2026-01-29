@ECHO OFF

ECHO This will convert HEIC images IN PLACE to JPG at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

magick mogrify -format jpg *.HEIC

del *.jpg~

dir
