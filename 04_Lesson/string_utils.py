class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк.
    """

    def capitalize(self, string: str) -> str:
        """
        Делает первую букву заглавной и возвращает измененную строку.
        Пример: `capitalize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Удаляет пробелы в начале строки, если они присутствуют.
        Пример: `trim("   skypro") -> "skypro"`
        """
        return string.lstrip(' ')

    def contains(self, string: str, symbol: str) -> bool:
        """
        Проверяет наличие символа в строке.
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все вхождения указанного символа из строки.
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        return string.replace(symbol, "")
