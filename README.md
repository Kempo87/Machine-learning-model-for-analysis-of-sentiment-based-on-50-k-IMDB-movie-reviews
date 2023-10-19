# OPIS PROGRAMU: 
<p align="justify">
program napisany w języku python, który służy do analizy sentymentu (nastroju) tekstu. Pomaga przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu można automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności pomaga w zidentyfikowaniu tych najbardziej pozytywnych i negatywnych wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu można udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będzie można odpowiednio wcześniej zareagować i odpowiedzieć na niego, zanim taki komentarz dotrze do szerszego grona.
</p>

## Program wczytuje recenzje filmów:

Wczytuje pozytywne recenzje z plików tekstowych znajdujących się w katalogu "positive_reviews".

Wczytuje negatywne recenzje z plików tekstowych znajdujących się w katalogu "negative_reviews".


### Program prosi użytkownika o wprowadzenie własnego komentarza (np. "This is a wonderful movie").

#### Analiza sentymentu komentarza:


Komentarz użytkownika jest analizowany pod kątem sentymentu.


Słowa z komentarza są przekształcane na małe litery, a ewentualne znaczniki HTML, takie jak < br / >, są zamieniane na spacje.


Dla każdego słowa w komentarzu program oblicza sentyment na podstawie wczytanych wcześniej recenzji.
<p align="justify">
Sentyment jest liczony jako różnica między ilością wystąpień danego słowa w pozytywnych i negatywnych recenzjach, podzielona przez sumę tych wystąpień. Wartość sentymentu mieści się w przedziale od -1 do 1.
</p>

##### Wynik analizy sentymentu:
<p align="justify">
Program wyświetla sentyment każdego słowa w komentarzu.
Na podstawie sentymentu słów w komentarzu program oblicza średni sentyment całego komentarza.
Program określa, czy komentarz jest pozytywny (sentyment > 0) lub negatywny (sentyment <= 0).
Wynik jest wyświetlany w postaci komunikatu, który informuje użytkownika, czy komentarz jest pozytywny czy negatywny, oraz podaje wartość sentymentu.
Program ten może być używany do analizy sentymentu tekstów na podstawie wczytanych recenzji. Jego wyniki mogą pomóc w ocenie, czy dany tekst jest pozytywny czy negatywny.
</p>
