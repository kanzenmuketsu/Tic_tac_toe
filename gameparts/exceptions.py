class InvalidFieldError(IndexError):
    """
    Ошибка возникает при попытке получить несуществующую
    ячейку игрового поля.
    """

    def __str__(self):
        return 'Вы выбрали несуществующую ячейку игрового поля'