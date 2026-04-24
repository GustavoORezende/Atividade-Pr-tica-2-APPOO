from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# ==========================================
# PARTE 1: Classe Abstrata
# ==========================================
class Emprestimo(ABC):
    """
    Classe abstrata que representa um empréstimo genérico.
    """
    @abstractmethod
    def registrar(self, banco_de_dados):
        pass

# ==========================================
# PARTE 2: Subclasse EmprestimoLivro
# ==========================================
class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario, titulo):
        # A atribuição aqui passa automaticamente pelos setters (@property)
        self.nome_usuario = nome_usuario
        self.titulo = titulo
        self._prazo_devolucao = None
        self.tipo = "Livro"

    # --- ENCAPSULAMENTO COM @property ---
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
        if data is not None and not isinstance(data, datetime):
            raise TypeError("Erro de Validação: O prazo de devolução deve ser uma data válida.")
        self._prazo_devolucao = data
    # ------------------------------------

    def verificar_duplicidade(self, banco_de_dados):
        for emp in banco_de_dados:
            if type(emp) is EmprestimoLivro:
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


# ==========================================
# PARTE 3: Subclasse EmprestimoRevista
# ==========================================
class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario, titulo, edicao):
        super().__init__(nome_usuario, titulo)
        self.edicao = edicao
        self.tipo = "Revista"

    # --- ENCAPSULAMENTO COM @property ---
    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, valor):
        valor_str = str(valor).strip()
        if not valor_str:
            raise ValueError("Erro de Validação: A edição da revista não pode ser vazia.")
        self._edicao = valor_str
    # ------------------------------------

    def verificar_duplicidade(self, banco_de_dados):
        for emp in banco_de_dados:
            if type(emp) is EmprestimoRevista:
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


# ==========================================
# PARTE 4: Funções Independentes de Saída
# ==========================================
def listar_emprestimos(banco_de_dados):
    print("\n--- Lista de Empréstimos Cadastrados ---")
    if not banco_de_dados:
        print("Nenhum empréstimo cadastrado.")
    for emp in banco_de_dados:
        print(emp)
    print("----------------------------------------\n")


# ==========================================
# PARTE 5: Área de Testes (Simulando o Uso)
# ==========================================
if __name__ == "__main__":
    banco_de_dados = []

    print("\n=== INICIANDO TESTES VÁLIDOS (CAMINHO FELIZ) ===")
    livro_valido = EmprestimoLivro("Carlos", "Algoritmos: Teoria e Prática")
    revista_valida = EmprestimoRevista("Ana", "Mundo Estranho", "Edição 15")
    
    livro_valido.registrar(banco_de_dados)
    revista_valida.registrar(banco_de_dados)
    
    # Teste de duplicidade intencional (Aviso esperado, não um erro crítico)
    livro_duplicado = EmprestimoLivro("Carlos", "Algoritmos: Teoria e Prática")
    livro_duplicado.registrar(banco_de_dados)


    print("\n=== INICIANDO CASOS DE TESTES ERRADOS (VALIDAÇÕES @PROPERTY) ===")
    
    # Teste de Erro 1: Usuário vazio
    try:
        print("\nTentando criar livro com usuário vazio...")
        livro_erro1 = EmprestimoLivro("   ", "Dom Casmurro")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    # Teste de Erro 2: Título vazio
    try:
        print("\nTentando criar livro com título vazio...")
        livro_erro2 = EmprestimoLivro("Rafael", "")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    # Teste de Erro 3: Edição vazia na revista
    try:
        print("\nTentando criar revista com edição vazia...")
        revista_erro1 = EmprestimoRevista("Gustavo", "Veja", "   ")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    # Teste de Erro 4: Alteração indevida de uma propriedade existente
    try:
        print("\nTentando alterar o nome do usuário 'Carlos' para vazio...")
        livro_valido.nome_usuario = "" 
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    # Teste de Erro 5: Passando um tipo de dado errado (ex: int no lugar de string)
    try:
        print("\nTentando criar livro com número inteiro no lugar do nome...")
        livro_erro3 = EmprestimoLivro(12345, "Harry Potter")
    except ValueError as e:
        print(f"🔴 Bloqueado com sucesso: {e}")

    print("\n=== ESTADO FINAL DO BANCO DE DADOS ===")
    listar_emprestimos(banco_de_dados)