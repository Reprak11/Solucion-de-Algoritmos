#!/bin/bash
mkdir app
mkdir app/common
touch app/common/__init__.py app/common/error_handling.py

mkdir app/$1
mkdir app/$1/api_v1_0
touch app/$1/api_v1_0/__init__.py app/$1/api_v1_0/resources.py app/$1/api_v1_0/schemas.py
touch app/$1/__init__.py app/$1/models.py 
touch app/__init__.py app/db.py app/ext.py

mkdir config
touch config/__init__.py config/default.py

touch entrypoint.py
