# 🔧 MGAP – Programação Linear Inteira para o Problema de Atribuição Generalizada Multinível

![banner](https://img.shields.io/badge/Sistema-Seguro%20e%20Centralizado-blue.svg)
![status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)
![licença](https://img.shields.io/badge/Licença-MIT-green.svg)

Este repositório contém a implementação de um modelo de **Programação Linear Inteira (PLI)** para resolver o **Problema de Atribuição Generalizada Multinível (MGAP)**, um problema clássico e desafiador da área de otimização combinatória.

## 📚 Sobre o Problema

O **MGAP (Multilevel Generalized Assignment Problem)** é uma extensão do problema de atribuição onde:

- Cada tarefa pode ser atribuída a um agente em **diferentes níveis de eficiência**, com impacto no consumo de recursos e no lucro obtido.
- Cada agente possui uma **capacidade limitada** de recursos.
- O objetivo é **maximizar o lucro total**, respeitando as restrições de capacidade.

Este problema é **NP-difícil**, e, por isso, frequentemente resolvido por métodos exatos ou heurísticos.

## 🎯 Objetivo do Projeto

Este projeto visa:

- 📥 Ler instâncias do MGAP a partir de arquivos `.yaml` com estrutura definida;
- 🧠 Construir o modelo de PLI na memória usando bibliotecas como `pulp`;
- 🚀 Resolver o problema utilizando um **solver via API**;
- ⏱️ Medir e registrar o **tempo de execução** e o **valor da solução** para cada instância;
- 📤 Salvar os resultados em arquivos de saída padronizados.

## 🧪 Instâncias Utilizadas

Trabalhamos com um conjunto diversificado de instâncias geradas aleatoriamente e extraídas dos seguintes artigos:

- *French, A.P., & Wilson, J.M. (2002). Heuristic Solution Methods for the Multilevel Generalized Assignment Problem. Journal of Heuristics, 8:143–153.*
- *Elhedhli, S.S. (2012). Exact Solution Methods for the Multilevel Generalized Assignment Problem. E3 Journal of Business Management and Economics.*  

## 🛠️ Tecnologias Utilizadas

- 💻 Linguagem: Python
- 📦 Biblioteca: `pulp`

## 📂 Estrutura do Projeto
```
mgap/
├── data/ # Instâncias do problema (entrada)
├── results/ # Saídas geradas pelo solver
├── src/ # Código-fonte principal
│ └── model.py # Implementação do modelo PLI
├── utils/ # Funções auxiliares
├── README.md # Este arquivo
└── requirements.txt # Dependências do projeto
```

## 📈 Resultados

Os experimentos realizados envolvem múltiplas instâncias com diferentes dimensões e complexidades. Os resultados são reportados em termos de:

- Tempo de execução
- Valor da solução (lucro total)

## 👥 Equipe

Este projeto foi desenvolvido como parte da disciplina **Modelagem e Otimização Algorítmica (MOA-INF)** da **Universidade Estadual de Maringá**, sob orientação do Prof. Mauro Mulati.


| Nome                             | RA       |
|----------------------------------|----------|
| [Raphael Ichiro](mailto:ra131593@uem.br) | 131593 |
| [Henrique Maeda](mailto:ra131594@uem.br)     | 131594   |
| [Gabriel Prado](mailto:ra128272@uem.br) | 128968   |
| [Kauan Eguchi](mailto:ra128854@uem.br)  | 128854   |

## 📄 Licença

Este projeto é acadêmico e está disponível para fins de estudo e pesquisa.

---

> *“A melhor maneira de resolver um problema difícil é modelá-lo corretamente.”*
