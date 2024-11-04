

from abc import ABC


class IQuerySource(ABC):

    def get_source_data(self, id):
        raise NotImplementedError