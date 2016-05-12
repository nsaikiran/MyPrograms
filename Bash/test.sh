#! /bin/bash

x=1
while [ $x -lt 10 ]
do
echo $x
(( x++ ))
done

echo /bin/*sh #To print all available shell types.


name=readme
x=1
echo "$name""$x"

while ( test $x -lt 5 )
do
echo $x
echo "This file contains data $name$x">$name$x
(( x++ ))
done


for files in readme*
do
mv $files "dont$files"
done


cat dont* > DONT

