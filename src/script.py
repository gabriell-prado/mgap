import json
import time
import pulp

# ------------------------
# Função para resolver o MGAP global (nível escolhido por tarefa)
# ------------------------
def solve_mgap_global(p, b, c):
    m = len(p)         # número de agentes
    n = len(p[0])      # número de tarefas
    l = 2              # níveis

    prob = pulp.LpProblem("MGAP_GLOBAL", pulp.LpMaximize)

    # x[i][j][k] = 1 se agente i faz tarefa j no nível k
    x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary") for k in range(l)] for j in range(n)] for i in range(m)]

    # Função objetivo
    prob += pulp.lpSum(p[i][j][k] * x[i][j][k] for i in range(m) for j in range(n) for k in range(l))

    # Restrição: cada tarefa deve ser atribuída uma única vez (a algum agente e nível)
    for j in range(n):
        prob += pulp.lpSum(x[i][j][k] for i in range(m) for k in range(l)) == 1

    # Restrição: limite de capacidade por agente
    for i in range(m):
        prob += pulp.lpSum(c[i][j][k] * x[i][j][k] for j in range(n) for k in range(l)) <= b[i]

    # Resolver
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
                        "custo": c[i][j][k]
                    })

    return resultado

# ------------------------
# Executar para todas as instâncias
# ------------------------
def executar_experimentos(json_path, saida_path):
    with open(json_path, "r", encoding="utf-8") as f:
        instancias = json.load(f)

    resultados_finais = []

    for instancia in instancias:
        print(f"\n=== {instancia['nome']} ===")
        resultado = solve_mgap_global(instancia["p"], instancia["b"], instancia["c"])
        resultado_final = {
            "instancia": instancia["nome"],
            **resultado
        }
        resultados_finais.append(resultado_final)

        # Também exibe no terminal
        print(f"Status: {resultado['status']}")
        print(f"Lucro total: {resultado['lucro_total']}")
        print(f"Tempo: {resultado['tempo_segundos']}s")
        for atrib in resultado["atribuições"]:
            print(f"Agente {atrib['agente']} faz Tarefa {atrib['tarefa']} no Nível {atrib['nivel']} (lucro={atrib['lucro']}, custo={atrib['custo']})")

    # Salvar resultados
    with open(saida_path, "w", encoding="utf-8") as f:
        json.dump(resultados_finais, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Resultados salvos em: {saida_path}")

# ------------------------
# Rodar
# ------------------------
if __name__ == "__main__":
    executar_experimentos("../data/instances.json", "../results/resultados_globais.json")
