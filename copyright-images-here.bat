@ECHO OFF

SETLOCAL
SET CR_NAME=sean ryan

ECHO This will annotate images IN PLACE at current directory!

ECHO PRESS CTRL+C to cancel

PAUSE

dir

for %%i in (*.png) do magick convert "%%i" -gravity SouthEast -pointsize 14 -fill White -annotate +10+10 "%CR_NAME%" "%%i"
for %%i in (*.jpg) do magick convert "%%i" -gravity SouthEast -pointsize 14 -fill White -annotate +10+10 "%CR_NAME%" "%%i"

dir
