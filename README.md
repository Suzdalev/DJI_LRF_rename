# DJI *.LRF 
DJI *.LRF file is Low Resolution File, just compressed version of original recording. 
This file is not useless, it could be used as proxy file for video editing.

# What does script do?

This script basically renames all *.LRF files into *_proxy.mp4 files
e.g.

> DJI_0001.LRF ==> DJI_0001_proxy.mp4 

Script renames all files in current folder(where the script is), and recursively in all subfolders.

# Usage

pyhton interpreter:
```
python.exe ./dji_LRF_rename.py
```
or
```
python ./dji_LRF_rename.py
```

For Windows users there are executable file, created by
```
pyinstaller -F dji_LRF_rename.py
```
You can download it in releases section
