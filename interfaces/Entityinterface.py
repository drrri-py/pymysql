from abc import ABC, abstractmethod

class EntityInterface(ABC):
    @abstractmethod
    def all(self):
        pass
    
    @abstractmethod
    def store(self, obj):
        pass
    
    @abstractmethod
    def find(self, obj_id):
        pass
    
    @abstractmethod
    def update(self, obj_id, obj):
        pass
    
    @abstractmethod
    def delete(self, obj_id):
        pass
