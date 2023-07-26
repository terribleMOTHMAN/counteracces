import requests
from bs4 import BeautifulSoup


def pars(
        url="https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205531612323126&prior=any&documentType=any&accepted=0&onlyHPAll=0&onlyHPfirst=1&acceptedEntrant=any&onlyActive=1&onlyPaid=0"):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')

    data = []

    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 0:
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            data.append(row_data)

    head = data[0]
    result = {}
    for i in range(1, len(data)):
        result[data[i][1]] = {'приоритет': data[i][2], 'сумма': int(data[i][10])}
    output = [[head[0], head[1], head[2], 'Сумма_баллов']]
    k = 0
    for i in result.keys():
        k += 1
        output.append([str(k), i, result[i]['приоритет'], str(result[i]['сумма'])])
    return output