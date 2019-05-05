#conding: utf-8-
#Author:'Jungang'
#Time:2019/4/28

import os
import cv2
import numpy as np

def filename(root_path,picyuretype):
    file_name = []
    for root ,dirs, files in os.walk(root_path):
        for files in files:
            if os.path.splitext(files)[1] == picyuretype:
                filename.append(os.path.join(root,files))
    return file_name
