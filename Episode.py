
class Episode:
    'IMDB Episode Class'
    dummy=10
    def __init__(self,url,name,number,rating,storyline,imdb_title_number):
        self.url = url
        self.name = name
        self.number = number
        self.rating = rating
        self.storyline = storyline
        self.imdb_title_number = imdb_title_number

    def show_details(self):
        # print(self.number+"   ["+self.url+"]")
        print(self.number)
        print(self.rating)
        print("["+self.name+"]"+"  ---  ["+self.imdb_title_number+"]")
        print(self.storyline)
        print('-------------------------------')

    def write_file(self):
        print("Work in progress")

    def write_div(self):
        print("Work in progress")