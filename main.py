from abc import ABC , abstractmethod

class Emprestimo(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def registrar(self):
        pass

class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario, titulo):
        super().__init__()
        self.nome_usuario = nome_usuario
        self.titulo = titulo

    def registrar(self):
        pass

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, edicao):
        super().__init__()
        self.edicao = edicao

    def registrar(self):
        pass

