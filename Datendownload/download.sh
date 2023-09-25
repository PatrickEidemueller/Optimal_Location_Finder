#!/bin/bash

for ((i=2004; i <= 2021; i=$i+1)); do
    mv $i.csv.gz weather/
done
