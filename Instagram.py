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

# Acessar site
driver.get("https://help.instagram.com/contact/instagramcounterfeitform")

# Step 01: Entendo e desejo continuar
driver.find_element_by_xpath('//*[@id="u_0_2"]/label[1]/span').click()

# Step 02: Forneça suas informações de contato
driver.find_element_by_xpath('//*[@id="u_0_5"]/label[1]/span').click()

# Step 03: Eu ou a minha organização
driver.find_element_by_xpath('//*[@id="u_0_6"]/label[1]/span').click()

# Step 04: Seu nome (nome e sobrenome)
driver.find_element_by_id("213007228830668").send_keys(config.Name)

# Step 05: Responsabilidade do seu cargo
driver.find_element_by_xpath('//*[@id="1592946270964471"]/option[4]').click()

# Step 06: Endereço postal
driver.find_element_by_id("429750330422486").send_keys(config.Adress3)

# Step 07: Preencher Número de telefone
driver.find_element_by_id("375897116110187").send_keys(config.Phone)

# Step 08: Preencher Endereço de email
driver.find_element_by_id("1861865760756260").send_keys(config.email)

# Step 09: Preencher Confirme seu endereço de e-mai
driver.find_element_by_id("575682395964179").send_keys(config.email)

# Step 10: Preencher Nome do detentor dos direitos:
driver.find_element_by_id("138264076657877").send_keys(config.NameRigths)

# Step 11: Preencher Forneça um link para a presença online oficial do proprietário do direito.: 
driver.find_element_by_id("691245767724800").send_keys(config.Instapage)

# Step 12: Clicar em Forneça informações sobra sua marca comercial
driver.find_element_by_xpath('//*[@id="u_0_a"]/label[1]/span').click()

# Step 13: Preencher Qual é a sua marca?
driver.find_element_by_id("1876333722592163").send_keys(config.Brand)

# Step 14: Preencher Onde sua marca está registrada
driver.find_element_by_id("u_0_13").send_keys(config.Country)

# Step 15: Preencher Qual é seu número de registro da marca comercial (se aplicável)
driver.find_element_by_id("1500464686911107").send_keys(config.TradeMark)

# Step 16: Preencher Que categorias de bens de consumo e/ou serviços são abrangidas pelo seu registro
driver.find_element_by_id("1652300861681946").send_keys(config.Category)

# Step 17: Preencher Se possível, forneça um link (URL) que leve diretamente ao seu registro da marca.:
driver.find_element_by_id("1624850237799205").send_keys(config.URLTradeMark)

# Step 19: Clicar em Forneça o conteúdo que você deseja denunciar
driver.find_element_by_xpath('//*[@id="u_0_k"]/label[1]/span').click()

# Step 20: Clicar em Uma Página, grupo ou perfil inteiro
driver.find_element_by_xpath('//*[@id="SupportFormRow.1112475925434379"]/div[4]/label[1]/span').click()

# Step 21: Preencher Forneça links (URLs) que levem diretamente ao conteúdo específico que você está denunciando.
driver.find_element_by_id("774288576003882").send_keys(URLs)

# Step 22: Preencher Forneça links (URLs) que levem diretamente ao conteúdo específico que você está denunciando.
driver.find_element_by_id("125859267561673").send_keys(config.Description)

# Step 23: Clicar em Confirmar declaração
driver.find_element_by_xpath('//*[@id="u_0_s"]/label[1]/span').click()

# Step 24: Clicar em Sim
driver.find_element_by_xpath('//*[@id="u_0_q"]/label[1]/span').click()

# Step 25: Preencher Assinatura eletrônica:
driver.find_element_by_id("348034581955173").send_keys(config.Name)

quit()
