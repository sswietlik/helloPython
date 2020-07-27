# /home/slavo/temp/
# /home/slavo/temp/data_input/

import os
import datetime

                                ##W zmiennej data_input_catalog zapamiętaj ścieżkę 'c:\temp\data_input'
data_input_catalog = r'/home/slavo/temp/data_input/'

                                #W zmiennej data_output_catalog zapamiętaj ścieżkę 'c:\temp\data_output'
data_output_catalog = r'/home/slavo/temp/data_output/'

                                #W zmiennej today zapisz dzisiejszą datę
today = datetime.date.today()

                                #Połącz ścieżkę znajdującą się w data_output_catalog
                                # z napisem w postaci ROK-MIESIAC-DZIEŃ wyliczoną w oparciu o  następujące wyrażenie
                                # today.strftime("%Y-%m-%d")
today_output_catalog = os.path.join(data_output_catalog,today.strftime('%Y-%m-%d'))

                                #W zmiennej is_input_catalog_ok zapisz wynik testu sprawdzającego
                                # czy katalog data_input_catalog ISTNIEJE i jest katalogiem
is_input_catalog_ok = os.path.isdir(data_input_catalog)

                                #W zmiennej is_output_catalog_ok zapisz wynik testu sprawdzającego
                                # czy katalog data_output_catalog ISTNIEJE i jest katalogiem
is_output_catalog_ok = os.path.isdir(data_output_catalog)

                                #W zmiennej is_today_output_catalog_ok zapisz wynik testu sprawdającego czy
                                # today_output_catalog NIE ISTNIEJE ani jako plik ani jako katalog
is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and not(os.path.isfile(today_output_catalog))


                                #Jeżeli wynik wszystkich 3 wyżej wymienionych testów
                                # jest poprawny, to wyświetl komunikat 'Conditions met! We can continue!'
if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok :
    print('Conditions met! We can continue!')

                                #W przeciwnym razie wyświetl komunikat o błędzie, a następnie
                                # w zależności od wartości logicznej zmiennych is_...._ok wyświetl,
                                # co dokładnie jest nie tak (np brak katalogu input lub output itp)
else:
    print('Prerequisites not met! Check the paths!')

                                #display detailed error conditions
    if not is_input_catalog_ok:
        print('Input catalog %s must exist' % data_input_catalog)
    if not is_output_catalog_ok:
        print('Output catalog %s must exist!' % data_output_catalog)
    if not is_today_output_catalog_ok:
        print('Today output %s cannot exist (neither as file and dir)' %today_output_catalog)



