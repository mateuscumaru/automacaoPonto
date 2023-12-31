from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from teste_ponto import retorna_ponto


class MeusDados:
    def __init__(self):
        self.login = "" # Sua matricula aqui
        self.senha = "" # Sua senha aqui
        self.url_portal = "" # URL do Portal de ponto


meusDados = MeusDados()

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(meusDados.url_portal)

inputElement = driver.find_element(By.ID, "txtUser")
inputElement.send_keys(meusDados.login)

inputElement = driver.find_element(By.ID, "txtPass")
inputElement.send_keys(meusDados.senha)
inputElement.send_keys(Keys.ENTER)

portalButton = driver.find_element(By.XPATH, '//*[@id="ctl18_REC_titleControl"]')
portalButton.click()

pontoButton = driver.find_element(By.XPATH, '//*[@id="ctl09_ctl00_tvAccordionContents_ctl00_ctl04__CaptionCell"]/a/span')
pontoButton.click()

# Tentando pegar pelos dias que estou com falta
# def qtd_faltas():
#     cont1 = 0
#     for j in range(2, 29):
#         text_faltas = driver.find_element(By.XPATH, '//*[@id="ctl26_gridEspelhoCartao_gridEspelhoCartao"]/tbody/tr[%s]/td[16]' % j)
#         if text_faltas.text == '08:00':
#             cont1 += 1
#
#     return cont1


# horarios_ponto = retorna_ponto(qtd_faltas())
#
# print(qtd_faltas())
# print(horarios_ponto)

anexosButton = driver.find_element(By.XPATH, '//*[@id="ctl26_ctl01_ctl01"]')
anexosButton.click()

window_before = driver.window_handles[0]
# print(window_before)

entradaBatidaButton = driver.find_element(By.XPATH, '//*[@id="ctl26_ctl01_ctl09"]/tbody/tr/td[2]/span')
entradaBatidaButton.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.maximize_window()
# print(window_after)

justificativaElement = driver.find_element(By.ID, 'GB_txtJustificativa')
if justificativaElement.get_attribute('value') == '':
    justificativaElement.send_keys('Home Office')

'''
for x in range(33):
    print('GB_l%s_lblData / GB_l%s_lblDia / GB_l%s_txtEnt1 / GB_l%s_txtSai1' % (x, x, x, x))
'''


def qtd_dias_uteis():
    cont = 0

    for m in range(30):
        text_button = driver.find_element(By.ID, 'GB_l%s_lblDia' % m)
        if text_button.text != 'SÁB' and text_button.text != 'DOM':
            cont += 1

    return cont


horarios_ponto = retorna_ponto(qtd_dias_uteis())

print(horarios_ponto)

i = 0
j = 0

for n in range(30):
    text_button2 = driver.find_element(By.ID, 'GB_l%s_lblDia' % n)
    pontoEnt = driver.find_element(By.ID, 'GB_l%s_txtEnt1' % n)
    pontoSai = driver.find_element(By.ID, 'GB_l%s_txtSai1' % n)

    if text_button2.text != 'SÁB' and text_button2.text != 'DOM':
        '''
        print(textButton.text)
        print(pontoEnt.get_attribute('value'))
        print(pontoSai.get_attribute('value'))
        print(horarios_ponto[i][j])
        print(horarios_ponto[i][j+1])
        '''
        if pontoEnt.get_attribute('value') == '':
            pontoEnt.send_keys(horarios_ponto[i][j])
        if pontoSai.get_attribute('value') == '':
            pontoSai.send_keys(horarios_ponto[i][j+1])
        i += 1

# saveButton = driver.find_element(By.XPATH, '//*[@id="GB_btnSalvar_tblabel"]')
# saveButton.click()

# driver.close()

# driver.switch_to.window(window_before)
# driver.close()
