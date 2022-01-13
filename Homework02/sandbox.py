# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:10:29 2021

@author: Jimi
"""
# from bs4 import BeautifulSoup as soup

# html_doc = '''<td id="overview-top" class="name-overview-widget__section">

#         <div id="resume-teaser">
#             <div id="add-photos-pro">
#             </div>
#             <div id="resume-links">

#             </div>
#         </div>

# <div class="txt-block" id="name-bio-text">
#         <div class="name-trivia-bio-text">
          
#             <div class="inline">
#     Melora Hardin was born on June 29, 1967 in Houston, Texas, USA as Melora Diane Hardin. She is an actress, known for <a href="/title/tt0974661?ref_=nm_ov_bio_lk1">17 Again</a> (2009), <a href="/title/tt1114677?ref_=nm_ov_bio_lk2">Hannah Montana: The Movie</a> (2009) and <a href="/title/tt0386676?ref_=nm_ov_bio_lk3">The Office</a> (2005). She has been married to <a href="/name/nm0413556?ref_=nm_ov_bio_lk4">Gildart Jackson</a> since June 4, 1997. They have two children.            <span class="see-more inline nobr-only">
#                     <a href="/name/nm0002124/bio?ref_=nm_ov_bio_sm">See full bio</a> »
#             </span>
# </div>        </div>
# </div>


#     <div id="name-born-info" class="txt-block">
#         <h4 class="inline">Born:</h4>
   
#   <time datetime="1967-6-29">
# <a href="/search/name?birth_monthday=6-29&amp;refine=birth_monthday&amp;ref_=nm_ov_bth_monthday">June 29</a>, 
     
# <a href="/search/name?birth_year=1967&amp;ref_=nm_ov_bth_year">1967</a>    
#   </time>
#             in
#             <a href="/search/name?birth_place=Houston,%20Texas,%20USA&amp;ref_=nm_ov_bth_place">Houston, Texas, USA</a>
#     </div>

#                    </td>'''

# page_soup = soup(html_doc, 'html.parser')
# # print(page_soup.prettify())

# more = page_soup.find('span', class_="see-more inline nobr-only")
# # print(more.select('a')[0]['href'])

# details = '''<div class="header" id="bio_content">
# <script>
#     if (typeof uet == 'function') {
#       uet("bb", "NameBioWidget", {wb: 1});
#     }
# </script>
#     <script>
#       if ('csm' in window) {
#         csm.measure('csm_NameBioWidget_started');
#       }
#     </script>
# <div class="header"><div class="nav"><div class="desc">Showing all 29 items</div></div>
#   <div class="jumpto">
# Jump to:
# <a href="#overview">Overview</a>&nbsp;(2)&nbsp;    <span class="ghost">|</span>
# <a href="#mini_bio">Mini Bio</a>&nbsp;(2)&nbsp;    <span class="ghost">|</span>
# <a href="#trivia">Trivia</a>&nbsp;(5)&nbsp;    <span class="ghost">|</span>
# <a href="#quotes">Personal Quotes</a>&nbsp;(20)  </div>
# </div>
#    <a name="overview"></a>
#    <h4 class="li_group">Overview (2)</h4>
#   <table id="overviewTable" class="dataTable labelValueTable">
#     <tbody><tr class="even"><td class="label">Born</td>
#     <td>
   
#   <time datetime="1991-9-9">
# <a href="/search/name?birth_monthday=9-9&amp;refine=birth_monthday&amp;ref_=nmbio_ov_1_monthday">September 9</a>, 
     
# <a href="/search/name?birth_year=1991&amp;ref_=nmbio_ov_1_year">1991</a>    
#   </time>
# in&nbsp;<a href="/search/name?birth_place=Columbia,%20South%20Carolina,%20USA&amp;ref_=nmbio_ov_3">Columbia, South Carolina, USA</a>    </td>
#     </tr>
#     <tr class="odd"><td class="label">Height</td>
#     <td>
# 5'&nbsp;7"&nbsp;(1.7&nbsp;m)    </td></tr>
#   </tbody></table>
#    <a name="mini_bio"></a>
#    <h4 class="li_group">Mini Bio (2)</h4>
#         <div class="soda odd">
#           <p>
#               Kelsey Asbille Chow is the oldest of three siblings, a younger brother and younger sister. At a young age she studied dance, and grew to love performing. School plays led to community theater, then she was member of the Hammond Select Ensemble, which she has performed with in Italy and other places. She has a recurring role in "<a href="/title/tt0368530?ref_=nmbio_mbio">One Tree Hill</a> (2003)", also co-stars Matisse Burrows in the Disney movie "<a href="/title/tt1376699?ref_=nmbio_mbio">Den Brother</a> (2010)". She is perhaps best known for her role as Mikayla in Disney XD's popular TV show "<a href="/title/tt1571313?ref_=nmbio_mbio">Pair of Kings</a> (2010)".<br>
#           </p>
#           <p><em>- IMDb Mini Biography By: 
#           <a href="/search/name?bio_author=Elizabeth%20L&amp;view=simple&amp;sort=alpha" name="ba">
#             Elizabeth L
#           </a>
#           </em></p>
    
#         </div>
#         <div class="soda even">
#           <p>
#               Kelsey Asbille Chow (born September 9, 1991) is an American actress. She is known for her role as Mikayla in the Disney XD sitcom Pair of Kings. From 2005 to 2009, she had a recurring role as Gigi Silveri on the drama One Tree Hill. She portrayed Tracy Stewart in MTV's Teen Wolf from 2015-2016. Chow was born to a Chinese father, and an American mother in Columbia, South Carolina. Her father is the son of Chinese immigrants and her mother is descendants of White and Indigenous Americans. She stated in 2010 that she wanted to be able to speak more fluently in Mandarin Chinese as well as be able to read traditional Chinese characters. She has two younger siblings: a brother who is two years younger and a sister who is eight years younger. She attended Hammond School for high school, located in Columbia, SC. Kelsey Chow's residence is in Los Angeles, California, but she lives in New York City where she attends Columbia University.<br><br>After gaining experience in community theatre, Chow got her first television role in 2005 where she played the recurring role of Gigi Silveri on One Tree Hill at the age of 13 appearing on the show until 2009.<br><br>In 2008, she guest starred on The Suite Life of Zack &amp; Cody. She also co-starred in the Disney Channel original film, Den Brother.<br><br>From 2010 to 2013, Chow co-starred as Mikayla on Disney XD original series, Pair of Kings.<br><br>In 2012, Chow had a small part in The Amazing Spider-Man, and was later cast in the feature film Run.<br><br>In 2014, she was cast in the Fox drama Hieroglyph. However, the series was cancelled before it premiered.<br><br>She co-starred in the music video for Hayley Kiyoko's song "Girls Like Girls". Kelsey appeared in the recurring role of Tracy Stewart on season 5, part 1 of Teen Wolf, which premiered on June 29, 2015 and reassumed her role for part 2, which premiered on January 5, 2016.<br><br>For all of her work up through 2017 she has used the name Kelsey Chow. For Wind River and Yellowstone, where she played Native American women, she used the name Kelsey Asbille.<br>
#           </p>
#           <p><em>- IMDb Mini Biography By: 
#           <a href="/search/name?bio_author=ahmetkozan&amp;view=simple&amp;sort=alpha" name="ba">
#             ahmetkozan
#           </a>
#           </em></p>
    
#         </div>

#    <a name="trivia"></a>
#    <h4 class="li_group">Trivia (5)</h4>
#     <div class="soda odd">
#           She was born to Jim and Jean Chow. She has a younger sister and brother.<br>
#     </div>
#     <div class="soda even">
#           She shared the small screen with G. Hannelius in the 2010 television movie Den Brother.<br>
#     </div>
#     <div class="soda odd">
#           She graduated from Hammond School in her hometown of Columbia, South Carolina.<br>
#     </div>
#     <div class="soda even">
#           She had her breakout television role as Gigi Silveri on One Tree Hill.<br>
#     </div>
#     <div class="soda odd">
#           The New York Times on August 1, 2017 reported that Kelsey Asbille Chow had identified herself as a member of the Eastern Band of Cherokee Indians. However, a letter from the tribe on September 6, 2017 stated that "she is not now nor has she ever been an enrolled member of the Eastern Band of Cherokee Indians.".<br>
#     </div>
#    <a name="quotes"></a>
#    <h4 class="li_group">Personal Quotes (20)</h4>
#     <div class="soda odd">
#           When you're young, you don't think about your career or your future - you perform because you love it.<br>
#     </div>
#     <div class="soda even">
#           <a href="/title/tt0368530?ref_=nmbio_qu_2">One Tree Hill</a> (2003) will always be very, very special to me. It was my first television show. And my first gig in the business. It was surreal. I booked the role when I was 13. I had just started high school, and literally, I think, a week into high school, I found out I got the role. It was unimaginable! I learned so much from that show.<br>
#     </div>
#     <div class="soda odd">
#           I've always wanted to work with <a href="/name/nm0000125?ref_=nmbio_qu_3">Sean Connery</a> - there's something about his style, and his calm, cool demeanor that I find intriguing.<br>
#     </div>
#     <div class="soda even">
#           I was really young when I started on <a href="/title/tt0368530?ref_=nmbio_qu_4">One Tree Hill</a> (2003) and the encouragement from my friends and family has been crucial in my development as an actress. I'm also continuously surprised and humbled by the kindness and generosity of the fans.<br>
#     </div>
#     <div class="soda odd">
#           My 94-year-old grandmother has always been so inspiring to me. She is kind, smart, brave, and independent. After graduating number one in her medical school class at a time when it was extremely rare for women to attend medical school, she worked with the World Health Organization in North Africa to eradicate tuberculosis.<br>
#     </div>
#     <div class="soda even">
#           I like vintage dresses that I can just slip on.<br>
#     </div>
#     <div class="soda odd">
#           I wish I could read minds. It's a dangerous superpower, so I'd wish for it to come with a switch where I could turn it off if I wanted to. You'd learn a lot about people, that's for sure!<br>
#     </div>
#     <div class="soda even">
#           <a href="/title/tt0368530?ref_=nmbio_qu_8">One Tree Hill</a> (2003) was my first television experience, so naturally I was nervous initially. There is no rehearsal, you get your script a few days ahead, and you work. I was also the youngest actor, 13, on set at that time, but it was amazing to be able to 'learn the ropes' with such a supportive group of people.<br>
#     </div>
#     <div class="soda odd">
#           Dance and theatre afforded me the opportunity to discover my passion for acting, for telling stories.<br>
#     </div>
#     <div class="soda even">
#           I enjoyed the drama of <a href="/title/tt0368530?ref_=nmbio_qu_10">One Tree Hill</a> (2003) and the opportunity to be one of the comedic aspects, initially.<br>
#     </div>
#     <div class="soda odd">
#           <a href="/title/tt1571313?ref_=nmbio_qu_11">Pair of Kings</a> (2010) is so much fun, literally. It is a very physical show with loads of stunts and green screen work, and you never know what great adventure is ahead of you! It's also a nice change in terms of being of similar ages to <a href="/name/nm2480883?ref_=nmbio_qu_11">Larramie Doc Shaw</a> and <a href="/name/nm1102053?ref_=nmbio_qu_11">Mitchel Musso</a>.<br>
#     </div>
#     <div class="soda even">
#           I'm very lucky to have a strong support system with my friends and my family. They have kept me grounded.<br>
#     </div>
#     <div class="soda odd">
#           I definitely want to study global health. Right now I'm working on all the prerequisite core curriculum that Columbia has. So getting all of that out of the way. And I definitely want to pursue something along the lines of public health.<br>
#     </div>
#     <div class="soda even">
#           The more you love a person, you more you should respect that person. Encourage her to be the best she can be, and you'll both be happier.<br>
#     </div>
#     <div class="soda odd">
#           I love mixing prints. The costume designer for <a href="/title/tt1571313?ref_=nmbio_qu_15">Pair of Kings</a> (2010) and I have actually incorporated the trend for my character 'Mikayla.'<br>
#     </div>
#     <div class="soda even">
#           I enjoy having the ability to play a variety of ethnicities. Being ethnically ambiguous allows me to explore many roles, and I enjoy being free to be whoever I want to be.<br>
#     </div>
#     <div class="soda odd">
#           <a href="/title/tt2215457?ref_=nmbio_qu_17">Run</a> (2013) is exciting, about family secrets, the mystery surrounding them and the outdoor sport of parkour. The story itself is full of intrigue and action, but the parkour takes the story to another level. It was an absolutely incredible experience, working with experts from all over the country.<br>
#     </div>
#     <div class="soda even">
#           It's fun to get away from myself for a while when I take on these roles that have very different personalities from my own. I get to say things I normally wouldn't say or act in ways I normally wouldn't act. After all, such roles are more challenging because you really have to immerse yourself in the character.<br>
#     </div>
#     <div class="soda odd">
#           I want to do roles that will challenge me. I'm definitely interested in period pieces. But I definitely don't want to limit myself. I'm very open to different roles.<br>
#     </div>
#     <div class="soda even">
#           <a href="/title/tt2066133?ref_=nmbio_qu_20">The Wine of Summer</a> (2013) is a beautiful film about love lost and found, and the complexities of life while discovering who you are. It was filmed primarily in and around Barcelona, and the imagery is breathtaking.<br>
#     </div>
#     <script>
#       if ('csm' in window) {
#         csm.measure('csm_NameBioWidget_finished');
#       }
#     </script>
# <script>
#     if (typeof uet == 'function') {
#       uet("be", "NameBioWidget", {wb: 1});
#     }
# </script>
# <script>
#     if (typeof uex == 'function') {
#       uex("ld", "NameBioWidget", {wb: 1});
#     }
# </script>
#                 </div>'''

# details_soup = soup(details, 'html.parser')
# print(details_soup.prettify())

# bio = details_soup.find('table', id='overviewTable')
# print(bio.next_sibling.next_sibling)

# bio2 = details_soup.select('a[name="mini_bio"]')[0]
# print(bio2)
# print('--------------')
# print(bio2.find_next_sibling())
# print('--------------')
# print(bio2.find_next_sibling().find_next_sibling())
# print('--------------')
# print(bio2.find_next_sibling().find_next('p'))
# print('--------------')
# print(bio2.find_next_sibling().find_next('p').text.strip())

import spacy
import en_core_web_sm
import csv

nlp = en_core_web_sm.load()

# data = [["Melora Hardin was born on June 29, 1967 in Houston, Texas, USA as Melora Diane Hardin. She is an actress, known for 17 Again (2009), Hannah Montana: The Movie (2009) and The Office (2005). She has been married to Gildart Jackson since June 4, 1997. They have two children.",'https://www.imdb.com/name/nm0002124/bio'],
#         ["Matthew Weiner was born on June 29, 1965 in Baltimore, Maryland, USA. He is a writer and producer, known for Mad Men (2007), The Sopranos (1999) and The Romanoffs (2018). He has been married to Linda Brettler since January 1991. They have four children.",'https://www.imdb.com/name/nm1980806/bio']]


# for (idx, (bio, act)) in enumerate(data):
#     # print('['+str(idx)+'] >', act)
    
#     biog = bio
    
#     doc = nlp(biog)
    
#     for idx, sent in enumerate(doc.sents):
#         # print(f'[{idx:2d}] >', sent)
        
#         my_sent = str(sent)
        
#         break
    
        
    
#     break

# print('-------------------------')

# doc = nlp(my_sent)
# for w in doc:
#     print(f'{w.text:15s} [{w.tag_:5s} | {w.pos_:6s} | {spacy.explain(w.tag_)}]')

# print('-------------------------')

# for w in doc:
#     print(f'{w.text:15s} [{w.dep_}]')
    
# print('-------------------------')

# for ent in doc.ents:
#     print(f'{ent.text:15s} [{ent.label_}]')
# print('-------------------------')
    
# from spacy.matcher import Matcher
# import re

# birthplace lexical
# pattern: * born * in * [place] re: born.+in.+([A-Z]\w+), ([A-Z]\w+) 

# birth_pattern = r"\bborn.+in.+([A-Z]\w+), ([A-Z]\w+), ([A-Z]\w+)"
# for bio, act in data:
#     doc = nlp(bio)
#     for match in re.finditer(birth_pattern, doc.text):
#         print(match)
#         print(match.span())
#         start, end = match.span()
#         span = doc.char_span(start, end)
#         if span is not None:
#             print('Found match:', span.text)


# text = "After her parents' divorce, she relocated with her mother to Hollywood where she attended the amazing University of Southern California Santa Clara and had a degree in Finance and lent her voice to both radio and animated cartoon shorts."

# pattern = [
#             {'ORTH': 'attended'},
#             {'OP': '+'},
#             {'ORTH': 'University'},
#             {'ORTH': 'of'},
#             {'IS_TITLE': True, 'OP': '+'},
#             {'IS_PUNCT': True, 'OP': '*'},
#             {'IS_TITLE': True, 'OP': '*'},
#           ]

# matcher = Matcher(nlp.vocab)
# matcher.add("matching", [pattern]) 
# sent = nlp(text)
# matches = matcher(sent)
# if len(matches)>0:
#     # print(matches)
#     match = matches[0]
#     # print(match)
#     for match in matches:
#         span = sent[match[1]:match[2]] 
#         # span = str_tok[match[1]:match[2]]
#         # sub_str = span
#         # print(type(span))
#         print(span)

import json

with open('./bios/cast1.jl', 'r') as fp:
    counts = {}
    for num, line in enumerate(fp):
        print(num)
        data = json.loads(line)
        count = 0
        for thing in data:
            if data[thing]:
                count += 1
        if count in counts.keys():
            counts[count].append(num)
        else:
            counts[count] = [num]
    print(counts[6])
    print(counts[5])
    print(counts[4])
    print('>>>>')