import funcoes

def TIMEURLmaisVisitado(url):
    duracaoUrl = {}
    for key, value in url.items():
        for key1, value1 in value.items():
            for posicao in value1:
                if key in duracaoUrl.keys():
                    duracaoUrl[key] += funcoes.toTime((posicao[1]))
                else:
                    duracaoUrl[key] = funcoes.toTime((posicao[1]))

    return duracaoUrl


def URLmaisVisitado(url):
    numVisitasURL = {}
    for key, value in url.items():
        for key1, value1 in value.items():
            for posicao in value1:
                if key in numVisitasURL.keys():
                    numVisitasURL[key] += 1
                else:
                    numVisitasURL[key] = 1

    return numVisitasURL


def MESmaisVisitado(url):
    mesMaisVisitado = {}
    for key, value in url.items():
        for key1, value1 in value.items():
            num_vistas = len(value1)
            if funcoes.toMes(key1) in mesMaisVisitado.keys():
                mesMaisVisitado[funcoes.toMes(key1)] += num_vistas
            else:
                mesMaisVisitado[funcoes.toMes(key1)] = num_vistas

    return mesMaisVisitado