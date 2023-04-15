benchmark=$1

echo -n "$benchmark= [" >> data.txt 
grep "$benchmark" text.txt | cut -d':' -f2-| xargs -ro echo -n >> data.txt
echo "]" >> data.txt
