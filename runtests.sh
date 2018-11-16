#!/data/data/com.termux/files/usr/bin/bash

until ag -l --python | entr -d python -m unittest discover -v; do sleep 1; done
