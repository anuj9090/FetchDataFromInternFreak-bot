import requests
import bs4
import telebot
from time import sleep
from telebot import types

bot = telebot.TeleBot("1866658555:AAG4WdgzUVE3o0pwaE4r2JZEiY99i5Unul5")

@bot.message_handler(commands=['start'])
def gree(msg):
#   print(msg)
  markup = types.ReplyKeyboardMarkup(row_width=3)
  itembtn1 = types.KeyboardButton('/Show_latest_post')
  itembtn2 = types.KeyboardButton('/Show_recently_added_posts')
  itembtn4 = types.KeyboardButton('/start')
  markup.add(itembtn1, itembtn2, itembtn4)
  bot.send_message(msg.chat.id, "Hi "+ msg.chat.first_name +",\nIt's the InternFreak bot and here's what I can do.😀", reply_markup=markup)

@bot.message_handler(commands=['Show_latest_post'])
def greet1(message1):
  res = requests.get('https://internfreak.co/jobs-and-internship-opportunities?page=1&limit=15')
  soup = bs4.BeautifulSoup(res.text, 'lxml')
  h1 = soup.select('.post-entry .heading a')
  Batch = soup.select('p')
 
  printop =soup.find_all('a')[6]
  lamba = str(printop)
  end = len(lamba)-len(h1[0].getText())-6
  url='https://internfreak.co/'+lamba[9:end]
  
  res2 = requests.get(url)
  soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
  ctc = soup2.select('h5')
  ctc_number = soup2.select('p')
  displaytelegram = h1[0].getText()+"\n"+"\n"+ Batch[0].getText()+ "\n"+ctc[2].getText() +" "+ctc_number[3].getText()+"\n"+"\n" +"Know More: "+ url
  displaylinkdin  = h1[0].getText()+"\n"+ Batch[0].getText()+ "\n"+ctc[2].getText() +" "+ctc_number[3].getText()+"\n"+"\n" +"Know More: "+ url
  # -----------
  linkedinKaMaal ="\n"+"\n"+"Join Discussion group for any doubts. ( https://t.me/chatter007)"+"\n"+"\n"+"Join the telegram channel to get the latest updates fast: https://bit.ly/3xlNvT0" + "\n"+"\n"+"Follow our page for more updates and do like/share the post to reach those who might be interested."+"\n"
  hastags="\n"+"#like #recruiting #softwareengineer #careers #boeing #helpinghands #fresher #hiring #jobs #recruitment #jobsearch #internship #jobhunt2021 #intern2021 #job #internship #international #studygram #employment #engineering #engineer #jobs #vacancy #staysafe #instagood #intern #india #millennials #postoftheday #post #professional #technology #tech #students #poster #awareness #lifestyle #developer #softwaredeveloper #enterpreneur #sony #viralpost #viral #hustlers #acies #faang #amazon #google #facebook #netflix #apple #dxctechnology #texasinstruments #adobe #adobehiring #dropbox #googlehiring #amazingcompany #educational #tcs #facebookads #comment #highpayingjobs #amount"

  bot.send_message(message1.chat.id, displaytelegram)
  sleep(4)   
  bot.send_message(message1.chat.id, displaylinkdin+linkedinKaMaal+hastags)

@bot.message_handler(commands=['Show_recently_added_posts'])

def greet(message):
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
  bot.send_message(message.chat.id, displaylinkedin)

bot.polling()







