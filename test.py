import data


organ_name = 'intellect'
bus_location = [123,445]

students = data.get_students_data()
print(students)
data.download_students_avatars(students)
data.download_organization_logo(organ_name)
#tours.convert_to_nearest_neighbor(bus_location,students)