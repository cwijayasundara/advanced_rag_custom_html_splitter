import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


""" write a function to load a file from the disk. File name is passed as a parameter."""


def load_file(filename: str) -> str:
    """Loads a file from the disk."""
    with open(filename, "r") as file:
        return file.read()
