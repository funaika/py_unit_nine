from dog import Dog


class Pack:
    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].getName()

    def add_member(self, new_dog: Dog):
        self.members.append(new_dog)

    def print_pack(self):
        print("The pack contains:")
        for dog in self.members:
            print(dog.getName())

    def new_leader(self, new_leader_index):
        if 0 <= new_leader_index < len(self.members) and new_leader_index != self.leader_index:
            old_leader_name = self.get_leader_name()
            self.leader_index = new_leader_index
        else:
            print("That is not a valid dog.")

    def perform_trick(self, trick_name):
        for dog in self.members:
            dog.do_trick(trick_name)

    def all_print_tricks(self):
        print("Individual tricks performed:")
        for dog in self.members:
            dog.print_tricks()
        print("All dogs perform together:")
        self.perform_trick("all")

dog1 = Dog("Spot")
dog2 = Dog("Daisy")
dog3 = Dog("Peanut")
pack = Pack(dog1)
pack.add_member(dog2)
pack.add_member(dog3)

print(pack)
pack.print_pack()

pack.new_leader(1)
pack.perform_trick("sit")
pack.all_print_tricks()

