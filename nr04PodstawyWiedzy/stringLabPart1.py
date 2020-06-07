quote="A good programmer is someone who always looks both ways before crossing a one-way street"
print(quote.upper()) #wyświetl quote tylko wielkimi literami
print(quote.lower()) #wyświetl quote tylko małymi literami
print(quote.endswith('street')) #czy tekst kończy się  'street'
print(quote.isupper()) #czy tekst jest zapisany wielkimi literami
print(quote.upper().isupper()) #powiększ tekst a następnie sprawdź czy jest napisany dużymi literami
print(quote.find('one')) #znajdź pozycję na której znajduje się słowo 'one'
print(quote.replace('one','1')) #podmień w tekście słowo 'one' na '1'
print(quote.replace('one','1').replace('both','2')) #podmień w tekście słowo 'one' na '1' a 'both' na '2'
print(quote.split(' ')) #rozdziel napisy ze wzgl na spacje
print(quote.isdigit(),quote.isdecimal(),quote.isalpha(),quote.isalnum())
 #sprawdź jednym ciągiem czy quote jest : liczbą, liczbą dziesietną, napisem bez cyfr, napisem z literami i cyframi

