# python3 -m venv .venv
# source .venv/bin/activate
# pip install requests

import requests 

url = "https://livingdevops.com"
post_endpoint = "/wp-json/wp/v2/posts"
page_endpoint = "/wp-json/wp/v2/pages"

# response = requests.get(url, timeout=5)
# if response.status_code == 200:
#     print(response)

posts = requests.get(url + post_endpoint)
last_post = posts.json()[-1]
print(last_post.get('link'), last_post.get('title')["rendered"])


# pages = requests.get(url + page_endpoint)
# print(pages.json()[-1].get('link'))

# for page in pages.json():
#     print(f" LINK:{ page.get('link')}")
#     print(f" TITLE:{ page.get('title')["rendered"]}")
#     print("----")