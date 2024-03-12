
import abc


class DataLoaderBase(abc.ABC):

    @abc.abstractmethod
    def load_data(self):
        pass


instance_data_loader = DataLoaderBase()


class JsonDataLoader(DataLoaderBase):

    def load_data(self):
        pass

json_loader = JsonDataLoader()

