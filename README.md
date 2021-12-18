# Travel-Blog-Api

Built using Django Rest Framework (DRF) using default SQLite 3 database. Unless the request sent by frontend follows below specifications, an automated HTTP response with error message is returned by DRF

### Blog post field types and details:

id: automatically set to be 1 greater than id of object with greatest id in database.
author_name: cannot be empty string, max length 100 characters
title: cannot be empty string, max length 50 characters
content: cannot be empty string, no restriction on max length, limitation of SQLite 3 database
created_at: django automatically initializes this to be the time at which request is sent

### Base URL

WIll provide once Django API successfully hosted

## Create a blog post

method: POST
endpoint: /api/create/
required data as below:

### Sample request object

```
{
  "author_name": "Yan H",
  "title": "test post",
  "content": "yay"
}
```

No need to put id and created_at field in request, automatically created

## Get all blog posts

method: GET
endpoint: /api/
No data required

## Get specific blog post

method: GET
endpoint: /api/{$id}/
Must specify id of post to get

## Delete specific blog post

method: DELETE
endpoint: /api/{$id}/
Must specify id of post to delete
