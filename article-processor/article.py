import datetime
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from frontmatter import Frontmatter


class MetaData(BaseModel):
    publish: bool
    title: str
    slug: Optional[str]
    path: Optional[str]
    date: Optional[datetime.date]
    summary: str
    reading_time: Optional[str]
    tags: list
    image: str


class Article(BaseModel):
    metadata: MetaData
    content: str
    dest: Optional[Path]

    @classmethod
    def from_file(cls, markdown_file: Path):
        raw_data = Frontmatter.read_file(markdown_file)
        frontmatter = raw_data.get("attributes")
        body = raw_data.get("body")
        return cls(metadata=MetaData(**frontmatter), content=body)
