#!/bin/bash

if [ ! -d ".venv" ] ; then
    if [ -f "$(which virtualenv)" ] ; then
        virtualenv --python=python2.7 --prompt=\(pyfitnesspal\) .venv
        .venv/bin/pip install -r requirements.txt
        .venv/bin/pip install -r dev-requirements.txt
    else
        echo "Please ensure that virtualenv is installed and on the PATH."
    fi
fi
