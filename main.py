import requests
import bs4
import telebot

res = requests.get('https://internfreak.co/jobs-and-internship-opportunities?page=1&limit=15')
soup = bs4.BeautifulSoup(res.text, 'lxml')

h1 = soup.select('.post-entry .heading a')
Batch = soup.select('p')
Category = soup.select('.post-entry .post-meta .category')

count = 0
serial = 1
my_list = []

while (count < 8):   
    a= str(serial) +". "+ h1[count].getText()
    b= Batch[count].getText()
    c= Category[count].getText()
    
    n=a+'\n'+b +'\n'+'#'+c+'\n'
    my_list.append(n)
    serial = serial +1
    count = count + 1


Content1 = '#SDE, Associate Engineer, Full Time Remote OFF Campus #Jobs and #Internships Opportunities for the batch of 2023, 2022.! \n \n Please #like/comment/share/Tag Your friends to reach those who might be interested. \n \n Visit internfreak.co \n \n'

Main ='\n'.join(my_list)
Content2 = "And much more! Only on internfreak.co \n \n Join the telegram channel for regular updates: https://bit.ly/31kyfMi (If the link doesn't work, look up InternFreak on the telegram app.) \n \n #letssupportfreshers #offcampus #Jobs4u #offcampusdrive #Internships #Jobsforfreshers #softwareengineer #fullstackdeveloper #freshershiring #hiring #recruitment #opportunities #internfreak #faang #dell #offcampus"


displaylinkedin = Content1 + Main + Content2 

# dusre bot ka code

# -------------



# -------------
printop =soup.find_all('a')[6]
lamba = str(printop)
end = len(lamba)-len(h1[0].getText())-6
url='https://internfreak.co/'+lamba[9:end]

res2 = requests.get(url)
soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
ctc = soup2.select('h5')
ctc_number = soup2.select('p')

displaytelegram = h1[0].getText()+"\n"+"\n" + Batch[0].getText()+ "\n"+ctc[2].getText() +" "+ctc_number[3].getText()+"\n"+"\n" +"Know More: "+ url
# -----------


bot = telebot.TeleBot("1742051172:AAEI7Mv-5oYeMpGTfMOE-vkTeeEK2TppByU")

@bot.message_handler(commands=['1'])
def greet1(message1):
  bot.send_message(message1.chat.id, displaytelegram)

@bot.message_handler(commands=['2'])
def greet(message):
  bot.send_message(message.chat.id, displaylinkedin)
bot.polling()







