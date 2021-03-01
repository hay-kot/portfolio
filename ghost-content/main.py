import json
from pathlib import Path

import requests
from dateutil import parser
from jinja2 import Template
from markdownify import markdownify as md

CWD = Path(__file__).parent
DEST = CWD.joinpath("dest")

API_KEY = ""
API_URL = ""
POST_TEMPLATE = CWD.joinpath("post-template.j2")


def generate_name(post: dict) -> Path:
    timestamp = parser.parse(post.get("created_at"))
    timestamp = timestamp.strftime("%Y-%m-%d")
    post_slug = post.get("slug")
    return DEST.joinpath(f"{timestamp}-{post_slug}.md")


def process_html(html: str) -> str:
    return md(html)


params = (("key", API_KEY),)

response = requests.get(API_URL, params=params)

posts = json.loads(response.text)["posts"]


for post in posts:
    with open(POST_TEMPLATE, "r") as f:
        template = Template(f.read())

    post["html"] = process_html(post["html"])
    dest = generate_name(post)
    content = template.render(post=post)

    with open(dest, "w") as f:
        f.write(content)
