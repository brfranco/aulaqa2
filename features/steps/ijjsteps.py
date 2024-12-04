from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")

@when(u'Insiro meus dados')
def step_impl(context):

    context.driver.find_element(By.ID, "nome").send_keys("Fulano")
    context.driver.find_element(By.ID, "email").send_keys("Fulano@teste.com")
    context.driver.find_element(By.ID, "assunto").send_keys(Keys.ARROW_DOWN , Keys.TAB)


@when(u'Envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"')
def step_impl(context):

    context.driver.find_element(By.ID, "mensagem").send_keys("Teste - Olá da turma de QA Avançado, Ilhabela Novembro 2024")


@then(u'Fecho o navegador')
def step_impl(context):
    context.driver.quit()