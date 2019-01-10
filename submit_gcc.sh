#!/bin/sh 
### General options 
### -- specify queue -- 
#BSUB -q hpcintro
### -- set the job Name -- 
#BSUB -J Assignment1
### -- ask for number of cores (default: 1) -- 
#BSUB -n 1 
### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"
### -- specify that we need 2GB of memory per core/slot -- 
#BSUB -R "rusage[mem=2GB]"
### -- specify that we want the job to get killed if it exceeds 3 GB per core/slot -- 
#BSUB -M 3GB
### -- set walltime limit: hh:mm -- 
#BSUB -W 24:00 
### -- set the email address -- 
# please uncomment the following line and put in your e-mail address,
# if you want to receive e-mail notifications on a non-default address
##BSUB -u your_email_address
### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -oo Output.out 
#BSUB -eo Error.err 

module load gcc/8.2.0
module swap gcc/8.2.0

make -f Makefile.gcc clean
make -f Makefile.gcc OPT="-g"

source ~/stdpy3/bin/activate

# here follow the commands you want to execute 
./run_all.sh gcc nopt

python viz.py nopt gcc



make -f Makefile.gcc clean
make -f Makefile.gcc OPT="-g -Ofast"

source ~/stdpy3/bin/activate

# here follow the commands you want to execute
./run_all.sh gcc Ofast

python viz.py Ofast gcc




make -f Makefile.gcc clean
make -f Makefile.gcc OPT="-g -Ofast -funroll-loops"

source ~/stdpy3/bin/activate

# here follow the commands you want to execute
./run_all.sh gcc Ofast_loop

python viz.py Ofast_loop gcc

