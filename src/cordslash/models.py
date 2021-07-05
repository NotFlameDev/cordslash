from __future__ import annotations


import datetime
from typing import Any, Optional, Union, List, Dict, Type

__all__ = ("User", "Channel", "Mentionable", "Embed")


class User:
    ...


class Channel:
    ...


class Mentionable:
    ...


class Embed:
    def __init__(
        self,
        *,
        title: Optional[Any] = None,
        description: Optional[Any] = None,
        colour: int = 0x000000,
        timestamp: Optional[Union[datetime.datetime, str]] = None,
        url: Optional[str] = None,
        type: str = "rich"
    ):
        self.title = str(title) if title else None
        self.description = str(description) if description else None
        self.timestamp = str(timestamp) if timestamp else None
        self.fields: List[Dict[str, Union[str, int]]] = []
        self.colour = colour
        self.url = url
        self.type = type

    def _to_dict(self: Embed) -> dict:
        return {key: value for key, value in self.__dict__.items() if value is not None}

    def add_field(self: Embed, *, name: str, value: str, inline: bool = True) -> Embed:
        payload = {"name": name, "value": value, "inline": inline}
        self.fields.append(payload)
        
        return self

    def set_author(self: Embed, *, name: str, url: str=None, icon_url: str=None) -> Embed:
        self.author = {"name": name}
        if url:
            self.author["url"] = url
        if icon_url:
            self.author["icon_url"] = icon_url

        return self

    def set_footer(self: Embed, *, text: str, icon_url: str=None) -> Embed:
        self.footer = {"text": text}
        if icon_url:
            self.footer["icon_url"] = icon_url

        return self

    def set_image(self: Embed, *, url: str) -> Embed:
        self.image = {"url": url}
        
        return self

    def set_thumbnail(self: Embed, *, url: str) -> Embed:
        self.thumbnail = {"url": url}

        return self

    def __len__(self: Embed) -> int:
        length = len(self.title) + len(self.description)
        for field in self.fields:
            length += len(field["name"]) + len(field["value"])
        length += (
            len(self.footer["text"]) + len(self.author["name"]) + len(self.timestamp)
        )

        return length

    @classmethod
    def from_dict(
        cls: Type[Embed],
        embed_dict: Dict[str, Union[List[Dict[str, Union[str, int]]], str, int]],
    ) -> Embed:
        self: Embed = cls.__new__(cls)
        
        self.fields = embed_dict.get("fields", None)
        self.colour = embed_dict.get("colour", None)
        self.description = embed_dict.get("description", None)
        self.footer = embed_dict.get("footer", None)
        self.image = embed_dict.get("image", None)
        self.title = embed_dict.get("title", None)
        self.timestamp = embed_dict.get("timestamp", None)
        self.author = embed_dict.get("author", None)
        self.url = embed_dict.get("url", None)
        self.thumbnail = embed_dict.get("thumbnail", None)

        return self