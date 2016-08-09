class Score(object):
    def __init__(self):
        self.batsman_name = []
        self.out_info = []


    def getScore(self, data):
        for i in data.find_all('tr', attrs={"class": ""}):
            self.batsman_name.append({'batsman_name': i.find('td', attrs={"class": "batsman-name"})})
            # self.batsman_name.append(i)

        # for i in data.find_all('div', attrs={"class": "end-of-over-info"}):
        #     end_over_txt = i.find('p').text
        #     # for n in i.find_all('li', 'end-of-over-player-stat'):
        #     #     self.eof.append(n)
        #         # for m in n.find_all('span', 'large-10 medium-10 columns'):
        #         #     self.eof.append(m.text)
        #     self.eof.append({'End Of Overs': end_over_txt , 'batsman1': i.find('span').text})

