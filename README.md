# python-utils

Python libraries for data science, data management, web scraping, database management, file manipulation etc...

# Python
Python3.0 or higher.

# Dependencies
numpy, pandas, scikit-learn

# Installation

Install dependency packages and clone pyenv repository.
```
$ yum install gcc gcc-c++ make git openssl-devel bzip2-devel zlib-devel readline-devel sqlite-devel bzip2 sqlite zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel
$ git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```

Add below scripts on ~/.bash_profile
```
export PYENV_ROOT="${HOME}/.pyenv"
if [ -d "${PYENV_ROOT}" ]; then
    export PATH=${PYENV_ROOT}/bin:$PATH
    eval "$(pyenv init -)"
fi
```

Reload ~/.bash_profile
```
$ source ~/.bashrc
```
