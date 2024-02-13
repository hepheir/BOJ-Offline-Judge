import os
import pathlib
import shelve


DATABASE_DIR = pathlib.Path(__file__).parent / 'cache'


class Database(shelve.DbfilenameShelf):
    def __init__(self, name: str):
        self.__file__ = DATABASE_DIR / name
        self._create_file()

    def _create_file(self):
        os.makedirs(self.__file__.parent, exist_ok=True)
        shelve.DbfilenameShelf.__init__(self, self.__file__, writeback=True)

    def _delete_file(self):
        self.close()
        os.remove(self.__file__)



def _hard_reset():
    os.removedirs(DATABASE_DIR)
