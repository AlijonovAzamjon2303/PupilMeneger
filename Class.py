class Pupil:
    def __init__(self, ism, fam, yil, gpa):
        self.ism = ism
        self.fam = fam
        self.yil = yil
        self.gpa = gpa

    def get_info(self):
        return f"Ism: {self.ism} Fam: {self.fam} Yil: {self.yil} GPA: {self.gpa}"


class PupilManager:
    def __init__(self):
        self.pupils = []

    def add_pupil(self, pupil):
        self.pupils.append(pupil)

    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())

    def get_max_gpa(self):
        gpa = 0
        for pupil in self.pupils:
            if pupil.gpa > gpa:
                gpa = pupil.gpa

        return gpa

    def change_gpa(self, ism, fam, new_gpa):
        for pupil in self.pupils:
            if pupil.ism == ism and pupil.fam == fam:
                pupil.gpa = new_gpa


pupil1 = Pupil("Sarvar", "Ismatullayev", 2008, 70)
pupil2 = Pupil("Chingiz", "Shukurov", 2008, 75)

manager = PupilManager()

manager.add_pupil(pupil1)
manager.add_pupil(pupil2)
manager.change_gpa("Chingiz", "Shukurov", 80)


manager.get_pupils()