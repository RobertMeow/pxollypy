import sqlite3

SCHEMA = """
         CREATE TABLE conversations (peer_id INT, local_id TEXT, upeer_id INT);
         CREATE TABLE config (confirmation_code TEXT NOT NULL DEFAULT '',
                              token TEXT NOT NULL DEFAULT '0',
                              pxolly_token TEXT NOT NULL DEFAULT '0',
                              secret_key TEXT NOT NULL DEFAULT '0');"""


class ControlDatabase:
    __slots__ = ['con', 'sql', 'API', 'token', 'pxolly_token', 'code', 'secret_key']

    def __init__(self):
        self.con = sqlite3.connect('Application/database/warp_database.db', check_same_thread=False)
        self.sql = self.con.cursor()
        self.API = None

        self.update_config(update=False)
        config = self.get_config()
        self.token,  self.pxolly_token,  self.code,  self.secret_key = config[0], config[1], config[2], config[3]

    def receive(self, *args):
        """
        Получение одинарного значения
        :param args: SQL-запрос, остальное
        :return: Результат
        """
        self.sql.execute(*args)
        return self.sql.fetchone()[0]

    def receives(self, *args):
        """
        Получение данных
        :param args: SQL-запрос, остальное
        :return: Результат
        """
        self.sql.execute(*args)
        return self.sql.fetchall()

    def save(self, query: str, *args):
        """
        Добавление/удаление/обновление и тд
        :param query: SQL-запрос
        :param args: Остальное
        :return: None
        """
        if query.endswith(';'):
            self.sql.executescript(query)
        else:
            self.sql.execute(query, *args)
        self.con.commit()

    def create_tables(self) -> bool:
        """
        Создание таблиц
        :return: bool
        """
        if self.receive("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'config'") == 0:
            self.save(SCHEMA)
            self.save("INSERT INTO config (confirmation_code) VALUES ('0')")  # () VALUES ()
            return True
        return False

    def update_config(self, update=True) -> None:
        """
        Обновление конфигурации
        :return: None
        """
        if update or self.create_tables():
            token, pxolly_token, code, secret_key = input("Токен: "), input("Токен от @pxolly: "), input("confirmation code: "), input("secret key: ")
            self.save(f"UPDATE config SET token = '{token}', confirmation_code = '{code}', secret_key = '{secret_key}', pxolly_token = '{pxolly_token}'")
            # TODO: да, можно было сделать через безопасный режим (?), знаю, ацтань

    def get_config(self):
        return self.receives("SELECT token, pxolly_token, confirmation_code, secret_key FROM config")[0]

    def get_chat_uid(self, chat_id):
        return self.receive(f"SELECT peer_id FROM conversations WHERE local_id = '{chat_id}'")
