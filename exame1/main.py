import LerFicheiro
import Calculo

vendas = LerFicheiro.ler("livros")

print(vendas)
print(Calculo.vendasMes(vendas))
print(Calculo.vendasLivro(vendas))
print(Calculo.livroAlancar(vendas))