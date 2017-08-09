import requests

urlBase = 'https://horizon.mcgill.ca'
urls = {'login':'/pban1/twbkwbis.P_ValLogin'}

class MinervaSess:
    def __init__(self, sid, PIN):
        self.payload = {'sid' : sid, 'PIN' : PIN}
        #self.sid = sid
        #self.PIN = PIN
        self.resp = None
        self.cookies = {'TESTID' : 'set'}

    def login(self):
        if self.resp != None:
            return True
        self.resp = requests.post(urlBase+urls['login'], data=self.payload, cookies=self.cookies)
        if noerror: #this but real
            return True
        self.resp = None #clear this since it didn't work
        return False
