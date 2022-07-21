# Exercise 1
# Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
# Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface
from abc import ABC
from abc import abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def serialization(self):
        pass

    @abstractmethod
    def deserialization(self):
        pass


class SerializationToJSON(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def serialization(self):
        import json
        self.data = json.dumps(self.data)
        return self.data

    def deserialization(self):
        import json
        self.data = json.loads(self.data)
        return self.data


class SerializationToBin(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def serialization(self):
        import pickle
        self.data = pickle.dumps(self.data)
        return self.data

    def deserialization(self):
        import pickle
        self.data = pickle.loads(self.data)
        return self.data
