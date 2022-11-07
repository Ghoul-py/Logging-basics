import logging
logging.basicConfig(filename='studentrecord.log', level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")
class Student:
    def __init__(self, first, last, age, roll_no) -> None:
        self.first = first
        self.last = last
        self.age = age
        self.roll_no = roll_no

        logging.info("{} {} is {} old and his roll_no is {}".format(self.first,self.last,self.age,self.roll_no))

    @property
    def email(self):
        return "{}{}@gmail.com".format(self.first, self.last)
    @property
    def full_name(self):
        full_name = "{} {}".format(self.first, self.last)
        return full_name.title()

s1 = Student('sangraiz', 'khan', 26, 1961124)
s2 = Student('maaz', 'khan', 23, 1961112)
s3 = Student('hamza', 'hussain', 22, 1961120)

