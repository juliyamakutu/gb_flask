#!/usr/bin/env bash
pip install -r requirements.txt
flask db upgrade
if [ ! -f tags.lock ]; then
    flask create-tags
fi
