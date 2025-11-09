import requests
from requests.auth import HTTPBasicAuth



# /wp-json/wp/v2/posts
# /wp-json/wp/v2/posts/{id}
url = "https://livingdevops.com"
your_username  = 'livingdevops'
your_password = 'application password here'

# posts = requests.get(url + "/wp-json/wp/v2/posts")
# page = 1
# per_page = 1
# response = requests.get(url + "/wp-json/wp/v2/posts", params={"page": page, "per_page": per_page})

# print(response.json())
# for post in response.json():
#     print(f" LINK:{ post.get('link')}")
#     print(f" TITLE:{ post.get('title')['rendered']}")
#     print("----")

def list_posts(page=1, per_page=5):
    response = requests.get(url + "/wp-json/wp/v2/posts", params={"page": page, "per_page": per_page})
    for post in response.json():
        print(f" LINK:{ post.get('link')}")
        print(f" ID:{ post.get('id')}")
        print(f" TITLE:{ post.get('title')['rendered']}")
        print("----")

def get_post(post_id):
    response = requests.get(url + f"/wp-json/wp/v2/posts/{post_id}")
    post = response.json()
    print(f" LINK:{ post.get('link')}")
    print(f" TITLE:{ post.get('title')['rendered']}")
    print(f" CONTENT:{ post.get('content')['rendered']}")
    print("----")

def create_post(title, content, status="draft"):
    data = {
        "title": title,
        "content": content,
        "status": status
    }
    response = requests.post(
        url + "/wp-json/wp/v2/posts",
        json=data,
        auth=HTTPBasicAuth(your_username, your_password)
    )
    print(response.json())


def update_post(post_id, title=None, content=None, status=None):
    data = {}
    if title:
        data["title"] = title
    if content:
        data["content"] = content
    if status:
        data["status"] = status

    response = requests.post(
        url + f"/wp-json/wp/v2/posts/{post_id}",
        json=data,
        auth=HTTPBasicAuth(your_username, your_password)
    )
    print(response.json())

def delete_post(post_id, force=True):
    response = requests.delete(
        url + f"/wp-json/wp/v2/posts/{post_id}",
        params={"force": str(force).lower()},
        auth=HTTPBasicAuth(your_username, your_password)
    )
    print(response.json())

def patch_post_title(post_id, title):
    data = {"title": title}
    response = requests.patch(
        url + f"/wp-json/wp/v2/posts/{post_id}",
        json=data,
        auth=HTTPBasicAuth(your_username, your_password)
    )
    print(response.json())
# create_post("title", "content", status="draft") -> 1774

# create_post("Testing api post creation", " this is a crud demo for my python bootcamp", status="private")
# get_post(1775)
# post_to_update = 1775
# update_post(post_to_update, title= "this is updating the post from patch method")


# post_to_delete = 1774
# delete_post(post_to_delete)

username = 'akhileshmishrabiz'
PAT = 'Your pat token here'
def list_github_public_repos(username):
    github_api_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(github_api_url, params={"type": "public"})
    repos = response.json()
    for repo in repos:
        print(f"Name: {repo['name']}, URL: {repo['html_url']}")

def create_github_repo(repo_name, description="", private=False, token=""):
    github_api_url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private
    }
    response = requests.post(github_api_url, json=data, headers=headers)
    print(response.json())

# list_github_public_repos(username)
# create_github_repo("dumdum", description="dumdum repo", private=False, token=PAT)

def delete_github_repo(repo_name, token=""):
    github_api_url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(github_api_url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    else:
        print(f"Failed to delete repository '{repo_name}'. Status code: {response.status_code}")
        print(response.json())
delete_github_repo("dumdum", token=PAT)