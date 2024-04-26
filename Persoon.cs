using System;

class Persoon
    
    private string naam;
    private int leeftijd;
    private char geslacht;
    private bool isStudent;
    private double gemiddeldCijfer;

    public Persoon(string naam, int leeftijd, char geslacht, bool isStudent, double gemiddeldCijfer)
    {
        this.naam = naam;
        this.leeftijd = leeftijd;
        this.geslacht = geslacht;
        this.isStudent = isStudent;
        this.gemiddeldCijfer = gemiddeldCijfer;
    }
