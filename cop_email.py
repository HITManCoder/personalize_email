import yagmail
import pandas as pd
from random import randint
from time import sleep




pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 150)
pd.set_option('display.width', 500)

#setup
"""
df=pd.read_csv(filename)

df2=pd.concat([df, df['Name'].str.split(',', expand=True)], axis=1)
df3=df2[['Unnamed: 0',1,0,'Email', 'Organization Level 6', 'Organization Level 5', 'Name']]
df2 = df3.rename(columns={0: 'last name', 1: 'first name', 'Unnamed: 0':'Known'})
df2.to_csv(filename2)
"""

#Email
title="You are Awesome, EOI Granted, What's Next"
body="""If you haven't heard, ConocoPhillips graciously accepted my expression of interest (after we recovered our power, water and internet :).  Over the past few months, since raising my hand, I have been ruminating on my 14 years at COP, and it all keeps boiling down to you.  My thoughts did not pull to an exciting project, a good performance review, the money earned or money saved, not even the awesome destinations work took me, it was the people.  The time we spent together was wonderful and it's people like yourself that made my career so fulfilling and ultimately the decision to EOI so difficult.  I appreciate every second we spent together over the past 14 years and want to thank you for being awesome and a special part of mine and my family's life.  My wish is that we continue the journey and in hopes that we do I'll leave you with my contact info and what I'll be working on next.

I blog about once a month on life, finances, and behavioral science at HIT Investments.  Subscribe here or follow my blog here
If you like compounding $, I manage the fund HIT Capital (and have room for a few more investors).  Follow my semi-annual reports here or visit the website here (the password is hitcapital).
If you want to shoot me an email I'm at Stephen.Read@hitinvestmentsllc.com
If you prefer social media my linkedin is https://www.linkedin.com/in/stephenreadhit/
If you prefer good ole text or voice my cell # is 3092537887
If you want to follow current and future code, my github account is hitmancoder
My personal favorite, if you want to catch up in person, grab a coffee/beer/grub, take a walk, or ride the anthills, book some time on my new calendar here

Thank you for all you have done for my family and I and for making the past 14 years so fulfilling.  I look forward to staying in touch and seeing where the next 14 years takes us :)

Warm Regards,
Stephen Read 
Investment Engineer
T. 309.253.7887 
       
"""

filename=r"C:\Users\Stephen\Python\Emails\email_practice.csv"
dfemaillist=pd.read_csv(filename,header=None)

for a in dfemaillist.iterrows():
    name=(a[1][0])+','
    email=(a[1][1])
    sleep(randint(1, 10))

    print(name)
    print(title)
    print(body)

    """yag = yagmail.SMTP('HITTravelDeals@gmail.com', password)
    contents = [name, body]
    yag.send(email, title, contents)
"""