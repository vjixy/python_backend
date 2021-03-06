from app.models.item import Item

class DatabaseManipulation():
    def __init__(self, con) -> None:
        self.con = con
        self.create_item_database()

        # cur = self.con.cursor()
        # self.create_user_database()
        # self.create_model_database()
        # self.create_receipt_database()
        # self.create_brand_database()
        # self.create_market_database()
        # self.create_receipt_item_database()
        # self.create_stock_database()
        # self.create_item_database()
        
        
    def create_stock_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS stock
                            (stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                market_id INTEGER NOT NULL,
                                item_id INTEGER NOT NULL,
                                price NUMBER NOT NULL,
                                quantity INTEGER NOT NULL)''')
    
    def create_market_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS market
                            (market_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                name text NOT NULL,
                                location text NOT NULL)''')

    # def create_item_database(self):
    #     cur.execute('''CREATE TABLE IF NOT EXISTS item
    #                         (item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                             brand_id INTEGER NOT NULL,
    #                             model_id INTEGER NOT NULL,
    #                             name text NOT NULL,
    #                             description text NOT NULL,
    #                             type text NOT NULL)''')
    def create_item_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS item
                            (item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name text NOT NULL,
                                brand text NOT NULL,
                                type text NOT NULL,
                                category text NOT NULL,
                                description text NOT NULL,
                                model_path text NOT NULL,
                                model_location text NOT NULL,
                                model_extras text NOT NULL,
                                texture_path text NOT NULL,
                                price float NOT NULL
                                )''')

    def create_brand_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS brand
                            (brand_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                name text NOT NULL)''')

    def create_model_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS model
                            (model_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                model_name text NOT NULL,
                                model_path text NOT NULL,
                                model_obj BINARY)''')

    def create_user_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS user
                            (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                username text NOT NULL,
                                email text NOT NULL,
                                password text NOT NULL)''')

    def create_receipt_item_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS receipt_item
                            (receipt_item_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                receipt_id INTEGER NOT NULL,
                                quantity INTEGER NOT NULL,
                                price_per_item NUMBER NOT NULL,
                                total NUMBER NOT NULL)''')

    def create_receipt_database(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS receipt
                            (receipt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                market_id INTEGER NOT NULL,
                                total NUMBER NOT NULL)''')

    def _values_to_str(self, values):
        str_value = ""

        for value in values:
            try:
                str_value+="'"+value+"',"
            except:
                str_value+=value.__str__()+","

        return str_value[:-1]


    def addAnny(self, table_name, values):
        self.create_item_database()
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO " + table_name + " VALUES (" + self._values_to_str(values) + ")")
            self.con.commit()
        except Exception as e:
            print(e)
            return e.__str__

    def selectAny(self, table_name):
        cur = self.con.cursor()
        return cur.execute("SELECT * FROM " + table_name ).fetchall()
    
    def deleteAny(self, table_name):
        self.con.execute("DROP TABLE "+ table_name)

    def getItems(self):
        item_list = self.selectAny("item")
        print(item_list)
        item_dict = {}
        try:
            for item in item_list:
                item_dict[item[0]] = Item(
                    name = item[1],
                    brand = item[2],
                    type = item[3],
                    category = item[4],
                    description = item[5],
                    model_path = item[6],
                    model_location = item[7],
                    model_extras = item[8],
                    texture_path = item[9],
                    price = item[10]
                )

        except Exception as e:
            raise Exception("found error: "+ e.__str__())

        return item_dict

    def getItemById(self, item_id):
        cur = self.con.cursor()
        return cur.execute("SELECT * FROM item where item_id = " + str(item_id)).fetchall()
