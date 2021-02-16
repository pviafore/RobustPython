from dataclasses import dataclass

@dataclass
class Author:
    cookbooks: list[str]

def find_author(name: str):
    return Author([])


def add_authors_cookbooks(author_name: str, cookbooks: list[str] = []) -> bool:
    author = find_author(author_name)
    if author is None:
        assert False, "Author does not exist"
    else:
        for cookbook in author.cookbooks:
            cookbooks.append(cookbook)
        return True
