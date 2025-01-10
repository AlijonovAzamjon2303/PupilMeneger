class Pupil:
    def __init__(self, ism, fam, yosh, gpa):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh
        self.gpa = gpa

    def get_info(self):
        return f"Ism: {self.ism} Fam: {self.fam} Yosh: {self.yosh} GPA: {self.gpa}"


class PupilManager:
    def __init__(self):
        self.pupils = []

    def add_pupil(self, ism, fam, yosh, gpa):
        new_pupil = Pupil(ism, fam, yosh, gpa)
        self.pupils.append(new_pupil)

    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())

    def max_gpa(self):
        gpa = 0

        for pupil in self.pupils:
            if pupil.gpa > gpa:
                gpa = pupil.gpa

        return gpa


manager = PupilManager()

manager.add_pupil("Azamjon", "Alijonov", 18, 85)
manager.add_pupil("Javohir", "Imomaliyev", 18, 70)
manager.add_pupil("Badriddin", "Baxtiyorov", 18, 80)

print(manager.max_gpa())
