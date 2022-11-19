def toTime(string):
    tempo = string.split(":")
    hora = int(tempo[0])
    min = int(tempo[1])
    segundos = hora * 3600 + min * 60 + int(tempo[2])
    return segundos

def toMes(string):
    data = string.split("/")
    mes = data[1]
    return mes