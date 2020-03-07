class ContactList(list):
    def __init__(self, my_list):
        self.my_list = my_list
    
    def search_by_name(self, name):
        new_list = []
        for i in self.my_list:
            if i == name:
                new_list.append(i)
        return new_list

all_contacts = ContactList(["Uson", "Asan", "Sagun", "Daniyar", "Bolot"])
print(all_contacts.search_by_name("Bolot"))
print(all_contacts.search_by_name("Sagun"))