# Descriptive Learning Lab

This repository documents my practical exploration of **Descriptive Learning and Pattern Mining**, developed alongside the *Aprendizado Descritivo* course at UFMG.

The goal of this repository is not only to follow the course content, but to go **beyond the syllabus** through hands-on experimentation, algorithm implementation, and applied data analysis.

All learning is done through **code, experiments, and reproducible notebooks**.

---

# Learning Strategy

My approach is based on three principles:

### 1. Learn Through Implementation

For every major concept or algorithm, I try to:

* implement the algorithm **from scratch**
* reproduce results using **Python libraries**
* test the algorithm on **real datasets**

This allows me to understand both the **theory and practical behavior** of descriptive learning algorithms.

---

### 2. Connect Theory With Practice

The course bibliography provides the **theoretical foundations**, especially in:

* pattern mining
* rule learning
* descriptive pattern discovery
* contrast and subgroup mining

This repository complements those materials with **practical implementation and experimentation**.

---

### 3. Build a Research-Oriented Knowledge Base

Instead of solving isolated exercises, this repository is structured as a **growing laboratory of experiments**, covering different areas of descriptive learning.

The goal is to build intuition about:

* how patterns emerge in data
* how algorithms search for structure
* how pattern quality is evaluated
* how these methods apply to real problems

---

# Core Topics Explored

The repository follows the structure of the course, focusing on the main areas of **descriptive pattern discovery**:

### Frequent Pattern Mining

Discovering patterns that frequently appear in datasets.

Examples:

* Apriori
* FP-Growth
* Eclat

Applications:

* market basket analysis
* co-occurrence discovery
* recommendation systems

---

### Association Rule Mining

Finding relationships between items or events.

Key concepts:

* support
* confidence
* lift
* conviction
* leverage

Applications:

* product recommendation
* medical correlations
* behavioral analysis

---

### Sequential Pattern Mining

Discovering patterns in ordered data such as:

* user behavior
* clickstreams
* biological sequences
* logs

Algorithms explored:

* GSP
* PrefixSpan
* SPADE

---

### Graph Pattern Mining

Mining patterns inside graph structures.

Applications:

* molecular structures
* social networks
* knowledge graphs

Example topics:

* frequent subgraph mining
* structural pattern discovery

---

### Subgroup Discovery

Finding **interpretable subsets of data** where the behavior of a target variable is unusual or interesting.

Example pattern:

```
Age > 60 AND cholesterol > 200
→ higher probability of heart disease
```

This area connects strongly to **interpretable machine learning**.

---

### Exceptional Model Mining

Discovering **subsets of data where a model behaves differently**.

Example:

```
A regression model works well for one subgroup
but performs poorly for another.
```

This helps reveal **hidden structures and model limitations**.

---

# Repository Structure

```
descriptive-learning-lab/

frequent_patterns/
    apriori_from_scratch.py
    fp_growth.py
    pattern_experiments.ipynb

association_rules/
    rule_metrics.py
    rule_mining.ipynb

sequence_mining/
    prefixspan.py
    sequence_patterns.ipynb

graph_mining/
    graph_pattern_experiments.ipynb

subgroup_discovery/
    subgroup_search.py
    subgroup_analysis.ipynb

exceptional_model_mining/
    emm_experiments.ipynb

datasets/
```

Each topic includes:

* algorithm implementations
* experiments with real datasets
* notebooks documenting insights and results

---

# Tools Used

Main libraries used in this repository:

* Python
* NumPy
* Pandas
* scikit-learn
* matplotlib / seaborn
* networkx
* mlxtend

---

# Learning Resources

The theoretical foundations are mainly based on:

* *Data Mining and Analysis – Zaki & Meira*
* *Supervised Descriptive Pattern Mining – Ventura & Luna*
* *Foundations of Rule Learning – Fürnkranz et al.*
* *Contrast Data Mining – Dong & Bailey*
* *Machine Learning: The Art and Science of Algorithms that Make Sense of Data – Flach*

Practical experimentation is complemented with modern machine learning and data science resources.

---

# Goals of This Repository

* develop a deep understanding of **descriptive learning algorithms**
* build intuition about **structure discovery in data**
* practice **implementing algorithms from scratch**
* explore **real-world applications of pattern mining**
* create a **public record of experiments and learning progress**

---

# Long-Term Vision

This repository is intended to evolve into a **personal laboratory for pattern discovery and descriptive machine learning**, supporting future research and applications in:

* interpretable machine learning
* knowledge discovery in databases
* explainable AI
* large-scale data mining
* data-driven decision systems
