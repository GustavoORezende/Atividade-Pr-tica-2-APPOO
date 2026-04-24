from abc import ABC , abstractmethod
class Emprestimo(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def registrar(self):
        pass

class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario, titulo, prazo):
        super().__init__()
        self.nome_usuario = nome_usuario
        self.titulo = titulo
    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        if nome_usuario == "":
            raise ValueError("nome não pode ser vazio")
        self._nome_usuario = nome_usuario
    @property
    def titulo(self, titulo):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        if titulo == "":
            raise ValueError("titulo não pode ser vazio")
        self._titulo = titulo

    @property
    def prazo(self, prazo):
        return self._prazo

    @prazo.setter
    def prazo(self, prazo):
        if prazo == "":
            raise ValueError("prazo não pode ser vazio")
        self._titulo = prazo


    def registrar(self):
        pass

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, edicao):
        super().__init__()
        self.edicao = edicao

    def registrar(self):
        pass

