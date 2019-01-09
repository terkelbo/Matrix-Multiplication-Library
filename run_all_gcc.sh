#!/bin/sh

CC=${1-"gcc"}

NUMBER_ROWS="50 100 200 300 400 500"
LOOPS=1000
LOGEXT=$CC.dat

/bin/rm -f nat.$LOGEXT lib.$LOGEXT knm.$LOGEXT kmn.$LOGEXT mkn.$LOGEXT mnk.$LOGEXT nkm.$LOGEXT nmk.$LOGEXT
for m in $NUMBER_ROWS
do
    ./matmult_c.${CC} nat $m $m-10 $m-30 | grep -v CPU >> nat.$LOGEXT
    ./matmult_c.${CC} lib $m $m-10 $m-30 | grep -v CPU >> lib.$LOGEXT
    ./matmult_c.${CC} knm $m $m-10 $m-30 | grep -v CPU >> knm.$LOGEXT
    ./matmult_c.${CC} kmn $m $m-10 $m-30 | grep -v CPU >> kmn.$LOGEXT
    ./matmult_c.${CC} mkn $m $m-10 $m-30 | grep -v CPU >> mkn.$LOGEXT
    ./matmult_c.${CC} mnk $m $m-10 $m-30 | grep -v CPU >> mnk.$LOGEXT
    ./matmult_c.${CC} nkm $m $m-10 $m-30 | grep -v CPU >> nkm.$LOGEXT
    ./matmult_c.${CC} nmk $m $m-10 $m-30 | grep -v CPU >> nmk.$LOGEXT
done

exit 0    	    					
    	    					
