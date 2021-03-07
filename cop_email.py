import yagmail
import pandas as pd
from random import randint
from time import sleep
import keyring


#File Clean
"""
df=pd.read_csv(filename)

df2=pd.concat([df, df['Name'].str.split(',', expand=True)], axis=1)
df3=df2[['Unnamed: 0',1,0,'Email', 'Organization Level 6', 'Organization Level 5', 'Name']]
df2 = df3.rename(columns={0: 'last name', 1: 'first name', 'Unnamed: 0':'Known'})
df2.to_csv(filename2)
"""

#Email
password = keyring.get_password("Gmail HIT Travel", "HITTravelDeals@gmail.com")

title="You are Awesome, EOI Granted, What's Next"

body_0 = """
If you haven't heard, ConocoPhillips graciously accepted my expression of interest early last week <a href="https://www.hitinvestments.com/freeze/">(after we recovered power, water and internet :)</a>.
xxx
Over the past few months, since initially raising my hand for severance, I took time to reflect on my 14 year career at ConocoPhillips. To my surprise, the thoughts did not flow to an exciting project, a great performance review, supervising offshore, inking a big deal, or all the money earned and or saved, it was you, the people I met and relationships built along the way.

Our time together was wonderful and it was co-workers like yourself that made my career so fulfilling and ultimately the decision to EOI so difficult.

I appreciate you and each second we spent together over the past 14 years.  Thank you for being awesome and a special part of my family and I's life.

Although I will no longer be badging in, my wish is that our mutual journey continues and in hopes that it does my contact info and what I'm building next is below:
"""
body_1="""<div> <ul> <li> Educate - I blog once a month on life, finances, and behavioral economics. Follow the blog <a href="https://www.hitinvestments.com/subscribe">here</a>.
<li> Grow - If you like to put your money to work, I manage the fund HIT Capital (and it has room for a few more investors). Sign up for my semi-annual reports <a href="https://www.hitinvestments.com/subscribe">here</a> or visit the website <a href="http://www.hitcapitallllp.com">here</a> (password is hitcapital).
<li> Email - I'm at Stephen.Read@HITinvestmentsLLC.com 
<li> Socialize - I'm on <a href="https://www.linkedin.com/in/stephenreadhit/">Linkedin</a> and my Twitter handle is @HITInvestments 
<li> Call - my number is 3092537887 
<li> Code - my github account is hitmancoder 
<li> Meet Up - If you have time to catch up, grab lunch, take a walk, or ride the anthills, my new calendar is <a href="http://www.calendly.com/hitinvestments" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://www.calendly.com/hitinvestments&amp;source=gmail&amp;ust=1615040022353000&amp;usg=AFQjCNFe0erKvimJc4AKy-QhiCfz34oHBg">here</a>
"""
body_2="""Thank you for being you, being awesome, and for fulfilling my journey at COP. I look forward to staying in touch and seeing where the next 14 years takes us :)"""

body_3="""
Warm Regards,
Stephen Read
Engineer, Coder, Dad, Investor, Writer
T 309.253.7887 
https://www.hitinvestments.com
"""

filename=r"C:\Users\Stephen\Python\Emails\email_practice.csv"
dfemaillist=pd.read_csv(filename,header=None)



for a in dfemaillist.iterrows():
    name=(a[1][0])+','
    email=(a[1][1])
    sleep(randint(1, 240))

    print(name, email)

    yag = yagmail.SMTP('xx', password)
    contents = [name, body_0,body_1,body_2,body_3]
    yag.send(email, title, contents)
