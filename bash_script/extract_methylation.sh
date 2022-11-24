#!/bin/bash

#********************************************************************
#
# extract_methylation.sh
# ${methylation_task}bash/script/extract_methylation.sh

# this is a strict mode for shell. it ensures that all commands exits with 0 and that all variables are set
set -e
set -u

########################################################################################################################
# Help                                                                                                                 #
########################################################################################################################
Help() {

  # Display Help
  echo -e "\n";
  echo "Script to extract methylation"
  echo "Syntax: $0 [-o|-i]";
  echo "options:";
  echo "-o    absolute path to output files. Required=true";
  echo "-i    absolute directory path to input files. Required=true";
  echo "-r    path to reference genome .fasta"
  echo "-h    Display Help";
  echo "-f    force remove or delete previously created existing program file paths. e.g. true or false. Default=false"
  echo -e "\n";
}


########################################################################################################################
########################################################################################################################
# Main program                                                                                                         #
########################################################################################################################
########################################################################################################################
# Process the input options. Add the options as needed                                                                 #
########################################################################################################################

REMOVE_PATH="false";  #DEFAULT_REMOVE_PATH
NUMBER_CPU=4;

while getopts o:i:f:n:r:h flag # the colon after any alphabet shows that an input argument is required.
do
    case "${flag}" in

	o) PATH_TO_OUT_DIRECTORY=${OPTARG};;
  i) ABS_DIR_PATH_TO_INPUT=${OPTARG};;
  n) NUMBER_CPU=${OPTARG};;
  r) REFERENCE_GENOME=${OPTARG};;
  f) REMOVE_PATH="true";;
  h) Help
    exit;; # display Help
  \?) echo "Error: Invalid option"
    exit;; # incorrect option

    esac
done

check_mandatory_cli_arguments() {

  # mandatory argument checks
  NUM_REGULAR_EXPRESSION="^[0-9]+$";
  DOT="[.]";

  if [ ! -d "$PATH_TO_OUT_DIRECTORY" ] ; then
      echo -e "\nMissing mandatory -o commandline options.\n" >&2;
      Help
      exit 1

  elif [ ! -d "$ABS_DIR_PATH_TO_INPUT" ] ; then
      echo -e "\nMissing mandatory -i commandline options.\n" >&2;
      Help
      exit 1

  elif ! [[ "$NUMBER_CPU" =~ $NUM_REGULAR_EXPRESSION ]];
    then
          echo -e "\nMissing mandatory -n commandline options as an integer e.g. 16 and not 16.0\n" >&2;
          Help
          exit 1

  elif ! [[ "$NUMBER_CPU" =~ $NUM_REGULAR_EXPRESSION ]] && [[ "$PANTHER_VERSION" =~ $DOT ]];
  then
        echo -e "\nMissing mandatory -n commandline options as an integer e.g. 16 and not 16.0\n" >&2;
        Help
        exit 1

  fi

}

generate_bed_graph_files() {

  for ABSOLUTE_PATH_TO_BAM_FILE in "$ABS_DIR_PATH_TO_INPUT"/*bam; do

    ABSOLUTE_PATH_TO_SAM_FILE="${ABSOLUTE_PATH_TO_BAM_FILE%.*}""_CpG.bedGraph";

    echo "extracting methylation information from bam file: " "$ABSOLUTE_PATH_TO_BAM_FILE" " to bedGraph file:""$ABSOLUTE_PATH_TO_SAM_FILE";

    MethylDackel extract "$REFERENCE_GENOME" "$ABSOLUTE_PATH_TO_BAM_FILE"

#    samtools view -h "$ABSOLUTE_PATH_TO_BAM_FILE" > "${ABSOLUTE_PATH_TO_SAM_FILE}";

  done;

  }

main() {

  check_mandatory_cli_arguments;
  generate_bed_graph_files;

}

main;



