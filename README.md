


# 🏀 NBA Stats Scraper & Analysis

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.0%2B-brightgreen)](https://selenium.dev)
[![Pandas](https://img.shields.io/badge/pandas-1.3%2B-orange)](https://pandas.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/DarleiVN/nba_stats_scraper/issues)

**Coleta automatizada de estatísticas da NBA** | **Armazenamento em JSON** | **Análise e visualização com pandas, matplotlib e seaborn**

Projeto desenvolvido com foco em **confiabilidade na extração** e **validação dos dados**, simulando um ambiente real de desenvolvimento com testes e documentação clara.

---

## 🚀 Funcionalidades

- 🔎 **Web scraping robusto** da tabela de líderes da NBA usando **Selenium** e **WebDriverWait** (tratamento de elementos dinâmicos).
- 💾 **Persistência** dos dados em **JSON** com timestamp (garante reprodutibilidade).
- 📊 **Análise de dados** com **pandas** – colunas traduzidas para facilitar visualização em português.
- 📈 **Geração automática de gráficos** com **matplotlib** e **seaborn** (Top 10 em pontos por jogo).
- 🧪 **Testes automatizados** para validar a extração e a integridade dos dados.

---

## 📂 Estrutura do Projeto

```
nba_stats_scraper/
├── main/
│   ├── __init__.py
│   ├── main.py           # Orquestra todo o fluxo (scraping → armazenamento → análise)
│   ├── scraper.py        # Classe NBAScraper (Selenium + esperas explícitas)
│   ├── storage.py        # Classe StorageManager (leitura/escrita JSON, DataFrame)
│   ├── analysis.py       # Classe NBAAnalysis (geração de gráficos)
│   └── tests/            # Testes unitários e de integração
│       ├── test_scraper.py
│       └── test_storage.py
├── data/                 # Arquivos JSON gerados (ignorados no .gitignore)
├── plots/                # Gráficos salvos (ignorados no .gitignore)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/DarleiVN/nba_stats_scraper.git
cd nba_stats_scraper
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o projeto
```bash
python -m main.main
```

**O que acontece na execução:**
1. O Selenium abre o navegador (modo headless por padrão).
2. Coleta as estatísticas (pontos, rebotes, assistências, minutos).
3. Salva os dados em `data/nba_stats_AAAA-MM-DD.json`.
4. Carrega o JSON em um DataFrame com colunas em português.
5. Gera e salva o gráfico dos **Top 10 pontuadores** em `plots/top10_pontos.png`.

---

## 🧪 Testes e Qualidade

Para garantir que a extração funcione mesmo com mudanças no site, o projeto inclui testes unitários e de integração.

### Executar os testes
```bash
python -m pytest main/tests/ -v
```

### Cobertura dos testes
- **`test_scraper.py`**: Verifica se a URL da NBA está acessível e se a tabela é encontrada.
- **`test_storage.py`**: Valida se os dados são salvos corretamente e se o DataFrame é criado com as colunas esperadas.


## 🛠️ Tecnologias Utilizadas

| Área           | Ferramentas                                      |
|----------------|--------------------------------------------------|
| Linguagem      | Python 3.10+                                     |
| Web Scraping   | Selenium, WebDriver Manager                       |
| Dados          | pandas, JSON                                     |
| Visualização   | matplotlib, seaborn                              |
| Testes         | pytest, unittest                                 |
| Versionamento  | Git, GitHub                                      |

---

## 📈 Exemplo de Gráfico Gerado

![Top 10 Pontuadores da NBA](plots/top10_pontos.png)

---

## 🐞 Relatório de Bugs e Contribuições

Encontrou um problema ou tem uma sugestão?  
Fique à vontade para abrir uma [Issue](https://github.com/DarleiVN/nba_stats_scraper/issues) descrevendo:
- Passos para reproduzir o erro
- Comportamento esperado vs. obtido
- Log de erro (se houver)

Pull requests são muito bem-vindos! 🚀

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido por [Darlei Vieira](https://github.com/DarleiVN)**  
📧 darlei.niz09@gmail.com  
🔗 [linkedin.com/in/darlei-vieira](https://linkedin.com/in/darlei-vieira)
