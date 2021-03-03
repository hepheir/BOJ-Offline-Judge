import os


class units:
    class ms(int):
        pass

    class KB(int):
        pass


def shorten_path(path:os.PathLike):
    common_path = os.path.commonpath([path, os.getcwd()])
    return path.replace(common_path, "")
