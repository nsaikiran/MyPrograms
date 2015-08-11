#Most of the time whilte-spaces matters
# No white-space around = sign


# This shell script demonstrates input and output redirection
echo "Enter some text ( Use EOF (Ctrl+D) to stop )... "
echo
echo
cat >  test.txt

# lines=$(wc -l < test.txt) #also works

lines=`wc -l < test.txt`

echo
echo "No. of lines you entered are : $lines ."
echo
echo "Add some more lines ."

#This appends text to file
cat >> test.txt
echo
echo "File contents are ::"
echo

cat test.txt

lines2=`wc -l < test.txt`

diff=`expr $lines2 - $lines`

echo
echo "You added "$diff" lines"
echo
echo "removing file..."

rm test.txt

