import shutil
from datetime import datetime
from pathlib import Path

from jinja2 import Template
from slugify import slugify

from article import Article

CWD = Path(__file__).parent
DRAFTS = CWD.parent.joinpath("drafts")
POST_TEMPLATE = CWD.joinpath("post-template.j2")

# Destionations in Nuxt
SITE = CWD.parent.joinpath("site")
PUBLISHED_DIR = SITE.joinpath("content")
ASSET_DIR = SITE.joinpath("static")

WPM = 300
WORD_LENGTH = 5


def estimate_reading_time(text):
    total_words = 0
    for current_text in text:
        total_words += len(current_text) / WORD_LENGTH
    total_time = round((total_words / WPM))
    return f"{total_time} Minute Read"


def set_destination(article: Article) -> Path:
    timestamp = article.metadata.date.strftime("%Y-%m-%d")
    post_slug = article.metadata.slug
    return PUBLISHED_DIR.joinpath(f"{timestamp}-{post_slug}.md")


def write_metadata(article: Article):
    article.metadata.reading_time = estimate_reading_time(article.content)
    slug = slugify(article.metadata.title)
    article.metadata.slug = slug
    image = article.metadata.image.removeprefix("./")
    article.metadata.image = f"/{slug}/{image}"
    article.metadata.path = f"/{slug}"
    article.metadata.date = datetime.now()

    return article


def write_article(article: Article):
    with open(POST_TEMPLATE, "r") as f:
        template = Template(f.read())

    content = template.render(article=article.dict())

    with open(article.dest, "w") as f:
        f.write(content)


def set_assett_reference(article: Article, file_name):
    article.content = article.content.replace(
        f"./{file_name}", f"/{article.metadata.slug}/{file_name}"
    )
    return article.content


def copy_assets(article: Article, src: Path):
    dest = ASSET_DIR.joinpath(article.metadata.slug)
    dest.mkdir(parents=True, exist_ok=True)
    for file in src.glob("*.*"):
        if file.suffix != ".md":
            article.content = set_assett_reference(article, file.name)
            shutil.copy(file, dest)


def publish_article(article: Article, folder: Path):
    article = write_metadata(article)
    article.dest = set_destination(article)

    copy_assets(article, folder)  # Sets References

    write_article(article)  # Dumps Article Content


if __name__ == "__main__":
    print("--- Starting Publishing Articles ---")
    print("\n")

    for draft in DRAFTS.iterdir():
        if draft.name == "template":
            continue
        if draft.joinpath("draft.md").exists() == True:
            article = Article.from_file(draft.joinpath("draft.md"))
            if article.metadata.publish:
                publish_article(article, draft)
                print(f"Publishing: {article.metadata.title}")
            else:
                print(f"Not Ready To Publish: {article.metadata.title}")

    print("\n")
    print("--- Articles Published ---")
