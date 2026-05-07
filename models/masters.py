class Masters:
    def __init__(self, Master_ID, Last_Name, First_Name, Mid_Name, Phone, Specialization):
        self.__Master_ID = Master_ID
        self.__Last_Name = Last_Name
        self.__First_Name = First_Name
        self.__Mid_Name = Mid_Name
        self.__Phone = Phone
        self.__Specialization = Specialization
    
    def set_Master(self, Master_ID):
        self.__Master_ID = Master_ID
    def set_Last_Name(self, Last_Name):
        self.__Last_Name = Last_Name
    def set_First_Name(self, First_Name):
        self.__First_Name = First_Name
    def set_Mid_Name(self, Mid_Name):
        self.__Mid_Name = Mid_Name
    def set_Phone(self, Phone):
        self.Phone = Phone
    def set_Specialisation(self, Specialization):
        self.__Specialization = Specialization
    def get_Master_id(self):
        return self.__Master_ID
    def get_Last_Name(self):
        return self.__Last_Name
    def get_First_Name(self):
        return self.__First_Name
    def get_Mid_Name(self):
        return self.__Mid_Name
    def get_Phone(self):
        return self.Phone
    def get_Specialization(self):
        return self.Specialization