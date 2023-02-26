import os


def touch(path: str, file: bool = False) -> bool:
    """
    Create an object (file or directory) if it doesn't exist.

    :param str path: path to the object
    :param bool file: is it a file?
    :return bool: True if the object was created
    """
    if file:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
            return True

        return False

    if not os.path.isdir(path):
        os.mkdir(path)
        return True

    return False
