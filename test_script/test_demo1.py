from generic.base_setup import Base_Setup
from generic.utility import Excel

class Test_1(Base_Setup):

    def test_1(self):
        print(self.driver.title)
        v=Excel.get_data("test_data/Book1.xlsx","Sheet1",1,1)
        print("From excel",v)
