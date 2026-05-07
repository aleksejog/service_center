class Employees:
    def __init__(self, Employee_ID, Last_Name, First_Name, Mid_Name, Phone, Position):
        self.__Employee_ID = Employee_ID
        self.__Last_Name = Last_Name
        self.__First_Name = First_Name
        self.__Mid_Name = Mid_Name
        self.__Phone = Phone
        self.__Position = Position
    
    def set_Employee_id(self, Employee_ID):
        self.__Employee_ID = Employee_ID
    def set_Last_Name(self, Last_Name):
        self.__Last_Name = Last_Name
    def set_First_Name(self, First_Name):
        self.__First_Name = First_Name
    def set_Mid_Name(self, Mid_Name):
        self.__Mid_Name = Mid_Name
    def set_Phone(self, Phone):
        self.Phone = Phone
    def set_Position(self, Position):
        self.__Position = Position
    def get_Employee_ID(self):
        return self.Employee_ID
    def get_Last_Name(self):
        return self.__Last_Name
    def get_First_Name(self):
        return self.__First_Name
    def get_Mid_Name(self):
        return self.__Mid_Name
    def get_Phone(self):
        return self.__Phone
    def get_Position(self):
        return self.__Position