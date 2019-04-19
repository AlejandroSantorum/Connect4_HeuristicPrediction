#!/bin/bash

M=17000
Aux=$M
while [ true ]
do
    python3 c4_scrape.py $Aux
    Aux="$(($Aux-$?))"
    if [ $Aux = 0 ]
      then
      break
    fi
done
# To give permissions run: chmod +x name_of_script.sh
