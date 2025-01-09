import scrapy


class MaisVendidoPorCategoriaSpider(scrapy.Spider):
    name = "mais_vendido_por_categoria_mercado_livre"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = [
            "https://www.mercadolivre.com.br/mais-vendidos/MLB5672",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB271599",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1403",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1071",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1367",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1368",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1384",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1246",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1132",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1430",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1574",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1051",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1500",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1039",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB5726",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1000",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1276",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB263532",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB12404",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1144",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1499",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1648",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1182",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB3937",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1196",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1168",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB264586",
            "https://www.mercadolivre.com.br/mais-vendidos/MLB1953"
        ]

    def parse(self, response):
        # Extração da categoria
        category = response.css("h2.ui-label-builder.ui-search-breadcrumb__title::text").get()

        # Extração dos produtos mais vendidos
        products = response.css("div.poly-card__content")

        for product in products:
            prices = product.css("span.andes-money-amount__fraction::text").getall()
            cents = product.css("span.andes-money-amount__cents::text").getall()
            yield {
                "category": category,
                "product_name": product.css("a.poly-component__title::text").get(),
                "podio": product.css("span.poly-component__highlight::text").get(),
                "old_price_reais": prices[0] if len(prices) > 0 else None,
                "old_price_centavos": cents[0] if len(cents) > 0 else None,
                "new_price_reais": prices[1] if len(prices) > 1 else None,
                "new_price_centavos": cents[1] if len(cents) > 1 else None,
                "reviews_rating_number": product.css(
                    "span.poly-reviews__rating::text"
                ).get(),
                "reviews_amount": product.css("span.poly-reviews__total::text").get(),
            }
        
        
        