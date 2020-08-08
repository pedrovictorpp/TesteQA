from selenium.webdriver import Chrome
from time import sleep

"""
Eu como usuario
Quero pesquisar um item na "kabum"
Para adicionar ao meu carrinho
"""
busca = 'i5' #Item a ser buscado


def busca_descricao_classe (browser, classe):
    #Realiza a busca de classes por nome e retorna o texto contido dentro destas classes
    resultado = []
    elements = browser.find_elements_by_class_name(classe)
    for descricao in elements:
        resultado.append(descricao.text)
    return resultado

def valida_lista (browser,pesquisa,lista):
    #valida itens de uma lista baseado no termo buscado
    for item in lista:
        assert pesquisa in item.lower()

browser = Chrome()

"""
Dado que estou na pagina principal do site "kabum"
Quando pesquiso por um produto
Então sou direcionado a pagina de pesquisa com a lista com itens contendo o termo buscado
"""
browser.get('https://www.kabum.com.br/')
sleep (2)
buscador = browser.find_element_by_class_name('sprocura')
buscador.send_keys(busca)
browser.find_element_by_id('bt-busca').click()
lista_pesquisa = busca_descricao_classe(browser,'eITELq')
valida_lista (browser, busca, lista_pesquisa)
sleep(2)
"""
Dado que estou na pagina de pesquisa
Quando clicko sobre um dos itens
Então sou direcionado a pagina de compra com os detalhes do item selecionado
"""
item = browser.find_elements_by_class_name('item-nome')
item_selecionado = item[0].text
item[0].click()
sleep(2)
"""
Dado que estou na pagina de detalhes do item
Quando clicko sobre o botão de compra
Então sou direcionado a pagina de compra com os detalhes da compra
"""
bt_comprar = browser.find_elements_by_class_name('botao-comprar')
bt_comprar[0].click()
sleep(2)
"""
Dado que estou na pagina de detalhes de compra
Quando clicko sobre o botão do carrinho
Então sou direcionado a pagina de carrinho de compras
"""
carrinho = browser.find_elements_by_class_name('text-carrinho')
carrinho[0].click()
sleep(1)
produto_carrinho = browser.find_elements_by_class_name('dwxlSw')
produto_carrinho = produto_carrinho[0].text.split('\n')
assert item_selecionado in produto_carrinho
quantidade = browser.find_elements_by_class_name('fpeyDB')
quantidade = quantidade[0].text.split('\n')
assert '1' in quantidade[0]

print('sucesso')

browser.quit()
