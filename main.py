import os
import requests
import bs4
import telebot
import random
from time import sleep
from telebot import types
import urllib.request
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import re


my_secret = os.environ.get('BotKey')
bot = telebot.TeleBot(my_secret )

@bot.message_handler(commands=['start'])
def gree(msg):
#   print(msg)
  markup = types.ReplyKeyboardMarkup(row_width=2)
  itembtn1 = types.KeyboardButton('/Show_latest_post')
  itembtn2 = types.KeyboardButton('/Show_recently_added_posts')
  itembtn4 = types.KeyboardButton('/start')
  itembtn5 = types.KeyboardButton('/Toss_A_Coin')

  markup.add(itembtn1, itembtn2, itembtn4, itembtn5)
  bot.send_message(msg.chat.id, "Hi "+ msg.chat.first_name +"\nIt's the InternFreak bot and here's what I can do.😀", reply_markup=markup)

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
  designation = soup2.select('p')[1].getText()
  location= soup2.select('h5')[3].getText()
  locationName=soup2.select('p')[5].getText()

  ctc = soup2.select('h5')
  ctc_number = soup2.select('p')
  displaytelegram = h1[0].getText()+"\n"+"\n"+ Batch[0].getText()+ "\n"+ctc[2].getText() +" "+ctc_number[3].getText()+"\n"+"\n" +"Know More: "+ url
  displaylinkdin  = h1[0].getText()+"\n"+ Batch[0].getText()+ "\n"+ctc[2].getText() +" "+ctc_number[3].getText()+"\n"+"\n" +"Know More: "+ url
  # -----------
  linkedinKaMaal ="\n"+"\n"+"Join The Telegram Channel To Get The Latest Updates: https://bit.ly/3xlNvT0" + "\n"+"\n"+"Follow our page for more updates and do like/share the post to reach those who might be interested."+"\n"
  hastags="\n"+"#like #recruiting #softwareengineer #careers #boeing #helpinghands #fresher #hiring #jobs #recruitment #jobsearch #internship #jobhunt2021 #intern2021 #job #internship #international #studygram #employment #engineering #engineer #jobs #vacancy #staysafe #instagood #intern #india #millennials #postoftheday #post #professional #technology #tech #students #poster #awareness #lifestyle #developer #softwaredeveloper #enterpreneur #sony #viralpost #viral #hustlers #acies #faang #amazon #google #facebook #netflix #apple #dxctechnology #texasinstruments #adobe #adobehiring #dropbox #googlehiring #amazingcompany #educational #tcs #facebookads #comment #highpayingjobs #amount"
  
  urlImgSlice=str(soup.find_all('a')[5])

  if ' ' in locationName:
    image_url = "http://3.108.247.213/uploads/"+  urlImgSlice[end+51:-8].replace(" ", "%20")
  else:
    image_url = "http://3.108.247.213/uploads/"+  urlImgSlice[end+51:-8]

  urllib.request.urlretrieve(image_url,"logoImg.png")
  
  orgimg = Image.open("logoImg.png").convert("RGBA")

  img2=orgimg.resize((422, 159))

  img = Image.open('./template.png')

  space=" "

  I1 = ImageDraw.Draw(img)
    # Custom font style and font size
  myFont = ImageFont.truetype('./OpenSans-ExtraBold.ttf', 40)
    # Add Text to an image
  designation_length = len(re.findall(r'\w+', designation))

  if len(urlImgSlice[end+51:-12].split())>1 :
    I1.text((500, 485),urlImgSlice[end+51:-12] +space+"Is", font=myFont, fill=(0, 0, 0))
    I1.text((570, 545), "Hiring  !", font=myFont, fill=(0, 0, 0))
  else:
    if designation_length ==1 :
      I1.text((500, 485),urlImgSlice[end+51:-12] +space+"Is Hiring ", font=myFont, fill=(0, 0, 0))
      I1.text((570, 545),   designation , font=myFont, fill=(0, 0, 0))
    if designation_length ==2 :
          
      I1.text((500, 485),urlImgSlice[end+51:-12]  +space+"Is Hiring ", font=myFont, fill=(0, 0, 0))
      I1.text((500, 545),   designation , font=myFont, fill=(0, 0, 0))
    if designation_length ==3 :  
    
      I1.text((480, 425),urlImgSlice[end+51:-12]  +space+"Is Hiring ", font=myFont, fill=(0, 0, 0))
      I1.text((480, 485),   designation.split()[0]+space+designation.split()[1], font=myFont, fill=(0, 0, 0))
      I1.text((580, 545),   designation.split()[2] , font=myFont, fill=(0, 0, 0))

    if designation_length ==4 :  
    
      I1.text((480, 425),urlImgSlice[end+51:-12]  +space+"Is Hiring ", font=myFont, fill=(0, 0, 0))
      I1.text((480, 485),   designation.split()[0]+space+designation.split()[1], font=myFont, fill=(0, 0, 0))
      I1.text((480, 545),   designation.split()[2]+space+designation.split()[3] , font=myFont, fill=(0, 0, 0))  
      
    if designation_length ==5 :  
    
      I1.text((480, 425),urlImgSlice[end+51:-12]  +space+"Is Hiring ", font=myFont, fill=(0, 0, 0))
      I1.text((480, 485),   designation.split()[0]+space+designation.split()[1], font=myFont, fill=(0, 0, 0))
      I1.text((480, 545),   designation.split()[2]+space+designation.split()[3]+designation.split()[4] , font=myFont, fill=(0, 0, 0))        
  
  I2 = ImageDraw.Draw(img)  
# Custom font style and font size
  myFont = ImageFont.truetype('./OpenSans-ExtraBold.ttf', 30)
    # Add Text to an image
  batch_length = len(re.findall(r'\w+', Batch[0].getText()))
  locationName_length = len(re.findall(r'\w+', locationName))
  
  if batch_length >=4:  
    
    if locationName_length==4:
      I2.text((550, 790), location,font=myFont, fill=(47, 92, 130))
      I2.text((425, 840), locationName,font=myFont, fill=(47, 92, 130))
    if locationName_length==3:
      I2.text((550, 790), location,font=myFont, fill=(47, 92, 130))
      I2.text((470, 840), locationName,font=myFont, fill=(47, 92, 130))
    if locationName_length==2:
      I2.text((550, 790), location,font=myFont, fill=(47, 92, 130))
      I2.text((510, 840), locationName,font=myFont, fill=(47, 92, 130))  
    if locationName_length==1:
      I2.text((480, 790), location+space+locationName,font=myFont, fill=(47, 92, 130))

  else:
    
    if locationName_length==4:
      I2.text((550, 720), location,font=myFont, fill=(47, 92, 130))
      I2.text((425, 780), locationName,font=myFont, fill=(47, 92, 130))    
    if locationName_length==3:
      I2.text((550, 720), location,font=myFont, fill=(47, 92, 130))
      I2.text((470, 780), locationName,font=myFont, fill=(47, 92, 130))
    if locationName_length==2:
      I2.text((550, 720), location,font=myFont, fill=(47, 92, 130))
      I2.text((510, 780), locationName,font=myFont, fill=(47, 92, 130))       
    if locationName_length==1:
      I2.text((480, 720), location+space+locationName,font=myFont, fill=(47, 92, 130))
   
  I3 = ImageDraw.Draw(img)  
# Custom font style and font size
  myFont = ImageFont.truetype('./OpenSans-ExtraBold.ttf', 30)
  
  
  if 'Batch' in Batch[0].getText():
    
    if batch_length ==2:
      I3.text((530, 650), Batch[0].getText(), font=myFont, fill=(47, 92, 130))
    if batch_length ==3:
      I3.text((530, 650), Batch[0].getText(), font=myFont, fill=(47, 92, 130))
    if batch_length ==4:
      I3.text((580, 650), Batch[0].getText()[:7],font=myFont, fill=(47, 92, 130))
      I3.text((500, 700), Batch[0].getText()[7:],font=myFont, fill=(47, 92, 130))  
    if batch_length ==5:
      I3.text((580, 650), Batch[0].getText()[:7],font=myFont, fill=(47, 92, 130))
      I3.text((500, 700), Batch[0].getText()[7:],font=myFont, fill=(47, 92, 130)) 
      
  else:
    I3.text((530, 650), Batch[0].getText(), font=myFont, fill=(47, 92, 130))

  # Add Text to an image
  # Save the edited image
  
  img.paste(img2, (0,200), mask = img2)

  img.save("./car2.png")

  # files={'photo':open('./car2.png','rb')}

  # requests.post('https://api.telegram.org/bot1866658555:AAG4WdgzUVE3o0pwaE4r2JZEiY99i5Unul4/sendPhoto?chat_id=568861307',files=files)
    
  bot.send_photo(message1.chat.id, caption=displaytelegram,photo=open('./car2.png', 'rb'))
  sleep(7)
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


@bot.message_handler(commands=['Toss_A_Coin'])
def Toss_A_Coin(msg):
#   print(msg)
  list1 = ["It's Tail","It's Head"]
  bot.send_message(msg.chat.id, random.choice(list1))




bot.polling()







