from dataclasses import dataclass, field


@dataclass
class QuoteItem:
    text: str
    author: str
    tags: list[str] = field(default_factory=list)
