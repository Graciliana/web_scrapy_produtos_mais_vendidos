import scrapy

class CategoryMercadoLivreSpider(scrapy.Spider):
    name = "category_mercado_livre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/categorias"]

    def parse(self, response):
        ...
<h2 class="categories__title" itemprop="name"><a href="https://www.mercadolivre.com.br/c/servicos#c_id=/home/categories/category-l1/category-l1&amp;c_category_id=MLB1540&amp;c_uid=19b6f8fe-ccc5-11ef-a6ab-0d64f15ef42d" class="categories__title" itemprop="url">Serviços</a></h2>

<h3 class="categories__subtitle-title">Academia e Esportes</h3>