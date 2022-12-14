"""Static descriptors are relatively pointless.  Descriptors tend to run computations
rather than. Let's build a descriptor that constantly computes the files in a given
directory when asked.  Without thinking too much you may think this is kind of the
point of a property in a class,  @property() IS-A descriptor remember.

Hypothetically, lets assume a folder exists on disk /tmp/files (
"""
from pathlib import Path
import os
import shutil


class FolderFiles:

    def __get__(self, obj, objtype=None):
        return [str(p) for p in Path(obj.path).iterdir()]

class Directory:

    files = FolderFiles()

    def __init__(self, path: str) -> None:
        self.path = path


def main():
    """Tests:
    Create two files on disk in /tmp/files/*
    Note: This is UNIX specific with separators etc.
    >>> os.makedirs("/tmp/files/", exist_ok=True)
    >>> open("/tmp/files/one.txt", "w+")
    <...
    >>> open("/tmp/files/two.log", "w+")
    <...
    >>> d = Directory("/tmp/files/")
    >>> d.files
    ['/tmp/files/one.txt', '/tmp/files/two.log']
    >>> os.remove("/tmp/files/two.log")
    >>> d.files
    ['/tmp/files/one.txt']
    >>> shutil.rmtree("/tmp/files")
    ...
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)