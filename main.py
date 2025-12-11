import datetime
from stored_in_json import write_data

class Personal_Notes:
    def __init__(self):
        self.name = None
        self.notes = []
        self.email = None
        self.contact = None

    def add_notes(self,note):
        """This method adds a note to the notes list"""
        detailed_note={}
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        detailed_note[date] = note
        self.notes.append(detailed_note)

    def search_notes(self,note):
        """This method searches for notes in the notes list"""
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
        """This method deletes a note from the notes list"""
        for note_details in self.notes:
            if note in note_details.values():
                self.notes.remove(note_details)

    def show_notes(self):
        """This method displays all the notes in the notes list"""
        print(self.notes)

    def user_info(self):
        """This method accepts information about the user"""
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

    def menu(self):
        """This method displays the menu with all operations"""
        while True:
            print("!!!!!!!!!!!!!!!!!!- Note Organizer -!!!!!!!!!!!!!!!!!!"
                  "\n1.Add User Information with notes"
                  "\n2.Add Note"
                  "\n3.Show Notes"
                  "\n4.Search Note"
                  "\n5.Delete Note"
                  "\n6.Save to Json File")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    self.user_info()
                case 2:
                    if self.name and self.email and self.contact:
                        new_note = input("Enter new note: ")
                        self.add_notes(note=new_note)
                    else:
                        print("!!! WARNING:Please enter user's name ,email and contact.!!!")
                case 3:
                    self.show_notes()
                case 4:
                    search_note = input("Enter your note: ")
                    self.search_notes(search_note)
                case 5:
                    self.delete_notes(note=input("Enter your note to delete: "))
                case 6:
                    file_name = input("Enter file name: ")
                    final_dict ={
                        "name":self.name,
                        "email":self.email,
                        "contact":self.contact,
                        "notes":self.notes,
                    }
                    write_data(final_dict,file_name)

            user_choice = input("Do you want do it again?(y/n)")
            if user_choice == "y":
                continue
            else:
                break


if __name__ == '__main__':
    day1 = Personal_Notes()
    day1.menu()
