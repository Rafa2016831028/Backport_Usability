import csv
from github import Github
import time
from datetime import datetime
import pytz
import sys
csv.field_size_limit(sys.maxsize)

def initialize_G():
    with open('keys.gconfig', 'r') as file:
        accesskey = file.read().replace('\n', '')
    g = Github(accesskey)

    with open('keys_multiple.gconfig') as f:
        backup_keys = f.readlines()
    backup_keys = [x.strip() for x in backup_keys] 
    no_bused_key = 0
    return g, backup_keys, no_bused_key, accesskey   