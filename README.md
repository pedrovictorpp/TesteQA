TesteQA
Este é um script para teste de entrevista de QA, ele deve acessar o site https://www.kabum.com.br/ pesquisar por "i5" adicionar o primeiro item da lista apresentada ao carrinho e confirmar que o item correto foi adicionado ao carrinho e a quantidade certa.


Instalação
Basta baixar o arquivo e executar via python

Requisitos
Para execução dos teste é necessario ter python e selenium baixados e instalados.

Onde encontrar
python
https://www.python.org/
Selenium
https://www.selenium.dev/

Teste realizado

A automação vai acessar o site https://www.kabum.com.br/, preencher o campo de pesquisa o termo 'i5' e clickar em "Buscar", neste momento o site deve retornar uma pagina com uma lista de produtos, o sistema vai conferir se o resultado apresentado na pagina contem 'i5' no nome, após confirmar que os resultados estão corretos vai selecionar o primeiro da lista o que deve enviar para a pagina de finalização de compra, neste momento o sistema vai clickar no link para o carrinho de compras e confirmar que o item selecionado foi adicionado corretamente.
