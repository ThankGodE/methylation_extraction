This scripts extracts methylation based on CpG context:

````
Script to extract methylation
Syntax: {home}/methylation_task/bash_script/extract_methylation.sh [-o|-i]
options:
-o    absolute path to output files. Required=true
-i    absolute directory path to input files. Required=true
-r    path to reference genome .fasta
-h    Display Help
-f    force remove or delete previously created existing program file paths. e.g. true or false. Default=false
````


Transformation of the extracted methylations happens through a Python Script which is also captured in a function 
the bash script above:

````
    usage:  methylation_extraction.py
    -o path2out
    
    This script extracts methylation information from a bam file Required: -
    Python >= 3.6 - Pathos - Pandas - MethylDackel>=0.5.1 - HTSlib>=1.9
    
    optional arguments:
        -h, --help            show this help message and exit
        -o PATH2OUT_FILE, --path2out_file PATH2OUT_FILE
        absolute path to processed output file (default: None)
        -i PATH2BAM_FILES, --path2bam_files PATH2BAM_FILES
        absolute path (parent directory) to bam files
        (default: None)
        -n NUM_CPUS, --num_cpus NUM_CPUS
        number of cpus to use (default: 4)
````
