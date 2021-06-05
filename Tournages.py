import math

class tournage:
    
    def __init__(self,today,stduentsList):
        self.students = stduentsList
    
    students = [
        {'age': 22, 'home_location': [3456, 567], 'id': 3456, 'name': 'Nawfel Sekrafi', 'organization': [{'id': 123, 'location': [123, 123], 'name': 'intellect'}], 'phone_number': 23232355, 'weeks_of_study': [{'days': [{'n': 'sunday', 'yemchi': ['10:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 1, 'year': 2021}, {'days': [{'n': 'monday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 30, 'year': 2021}]},
        {'age': 22, 'home_location': [100, 100], 'id': 345236, 'name': 'aziz', 'organization': [{'id': 124, 'location': [123, 123], 'name': 'Intellect'}], 'phone_number': 23232321, 'weeks_of_study': [{'days': [{'n': 'sunday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 1, 'year': 2021}, {'days': [{'n': 'monday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 30, 'year': 2021}]}
        ]

    def convert_to_nearest_neighbor(self):
        # bus location needs to be a parameter
        # students initial list must be parameter
        bus_location =[234,987]
        tab ={}
        for s in self.students:
            # distance between tow points : d=√((x_2-x_1)²+(y_2-y_1)²)
            distance = math.sqrt((s["home_location"][0] - bus_location[0])**2 + (s["home_location"][1] - bus_location[1])**2)
            d={s["name"]:distance}
            tab.update(d)
        # sorting tab
        return sorted(tab.items(), key=lambda x: x[1])
"""
    # Liste des tournages go.
    go_8 = []
    go_10 = []
    go_12 = []
    go_14 = []
    go_16 = []
    # plus court chemain go .
    plus_court8 = []
    plus_court10 = []
    plus_court12 = []
    plus_court14 = []
    plus_court16 = []

    # Liste des tournages go back.
    back_10 = []
    back_12 = []
    back_14 = []
    back_16 = []
    back_18 = []

    # plus court chemain go back .
    plus_court_back_10 = []
    plus_court_back_12 = []
    plus_court_back_14 = []
    plus_court_back_16 = []
    plus_court_back_18 = []

    def filter(self,day):
        for s in self.students:
            for j in s["weeks_of_study"]:
                for i in j["days"]:
                    if i["n"] == day:
                        # remplir les sous-tabs d'aller
                        if '8:00' in i["yemchi"]:
                            self.go_8.append(s)
                        if '10:00' in i["yemchi"]:
                            self.go_10.append(s)
                        if '12:00' in i["yemchi"]:
                            self.go_12.append(s)
                        if '14:00' in i["yemchi"]:
                            self.go_14.append(s)
                        if '16:00' in i["yemchi"]:
                            self.go_16.append(s)
                        # remplir les sous-tabs de retour
                        if '10:00' in i["yrawe7"]:
                            self.back_10.append(s)
                        if '12:00' in i["yrawe7"]:
                            self.back_12.append(s)
                        if '14:00' in i["yrawe7"]:
                            self.back_14.append(s)
                        if '16:00' in i["yrawe7"]:
                            self.back_16.append(s)
                        if '18:00' in i["yrawe7"]:
                            self.back_18.append(s)
        print("go_8 values")
        for v in self.go_8:
            print(v)

"""
















students = [
        {'age': 22, 'home_location': [3456, 567], 'id': 3456, 'name': 'Nawfel Sekrafi', 'organization': [{'id': 123, 'location': [123, 123], 'name': 'intellect'}], 'phone_number': 23232355, 'weeks_of_study': [{'days': [{'n': 'sunday', 'yemchi': ['10:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 1, 'year': 2021}, {'days': [{'n': 'monday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 30, 'year': 2021}]},
        {'age': 22, 'home_location': [100, 100], 'id': 345236, 'name': 'aziz', 'organization': [{'id': 124, 'location': [123, 123], 'name': 'Intellect'}], 'phone_number': 23232321, 'weeks_of_study': [{'days': [{'n': 'sunday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 1, 'year': 2021}, {'days': [{'n': 'monday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}, {'n': 'tuesday', 'yemchi': ['8:00', '14:00'], 'yrawe7': ['12:00', '18:00']}], 'n': 30, 'year': 2021}]}
        ]
bus_location = [123,432]
t1 = tournage("saturday",students)
result = t1.convert_to_nearest_neighbor()
print ("result")
print(result)
