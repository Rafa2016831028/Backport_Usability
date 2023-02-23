import json
import requests
import csv
import numpy as np
import pandas as pd


def callAPI(output_path = "OutDemo"):
    try:
        req = requests.get("https://api.stackexchange.com/2.3/search?page=1&pagesize=100&order=desc&sort=activity&intitle=backport&site=stackoverflow")
        response = req.json()
        print(response)
        dataResponse = response['items']
        # df = pd.DataFrame(columns =  ["id", "tags", "ownerId", "link", "isAnswered", "answerCount"])
        df = pd.DataFrame(columns =  ["title", "ownerId", "link", "isAnswered", "answerCount"])
        
        for post in dataResponse:
            tags = post['tags']
            owner = post['owner']['user_id']
            title = post['title']
            answerCount = post['answer_count']
            isAnswered = post['is_answered']
            link =post['link']

            list_row = [title, owner, link, answerCount, isAnswered]
            df.loc[len(df)] = list_row

            df.to_csv('Outcome/out.csv')  
    except:
        print("An error occured in fetching data! ")

callAPI()