import re


class CPF:
    value = None
    __format = '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$'

    def __init__(self, cpf: str):
        self.value = cpf

    def validate(self) -> bool:
        if self.value is None:
            return False
        else:
            return re.search(self.__format, self.value) is not None
