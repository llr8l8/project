class Eployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_voild_postition(position):
        voild_position = {"manger", "casher", "cook", "jantior"}
        return position in voild_position

ep1=Eployee("ali","manger")
ep2=Eployee("ahmed","cook")
print(ep2.get_info())
print(Eployee.is_voild_postition("cook"))

