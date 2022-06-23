#!/usr/bin/env bash
pipenv shell
set FLASK_ENV=development FLASK_APP=expenses_manager.py
flask run