import requests

urlBase = 'https://horizon.mcgill.ca'
urls = {'login':'/pban1/twbkwbis.P_ValLogin',
        'term' : '/pban1/bwckgens.p_proc_term_date'}

class MinervaSess:
    def __init__(self, sid, PIN):
        self.payload = {'sid' : sid, 'PIN' : PIN}
        #self.sid = sid
        #self.PIN = PIN
        self.resp = None

    def login(self):
        if self.resp != None:
            return True
        self.resp = requests.post(urlBase+urls['login'], data=self.payload, cookies={'TESTID' : 'set'})
        #start checking success
        try:
            self.resp.cookies['SESSID']
        except KeyError:
            self.resp = None #clear it
            return False
        self.jar = self.resp.cookies.get_dict()
        return True

    def setTerm(self, session, year):
        if self.resp == None:
            return False
        if session == 'fall':
            session = 'Fall'
        elif session == 'win':
            session = 'Winter'
        else:
            session = 'Summer'
        old_sessid = self.jar['SESSID']
        self.resp = requests.post(urlBase+urls['term'], data={'p_term':session+' '+year}, cookies=self.jar)

        if old_sessid == self.resp.cookies['SESSID']:
            return False
        self.jar = self.resp.cookies.get_dict()
        return True

    def searchCRN(self, crn, prefix, faculty):
        if self.resp == None:
            return -1
        old_sesid = self.jar['SESSID']
        data = {'crn':crn, 'sel_subj':prefix, 'sel_coll':faculty}
        self.resp = requests.post(urlBase+urls['search'], data=data, cookies=self.jar)
        if old_sessid == self.resp.cookies['SESSID']:
            return -1
        
