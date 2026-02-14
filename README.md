# 🏀 NBA Stats Scraper & Analysis

Projeto em **Python** para coletar estatísticas da NBA diretamente do site oficial, salvar em **JSON**, carregar em **pandas DataFrame** e gerar gráficos dos líderes em diferentes estatísticas.

---

## 🚀 Funcionalidades
- 🔎 Web scraping da tabela de líderes da NBA usando **Selenium**
- 💾 Armazenamento dos dados em **JSON**
- 📊 Conversão para **pandas DataFrame** com colunas traduzidas para português
- 📈 Geração de gráficos com **matplotlib** e **seaborn**

O arquivo JSON gerado contém:
- Nome/Jogador  
- Pontos por jogo  
- Rebotes  
- Assistências  
- Minutos em quadra  

---

## 📂 Estrutura do projeto

Python_webScraping/ 
│ 
├── main/ 
    |
    ├── init.py
    |tests/ #pasta com arquivos de testes locais.    
    ├── main.py          # Arquivo principal (executa o fluxo completo)│   
    ├── scraper.py       # Classe NBAScraper (Selenium) │   
    ├── storage.py       # Classe StorageManager (JSON + DataFrame) │   
        └── analysis.py      # Classe NBAAnalysis (gráficos) 
    ├── requirements.txt 
    └── README.md


---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DarleiVN/nba_stats_scraper.git
   cd nba-stats-scraper

   python -m venv .venv

# Crie e ative o ambiente virtual:
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Instale as dependências:

pip install -r requirements.txt



## Execução do projeto
//No terminal do projeto rode

python -m main.main

O programa irá:
1. 	Coletar os dados da tabela de líderes da NBA.
2. 	Salvar os dados em .
3. 	Carregar os dados em um DataFrame com colunas traduzidas.
4. 	Gerar o gráfico dos Top 10 jogadores em pontos por jogo
