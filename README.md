# Backport_Usability
This project aims to investigate the usability aspect of Backport scheme in the popular version control system Github project

# Use These commands in the terminal
- pip install PyGithub

# Stack Exchange
 - Search posts with 'backport' word in Title or body
 ```
SELECT Id, CreationDate,
       Score, ViewCount, Tags, Title,Body, CommentCount,OwnerUserId
       AnswerCount, FavoriteCount
  FROM posts
 WHERE Title Like '%backport%';

```