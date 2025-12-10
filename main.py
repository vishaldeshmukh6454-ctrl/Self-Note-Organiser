import datetime

class Personal_Notes:
    def __init__(self):
        self.name = None
        self.notes = []
        self.email = None
        self.contact = None

    def add_notes(self,note):
        detailed_note={}
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        detailed_note[date] = note
        self.notes.append(detailed_note)

    def search_notes(self,note):
        matched_notes=[]
        for note_details in self.notes:
            if note in note_details.values():
                matched_notes=note_details
                break
        if matched_notes:
            print("The note is present in the notes list.")
        else:
            print("The note is not present in the notes list.")


    def delete_notes(self,note):
        for note_details in self.notes:
            if note in note_details.values():
                self.notes.remove(note_details)


    def update_notes(self,note):
        pass

    def show_notes(self):
        print(self.notes)

    def user_info(self):
        user_info=input("Enter name,email,contact:\t").split(",")
        self.name = user_info[0]
        self.email = user_info[1]
        self.contact = user_info[2]
        note=input("Enter your note: ")
        self.add_notes(note)

        # self.notes.append(self.add_notes(user_info[3]))
        # self.name=input("Enter your name: ")
        # self.email=input("Enter your email: ")
        # self.contact=input("Enter your contact: ")



    def accept_notes(self,note):
        pass
    def menu(self):
        while True:
            print("!!!!!!!!!!!!!!!!!!- Note Organizer -!!!!!!!!!!!!!!!!!!"
                  "\n1.Add User Information with notes"
                  "\n2.Add Note"
                  "\n3.Show Notes"
                  "\n4.Search Note"
                  "\n5.Delete Note")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    self.user_info()
                case 2:
                    new_note = input("Enter new note: ")
                    self.add_notes(note=new_note)
                case 3:
                    self.show_notes()
                case 4:
                    search_note = input("Enter your note: ")
                    self.search_notes(search_note)
                case 5:
                    self.delete_notes(note=input("Enter your note to delete: "))

            user_choice = input("Do you want do it again?(y/n)")
            if user_choice == "y":
                continue
            else:
                break
if __name__ == '__main__':
    day1 = Personal_Notes()
    day1.menu()
