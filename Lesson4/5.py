whole_list = [[1,2,3], ["Lili", "Olha", "Pavlo"], ["Monday", "Sunday", "Friday"]]  # create a list of three lists
print("List  of three lists {}".format(whole_list))

whole_list[1][0] = "Nina"  # update one of elements inside of this list
print("Updated list {}".format(whole_list))

new_list = [1, 2, 4, {"Lili": "QA", "Olha": "Middle QA"}]  # create list with dict inside
print("List with dict inside {}".format(new_list))

wall_list = {"name": "one", "surname": "two"}
small_list = [1, 2, 3]
wall_list.update({"surname": small_list})
print("Dict with list inside {}".format(wall_list))  # Dict with list inside



