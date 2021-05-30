class tournage:
    """
    def __init__(self,today,stduentsList):
        self.students = stduentsList
    """
    students = [
        {'age': 22, 'home_location': [3456, 567], 'id': 3456, 'name': 'Nawfel Sekrafi', 'organization': [{'id': 123, 'location': [123, 123], 'name': 'intellect'}], 'phone_number': 23232355, 'schedule_of_study': [{'day': 'monday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}, {'day': 'tuesday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}, {'day': 'friday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}, {'day': 'saturday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}]},
        {'age': 22, 'home_location': [3456, 567], 'id': 345236, 'name': 'aziz', 'organization': [{'id': 124, 'location': [123, 123], 'name': 'Intellect'}], 'phone_number': 23232321, 'schedule_of_study': [{'day': 'saturday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}, {'day': 'tuesday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}, {'day': 'friday', 'hours': [{'end': '16:00', 'start': '14:00'}, {'end': '10:00', 'start': '8:00'}], 'week': 1, 'year': 2021}]}
        ]


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

    def filter(self):
        for s in self.students:
            for j in s["schedule_of_study"]:
                for k,v in j.items() :











t1 = tournage()
t1.filter()


