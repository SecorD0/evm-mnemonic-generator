from typing import Optional


def read_lines(path: str, skip_empty_rows: bool = False, encoding: Optional[str] = None) -> list:
    """
    Read a file and return a list of lines.

    :param str path: path to the file
    :param bool skip_empty_rows: if True it doesn't include empty rows to the list
    :param Optional[str] encoding: the name of the encoding used to decode or encode the file
    :return list: the list of lines
    """
    with open(path, encoding=encoding) as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]
    if skip_empty_rows:
        lines = list(filter(lambda a: a, lines))

    return lines
