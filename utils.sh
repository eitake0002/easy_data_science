#!/bin/sh

# Load this file.
# . ./easy_data_science/utils.sh

#--------------------------------------------------------------------
# Common utils
#--------------------------------------------------------------------

# Exec python file without createing .pyc
function py(){
  python -B $1
}

#--------------------------------------------------------------------
# pep8
#--------------------------------------------------------------------

# Install pep8 and autopep8 with pip
function install-pep(){
  pip install pep8
  pip install autopep8
}

# Check pep8
function pep-check(){
  pep8 $1
}

# Auto refactor.
function pep-auto(){
  autopep8 -i $1
}

# --------------------------------------------------------------------
# unittset
# --------------------------------------------------------------------
function pytest(){
  python -B -m unittest $1
}
