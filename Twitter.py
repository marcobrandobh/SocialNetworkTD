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

# Acessar Site
driver.get("https://help.twitter.com/forms/impersonation")

# Step 01: Uma conta está fingindo ser ou representar minha empresa, marca ou organização.
driver.find_element_by_xpath('//*[@id="brand_imp"]').click()

# Step 02: Eu sou um representante autorizado da empresa, marca ou organização.
driver.find_element_by_xpath('//*[@id="company_tm"]').click()

# Step 03: Seu nome e sobrenome
driver.find_element_by_id("reporter_name").send_keys(config.Name)

# Step 04: e-mail da empresa
driver.find_element_by_id("email").send_keys(config.email)

# Step 05: Eu confirmo que estou denunciando a partir do meu endereço de e-mail empresarial
driver.find_element_by_xpath('//*[@id="disc_company_email"]').click()

# Step 06: Seu número de telefone
driver.find_element_by_id("reporter_phone").send_keys(config.Phone)

# Step 07: Eu trabalho diretamente para a empresa em nome da qual estou fazendo a denúncia.
driver.find_element_by_xpath('//*[@id="direct_brand_imp"]').click()

# Step 08: Seu cargo
driver.find_element_by_id("company_job_title").send_keys(config.role)

# Step 09: Nome da empresa
driver.find_element_by_id("company_name_company_rep_registered").send_keys(config.Brand)

# Step 10: Nome de usuário da empresa no Twitter (opcional)
driver.find_element_by_id("company_username_company_rep_registered").send_keys(config.TwitterPage)

# Step 11: Endereço da empresa
driver.find_element_by_id("company_address_company_rep_registered").send_keys(config.Adress)

# Step 12: Cidade, estado/região e código postal da empresa
driver.find_element_by_id("company_city_company_rep_registered").send_keys(config.Adress2)

# Step 13: País da empresa
driver.find_element_by_id("company_country_company_rep_registered").send_keys(config.Country)

# Step 14: Website da empresa
driver.find_element_by_id("company_website_company_rep_registered").send_keys(config.Site)

# Step 15: Qual nome de usuário está causando o problema?
driver.find_element_by_id("impostor_username").send_keys(URLs)

# Step 16: Utilizando o nome da nossa empresa, marca ou organização.
driver.find_element_by_xpath('//*[@id="name_use"]').click()

# Step 17: no nome da conta
driver.find_element_by_xpath('//*[@id="name_use_account_name"]').click()

# Step 18: na conta @nomedeusuário
driver.find_element_by_xpath('//*[@id="name_use_username"]').click()

# Step 20: Nossa empresa não quer usar ativamente este nome de usuário no Twitter.
driver.find_element_by_xpath('//*[@id="brand_report"]').click()

# Step 21: Entendo que o Twitter pode fornecer a terceiros ...
driver.find_element_by_xpath('//*[@id="third_parties"]').click()

# Step 22: Declaro, sob a pena de perjúrio, que todas as informações acima fornecidas são precisas.
driver.find_element_by_xpath('//*[@id="accuracy"]').click()
