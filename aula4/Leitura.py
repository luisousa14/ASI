def ler(nomeFicheiro):
    url = {}

    with open(nomeFicheiro) as fp:
        for linha in fp:
            linha = linha.strip().split(";")
            if linha[0] in url.keys():
                visitas = url[linha[0]]
                detalhes_visitas = (linha[2], linha[3])
                if linha[1] in visitas.keys():
                    visitas[linha[1]].append(detalhes_visitas)
                else:
                    visitas[linha[1]] = [detalhes_visitas]
            else:
                visitas = {}
                detalhes_visitas = (linha[2], linha[3])
                visitas[linha[1]] = [detalhes_visitas]
                url[linha[0]] = visitas

    fp.close()
    return url

