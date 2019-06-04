# #!/bin/bash
FILES=*.txt

counter=1
for f in $FILES
do
  echo "../data/papers_own_impl/$f $f" >> fileName2
  counter=$((counter+1))
done
