# Python-HTTP-API-
Sending a GET request to the site https://jsonplaceholder.typicode.com / , which has access to the database of users, posts, comments, etc. Next, the count for each user of the number of posts left and the number of comments left. And uploading to the site https://webhook .site in the form of a POST request, a JSON file of the following context:

{
"statistics": [
{
"id": 1,
"username": "lolkek",
"email": "user1@mail.dot",
"posts": 125,
"comments": 1358
},
{
"id": 2,
"username": "cheburek",
"email": "user2@mail.dot",
"posts": 5,
"comments": 12
}
]
}

To automatically verify the correctness of the solution, we will need a pickle of the request response object. We get it by executing the following code:

response = request.post(.....)
with open("rest_api_req.pickle", 'wb') as f:
pickle.dump(response, f)
