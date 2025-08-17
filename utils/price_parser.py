import re


class PriceParser:
    @staticmethod
    def parse_price(price_text: str) -> float:
        if not price_text:
            return 0.0

        found_numbers = re.findall(r'(\d+[\.,]?\d*)', price_text)

        if found_numbers:
            price_str = found_numbers[-1].replace(',', '.')
            return float(price_str)
        else:
            return 0.0
