import re

def Curs_7_2():
    with open('data.txt') as file:
        text = file.read()
    
    format_ora = re.findall('[0-2][0-3]:[0-5][0-9]', text)
    format_data = re.findall(r'\d{0,2}/[a-z]{3}/\d{2,4}', text)
    
    numere = re.findall(r'-?[^:/\n]\d*\,?\.?\d+e?\d*', text)
    majuscula = re.findall(r'\b [A-Z]+[A-Za-z]+\b', text)

    return str(format_ora) + '\n' + str(format_data) + '\n' + str(numere) + '\n' + str(majuscula)


with open('data.txt') as file:
        text = file.read()

if __name__ == "__main__":
        
    pattern = re.compile(r'^-?\d+(,\d+)*(\.\d+(e\d+)?)?$')

    format_ora = re.findall('[0-2][0-3]:[0-5][0-9]', text)
    format_data = re.findall(r'\d{0,2}/[a-z]{3}/\d{2,4}', text)
    
    numere = re.findall(r'-?[^:/\n]\d*\,?\.?\d+e?\d*', text)
    majuscula = re.findall(r'\b [A-Z]+[A-Za-z]+\b', text)

    print(format_ora)
    print(format_data)
    print(numere)
    print(majuscula)

    # matches = pattern.finditer(text)
    # for match in matches:
    #     print(match)
