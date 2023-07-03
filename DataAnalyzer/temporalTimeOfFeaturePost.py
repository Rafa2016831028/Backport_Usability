import sys
import os
from os import listdir
import matplotlib.pyplot as plt
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
                filename='/home/tanvir/workplace/Backport_Usability/'+file_path
                posts = pd.read_csv(filename, index_col=None, header=0)
                all_posts.append(posts)
            domain_posts = pd.concat(all_posts, axis=0, ignore_index=True)
        domain_posts=domain_posts.drop_duplicates(subset=['Post Link'])
        print(len(domain_posts.index))
        
        # result = domain_posts.columns
        # print(domain_path.dtypes)
        # domain_posts['date'] = pd.to_datetime(domain_posts['CreationDate'], dayfirst=True).dt.strftime("%y/%m/%d %H:%M:%S")
        
        domain_posts['date'] = domain_posts['CreationDate'].str[:4]
        domain_posts = domain_posts[domain_posts["date"].str.contains("/") == False]
        domain_posts['date'] = pd.to_numeric(domain_posts['date'], errors='raise')
        domain_posts.hist(column='date')
        # domain_posts['year']= domain_posts['date'].dt.year
        # print(domain_posts['date'].head(5))
        
        domain_posts.hist('date')
        plt.show()
        
        # check value with index 
        # print(domain_posts.iloc[1528])
    
        print("-------------------- -------------")
        


analyzeFiles('SO_Data')

