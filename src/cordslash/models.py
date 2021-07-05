import datetime
from typing import Union, Any


__all__ = ("User", "Channel", "Mentionable", "Embed")


class User:
    ...


class Channel:
    ...


class Mentionable:
    ...


class Embed:
    def __init__(self, *, title: Any = None,
                 description: Any = None,
                 color: int = 0x000000,
                 timestamp: Union[datetime.datetime, str] = None,
                 url:str = None,
                 type: str = "rich"):
        self.title = str(title) if title else None
        self.description = str(description) if description else None
        self.timestamp = str(timestamp) if timestamp else None
        self.color = color
        self.url = url
        self.fields = []

    def _to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}

    def add_field(self, *, name, value, inline = True):
        to_dict = {"name": name,
                 "value": value,
                 "inline": inline}
        self.fields.append(to_dict)

    def set_author(self, *, name, url = None, icon_url = None):
        self.author = {"name": name}
        if url:
            self.author["url"] = url
        if icon_url:
            self.author["icon_url"] = icon_url

    def set_footer(self, *, text, icon_url = None):
        self.footer = {
            "text": text
        }
        if icon_url:
            self.footer["icon_url"] = icon_url

    def set_image(self, *, url):
        self.image = {
            "url": url}

    def set_thumbnail(self, *, url):
        self.thumbnail = {"url": url}

    def __len__(self):
        length = len(self.title) + len(self.description)
        for field in self.fields:
            length += len(field["name"]) + len(field["value"])
        length += len(self.footer["text"]) + len(self.author["name"]) + len(self.timestamp)
        return length


    def from_dict(self, embed_dict: dict):
        self.fields = embed_dict.get("fields", None)
        self.color = embed_dict.get("color", None)
        self.description = embed_dict.get("description", None)
        self.footer = embed_dict.get("footer", None)
        self.image = embed_dict.get("image", None)
        self.title = embed_dict.get("title", None)
        self.timestamp = embed_dict.get("timestamp", None)
        self.author = embed_dict.get("author", None)
        self.url = embed_dict.get("url", None)
        self.thumbnail = embed_dict.get("thumbnail", None)
        return self

    
# TODO: add functionality


