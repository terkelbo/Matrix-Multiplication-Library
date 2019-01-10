#!/bin/bash
#BSUB -J collect
#BSUB -o collect.out
#BSUB -q hpcintro
#BSUB -n 1
#BSUB -R "rusage[mem=2GB]"
#BSUB -W 2:00

module load studio
module load gcc/8.2.0
module swap gcc/8.2.0
make -f Makefile.gcc clean
make -f Makefile.gcc

#Algorithm
ALGO="blk"

#Parameters
PARAM="1000 1000 1000"
BS="1000"

#Experiment parameters
EXPNAME="collect.data.$ALGO.er"

rm -rf $EXPNAME

COUNTERS="-h dcm,on,l2m,on,l3m,on"

#Start collect algorithm
collect -o $EXPNAME $COUNTERS ./matmult_c.gcc $ALGO $PARAM $BS
