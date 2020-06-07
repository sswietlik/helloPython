drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'
path = drive + folder + file
print(path)

justText = "text with\nnewline"   #wyświetla po backslashu w nowej linii
print(justText)

justText = r"text with\nnewline"   #użycie  R przed tekstem sprawia że
                                    # wyświetlany jest surowy tekst i tak jest traktowany backslash
print(justText)

justText="Mc Donald's"
print(justText)

justText='Mc Donald\'s'     #jeśli niechcę używać cudzysłowa a pojedynczy apostrof
                           # to apostrof należy poprzedzić backslash
print(justText)
