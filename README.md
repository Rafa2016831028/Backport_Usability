# Backport_Usability
This project aims to investigate the usability aspect of Backport scheme in the popular version control system Github project

# Use These commands in the terminal
- pip install PyGithub

# Stack Exchange
 - Search posts with 'backport' word in Title or body
 - [Link of website](https://data.stackexchange.com/stackoverflow/query/new)

 ```
SELECT Id as [Post Link], owneruserid as [User Link], CreationDate,
       Score, ViewCount, Tags, Title,Body, CommentCount,OwnerUserId
       AnswerCount, FavoriteCount
  FROM posts
 WHERE Title Like '%backport%';
```

 ```
SELECT Id as [Post Link], owneruserid as [User Link], CreationDate,
       Score, ViewCount, Tags, Title,Body, CommentCount,OwnerUserId
       AnswerCount, FavoriteCount
  FROM posts
 WHERE Title Like '%backport%' or Tags like '%backport%';
 ```

 ```
SELECT Id as [Post Link], owneruserid as [User Link], CreationDate,
       Score, ViewCount, Tags, Title,Body, CommentCount,OwnerUserId
       AnswerCount, FavoriteCount
  FROM posts
 WHERE Title Like '%cherry-pick%' or Body Like '%cherry-pick%';

 ```