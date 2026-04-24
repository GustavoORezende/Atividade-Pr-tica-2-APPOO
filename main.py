from abc import ABC , abstractmethod
from pathlib import Path

class Emprestimo(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def registrar(self):
        pass

class EmprestimoLivro(Emprestimo):
    def __init__(self, nome_usuario, titulo):
        super().__init__(nome_usuario)
        self.titulo = titulo

    def to_dict(self):
        return {
           "usuario": self.nome_usuario,
           "tipo": self.titulo
        }
    
    def registrar(self):
        pass

class EmprestimoRevista(EmprestimoLivro):
    def __init__(self, nome_usuario, edicao):
        super().__init__(nome_usuario)
        self.edicao = edicao
    
    def to_dict(self):
        return {
           "usuario": self.nome_usuario,
           "tipo": self.titulo
        }
        

    def registrar(self):
        pass

class BancoDeDados:
    def __init__(self):
        self._emprestimos = []

    def adicionar(self, emprestimo: Emprestimo):
        self._emprestimos.append(emprestimo)

    def salvar(self, nome_arquivo):
        caminho = Path(nome_arquivo)
        conteudo = self.extrair_dados()
        caminho.write_text(conteudo, encoding="utf-8")
        print(f"Arquivo salvo em {caminho.resolve()}")

    def extrair_dados(self) -> str:
        if not self._emprestimos:
            return "Banco Vazio"
        
        linhas =[]

        for emprestimo in self._emprestimos:
            dados = emprestimo.to_dict()
            linha = " | ".join(f"{k}:{v}" for k, v in dados.items())
            linhas.append(linha)

            return "\n".join(linhas)
        

def main():
    emprestimo1 = EmprestimoLivro("Gustavo", "O Samurai")
    emprestimo2 = EmprestimoLivro("Rafel", "O Labubu") 
    emprestimo3 = EmprestimoLivro("Gustavo", "O Samurai")
    emprestimo4 = EmprestimoRevista("Outro Gustavo", "O clone")
    emprestimo5 = EmprestimoRevista("O mesmo Rafael", "Rei do BrainRot")
    emprestimo6 = EmprestimoRevista("Outro Gustavo", "O clone")

    banco = BancoDeDados()

    emprestimos = [emprestimo1,emprestimo2,emprestimo3,emprestimo4,emprestimo5,emprestimo6]

    for emprestimo in emprestimos:
        banco.adicionar(emprestimo) 
        banco.salvar("emprestimos.txt")

main()