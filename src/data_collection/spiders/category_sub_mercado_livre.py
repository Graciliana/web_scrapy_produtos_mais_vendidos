import scrapy

class CategoryMercadoLivreSpider(scrapy.Spider):
    name = "category_mercado_livre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/categorias"]

    def parse(self, response):
        categories = response.css('div.categories__container')
        for  category in categories:
            yield {
                "category": category.css("h2.categories__title a::text").get(),
                "subcategory": category.css("h3.categories__subtitle-title ::text").getall()
            }