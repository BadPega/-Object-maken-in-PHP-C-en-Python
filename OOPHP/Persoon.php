<?php 
class Persoon {
    private $naam;
    private $leeftijd;
    private $geslacht;
    private $isStudent;
    private $gemiddeldCijfer;
  
    public function __construct($naam, $leeftijd, $geslacht, $isStudent, $gemiddeldCijfer) {
      $this->naam = $naam;
      $this->leeftijd = $leeftijd;
      $this->geslacht = $geslacht;
      $this->isStudent = $isStudent;
      $this->gemiddeldCijfer = $gemiddeldCijfer;
    }
}