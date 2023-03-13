# trojanconverter

README


This is a Python script that downloads files from URLs and convert them into trojan executable. It requires the requests, subprocess, os, and tempfile modules to be installed.

How to use


To use this script, follow these steps:

Import the required modules by adding this code to the top of your script:



import requests

import subprocess

import os

import tempfile


- Copy and paste the code from this repository's trojan.py file into your Python script.


- Edit the pdf_url and exe_url variables with the URLs of the files you want to download and run.


- Edit the pdf_name and exe_name variables with the names you want to give the downloaded files.


- Run your Python script.


- The script will download the files from the URLs, save them with the specified names in your temporary directory, and then run them using subprocess. Once the files have been run, they will be deleted from your temporary directory.
