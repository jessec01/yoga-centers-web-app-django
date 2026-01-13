
class GroupDataService:
    @staticmethod
    def group_data(username,first_name,last_name,email,phone,password):
        data={
            'username':username,
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone,
            'password':password
        }
        return data