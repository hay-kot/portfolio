import datetime
import json
from pathlib import Path
from dateutil import parser

import requests
from jinja2 import Template

CWD = Path(__file__).parent
DEST = CWD.joinpath("dest")

API_KEY = "be6bc60a4d832f5a46d6dec44f"
API_URL = "https://blog.hay-kot.dev/ghost/api/v3/content/posts/"
POST_TEMPLATE = CWD.joinpath("post-template.j2")


def generate_name(post: dict) -> Path:
    timestamp = parser.parse(post.get("created_at"))
    timestamp = timestamp.strftime("%Y-%m-%d")
    post_slug = post.get("slug")
    return DEST.joinpath(f"{timestamp}-{post_slug}.md")


params = (("key", API_KEY),)

response = requests.get(API_URL, params=params)

posts = json.loads(response.text)["posts"]


for post in posts:
    with open(POST_TEMPLATE, "r") as f:
        template = Template(f.read())
    dest = generate_name(post)
    content = template.render(post=post)

    with open(dest, "w") as f:
        f.write(content)
