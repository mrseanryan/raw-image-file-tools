@ECHO OFF

ECHO This will resize image '%1' IN PLACE at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

magick mogrify -resize 1600 %1

del *.jpg~ 

dir
