import Leitura
import Stats

print(Leitura.ler("dados.txt"))

print(Stats.TIMEURLmaisVisitado(Leitura.ler("dados.txt")))
print(Stats.URLmaisVisitado(Leitura.ler("dados.txt")))
print(Stats.MESmaisVisitado(Leitura.ler("dados.txt")))