class Commentry(object):
    def __init__(self):
        self.details = []
        self.eof = []


    def getCommentry(self, data):
        for i in data.find_all('div', attrs={"class": "commentary-event"}):
            self.details.append({'Overs': i.find('div').text, 'Commentry': i.find('p').text})

        # for i in data.find_all('div', attrs={"class": "end-of-over-info"}):
        #     end_over_txt = i.find('p').text
        #     # for n in i.find_all('li', 'end-of-over-player-stat'):
        #     #     self.eof.append(n)
        #         # for m in n.find_all('span', 'large-10 medium-10 columns'):
        #         #     self.eof.append(m.text)
        #     self.eof.append({'End Of Overs': end_over_txt , 'batsman1': i.find('span').text})

