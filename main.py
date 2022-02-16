import os
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


displayk = Content1 + Main + Content2 

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

@bot.message_handler(commands=['l2'])
def greet(message):
  bot.send_message(message.chat.id, displayk)
bot.polling()




