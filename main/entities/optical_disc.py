from datetime import date, datetime


class OpticalDisc:
    __type_name: str = ''
    __title: str = ''
    __published_date: date = None
    __genre: str = ''
    __price: float = 0.0
    __description: str = ''
    __fsk: int = 0
    __ean: str = ''
    __item_created: datetime = None

    def __init__(self):
        pass

    # Setters
    def set_type_name(self, type_name: str):
        self.__type_name = type_name

    def set_title(self, title: str):
        self.__title = title

    def set_published_date(self, published_date: date):
        self.__published_date = published_date

    def set_genre(self, genre: str):
        self.__genre = genre

    def set_price(self, price: float):
        self.__price = price

    def set_description(self, description: str):
        self.__description = description

    def set_fsk(self, fsk: int):
        self.__fsk = fsk

    def set_ean(self, ean: str):
        self.__ean = ean

    def set_item_created(self, item_created: datetime):
        self.__item_created = item_created

    # Getters
    def get_type_name(self) -> str:
        return self.__type_name

    def get_title(self) -> str:
        return self.__title

    def get_published_date(self) -> date:
        return self.__published_date

    def get_genre(self) -> str:
        return self.__genre

    def get_price(self) -> float:
        return self.__price

    def get_description(self) -> str:
        return self.__description

    def get_fsk(self) -> int:
        return self.__fsk

    def get_ean(self) -> str:
        return self.__ean

    def get_item_created(self) -> datetime:
        return self.__item_created
