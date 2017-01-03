#!/usr/bin/env bash


SRCS=`find ./data.ko/*.txt`

mkdir -p ./output.ko/

for src in $SRCS
do
outname=`basename $src`
echo $src, $outname
python ./src/make_chatpair.py --input $src --output ./output.ko/pair_$outname

done
