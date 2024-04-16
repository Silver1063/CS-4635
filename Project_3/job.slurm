#!/bin/bash
#SBATCH --mem=16g
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4    # <- match to OMP_NUM_THREADS
#SBATCH --partition=cpu      # <- or one of: gpuA100x4 gpuA40x4 gpuA100x8 gpuMI100x8
#SBATCH --account=bbrx-delta-cpu    # <- match to a "Project" returned by the "accounts" command
#SBATCH --job-name=myjobtest
#SBATCH --time=00:01:00      # hh:mm:ss for the job
#SBATCH --constraint="scratch"


module reset # drop modules and explicitly load the ones needed
             # (good job metadata and reproducibility)
             # $WORK and $SCRATCH are now set
module load python  # ... or any appropriate modules
module list  # job documentation and metadata
source myenv/bin/activate
echo "job is starting on `hostname`"
echo $(pwd)
time srun python3 random_io.py > output
