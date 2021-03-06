from . import ExporterModel
from . import FEM_model
from . import RuntimeModel


class FEM(ExporterModel.Module):
    def __init__(self, name=None):
        if not name:
            name = self.__class__.__name__
        super(FEM, self).__init__(name, visible=True)
        self.model = FEM_model

    def set_runtime_hooks(self):
        pass