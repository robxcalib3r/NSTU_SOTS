# userdb.py

import datetime

temp_date = datetime.date.today()
class BusDB:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
        self.Maijtime = {"1.00 PM":0, "2.00 PM":0, "3.00 PM":0, "4.00 PM":0, "5.00 PM":0, "6.00 PM":0, "7.00 PM":0}
        self.camtime = {"7.00 AM":0, "8.00 AM":0, "9.00 AM":0, "9.30 AM":0, "12.00 PM":0, "1.00 PM":0, "7.00 PM":0}
        self.temp = 0
        self.temp1 = 0

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email,  arriveTo1, arriveTo, time1, time, dateT = line.strip().split(";")
            self.users[email] = (arriveTo1, arriveTo, time1, time, dateT)

        self.file.close()

    def addDataPerson(self, email, time1, time, arriveTo1, arriveTo):

        if arriveTo == "Campus":
            try:
                if self.users[email][2] != time.strip() or self.users[email][3] != self.get_date():
                    self.users[email] = (arriveTo1.strip(), arriveTo.strip(), time1.strip(), time.strip(), self.get_date())
                    self.save()
                    return 1
                else:
                    print("Data exists already")
                    return -1
            except:

                self.users[email] = (arriveTo1.strip(), arriveTo.strip(), time1.strip(), time.strip(), self.get_date())
                self.save()
                return 1


        # date = self.get_date().strip()
        # if date not in self.users:
        #     if self.users[date][1] != "Maijdee":
        #         for t in ["7.00 AM", "8.00 AM", "9.00 AM", "9.30 AM", "12.00 PM", "1.00 PM", "7.00 PM"]:
        #             if self.users[date][2] == t:
        #                 self.Maijtime[t] += 1
        #                 if email.strip() not in self.users:
        #                     self.users[self.get_date().strip()] = (departFrom.strip(), arriveTo.strip(), time.strip(), email.strip())
        #                     self.save()
        #                     return 1
        #                 else:
        #                     print("Data exists already")
        #                     return -1
        #     if self.users[date][1] == "Campus":
        #         for t in ["1.00 PM", "2.00 PM", "3.00 PM", "4.00 PM", "5.00 PM", "6.00 PM", "7.00 PM"]:
        #             if self.users[date][2] == t:
        #                 self.camtime[t] += 1
        #                 if email.strip() not in self.users:
        #                     self.users[self.get_date().strip()] = (
        #                     departFrom.strip(), arriveTo.strip(), time.strip(), email.strip())
        #                     self.save()
        #                     return 1
        #                 else:
        #                     print("Data exists already")
        #                     return -1


    def getFreq(self):
        for email in self.users:
            time1 = self.users[email][2]
            time = self.users[email][3]

            self.temp1 = int(self.Maijtime[time1])
            self.temp1 += 1
            self.Maijtime[time1] = self.temp1

            self.temp = int(self.camtime[time])
            self.temp += 1
            self.camtime[time] = self.temp
        return self.Maijtime, self.camtime


    def getData(self, index):
        if index in self.users:
            return self.users[index]
        else:
            return -1

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + ";" + self.users[user][3] + ";" + self.users[user][4] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]