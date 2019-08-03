#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
import sys, os
import config

# Check if pip is installed
try:
    import pip

    # Check if selenium is installed
    try:
        from selenium import webdriver
    except ImportError:
        print("Selenium not installed, try execute command: pip install selenium")
        quit()

except ImportError:
    print("Pip not present. Try install pip with commands: sudo easy_install pip or brew install python")
    quit()

# Steps
URLs = sys.argv[1] 

# Inicializar Drive
driver = webdriver.Chrome(os.getcwd() + "/chromedriver")

# Maximizar janela
driver.maximize_window()

# Acessar página
driver.get("https://www.facebook.com/help/contact/634636770043106")

# Step 01: Clicar em Marca comercial
driver.find_element_by_xpath('//*[@id="SupportFormRow.128234280586859"]/div[3]/label[1]/span').click()

# Step 02: Clicar em Continuar com a sua denúncia de marca registrada
driver.find_element_by_xpath('//*[@id="u_0_5"]/label[1]/span').click()

# Step 03: Encontrei conteúdo que acredito que infringe minha marca comercial
driver.find_element_by_xpath('//*[@id="SupportFormRow.2078752822349324"]/div[9]/label[1]/span').click()

# Step 04: Continuar com minha denúncia de marca comercial
driver.find_element_by_xpath('//*[@id="u_0_a"]/label[1]/span').click()

# Step 05: Forneça suas informações de contato
driver.find_element_by_xpath('//*[@id="u_0_e"]/label[1]/span').click()

# Step 06: Eu ou a minha organização
driver.find_element_by_xpath('//*[@id="u_0_f"]/label[1]/span').click()

# Step 07: Seu nome (nome e sobrenome)
driver.find_element_by_id("213007228830668").send_keys(config.Name)

# Step 08: Clicar e selecionar Responsabilidade do seu cargo: Outro funcionário
driver.find_element_by_xpath('//*[@id="1592946270964471"]/option[4]').click()

# Step 09: Preencher Endereço postal
driver.find_element_by_id("429750330422486").send_keys(config.Adress3)

# Step 10: Preencher Número de telefone
driver.find_element_by_id("384202775247727").send_keys(config.Phone)

# Step 11: Preencher Endereço de email
driver.find_element_by_id("622301541289923").send_keys(config.email)

# Step 12: Preencher Confirme seu endereço de e-mail
driver.find_element_by_id("1376658769024639").send_keys(config.email)

# Step 13: Preencher Nome do detentor dos direitos
driver.find_element_by_id("1193690677387082").send_keys(config.NameRigths)

# Step 14: Preencher Forneça um link para a presença online oficial do proprietário do direito.:
driver.find_element_by_id("817261985076647").send_keys(config.FBpage)

# Step 15: Clicar em Forneça informações sobra sua marca comercial
driver.find_element_by_xpath('//*[@id="u_0_j"]/label[1]/span').click()

# Step 16: Preencher Qual é a sua marca?:
driver.find_element_by_id("1876333722592163").send_keys(config.Brand)

# Step 17: Preencher Onde sua marca está registrada?: Brasil
driver.find_element_by_id("u_0_1h").send_keys(config.Country)

# Step 18: Preencher Qual é seu número de registro da marca comercial (se aplicável)?:
driver.find_element_by_id("1500464686911107").send_keys(config.TradeMark)

# Step 19: Preencher Que categorias de bens de consumo e/ou serviços são abrangidas pelo seu registro?: Setor Bancario
driver.find_element_by_id("332711233753465").send_keys(config.Category)

# Step 20: Preencher Se possível, forneça um link (URL) que leve diretamente ao seu registro da marca.
driver.find_element_by_id("407144802814187").send_keys(config.URLTradeMark)

# Informações de marca registrada
# Conteúdo que você deseja denunciar

# Step 21: Clicar em Forneça o conteúdo que você deseja denunciar
driver.find_element_by_xpath('//*[@id="u_0_t"]/label[1]/span').click()

# Step 22: Clicar em Uma Página, grupo ou perfil inteiro
driver.find_element_by_xpath('//*[@id="SupportFormRow.1112475925434379"]/div[3]/label[1]/span').click()

# Step 23: Preencher Forneça links (URLs) que levem diretamente ao conteúdo específico que você está denunciando.
driver.find_element_by_id("1622541521292980").send_keys(URLs)

# Informações de Contato
# Declaração
# Step 24: Clicar em Confirmar declaração
driver.find_element_by_id("125859267561673").send_keys(config.Description)

# Step 25: Clicar em Confirmar declaração
driver.find_element_by_xpath('//*[@id="u_0_15"]/label[1]/span').click()

# Step 26: Clicar em Sim
driver.find_element_by_xpath('//*[@id="u_0_17"]/label[1]/span').click()

# Step 27: Preencher Assinatura eletrônica:
driver.find_element_by_id("348034581955173").send_keys(config.Name)

# Step 28: Clicar em Enviar
#driver.find_element_by_id("u_0_1n").click()

quit()