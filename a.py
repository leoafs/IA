import re
def tamanhoItens(l):
    return sum([ len(x) for x in l] )
lead_re = re.compile(r'(^\s+)(.*)$')
def alinhaTexto(texto, larguraLinha, ultimaLinhaParagrafo=0):
    m = lead_re.match(texto)     # detect and save leading whitespace
    if m is None:
        esquerda, direita, largura = '', texto, larguraLinha
    else:
        esquerda, direita, largura = m.group(1), m.group(2), larguraLinha - len(m.group(1))
    itens = direita.split()
    for i in range(len(itens) - 1): # add required space to each words, exclude last item
        itens[i] += ' '
    if not ultimaLinhaParagrafo: # number of spaces to add
        ContaEsquerda = largura - tamanhoItens(itens)
        while ContaEsquerda > 0 and len(itens) > 1:
            for i in range(len(itens) - 1):
                itens[i] += ' '
                ContaEsquerda -= 1
                if ContaEsquerda < 1:  
                    break
    resultado = esquerda + ''.join(itens)
    return resultado
def justificar(texto, larguraLinha):
    palavras = texto.split()
    totalPalavras = len(palavras)
    espacoVazio = [[0] * totalPalavras for i in range(totalPalavras)]
    for i in range(totalPalavras):
        espacoVazio[i][i] = larguraLinha - len(palavras[i])
        for j in range(i + 1, totalPalavras):
            espacoVazio[i][j] = espacoVazio[i][j - 1] - len(palavras[j]) - 1
    minima = [0] + [10 ** 20] * totalPalavras
    quebras = [0] * totalPalavras
    for j in range(totalPalavras):
        i = j
        while i >= 0:
            if espacoVazio[i][j] < 0:
                custo = 10 ** 10
            else:
                custo = minima[i] + espacoVazio[i][j] ** 2
            if minima[j + 1] > custo:
                minima[j + 1] = custo
                quebras[j] = i
            i -= 1
    linhas = []
    j = totalPalavras
    while j > 0:
        i = quebras[j - 1]
        linhas.append(' '.join(palavras[i:j]))
        j = i
    linhas.reverse()
    for linha in linhas:
        print (alinhaTexto(linha, larguraLinha, ultimaLinhaParagrafo=0))
A = int(input());
while A != 0:
    B = input().split(" ");
    C = [];
    result = "";
    while B[0] != '':
        C.extend(B);
        B = input().split(" ");
    for i in range(len(C)):
        result += str(C[i]) + " "
    print (justificar(result, A))
    A = int(input());
