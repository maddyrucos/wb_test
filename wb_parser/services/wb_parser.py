import requests

def search_wb_products(query, min_price=None, max_price=None, min_discount_price=None, max_discount_price=None, min_rating=None, min_feedbacks=None, page=1):
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    params = {
        "appType": 1,
        "curr": "rub",
        "dest": -1257786,
        "query": query,
        "page": page,
        "resultset": "catalog"
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        products = data.get('data', {}).get('products', [])

        filtered = []
        for p in products:
            price_basic = p.get("priceU", 0)
            price_total = p.get("salePriceU", 0)
            rating = p.get("reviewRating", 0)
            feedbacks = p.get("feedbacks", 0)

            if min_price and price_basic < int(min_price * 100):
                continue
            if max_price and price_basic > int(max_price * 100):
                continue
            if min_discount_price and price_total < int(min_discount_price * 100):
                continue
            if max_discount_price and price_total > int(max_discount_price * 100):
                continue
            if min_rating and rating < min_rating:
                continue
            if min_feedbacks and feedbacks < min_feedbacks:
                continue

            filtered.append(p)

        return filtered
    except (requests.RequestException, ValueError) as e:
        print(f"Ошибка при запросе или парсинге: {e}")
        return []

if __name__ == "__main__":
    products = search_wb_products(
        "Смартфон",
        min_price=5000,
        max_price=10000,
        min_discount_price=5500,
        min_rating=4.5,
        min_feedbacks=20
    )

    print(f"Найдено товаров: {len(products)}")
    for p in products[:5]:
        name = p.get('name', 'Без названия')
        price = p.get('priceU', 0) / 100
        sale_price = p.get('salePriceU', 0) / 100
        rating = p.get('reviewRating', 0)
        feedbacks = p.get('feedbacks', 0)
        print(f"{name} — цена: {price:.2f}₽, со скидкой: {sale_price:.2f}₽, рейтинг: {rating}, отзывов: {feedbacks}")
        