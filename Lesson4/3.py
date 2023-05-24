empty = dict()
print(type(empty))

info = {"Lili": "QA", "Olha": "Middle QA"}
print(info)
info["Pavlo"] = "designer"
print(info)

info.update({"Lili": "QA", "Olha": "Middle QA"})
print(info)

info.pop("Olha")
print(info)

info.popitem()
print(info)

new_info = dict(info)
print(new_info)

info["Monna"] = "video editor"
print(info)
print(new_info)

