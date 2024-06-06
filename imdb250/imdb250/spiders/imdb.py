import scrapy

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.boxofficemojo.com/showdown/?ref_=bo_ft_hm_showdown"]

    def parse(self, response):
        # Itera sobre cada filme na página
        for filme in response.css('.a-align-center + .a-align-center'):
            # Captura o título do filme
            titulo = filme.css('.a-align-center+ .a-align-center .a-link-normal::text').get()
            # Tenta capturar o valor monetário associado
            valor = filme.css('.a-text-right~ .a-align-center+ .a-align-center .money::text').get()

            # Adiciona ao JSON apenas se ambos título e valor existirem
            if titulo and valor:
                yield {
                    'titulos': titulo,
                    'valor': valor
                }
