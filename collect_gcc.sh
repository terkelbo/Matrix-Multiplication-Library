#!/bin/bash
#BSUB -J collect
#BSUB -o collect.out
#BSUB -q hpcintro
#BSUB -n 1
#BSUB -R "rusage[mem=2GB]"
#BSUB -W 2:00

module load studio

#Algorithm
ALGO="mkn"

#Parameters
PARAM="1000 1000 1000"
BS="1000"

#Experiment parameters
EXPNAME="collect.data.$ALGO.er"

COUNTERS="-h dch,on,dcm,on,l2h,on,l2m,on"

#Start collect algorithm
collect -o $EXPNAME $COUNTERS ./matmult_c.gcc $ALGO $PARAM $BS
