import asyncoo 
import subprocess 
import json
import os 
import shutil
from datetime import datetime
from pathlib import Path
import paramiko
from mcp import server, types 

app = Server("Linux-config-server")



TARGET_SYSTEM  = {
    "localhost":{
        "host": "localhost",
        "type": "local"
    }

# add in the servers
# add path to what dir you want to acces 
