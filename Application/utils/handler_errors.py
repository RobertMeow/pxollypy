class HandlerError:
    @staticmethod
    def get_response_code(error_code):
        x = {917: '-1'}
        return x[error_code] if error_code in x else '-1'


"""
Ответ 1: беседа добавлена в базу данных
Ответ 0: не удалось добавить беседу в базу данных
Ответ -1: неизвестная ошибка
Ответ -2: сервер не поддерживает этот метод 
"""
