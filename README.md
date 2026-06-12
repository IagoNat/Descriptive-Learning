# Descoberta de Subgrupos para Identificação de Perfis de Alta Remuneração na RAIS 2024

Projeto desenvolvido para a disciplina **Aprendizado Descritivo (2026/1)** da Universidade Federal de Minas Gerais (UFMG).

## Objetivo

O objetivo deste trabalho é aplicar técnicas de **Subgroup Discovery** sobre dados da **RAIS 2024** para identificar perfis associados às maiores remunerações do mercado formal brasileiro.

A análise busca encontrar subgrupos interpretáveis caracterizados por atributos demográficos e ocupacionais, permitindo compreender quais características aparecem com maior frequência entre trabalhadores de alta renda.

---

## Base de Dados

Foi utilizada a base da **Relação Anual de Informações Sociais (RAIS) 2024**, disponibilizada pelo Ministério do Trabalho e Emprego. Os dados podem ser obtidos utilizando o FTP Client (discovery/ftp_client.py) e então extraídos. 

Após o processo de limpeza e pré-processamento, a base final utilizada na mineração contém:

* 465.916 registros
* 13 atributos
* informações demográficas, educacionais e ocupacionais

Os alvos analisados foram definidos pelos percentis de remuneração:

| Target | Percentil | Limite salarial |
| ------ | --------- | --------------- |
| P90    | 90%       | R$ 5.264,20     |
| P95    | 95%       | R$ 7.874,36     |
| P99    | 99%       | R$ 19.371,97    |

---

## Metodologia

O processo experimental foi dividido em cinco etapas:

1. Leitura dos microdados da RAIS
2. Normalização e tradução dos atributos categóricos
3. Construção dos targets binários
4. Descoberta de subgrupos utilizando PySubgroup
5. Avaliação dos padrões encontrados

Foi utilizada a seguinte configuração:

* Algoritmo: Beam Search
* Biblioteca: PySubgroup
* Profundidade máxima: 4
* Top-k: 20 subgrupos
* Quality Function: StandardQF(0.5)

---

## Experimentos Realizados

Foram conduzidos seis experimentos:

### Experimento 1 — Redundância

Avaliação da sobreposição entre os subgrupos encontrados utilizando Similaridade de Jaccard.

### Experimento 2 — Cobertura

Análise da cobertura acumulada dos casos positivos pelos subgrupos descobertos.

### Experimento 3 — Frequência de Atributos

Identificação dos atributos mais frequentes nos padrões encontrados.

### Experimento 4 — Diversidade

Cálculo da entropia dos atributos utilizados nos subgrupos.

### Experimento 5 — Influence da Quality Function

Comparação dos resultados obtidos com:

* StandardQF(0.0)
* StandardQF(0.5)
* StandardQF(1.0)

### Experimento 6 — Generalização

Validação dos padrões através de divisão treino/teste.

---

## Estrutura do Projeto

```text
.
├── subgroup_discovery.ipynb
│
├── data/
│   ├── extracted/
│   └── arquivos.json
│
├── dictionaries/
│
├── readers/
├── discovery/
├── profiling/
├── normalization/
│
├── requirements.txt
└── README.md
```

---

## Instalação

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente:

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## Dependências

Principais bibliotecas utilizadas:

* pandas
* numpy
* scipy
* matplotlib
* seaborn
* pysubgroup
* jupyterlab

---

## Execução

Abra o notebook principal:

```bash
jupyter lab
```

Em seguida execute as células:

```text
subgroup_discovery.ipynb
```

---

## Autor

Iago Nathan Cardoso Araújo

Universidade Federal de Minas Gerais (UFMG)

Departamento de Ciência da Computação

Disciplina: Aprendizado Descritivo (2026/1)
