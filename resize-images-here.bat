@ECHO OFF

ECHO This will resize images IN PLACE at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

magick mogrify -resize 1600 *.png
magick mogrify -resize 1600 *.jpg
magick mogrify -format jpg -resize 1600 *.HEIC

del *.jpg~ 

dir
