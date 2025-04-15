#!/bin/bash

# 收集靜態文件
python3 manage.py collectstatic --noinput

# 運行生產服務器，使用端口8050
python3 manage.py runserver 0.0.0.0:8050 --settings=userdata_project.settings_prod
