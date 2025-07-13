import time
import pulp
import os

def ler_instancia_txt(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]

    m, n, l = map(int, linhas[0].split())
    b = list(map(int, linhas[1].split()))

    p = []
    for i in range(m):
        linha = linhas[2 + i].split()
        linha_formatada = [tuple(map(int, par.split(','))) for par in linha]
        p.append(linha_formatada)

    a = []
    for i in range(m):
        linha = linhas[2 + m + i].split()
        linha_formatada = [tuple(map(int, par.split(','))) for par in linha]
        a.append(linha_formatada)

    return p, b, a

def solve_mgap_global(p, b, a):
    m = len(p)
    n = len(p[0])
    l = 2

    prob = pulp.LpProblem("MGAP_GLOBAL", pulp.LpMaximize)
    x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary") for k in range(l)] for j in range(n)] for i in range(m)]

    prob += pulp.lpSum(p[i][j][k] * x[i][j][k] for i in range(m) for j in range(n) for k in range(l))

    for j in range(n):
        prob += pulp.lpSum(x[i][j][k] for i in range(m) for k in range(l)) == 1

    for i in range(m):
        prob += pulp.lpSum(a[i][j][k] * x[i][j][k] for j in range(n) for k in range(l)) <= b[i]

    start = time.time()
    status = prob.solve()
    elapsed = time.time() - start

    resultado = {
        "status": pulp.LpStatus[status],
        "lucro_total": pulp.value(prob.objective),
        "tempo_segundos": round(elapsed, 4),
        "atribuições": []
    }

    for i in range(m):
        for j in range(n):
            for k in range(l):
                if pulp.value(x[i][j][k]) == 1:
                    resultado["atribuições"].append({
                        "agente": i + 1,
                        "tarefa": j + 1,
                        "nivel": k + 1,
                        "lucro": p[i][j][k],
                        "custo": a[i][j][k]
                    })

    return resultado

def escrever_resultado_txt(resultado, caminho_saida):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(f"Status: {resultado['status']}\n")
        f.write(f"Lucro total: {resultado['lucro_total']}\n")
        f.write(f"Tempo de execução: {resultado['tempo_segundos']}s\n\n")
        f.write("Atribuições:\n")
        for a in resultado["atribuições"]:
            f.write(f"Agente {a['agente']} faz Tarefa {a['tarefa']} no Nível {a['nivel']} (lucro={a['lucro']}, custo={a['custo']})\n")

if __name__ == "__main__":
    pasta_instancias = "../data/"
    pasta_resultados = "../results/"
    os.makedirs(pasta_resultados, exist_ok=True)

    arquivos = sorted([f for f in os.listdir(pasta_instancias) if f.endswith(".txt")])

    for nome_arquivo in arquivos:
        caminho_instancia = os.path.join(pasta_instancias, nome_arquivo)
        nome_saida = nome_arquivo.replace("instancia", "resultado")
        caminho_saida = os.path.join(pasta_resultados, nome_saida)

        p, b, a = ler_instancia_txt(caminho_instancia)
        resultado = solve_mgap_global(p, b, a)
        escrever_resultado_txt(resultado, caminho_saida)
        print(f"Resultado salvo em: {caminho_saida}")
