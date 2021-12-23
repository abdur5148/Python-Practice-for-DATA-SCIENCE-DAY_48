class Check(Exception):
    def __init__(self, msg):
        self.msg = msg


var = Check(input("Enter String : "))
