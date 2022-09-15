
class user:
    id: str
    name: str
    password: str 
    role: str
    favourite_book_list = ["book_title1", "book_title2"]
   
    page = ["page#1", "page#2"]
    bookmark_list = list(zip(favourite_book_list, page))

class reader(user):
    def __init__(self, id, name, password, role, favourite_book_list,bookmark_list):
        self.id = id
        self.name = name
        self.password = password
        self.role = role
        self.favourite_book_list = favourite_book_list
        self.bookmark_list = bookmark_list
        
    def __str__(self):

        return self.id + ";;;" + self.name + ";;;" + self.password + ";;;" + self.role + ";;;" + str(self.favourite_book_list) + ";;;" + str(self.bookmark_list)


myObject = print(reader("karina01", "karina", "1234", "reader",user.favourite_book_list,user.bookmark_list))
