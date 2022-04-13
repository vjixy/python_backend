

class DatabaseManipulation():
    def __init__(self, con) -> None:
        self.con = con
        self.create_items_stocks_database()
        self.create_market_database()
        
    def create_items_stocks_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS stocks
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                brand_id INTEGER NOT NULL,
                                name text NOT NULL,
                                model_path text NOT NULL,
                                description text NOT NULL)''')
        cur.close()
    
    def create_market_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS market
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                id_market INTEGER NOT NULL, 
                                model_path text NOT NULL, 
                                price FLOAT NOT NULL,
                                quantity INTEGER NOT NULL)''')
        cur.close()