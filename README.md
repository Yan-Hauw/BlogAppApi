# Travel-Blog-Api

Built using Django Rest Framework (DRF) using default SQLite 3 database. Unless the request sent by frontend follows below specifications, an automated HTTP response with error message is returned by DRF

### Blog post field types and details:

id: automatically set to be 1 greater than the greatest id of an object that was **previously created** <br>
author_name: cannot be empty string, max length 100 characters <br>
title: cannot be empty string, max length 50 characters <br>
content: cannot be empty string, no restriction on max length, limitation of SQLite 3 database <br>
created_at: django automatically initializes this to be the time at which request is sent

### Base URL

base-url: https://travel-blog-api-778.herokuapp.com

## Create a blog post

method: POST <br>
endpoint: /api/create/ <br>
required data as below:

### Sample request and response object

```
Request
POST /api/create/

{
    "author_name": "Yan",
    "title": "test post",
    "content": "asdfjansdg",
}

Response
{
    "id": 9, // largest id previously created was 8
    "author_name": "Yan",
    "title": "test post",
    "content": "asdfjansdg",
    "created_at": "2021-12-18T02:04:12.695260Z"
}
```

No need to put id and created_at field in request, automatically created

## Get all blog posts

method: GET <br>
endpoint: /api/ <br>
No data required

### Sample response object

```
Request
GET /api/

Response
[
    {
        "id": 1,
        "author_name": "Yan",
        "title": "First post by Yan: Starting MapHacks Hackathon",
        "content": "Let's get some stuff done!",
        "created_at": "2021-12-17T20:25:02.906377Z"
    },
    {
        "id": 9,
        "author_name": "Yan",
        "title": "test post",
        "content": "asdfjansdg",
        "created_at": "2021-12-18T02:04:12.695260Z"
    }
]
```

## Get specific blog post

method: GET <br>
endpoint: /api/{$id}/ <br>
Must specify id of post to get in endpoint url

### Sample request and response object

```
Request
GET /api/9/

Response
{
    "id": 9, // largest id previously created was 8
    "author_name": "Yan",
    "title": "test post",
    "content": "asdfjansdg",
    "created_at": "2021-12-18T02:04:12.695260Z"
}
```

## Delete specific blog post

method: DELETE <br>
endpoint: /api/delete/{$id}/ <br>
Must specify id of post to delete in endpoint url

### Sample request and response object

```
Request
DELETE /api/delete/10/

Response
reponse object is empty if delete succeeds
```
