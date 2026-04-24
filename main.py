from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Emprestimo(ABC):
    @abstractmethod
    def registrar(self, banco_de_dados):
        pass

class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario, titulo):
        self.nome_usuario = nome_usuario
        self.titulo = titulo
        self._prazo_devolucao = None
        self.tipo = "Livro"

    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Erro de Validação: O nome do usuário não pode ser vazio.")
        self._nome_usuario = valor.strip()

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Erro de Validação: O título do livro não pode ser vazio.")
        self._titulo = valor.strip()

    @property
    def prazo_devolucao(self):
        return self._prazo_devolucao

    @prazo_devolucao.setter
    def prazo_devolucao(self, data):
        if data is not None:
            if not isinstance(data, datetime):
                raise TypeError("Erro de Validação: O prazo de devolução deve ser uma data válida.")
            
            if data < datetime.now():
                raise ValueError("Erro de Validação: O prazo de devolução não pode ser uma data no passado.")
            
        self._prazo_devolucao = data

    def verificar_duplicidade(self, banco_de_dados):
        if not isinstance(banco_de_dados, list):
            raise TypeError("Erro Crítico: O banco de dados fornecido deve ser uma lista.")

        for emp in banco_de_dados:
            if isinstance(emp, EmprestimoLivro) and not isinstance(emp, EmprestimoRevista):
                if emp.nome_usuario == self.nome_usuario and emp.titulo == self.titulo:
                    return True
        return False

    def registrar(self, banco_de_dados):
        if self.verificar_duplicidade(banco_de_dados):
            print(f"Aviso: O empréstimo do livro '{self.titulo}' para '{self.nome_usuario}' já está cadastrado.")
        else:
            self.prazo_devolucao = datetime.now() + timedelta(days=7)
            banco_de_dados.append(self)
            print(f"Sucesso: Empréstimo do livro '{self.titulo}' registrado para '{self.nome_usuario}'.")

    def __str__(self):
        prazo_str = self.prazo_devolucao.strftime("%d/%m/%Y") if self.prazo_devolucao else "N/A"
        return f"[{self.tipo}] Usuário: {self.nome_usuario} | Título: {self.titulo} | Prazo: {prazo_str}"


class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario, titulo, edicao):
        super().__init__(nome_usuario, titulo)
        self.edicao = edicao
        self.tipo = "Revista"

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, valor):
        valor_str = str(valor).strip()
        if not valor_str:
            raise ValueError("Erro de Validação: A edição da revista não pode ser vazia.")
        self._edicao = valor_str

    def verificar_duplicidade(self, banco_de_dados):
        if not isinstance(banco_de_dados, list):
            raise TypeError("Erro Crítico: O banco de dados fornecido deve ser uma lista.")

        for emp in banco_de_dados:
            if isinstance(emp, EmprestimoRevista):
                if emp.nome_usuario == self.nome_usuario and emp.titulo == self.titulo and emp.edicao == self.edicao:
                    return True
        return False

    def registrar(self, banco_de_dados):
        if self.verificar_duplicidade(banco_de_dados):
            print(f"Aviso: O empréstimo da revista '{self.titulo}', edição '{self.edicao}' para '{self.nome_usuario}' já está cadastrado.")
        else:
            self.prazo_devolucao = datetime.now() + timedelta(days=2)
            banco_de_dados.append(self)
            print(f"Sucesso: Empréstimo da revista '{self.titulo}' (Ed. {self.edicao}) registrado para '{self.nome_usuario}'.")

    def __str__(self):
        prazo_str = self.prazo_devolucao.strftime("%d/%m/%Y") if self.prazo_devolucao else "N/A"
        return f"[{self.tipo}] Usuário: {self.nome_usuario} | Título: {self.titulo} | Edição: {self.edicao} | Prazo: {prazo_str}"


def listar_emprestimos(banco_de_dados):

    if not isinstance(banco_de_dados, list):
        print("\nErro: O banco de dados fornecido é inválido.")
        return

    print("\n--- Lista de Empréstimos Cadastrados ---")
    if not banco_de_dados:
        print("Nenhum empréstimo cadastrado.")
    for emp in banco_de_dados:
        print(emp)
    print("----------------------------------------\n")


if __name__ == "__main__":
    banco_de_dados = []

    print("\n=== INICIANDO TESTES VÁLIDOS (CAMINHO FELIZ) ===")
    livro_valido = EmprestimoLivro("Carlos", "Algoritmos: Teoria e Prática")
    revista_valida = EmprestimoRevista("Ana", "Mundo Estranho", "Edição 15")
    
    livro_valido.registrar(banco_de_dados)
    revista_valida.registrar(banco_de_dados)
    
    livro_duplicado = EmprestimoLivro("Carlos", "Algoritmos: Teoria e Prática")
    livro_duplicado.registrar(banco_de_dados)

    print("\n=== INICIANDO CASOS DE TESTES ERRADOS (VALIDAÇÕES @PROPERTY) ===")
    
    try:
        print("\nTentando criar livro com usuário vazio...")
        livro_erro1 = EmprestimoLivro("   ", "Dom Casmurro")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    try:
        print("\nTentando criar revista com edição vazia...")
        revista_erro1 = EmprestimoRevista("Gustavo", "Veja", "   ")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    try:
        print("\nTentando registrar um livro em um banco de dados inválido (uma string)...")
        banco_falso = "Isso não é uma lista"
        livro_erro_bd = EmprestimoLivro("João", "Senhor dos Anéis")
        livro_erro_bd.registrar(banco_falso)
    except TypeError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")
    try:
        print("\nTentando definir manualmente um prazo de devolução no passado...")
        livro_valido.prazo_devolucao = datetime(2020, 1, 1)
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    print("\n=== ESTADO FINAL DO BANCO DE DADOS ===")
    listar_emprestimos(banco_de_dados)