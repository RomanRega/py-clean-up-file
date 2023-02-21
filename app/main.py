import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: any, exc_val: str, exc_tb: str) -> None:
        os.remove(self.filename)
