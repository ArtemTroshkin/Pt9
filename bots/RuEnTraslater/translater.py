from config import RU_SYMBOLS, EN_SYMBOLS


class RuEnTranslater:
    def __init__(self, text: str):
        self.text = text
        self.ru_symbols = RU_SYMBOLS
        self.en_symbols = EN_SYMBOLS
        self._translate()

    def _translate(self):
        """Преобразует русский текст, написанный английской раскладкой

        :return:
        """
        self.current_text = str()
        for letter in self.text:
            for index, symbol in enumerate(self.en_symbols):
                if letter == symbol:
                    self.current_text += self.ru_symbols[index]

    def __str__(self) -> str:
        return self.current_text


str_ = 'Ghbdtn? vtyz pjden Fhn`v'
print(RuEnTranslater(str_))
