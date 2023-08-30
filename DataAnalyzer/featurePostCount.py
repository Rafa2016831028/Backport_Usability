import sys
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import itertools
import glob

def analyzeFiles(path_name = ''):
    """
    purpose:  Retrieve the domain specific SO posts and count popularity by the number of the post
    Args: the name of folder
    Returns: count of SO posts in each domain
    """
    path_folder = ['SO_Data/'+os.path.basename(x) for x in os.listdir(path_name)]
    
    for idx, domain_path in enumerate(path_folder):
        all_posts=[]
        feature_paths = [domain_path+'/'+os.path.basename(x) for x in os.listdir(domain_path)]
        for index, file_path in enumerate(feature_paths):
            with open(file_path,"r") as fp:
                print(file_path)
                # reader = csv.reader(fp, delimiter=",", quotechar='"', dialect=csv.excel_tab)
                # data_read = [row for row in reader]
                filename='/home/tanvir/workplace/Backport_Usability/'+file_path
                posts = pd.read_csv(filename, index_col=None, header=0)
                all_posts.append(posts)
            domain_posts = pd.concat(all_posts, axis=0, ignore_index=True)
        domain_posts=domain_posts.drop_duplicates(subset=['Post Link'])
        print(len(domain_posts.index))
        print(domain_posts.head(5))
            
        print("-------------------- -------------")
                    
    # with open(output_path, "w") as fpw:
    #     for key in fileDictionary.keys():
    #         fpw.write("%s, %s\n" % (key, fileDictionary[key]))  


analyzeFiles('SO_Data')