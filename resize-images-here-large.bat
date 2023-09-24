@ECHO OFF

ECHO This will resize images IN PLACE at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

magick mogrify -resize 3200 *.png
magick mogrify -resize 3200 *.jpg
magick mogrify -format jpg -resize 3200 *.HEIC

del *.jpg~ 

dir
