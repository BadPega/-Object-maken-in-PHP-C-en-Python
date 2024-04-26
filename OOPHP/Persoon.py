class Persoon:
  def __init__(self, naam, leeftijd, geslacht, is_student, gemiddeld_cijfer):
    self.naam = naam
    self.leeftijd = leeftijd
    self.geslacht = geslacht
    self.is_student = is_student
    self.gemiddeld_cijfer = gemiddeld_cijfer

  def __str__(self):
    return f"Naam: {self.naam}\nLeeftijd: {self.leeftijd}\nGeslacht: {self.geslacht}\nStudent: {'Ja' if self.is_student else 'Nee'}\nGemiddeld cijfer: {self.gemiddeld_cijfer}"
