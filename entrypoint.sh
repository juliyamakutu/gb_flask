#!/usr/bin/env bash
flask db upgrade
python wsgi.py