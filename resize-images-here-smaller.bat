@ECHO OFF

ECHO This will resize images IN PLACE at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

magick mogrify -resize 800 *.png
magick mogrify -resize 800 *.jpg
magick mogrify -format jpg -resize 800 *.HEIC

del *.jpg~ 

dir
