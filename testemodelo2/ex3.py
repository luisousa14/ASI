import LerFicheiro
import Calculos
import Listagens
import AlterarInfo

print(LerFicheiro.ler("Alunos"))
print(Calculos.media(LerFicheiro.ler("Alunos")[0]))
print(Listagens.listagem(LerFicheiro.ler("Alunos")[0], LerFicheiro.ler("Alunos")[1]))
AlterarInfo.adicionarDados(LerFicheiro.ler("Alunos")[0])
