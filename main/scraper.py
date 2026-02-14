from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NBAScraper:
    def __init__(self, url: str):
        self.url = url
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    def coletar_dados(self):
        try:
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 40)

            # Seleciona a tabela
            table = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table.Crom_table__p1iZz")
            ))

            # Captura os cabeçalhos da tabela no site
                
            headers = [th.text.strip() for th in table.find_elements(By.XPATH, ".//thead//th")]

            rows = table.find_elements(By.XPATH, ".//tbody//tr")
            jogadores = []

            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                # Cria um dicionário com as estatísticas
                jogador = {headers[i]: cols[i].text for i in range(len(headers))}
                jogadores.append(jogador)

            return jogadores

        except Exception as e:
            print("Erro ao coletar dados:", e)
            return []

    def fechar(self):
        if self.driver:
            self.driver.quit()