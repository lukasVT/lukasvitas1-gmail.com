import tkinter
from tkinter.ttk import Combobox
from tkinter.ttk import Frame
from tkinter.ttk import Treeview
from tkinter.ttk import Label
from tkinter import messagebox
from tkinter import N, E, S, W
import datetime


# Store the candidates as an object
class Candidate:
    def __init__(self, position, first_name, last_name):
        self.position = position
        self.first_name = first_name
        self.last_name = last_name


# Class to be able to convert all the candidates in the text file into an object.
class CandidateResults:
    def __init__(self, name, pref_one, pref_two, pref_three, pref_four):
        self.name = name
        self.pref_one = pref_one
        self.pref_two = pref_two
        self.pref_three = pref_three
        self.pref_four = pref_four


# Lukas and Kevin
class StartingGUI:
    def __init__(self):  # opening GUI to allow the user to choice between the frontend features or exit the program
        self.window_Login = tkinter.Tk()
        self.window_Login.title("Main Menu")
        self.window_Login.resizable(False, False)  # prevents user from changing size of window created
        canvas = tkinter.Canvas(self.window_Login.geometry("550x250"))  # window size changed
        canvas.pack()
        tkinter.Label(self.window_Login, text="GSU Voting System", font="Courier 30 underline bold").place(relx=0.1, rely=0.0)
        tkinter.Label(self.window_Login, text="Click on the option that you want", font="Courier 16 bold").place(relx=0.1,rely=0.2)
        button_login = tkinter.Button(self.window_Login, text="Login", font="16", command=LoginGUI)
        button_login.place(relx=0.2, rely=0.4)  # creates button which can be pressed and the location

        view_results = tkinter.Button(self.window_Login, text="View Results", font="16", command=ResultsGUI)
        view_results.place(relx=0.33, rely=0.4)

        exit_login = tkinter.Button(self.window_Login, text="Exit", font="16", command=self.window_Login.destroy)
        exit_login.place(relx=0.6, rely=0.4)  # creates button which can be pressed and the location

        Label(self.window_Login, text="In order to login; use username: 'AndyX' password: 'WicksX' where X is a number "
                                      "from 1 to 5.").place(relx=0.02, rely=0.6)
        Label(self.window_Login, text="E.G. - Andy1, Wicks1").place(relx=0.02, rely=0.7)
        Label(self.window_Login, text="When you log out, you will not be able to use the same ID again. "
                                      "More ID's are in StudentVoters.txt").place(relx=0.02, rely=0.8)

        self.window_Login.mainloop()


# Lukas
class LoginGUI:
    def login_check(self):  # function for the users entered results to be compared with info in text file
        for line in open("StudentVoters.txt", "r+").readlines():  # Read every line in the text file
            stored_login = line.split()  # Split on the space, and store the results in a list of two entities
            # Compares user input with the saved id and password values in the array
            if self.entry_id.get() == stored_login[0] and self.entry_password.get() == stored_login[1]:
                for lines in open("StudentVoted.txt", "r+").readlines():
                    stored_voters = lines.split()
                    if stored_voters[0] == stored_login[0] and stored_voters[1] == stored_login[1]:
                        messagebox.showerror("Error!", "You have already voted.", parent=self.window_Login)
                        return True
                else:
                    log_warning = messagebox.askyesno("Warning!", "Once you've logged on and voted for all or some of "
                                                                  "the available positions, you will lose the ability "
                                                                  "to re-log back onto the system. Please ensure you "
                                                                  "have left yourself approximately 5 minutes to"
                                                                  " spare. Do you wish to continue?",
                                                      parent=self.window_Login)
                    if log_warning is True:
                        open("StudentVoted.txt", "a").write(line)
                        self.gsu_voters()
                        self.window_Login.destroy()  # closes the login page window
                        RoleSelectionGUI()  # Runs the voting class.
                        return True
                    else:
                        return False
        else:
            # Displays an error when there login information is wrong or not registered.
            messagebox.showerror("Error", "Invalid information - You are ineligible to vote.", parent=self.window_Login)
            return False

    def __init__(self):
        self.window_Login = tkinter.Tk()
        self.window_Login.title("Login Page")
        self.window_Login.resizable(False, False)  # prevents user from changing size of window created
        canvas = tkinter.Canvas(self.window_Login.geometry("700x350"))  # changes the size of the window which is displayed
        canvas.pack()

        tkinter.Label(self.window_Login, text="GSU Voting Pole", font="Courier 30 underline bold").place(relx=0.1, rely=0.0)
        tkinter.Label(self.window_Login, text="Please enter your student details so that you are able to vote.", font="16").place(relx=0.1, rely=0.2)
        tkinter.Label(self.window_Login, text="User ID:", font="16").place(relx=0.1, rely=0.35)  # makes text saying user id, and defines the location
        self.entry_id = tkinter.Entry(self.window_Login, font="16")    # creates a entry slot, user can enter desired result
        self.entry_id.place(relx=0.1, rely=0.45)       # defines the location of the entry widget
        tkinter.Label(self.window_Login, text="Password:", font="16").place(relx=0.1, rely=0.55)  # makes text saying password, and defines the location
        self.entry_password = tkinter.Entry(self.window_Login, show="*", font="16")  # creates a entry slot, user can enter desired result
        self.entry_password.place(relx=0.1, rely=0.65)  # defines the location of the entry widget
        tkinter.Button(self.window_Login, text="Login", font="16", command=self.login_check).place(relx=0.2, rely=0.8)  # creates button which can be pressed and the location
        tkinter.Button(self.window_Login, text="Exit", font="16", command=self.window_Login.destroy).place(relx=0.33, rely=0.8)  # creates button which can be pressed and the location

        self.window_Login.mainloop()

    def gsu_voters(self):
        f_president = open("GSUCandidates_president.txt", "w")
        f_office1 = open("GSUCandidates_GSUOfficer1.txt", "w")
        f_office2 = open("GSUCandidates_GSUOfficer2.txt", "w")
        f_office3 = open("GSUCandidates_GSUOfficer3.txt", "w")
        f_faculty1 = open("GSUCandidates_FacultyOfficer1.txt", "w")
        f_faculty2 = open("GSUCandidates_FacultyOfficer2.txt", "w")
        f_faculty3 = open("GSUCandidates_FacultyOfficer3.txt", "w")
        f_faculty4 = open("GSUCandidates_FacultyOfficer4.txt", "w")
        f_faculty5 = open("GSUCandidates_FacultyOfficer5.txt", "w")
        f_faculty6 = open("GSUCandidates_FacultyOfficer6.txt", "w")
        f_faculty7 = open("GSUCandidates_FacultyOfficer7.txt", "w")
        f_faculty8 = open("GSUCandidates_FacultyOfficer8.txt", "w")
        f_faculty9 = open("GSUCandidates_FacultyOfficer9.txt", "w")
        f_faculty10 = open("GSUCandidates_FacultyOfficer10.txt", "w")
        f_faculty11 = open("GSUCandidates_FacultyOfficer11.txt", "w")
        f_faculty12 = open("GSUCandidates_FacultyOfficer12.txt", "w")
        f_faculty13 = open("GSUCandidates_FacultyOfficer13.txt", "w")
        f_faculty14 = open("GSUCandidates_FacultyOfficer14.txt", "w")
        f_faculty15 = open("GSUCandidates_FacultyOfficer15.txt", "w")
        f_faculty16 = open("GSUCandidates_FacultyOfficer16.txt", "w")
        for line in open("GSUCandidates.txt", "r").readlines():
            stored_candidates = line.split(",")
            if stored_candidates[0] == "President":
                f_president.write(line)
            elif stored_candidates[0] == "GSU Officer 1":
                f_office1.write(line)
            elif stored_candidates[0] == "GSU Officer 2":
                f_office2.write(line)
            elif stored_candidates[0] == "GSU Officer 3":
                f_office3.write(line)
            elif stored_candidates[0] == "Faculty Officer 1":
                f_faculty1.write(line)
            elif stored_candidates[0] == "Faculty Officer 2":
                f_faculty2.write(line)
            elif stored_candidates[0] == "Faculty Officer 3":
                f_faculty3.write(line)
            elif stored_candidates[0] == "Faculty Officer 4":
                f_faculty4.write(line)
            elif stored_candidates[0] == "Faculty Officer 5":
                f_faculty5.write(line)
            elif stored_candidates[0] == "Faculty Officer 6":
                f_faculty6.write(line)
            elif stored_candidates[0] == "Faculty Officer 7":
                f_faculty7.write(line)
            elif stored_candidates[0] == "Faculty Officer 8":
                f_faculty8.write(line)
            elif stored_candidates[0] == "Faculty Officer 9":
                f_faculty9.write(line)
            elif stored_candidates[0] == "Faculty Officer 10":
                f_faculty10.write(line)
            elif stored_candidates[0] == "Faculty Officer 11":
                f_faculty11.write(line)
            elif stored_candidates[0] == "Faculty Officer 12":
                f_faculty12.write(line)
            elif stored_candidates[0] == "Faculty Officer 13":
                f_faculty13.write(line)
            elif stored_candidates[0] == "Faculty Officer 14":
                f_faculty14.write(line)
            elif stored_candidates[0] == "Faculty Officer 15":
                f_faculty15.write(line)
            elif stored_candidates[0] == "Faculty Officer 16":
                f_faculty16.write(line)


# Kevin, John and Jericho
class RoleSelectionGUI:
    def __init__(self):
        self.window_selection = tkinter.Tk()
        self.window_selection.title("Vote Page")
        self.window_selection.resizable(False, False)    # Stops user from being able to resize the window.
        # self.window_selection.geometry("500x500")   # Changes the default size of the window.

        # First combobox containing the 3 primary positions and the button to submit choice.
        tkinter.Label(self.window_selection, text="Select the position you wish to vote for.").grid()
        self.available_positions = ["President", "GSU Officers", "Faculty Officers"]
        self.chosen_role = Combobox(self.window_selection, values=self.available_positions, state="readonly")
        # Sends feedback when the user has changed value in order to adjust the 2nd combobox values.
        # Reference for the support of implementing sub-combo-boxes:
        # https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-combobox/
        self.chosen_role.bind("<<ComboboxSelected>>", self.get_updated_value)
        self.chosen_role.grid(row=1)
        self.chosen_role.current(0)
        # Confirmation button that calls a method to prepare the files needed for the selected choice.
        # Also clears any potential objects stored in the candidates list.
        self.submit = tkinter.Button(self.window_selection, text="Submit",
                                     command=lambda: [self.choice_analysis(), self.candidates.clear()])
        self.submit.grid(row=1, column=1)

        self.candidates = []
        # Dictionary for the sub-combobox containing the places available.
        self.posts = {"President": [], "GSU Officers": ["1 - GSU Officer",
                                                        "2 - GSU Officer",
                                                        "3 - GSU Officer"], "Faculty Officers": ["1 - Faculty Officer",
                                                                                                                "2 - Faculty Officer",
                                                                                                                "3 - Faculty Officer",
                                                                                                                "4 - Faculty Officer",
                                                                                                                "5 - Faculty Officer",
                                                                                                                "6 - Faculty Officer",
                                                                                                                "7 - Faculty Officer",
                                                                                                                "8 - Faculty Officer",
                                                                                                                "9 - Faculty Officer",
                                                                                                                "10 - Faculty Officer",
                                                                                                                "11 - Faculty Officer",
                                                                                                                "12 - Faculty Officer",
                                                                                                                "13 - Faculty Officer",
                                                                                                                "14 - Faculty Officer",
                                                                                                                "15 - Faculty Officer",
                                                                                                                "16 - Faculty Officer"]}
        # Dictionary containing respective file names for each position.
        self.file_choice = {"President":"GSUCandidates_President.txt","1 - GSU Officer":"GSUCandidates_GSUOfficer1.txt",
                            "2 - GSU Officer":"GSUCandidates_GSUOfficer2.txt","3 - GSU Officer":"GSUCandidates_GSUOfficer3.txt",
                            "1 - Faculty Officer":"GSUCandidates_FacultyOfficer1.txt","2 - Faculty Officer":"GSUCandidates_FacultyOfficer2.txt",
                            "3 - Faculty Officer":"GSUCandidates_FacultyOfficer3.txt","4 - Faculty Officer":"GSUCandidates_FacultyOfficer4.txt",
                            "5 - Faculty Officer":"GSUCandidates_FacultyOfficer5.txt","6 - Faculty Officer":"GSUCandidates_FacultyOfficer6.txt",
                            "7 - Faculty Officer":"GSUCandidates_FacultyOfficer7.txt","8 - Faculty Officer":"GSUCandidates_FacultyOfficer8.txt",
                            "9 - Faculty Officer":"GSUCandidates_FacultyOfficer9.txt","10 - Faculty Officer":"GSUCandidates_FacultyOfficer10.txt",
                            "11 - Faculty Officer":"GSUCandidates_FacultyOfficer11.txt","12 - Faculty Officer":"GSUCandidates_FacultyOfficer12.txt",
                            "13 - Faculty Officer":"GSUCandidates_FacultyOfficer13.txt","14 - Faculty Officer":"GSUCandidates_FacultyOfficer14.txt",
                            "15 - Faculty Officer": "GSUCandidates_FacultyOfficer15.txt","16 - Faculty Officer":"GSUCandidates_FacultyOfficer16.txt"}
        # Second combobox containing the sub-positions or "places" for that position.
        # (e.g. 3 available posts for GSU Officer)
        tkinter.Label(self.window_selection, text="Select one (if any) places for that position.").grid(row=2)
        self.chosen_post = Combobox(self.window_selection, state="readonly")
        self.chosen_post.grid(row=3)
        self.button_close = tkinter.Button(self.window_selection, text="Exit", command=self.window_selection.destroy)
        self.button_close.grid(row=3, column=1)

        # Checks the vote's time eligibility. (Are they too early or too late to vote?)
        self.current_date = datetime.date.today()
        self.vote_start = datetime.date(2020, 1, 20)
        self.vote_end = datetime.date(2020, 1, 27)
        if self.current_date < self.vote_start:
            messagebox.showerror("Error!", "The election voting poll has not been open to the public yet. "
                                           "Please return on the: " + str(self.vote_start),
                                 parent=self.window_selection)
            self.window_selection.destroy()  # Closes the window.
        elif self.current_date > self.vote_end:
            messagebox.showerror("Error!", "The election voting poll has already ended.", parent=self.window_selection)
            self.window_selection.destroy()
        self.window_selection.mainloop()

    # Updates the sub-combobox list respectively with the value in the first combobox.
    def get_updated_value(self, event):
        if self.chosen_role.get() == "President":
            pass
        else:
            self.chosen_post["values"] = self.posts[self.chosen_role.get()]
            self.chosen_post.current(0)

    def choice_analysis(self):
        # Opens the file depending on the selected value in the combo-boxes.
        if self.chosen_role.get() == "President":
            f = open(self.file_choice[self.chosen_role.get()], "r")
            # Removes the value from the combobox so it cannot be selected again. - Updates the value and reassigns it.
            self.available_positions.remove(self.chosen_role.get())
            # Sets the current value to null (Basically removes it).
            self.chosen_role.set("")
            # Updates the values.
            self.chosen_role["values"] = self.available_positions
            self.chosen_role.current(0)
            self.get_updated_value(self.chosen_role.get())
        else:
            f = open(self.file_choice[self.chosen_post.get()], "r")
            self.posts[self.chosen_role.get()].remove(self.chosen_post.get())
            self.chosen_post["values"] = self.posts[self.chosen_role.get()]
            self.chosen_post.set("")
            if len(self.posts[self.chosen_role.get()]) != 0:
                self.chosen_post.current(0)

            if len(self.chosen_post.get()) == 0 and len(self.available_positions) > 1:
                print("TEST")
                self.available_positions.remove(self.chosen_role.get())
                self.chosen_role.set("")
                self.chosen_role["values"] = self.available_positions
                self.chosen_role.current(0)
                self.get_updated_value(self.chosen_role.get())
            elif len(self.chosen_post.get()) == 0 and len(self.available_positions) == 1:
                messagebox.showinfo("Thank you!", "After you finish that last vote, you'll have finished voting. "
                                                  "Thank you!", parent=self.window_selection)
                self.window_selection.destroy()

        # Converts all the relevant candidates into an object and stores it in a list called candidates.
        for line in f:
            position, first_name, last_name = line.strip("\n").split(",")
            self.candidates.append(Candidate(position, first_name, last_name))
        f.close()
        # Sorts the list into order by name.
        self.candidates.sort(key=lambda x: x.first_name)
        VoteCastGUI(self.candidates)


# Kevin and John
class VoteCastGUI:
    def __init__(self, candidates):
        # Defines the voting window.
        self.window_voting = tkinter.Tk()
        self.window_voting.title("Vote Page")
        self.window_voting.resizable(False, False)

        tkinter.Label(self.window_voting, text="Select your preferences").grid(column=1)
        # Declares some attributes.
        self.post = candidates[1].position
        self.candidate_names = []
        self.user_preferences = []
        self.current_votes = []
        # Merges first and last name together and stores it in candidate_name
        for candidate in candidates:
            self.candidate_names.append(candidate.first_name + " " + candidate.last_name)
        tkinter.Label(self.window_voting, text="Select your 1st preference").grid(row=1)
        self.preference_1 = Combobox(self.window_voting, values=self.candidate_names, state="readonly")
        self.preference_1.grid(row=1, column=1)

        tkinter.Label(self.window_voting, text="Select your 2nd preference").grid(row=2)
        self.preference_2 = Combobox(self.window_voting, values=self.candidate_names, state="readonly")
        self.preference_2.grid(row=2, column=1)

        tkinter.Label(self.window_voting, text="Select your 3rd preference").grid(row=3)
        self.preference_3 = Combobox(self.window_voting, values=self.candidate_names, state="readonly")
        self.preference_3.grid(row=3, column=1)

        tkinter.Label(self.window_voting, text="Select your 4th preference").grid(row=4)
        self.preference_4 = Combobox(self.window_voting, values=self.candidate_names, state="readonly")
        self.preference_4.grid(row=4, column=1)

        tkinter.Button(self.window_voting, text="Submit", command=self.check_entries).grid(row=5, column=1)

    def append_selection(self):
        self.user_preferences.clear()
        if len(self.preference_1.get()) != 0:
            self.user_preferences.append(self.preference_1.get())
        if len(self.preference_2.get()) != 0:
            self.user_preferences.append(self.preference_2.get())
        if len(self.preference_3.get()) != 0:
            self.user_preferences.append(self.preference_3.get())
        if len(self.preference_4.get()) != 0:
            self.user_preferences.append(self.preference_4.get())

    def check_entries(self):
        self.append_selection()
        if len(self.user_preferences) != 0:
            shown = False
            for i in range(len(self.user_preferences)):
                for j in range(i+1, len(self.user_preferences)):
                    if self.user_preferences[i] == self.user_preferences[j] and shown is False:
                        self.user_preferences.clear()
                        messagebox.showerror("Error!", "You cannot have duplicate entries in your vote.",
                                             parent=self.window_voting)
                        shown = True
                        break
                if shown is True:
                    break
            if shown is False:
                self.save_votes()
        else:
            messagebox.showerror("Error!", "You must select at least ONE candidate to submit.",
                                 parent=self.window_voting)

    def save_votes(self):
        f = open("Votes.txt", "a")
        f.write("%s,%s,%s,%s,%s \n" % (self.post, self.preference_1.get(), self.preference_2.get(),
                self.preference_3.get(), self.preference_4.get()))
        messagebox.showinfo("Summary", "Thank you, your vote has been submitted! Please remember to vote for the other "
                                       "available positions as well.", parent=self.window_voting)
        self.window_voting.destroy()


# James
class VotesProcessing:
    def __init__(self, required_position):
        # Peoples individual votes for their preferences are stored in votes.csv, these are then counted and put into
        # candidates_votes.txt. You then pick the position you want to find the winner for. The candidates are then put into
        # winner_ranking.txt where the winner is the first candidate in the file.
        self.required_position = required_position

        votes = open("Votes.txt", "r").readlines()  # Opens the file to read the students individual votes
        file2 = open("Calculated_Votes.txt", "w")  # Opens the file to write the votes each candidate received

        preferences = []
        candidate = ""
        counted_votes = []
        vote_data = []

        for line in votes:
            preferences.append((line.split(",")))

        # Gets all the roles that people have voted for
        unique_roles = []
        for unique in preferences:
            if unique[0] not in unique_roles:
                unique_roles.append(unique[0])

        def role_delete(role):  # Function to delete candidates from the list 'preferences' when given a position.
            def total_votes(roles):
                def count_votes(c):  # Function to add up the how many votes a candidate got for each preference.
                    p1 = 0
                    p2 = 0
                    p3 = 0
                    p4 = 0
                    for candidate_name in role_votes:  # Checks how many times a name appears for each preference
                        if names[c] == candidate_name[1]:
                            p1 += 1
                        elif names[c] == candidate_name[2]:
                            p2 += 1
                        elif names[c] == candidate_name[3]:
                            p3 += 1
                        elif names[c] == candidate_name[4]:
                            p4 += 1
                    return [roles, str(names[c]), str(p1), str(p2), str(p3), str(p4)]

                n = 0
                role_votes = []
                names = []
                for i in preferences:  # This loop puts all votes for a position into a new list
                    i[-1] = i[-1].strip()  # This removes the \n from the last value for each candidate
                    if preferences[n][0] == roles:
                        role_votes.append(preferences[n])
                        n += 1
                    else:
                        n += 1
                # This gets the individual names of each candidate for a position
                for individual in role_votes:
                    for name in individual:
                        if name not in names:
                            if len(name) > 2:  # Makes sure a blank space is not added to the list.
                                names.append(name)
                del names[0]  # removes the position value from the list
                count = 0
                # For each name their votes are added into the list vote_data
                for person in range(len(names)):
                    vote_data.append(count_votes(count))
                    count += 1

            position = 0
            total_votes(preferences[0][0])  # Adds up the candidates votes
            # Removes candidates once their votes have already been calculated
            for element in range(len(preferences)):
                if preferences[position][0] == role:
                    del preferences[position]
                else:
                    position += 1

        # For each role in the list preferences it will calculate each candidates votes for each preference
        for each_role in range(len(unique_roles)):
            if preferences[0][0] == "President":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "GSU Officer 1":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "GSU Officer 2":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "GSU Officer 3":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 1":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 2":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 3":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 4":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 5":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 6":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 7":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 8":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 9":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 10":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 11":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 12":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 13":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 14":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 15":
                role_delete(preferences[0][0])
            elif preferences[0][0] == "Faculty Officer 16":
                role_delete(preferences[0][0])

        # This writes each candidates votes to a file
        for item in vote_data:
            string_value = ",".join(item)  # This joins each value in the list with a comma
            file2.write("%s\n" % string_value)  # Makes it so that each candidate is on a new line
        file2.close()

        f = open("Calculated_Votes.txt", "r").readlines()  # Opens the text file with the candidates votes

        Role_candidates = []
        winner = []
        first_place = []

        def preference_1(elem):  # This gets the 1st preference votes and allows for a sort to occur
            return int(elem[1])

        def preference_2(elem):  # This gets the 2nd preference votes and allows for a sort to occur
            return int(elem[2])

        def preference_3(elem):  # This gets the 3rd preference votes and allows for a sort to occur
            return int(elem[3])

        def preference_4(elem):  # This gets the 4th preference votes and allows for a sort to occur
            return int(elem[4])

        def first_place_function():
            def win_function():  # This function works out who wins for the given position
                def role_tie(x):  # This function removes candidates from the list if they have votes less that the tie
                    i = 0
                    tie = int(winner[0][x])  # Puts the tie value into variable tie
                    for person in range(len(winner)):
                        if int(winner[i][x]) == tie:
                            i += 1
                        else:
                            del winner[
                                i: -1]  # All these candidates can be deleted as the list is sorted from high to low
                            del winner[-1]
                            break
                    return winner

                role_candidates = []
                winner = []
                re_election = 0
                for line in f:
                    candidate = (line.split(","))  # Puts each candidate from the text file into an embedded list
                    if candidate[0] == Position:
                        role_candidates.append(
                            candidate[1:6])  # Puts all the candidates of the given position into a list
                        winner = role_candidates
                winner.sort(key=preference_1,
                            reverse=True)  # Sorts the candidates with the 1st preference votes, high to low
                if winner[0][1] == winner[1][1]:  # Checks for a tie in 1st preference
                    winner = role_tie(1)  # gets the people who are tying
                    winner.sort(key=preference_2, reverse=True)  # Candidates sorted to see who wins from 2nd preference
                    if winner[0][2] == winner[1][2]:  # Checks for a tie in 2nd preference
                        winner = role_tie(2)  # gets the people who are tying
                        winner.sort(key=preference_3, reverse=True)
                        if winner[0][3] == winner[1][3]:  # Checks for a tie in 3rd preference
                            winner = role_tie(3)  # gets the people who are tying
                            winner.sort(key=preference_4, reverse=True)
                            if winner[0][4] == winner[1][4]:  # Checks for a tie in 4th preference
                                print("Tie, election needed.")  # In the unlikely event of a tie, a re election is needed
                                re_election = 1
                if re_election == 0:
                    return winner[0]  # Returns the candidate with the highest votes

            first_place = win_function()  # Puts the winner into variable first_place
            n = 0
            for line in f:
                candidate = (line.split(","))  # Puts each candidate from the text file into an embedded list
                if candidate[0] == Position:
                    Role_candidates.append(candidate[1:6])  # Puts all the candidates of the given position into a list
            # Removes the winning candidate from all the candidates for that position
            for person in range(len(Role_candidates)):
                if Role_candidates[n][0] == first_place[0]:
                    del Role_candidates[n]
                else:
                    n += 1
            # The remaining candidates are sorted
            Role_candidates.sort(key=preference_1, reverse=True)
            # The winner is put in the first position in the list
            Role_candidates.insert(0, first_place)
            # The list is then written to the file
            file = open("Winners_ranking.txt", "w")
            for item in Role_candidates:
                item[-1] = item[-1].strip()
                string_value = ",".join(item)
                file.write('%s\n' % string_value)
            file.close()
            return

        Position = self.required_position  # change this to get the winner for the different positions e.g. GSUOfficer1...

        if Position == "President":
            first_place_function()
        elif Position == "GSU Officer 1":
            first_place_function()
        elif Position == "GSU Officer 2":
            first_place_function()
        elif Position == "GSU Officer 3":
            first_place_function()
        elif Position == "Faculty Officer 1":
            first_place_function()
        elif Position == "Faculty Officer 2":
            first_place_function()
        elif Position == "Faculty Officer 3":
            first_place_function()
        elif Position == "Faculty Officer 4":
            first_place_function()
        elif Position == "Faculty Officer 5":
            first_place_function()
        elif Position == "Faculty Officer 6":
            first_place_function()
        elif Position == "Faculty Officer 7":
            first_place_function()
        elif Position == "Faculty Officer 8":
            first_place_function()
        elif Position == "Faculty Officer 9":
            first_place_function()
        elif Position == "Faculty Officer 10":
            first_place_function()
        elif Position == "Faculty Officer 11":
            first_place_function()
        elif Position == "Faculty Officer 12":
            first_place_function()
        elif Position == "Faculty Officer 13":
            first_place_function()
        elif Position == "Faculty Officer 14":
            first_place_function()
        elif Position == "Faculty Officer 15":
            first_place_function()
        elif Position == "Faculty Officer 16":
            first_place_function()
        else:
            print()


# Kevin
class ResultsGUI:
    candidates = []

    def __init__(self):
        # Declare a window GUI
        self.window_results = tkinter.Tk()
        self.window_results.title("Greenwich Student Union Election Results")
        self.window_results.resizable(False, False)
        # Declare a list to store all the candidates read from the file.
        # Add a Label and Combobox to choose which position the user wants to see.
        tkinter.Label(self.window_results, text="Select a position you wish to view:").grid()
        self.position_selection = Combobox(self.window_results, values=["President", "GSU Officers", "Faculty Officers"],
                                           state="readonly")
        self.position_selection.bind("<<ComboboxSelected>>", self.get_updated_value)
        self.position_selection.grid(row=0, column=1)
        # Defaults to the first value so that you can't select null.
        self.position_selection.current(0)
        # Creates a dictionary for the sub-combobox containing the places available.
        self.choices = {"President": [], "GSU Officers": ["GSU Officer 1", "GSU Officer 2", "GSU Officer 3"],
                        "Faculty Officers": ["Faculty Officer 1", "Faculty Officer 2", "Faculty Officer 3",
                                             "Faculty Officer 4", "Faculty Officer 5", "Faculty Officer 6",
                                             "Faculty Officer7", "Faculty Officer 8", "Faculty Officer 9",
                                             "Faculty Officer 10", "Faculty Officer 11", "Faculty Officer 12",
                                             "Faculty Officer 13", "Faculty Officer 14", "Faculty Officer 15",
                                             "Faculty Officer 16"]}
        self.chosen_post = Combobox(self.window_results, state="readonly")
        self.chosen_post.grid(row=1, column=1)

        # 'Select' button alongside the combobox. - Checks the input once pressed and clears the candidate list.
        tkinter.Button(self.window_results, text="Select",
                       command=lambda: [self.selection_check(), self.candidates.clear()]).grid(row=0, column=2)
        self.window_results.mainloop()

    # Updates the values of the sub-combobox when called.
    def get_updated_value(self, event):
        if self.position_selection.get() == "President":
            pass
        else:
            self.chosen_post["values"] = self.choices[self.position_selection.get()]
            self.chosen_post.current(0)

    def selection_check(self):
        if self.position_selection.get() == "President":
            # Pass the value of the primary combobox to A5 to process President.
            VotesProcessing(self.position_selection.get())
        else:
            # Pass the secondary combobox to A5 to process the sub-positions of the officers.
            VotesProcessing(self.chosen_post.get())
        f = open("Winners_Ranking.txt", "r")
        for line in f:
            name, pref_one, pref_two, pref_three, pref_four = line.split(",")
            self.candidates.append(CandidateResults(name, pref_one, pref_two, pref_three, pref_four))
        f.close()
        # Displays the winner, their total number of votes and the total overall number of votes.
        self.winner_summary()
        # Generates a table for the candidates.
        ResultsTable(tkinter.Toplevel())

    # Displays the winners, votes received and total votes casted below the comboboxes.
    def winner_summary(self):
        self.winner = tkinter.StringVar(self.window_results, value="Winner: " + str(self.candidates[0].name))
        Label(self.window_results, textvariable=self.winner).grid(row=2, column=1)
        self.votes_received = tkinter.StringVar(self.window_results, value="Votes Received: " + str(self.candidates[0].pref_one))
        Label(self.window_results, textvariable=self.votes_received).grid(row=3, column=1)
        self.overall_votes = tkinter.StringVar(self.window_results, value="Total Votes Casted: " + str(self.total_votes()))
        Label(self.window_results, textvariable=self.overall_votes).grid(row=4, column=1)

    def total_votes(self):
        votes = 0
        for candidate in self.candidates:
            votes += int(candidate.pref_one)
        return str(votes)


# Kevin
class ResultsTable(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.create_ui()
        self.load_table()
        self.grid(sticky=(N, S, W, E))
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

    # Creates a table and adjusts the overall size of the grid surrounding the generated table.
    def create_ui(self):
        tv = Treeview(self)
        tv['columns'] = ('1st Preference', '2nd Preference', '3rd Preference', '4th Preference')
        tv.heading("#0", text="Candidates", anchor="w")
        tv.column("#0", anchor="w")
        tv.heading("1st Preference", text="1st Preference")
        tv.column("1st Preference", anchor="center", width=100)
        tv.heading("2nd Preference", text="2nd Preference")
        tv.column("2nd Preference", anchor="center", width=100)
        tv.heading("3rd Preference", text="3rd Preference")
        tv.column("3rd Preference", anchor="center", width=100)
        tv.heading("4th Preference", text="4th Preference")
        tv.column("4th Preference", anchor="center", width=100)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_table(self):
        for candidate in ResultsGUI.candidates:
            self.treeview.insert('', 'end', text=candidate.name,
                                 values=(candidate.pref_one, candidate.pref_two,
                                         candidate.pref_three, candidate.pref_four))
        ResultsGUI.candidates.clear()


StartingGUI()
