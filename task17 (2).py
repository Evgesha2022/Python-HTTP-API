import requests
import json
import shutil
import pickle

BASE_URL = "https://webhook.site/f24f46e7-cf2d-4360-adf1-4599fbb2ea8f"

def get_json_coments(url, ):
    r = requests.get(url, stream=True)
    with open("comments.json", 'wb') as f:
             r.raw.decode_content = True
             shutil.copyfileobj(r.raw, f)
    f = open("comments.json")
    ds =json.loads(f.read()) 
    return ds
def get_json_posts(url, ):
    r = requests.get(url, stream=True)
    with open("posts.json", 'wb') as f:
             r.raw.decode_content = True
             shutil.copyfileobj(r.raw, f)
    f = open("posts.json")
    ds =json.loads(f.read()) 
    return ds
def get_json_users(url, ):
    r = requests.get(url, stream=True)
    with open("users.json", 'wb') as f:
             r.raw.decode_content = True
             shutil.copyfileobj(r.raw, f)
    f = open("users.json")
    ds =json.loads(f.read()) 
    return ds
statistics =[]
       
def find_comm():
        comm=[]
        counter=0
        for j in users:
            for i in com:
                    if(j["name"]==i["name"]):
                        counter+=1
            comm.append(counter)
            counter=0
        return comm
def find_posts():
        arrposts = []
        counter=0
        for j in users:
            for i in posts:
                      if(j["id"]==i["userId"]):
                             counter+=1
            arrposts.append(counter)
            counter=0
        return arrposts
def create_json():
        nls = []
        i=0
        for j in users:
              ls = {"id": j["id"],"username": j["username"],"email": j["email"],"posts": arrposts[i] , "comments": arrcomm[i]}
              
              #i+=1
              nls.append(ls)
        ans = {"statistics":nls}
        return ans


    
com = get_json_coments("https://jsonplaceholder.typicode.com/comments")
posts = get_json_posts("https://jsonplaceholder.typicode.com/posts")
users = get_json_users("https://jsonplaceholder.typicode.com/users")
arrposts = find_posts()
arrcomm = find_comm()

response = requests.post(BASE_URL, json.dumps(create_json(), sort_keys=False, indent=4) )
with open("task17.pickle", 'wb') as f:
        pickle.dump(response, f)

