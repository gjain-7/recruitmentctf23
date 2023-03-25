#! /usr/bin/bash

gunicorn --bind 127.0.0.1:5000 main:app >access.log 2>error.log &!