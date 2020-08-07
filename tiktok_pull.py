from TikTokApi import TikTokApi
#import TikTokApi
import datetime
import time
import psycopg2
import json
from random import randint

api = TikTokApi()
"""
results = 10

trending = api.trending(results)

for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok['desc'])

print(len(trending))
for x in trending[0]:
    print(x)

#viewcount, likes, shares, comments,video id,current time stamp,hashtags, collaborators, time stamp of creation, song id, creator
outfile=open('D:/Documents/tiktok_banque/tiktok_table.tsv','w')
for t in trending:
    stats=t['stats']
    #print('%s' % (stats['playCount'],stats['diggCount'],stats['shareCount'],stats['commentCount'],t['id'],str(datetime.datetime.now()),))
    #t['createTime'],,

tiktokData = api.get_Video_By_Url('https://www.tiktok.com/@benthamite/video/6827126743048948998', return_bytes=1)
with open("video.mp4", 'wb') as out:
    print(tiktokData)
"""
conn=psycopg2.connect('dbname=postgres user=postgres')
cur = conn.cursor()


count = 500
t_time=str(datetime.datetime.now()).replace(':','_')
#outfile_name=str('D:/Documents/tiktok_banque/bens_tiktok_table'+t_time+'.tsv')
#outfile=open(outfile_name,'w')
# https://www.whattoexpect.com/baby-names/list/top-baby-names-for-girls/
# https://family.disney.com/articles/1000-most-popular-boy-names/
names = [
'Emma',
'Olivia',
'Ava',
'Isabella',
'Sophia',
'Charlotte',
'Mia',
'Amelia',
'Harper',
'Evelyn',
'Abigail',
'Emily',
'Elizabeth',
'Mila',
'Ella',
'Avery',
'Sofia',
'Camila',
'Aria',
'Scarlett',
'Victoria',
'Madison',
'Luna',
'Grace',
'Chloe',
'Liam',
'Noah',
'William',
'James',
'Logan',
'Benjamin',
'Mason',
'Elijah',
'Oliver',
'Jacob',
'Lucas',
'Michael',
'Alexander',
'Ethan',
'Daniel',
'Matthew',
'Aiden',
'Henry',
'Joseph',
'Jackson',
'Samuel',
'Sebastian',
'David',
'Carter',
'Wyatt',
'Jayden',
'John',
'Owen',
'Dylan',
'Luke',
'Gabriel',
'Anthony',
'Isaac',
'Grayson',
'Jack',
'Julian',
'Levi',
'Christopher',
'Joshua',
'Andrew',
'Lincoln',
'Mateo',
'Ryan',
'Jaxon',
'Nathan',
'Aaron',
'Isaiah',
'Thomas',
'Charles',
'Penelope',
'Layla',
'Riley',
'Zoey',
'Nora',
'Lily',
'Eleanor',
'Hannah',
'Lillian',
'Addison',
'Aubrey',
'Ellie',
'Stella',
'Natalie',
'Zoe',
'Leah',
'Hazel',
'Violet',
'Aurora',
'Savannah',
'Audrey',
'Brooklyn',
'Bella',
'Claire',
'Skylar',
'Lucy',
'Paisley',
'Everly',
'Anna',
'Caroline',
'Nova',
'Genesis',
'Emilia',
'Kennedy',
'Samantha',
'Maya',
'Willow',
'Kinsley',
'Naomi',
'Aaliyah',
'Elena',
'Sarah',
'Ariana',
'Allison',
'Gabriella',
'Alice',
'Madelyn',
'Cora',
'Ruby',
'Eva',
'Serenity',
'Autumn',
'Adeline',
'Hailey',
'Gianna',
'Valentina',
'Isla',
'Eliana',
'Quinn',
'Nevaeh',
'Ivy',
'Sadie',
'Piper',
'Lydia',
'Alexa',
'Josephine',
'Emery',
'Julia',
'Delilah',
'Arianna',
'Vivian',
'Kaylee',
'Sophie',
'Brielle',
'Madeline',
'Peyton',
'Rylee',
'Clara',
'Hadley',
'Melanie',
'Mackenzie',
'Reagan',
'Adalynn',
'Liliana',
'Aubree',
'Jade',
'Katherine',
'Isabelle',
'Natalia',
'Raelynn',
'Maria',
'Athena',
'Ximena',
'Arya',
'Leilani',
'Taylor',
'Faith',
'Rose',
'Kylie',
'Alexandra',
'Mary',
'Margaret',
'Lyla',
'Ashley',
'Amaya',
'Eliza',
'Brianna',
'Bailey',
'Andrea',
'Khloe',
'Jasmine',
'Melody',
'Iris',
'Isabel',
'Norah',
'Annabelle',
'Valeria',
'Emerson',
'Adalyn',
'Ryleigh',
'Eden',
'Emersyn',
'Anastasia',
'Kayla',
'Alyssa',
'Caleb',
'Josiah',
'Christian',
'Hunter',
'Eli',
'Jonathan',
'Connor',
'Landon',
'Adrian',
'Asher',
'Cameron',
'Leo',
'Theodore',
'Jeremiah',
'Hudson',
'Robert',
'Easton',
'Nolan',
'Nicholas',
'Ezra',
'Colton',
'Angel',
'Brayden',
'Jordan',
'Dominic',
'Austin',
'Ian',
'Adam',
'Elias',
'Jaxson',
'Greyson',
'Jose',
'Ezekiel',
'Carson',
'Evan',
'Maverick',
'Bryson',
'Jace',
'Cooper',
'Xavier',
'Parker',
'Roman',
'Jason',
'Santiago',
'Chase',
'Sawyer',
'Gavin',
'Leonardo',
'Kayden',
'Ayden',
'Jameson',
'Kevin',
'Bentley',
'Zachary',
'Everett',
'Axel',
'Tyler',
'Micah',
'Vincent',
'Weston',
'Miles',
'Wesley',
'Nathaniel',
'Harrison',
'Brandon',
'Cole',
'Declan',
'Luis',
'Braxton',
'Damian',
'Silas',
'Tristan',
'Ryder',
'Bennett',
'George',
'Emmett',
'Justin',
'Kai',
'Max',
'Diego',
'Luca',
'Ryker',
'Carlos',
'Maxwell',
'Kingston',
'Ivan',
'Maddox',
'Juan',
'Ashton',
'Jayce',
'Rowan',
'Kaiden',
'Giovanni',
'Eric',
'Jesus',
'Calvin',
'Abel',
'King',
'Camden',
'Amir',
'Blake',
'Alex',
'Brody',
'Malachi',
'Emmanuel',
'Jonah',
'Beau',
'Jude',
'Antonio',
'Alan',
'Elliott',
'Elliot',
'Waylon',
'Xander',
'Timothy',
'Victor',
'Bryce',
'Finn',
'Brantley',
'Edward',
'Abraham',
'Patrick',
'Grant',
'Karter',
'Hayden',
'Richard',
'Miguel',
'Joel',
'Gael',
'Tucker',
'Rhett',
'Avery',
'Steven',
'Graham',
'Kaleb',
'Jasper',
'Jesse',
'Matteo',
'Dean',
'Zayden',
'Preston',
'August',
'Oscar',
'Jeremy',
'Alejandro',
'Marcus',
'Dawson',
'Lorenzo',
'Messiah',
'Zion',
'Maximus',
'River',
'Zane',
'Mark',
'Brooks',
'Nicolas',
'Paxton',
'Judah',
'Emiliano',
'Kaden',
'Bryan',
'Kyle',
'Myles',
'Peter',
'Charlie',
'Kyrie',
'Thiago',
'Brian',
'Kenneth',
'Andres',
'Lukas',
'Aidan',
'Jax',
'Caden',
'Milo',
'Paul',
'Beckett',
'Brady',
'Colin',
'Omar',
'Bradley',
'Javier',
'Knox',
'Jaden',
'Barrett',
'Israel',
'Matias',
'Jorge',
'Zander',
'Derek',
'Josue',
'Cayden',
'Holden',
'Griffin',
'Arthur',
'Leon',
'Felix',
'Remington',
'Jake',
'Killian',
'Clayton',
'Juliana',
'Charlie',
'Esther',
'Ariel',
'Cecilia',
'Valerie',
'Alina',
'Molly',
'Reese',
'Aliyah',
'Lilly',
'Parker',
'Finley',
'Morgan',
'Sydney',
'Jordyn',
'Eloise',
'Trinity',
'Daisy',
'Kimberly',
'Lauren',
'Genevieve',
'Sara',
'Arabella',
'Harmony',
'Elise',
'Remi',
'Teagan',
'Alexis',
'London',
'Sloane',
'Laila',
'Lucia',
'Diana',
'Juliette',
'Sienna',
'Elliana',
'Londyn',
'Ayla',
'Callie',
'Gracie',
'Josie',
'Amara',
'Jocelyn',
'Daniela',
'Everleigh',
'Mya',
'Rachel',
'Summer',
'Alana',
'Brooke',
'Alaina',
'Mckenzie',
'Catherine',
'Amy',
'Presley',
'Journee',
'Rosalie',
'Ember',
'Brynlee',
'Rowan',
'Joanna',
'Paige',
'Rebecca',
'Ana',
'Sawyer',
'Mariah',
'Nicole',
'Brooklynn',
'Payton',
'Marley',
'Fiona',
'Georgia',
'Lila',
'Harley',
'Adelyn',
'Alivia',
'Noelle',
'Gemma',
'Vanessa',
'Journey',
'Makayla',
'Angelina',
'Adaline',
'Catalina',
'Alayna',
'Julianna',
'Leila',
'Lola',
'Adriana',
'June',
'Juliet',
'Jayla',
'River',
'Tessa',
'Lia',
'Dakota',
'Delaney',
'Selena',
'Blakely',
'Ada',
'Camille',
'Zara',
'Malia',
'Hope',
'Samara',
'Vera',
'Mckenna',
'Briella',
'Izabella',
'Hayden',
'Raegan',
'Michelle',
'Angela',
'Ruth',
'Freya',
'Kamila',
'Vivienne',
'Aspen',
'Olive',
'Kendall',
'Elaina',
'Thea',
'Kali',
'Destiny',
'Amiyah',
'Evangeline',
'Cali',
'Blake',
'Elsie',
'Juniper',
'Alexandria',
'Myla',
'Ariella',
'Kate',
'Mariana',
'Lilah',
'Charlee',
'Daleyza',
'Nyla',
'Jane',
'Maggie',
'Zuri',
'Aniyah',
'Lucille',
'Leia',
'Melissa',
'Adelaide',
'Amina',
'Giselle',
'Lena',
'Camilla',
'Miriam',
'Millie',
'Brynn',
'Gabrielle',
'Sage',
'Annie',
'Logan',
'Lilliana',
'Haven',
'Jessica',
'Kaia',
'Magnolia',
'Amira',
'Adelynn',
'Makenzie',
'Stephanie',
'Nina',
'Phoebe',
'Arielle',
'Evie',
'Lyric',
'Alessandra',
'Gabriela',
'Paislee',
'Raelyn',
'Madilyn',
'Paris',
'Makenna',
'Kinley',
'Gracelyn',
'Talia',
'Maeve',
'Rylie',
'Kiara',
'Evelynn',
'Brinley',
'Jacqueline',
'Laura',
'Gracelynn',
'Lexi',
'Ariah',
'Fatima',
'Jennifer',
'Kehlani',
'Alani',
'Ariyah',
'Luciana',
'Allie',
'Heidi',
'Maci',
'Phoenix',
'Felicity',
'Joy',
'Kenzie',
'Veronica',
'Margot',
'Addilyn',
'Lana',
'Cassidy',
'Remington',
'Saylor',
'Ryan',
'Keira',
'Harlow',
'Miranda',
'Angel',
'Amanda',
'Daniella',
'Royalty',
'Gwendolyn',
'Ophelia',
'Heaven',
'Jordan',
'Madeleine',
'Esmeralda',
'Kira',
'Miracle',
'Elle',
'Amari',
'Danielle',
'Daphne',
'Willa',
'Haley',
'Gia',
'Kaitlyn',
'Oakley',
'Kailani',
'Winter',
'Alicia',
'Serena',
'Nadia',
'Aviana',
'Demi',
'Jada',
'Braelynn',
'Dylan',
'Ainsley',
'Alison',
'Camryn',
'Avianna',
'Bianca',
'Skyler',
'Scarlet',
'Maddison',
'Nylah',
'Sarai',
'Regina',
'Dahlia',
'Nayeli',
'Raven',
'Helen',
'Adrianna',
'Averie',
'Skye',
'Kelsey',
'Tatum',
'Kensley',
'Maliyah',
'Erin',
'Viviana',
'Jenna',
'Anaya',
'Carolina',
'Shelby',
'Sabrina',
'Mikayla',
'Annalise',
'Octavia',
'Lennon',
'Blair',
'Carmen',
'Yaretzi',
'Kennedi',
'Mabel',
'Zariah',
'Kyla',
'Christina',
'Selah',
'Celeste',
'Eve',
'Mckinley',
'Milani',
'Frances',
'Jimena',
'Kylee',
'Leighton',
'Katie',
'Aitana',
'Kayleigh',
'Sierra',
'Kathryn',
'Rosemary',
'Jolene',
'Alondra',
'Elisa',
'Helena',
'Charleigh',
'Hallie',
'Lainey',
'Avah',
'Jazlyn',
'Kamryn',
'Mira',
'Cheyenne',
'Francesca',
'Antonella',
'Wren',
'Chelsea',
'Amber',
'Emory',
'Lorelei',
'Nia',
'Abby',
'April',
'Emelia',
'Carter',
'Aylin',
'Cataleya',
'Bethany',
'Marlee',
'Carly',
'Kaylani',
'Emely',
'Liana',
'Madelynn',
'Cadence',
'Matilda',
'Sylvia',
'Myra',
'Fernanda',
'Oaklyn',
'Elianna',
'Hattie',
'Dayana',
'Kendra',
'Maisie',
'Malaysia',
'Kara',
'Katelyn',
'Maia',
'Celine',
'Cameron',
'Renata',
'Jayleen',
'Charli',
'Emmalyn',
'Holly',
'Azalea',
'Leona',
'Alejandra',
'Bristol',
'Collins',
'Imani',
'Meadow',
'Alexia',
'Edith',
'Kaydence',
'Leslie',
'Lilith',
'Kora',
'Aisha',
'Meredith',
'Danna',
'Wynter',
'Emberly',
'Julieta',
'Michaela',
'Alayah',
'Jemma',
'Reign',
'Colette',
'Kaliyah',
'Elliott',
'Johanna',
'Remy',
'Sutton',
'Emmy',
'Virginia',
'Briana',
'Oaklynn',
'Adelina',
'Everlee',
'Megan',
'Angelica',
'Justice',
'Mariam',
'Khaleesi',
'Macie',
'Karsyn',
'Alanna',
'Aleah',
'Mae',
'Mallory',
'Esme',
'Skyla',
'Madilynn',
'Charley',
'Allyson',
'Hanna',
'Shiloh',
'Henley',
'Macy',
'Maryam',
'Ivanna',
'Ashlynn',
'Lorelai',
'Amora',
'Ashlyn',
'Sasha',
'Baylee',
'Beatrice',
'Itzel',
'Priscilla',
'Marie',
'Jayda',
'Liberty',
'Rory',
'Alessia',
'Alaia',
'Janelle',
'Kalani',
'Gloria',
'Sloan',
'Dorothy',
'Greta',
'Julie',
'Zahra',
'Savanna',
'Annabella',
'Poppy',
'Amalia',
'Zaylee',
'Cecelia',
'Coraline',
'Kimber',
'Emmie',
'Anne',
'Karina',
'Kassidy',
'Kynlee',
'Monroe',
'Anahi',
'Jaliyah',
'Jazmin',
'Maren',
'Monica',
'Siena',
'Marilyn',
'Reyna',
'Kyra',
'Lilian',
'Jamie',
'Melany',
'Alaya',
'Ariya',
'Kelly',
'Rosie',
'Adley',
'Dream',
'Jaylah',
'Laurel',
'Jazmine',
'Mina',
'Karla',
'Bailee',
'Aubrie',
'Katalina',
'Melina',
'Harlee',
'Elliot',
'Hayley',
'Elaine',
'Karen',
'Dallas',
'Irene',
'Lylah',
'Ivory',
'Chaya',
'Rosa',
'Aleena',
'Braelyn',
'Nola',
'Alma',
'Leyla',
'Pearl',
'Addyson',
'Roselyn',
'Lacey',
'Lennox',
'Reina',
'Aurelia',
'Noa',
'Janiyah',
'Jessie',
'Madisyn',
'Saige',
'Alia',
'Tiana',
'Astrid',
'Cassandra',
'Kyleigh',
'Romina',
'Stevie',
'Haylee',
'Zelda',
'Lillie',
'Aileen',
'Brylee',
'Eileen',
'Yara',
'Ensley',
'Lauryn',
'Giuliana',
'Livia',
'Anya',
'Mikaela',
'Palmer',
'Lyra',
'Mara',
'Marina',
'Kailey',
'Liv',
'Clementine',
'Kenna',
'Briar',
'Emerie',
'Galilea',
'Tiffany',
'Bonnie',
'Elyse',
'Cynthia',
'Frida',
'Kinslee',
'Tatiana',
'Joelle',
'Armani',
'Jolie',
'Nalani',
'Rayna',
'Yareli',
'Meghan',
'Rebekah',
'Addilynn',
'Faye',
'Zariyah',
'Lea',
'Aliza',
'Julissa',
'Lilyana',
'Anika',
'Kairi',
'Aniya',
'Noemi',
'Angie',
'Crystal',
'Bridget',
'Ari',
'Davina',
'Amelie',
'Amirah',
'Annika',
'Elora',
'Xiomara',
'Linda',
'Hana',
'Laney',
'Mercy',
'Hadassah',
'Madalyn',
'Louisa',
'Simone',
'Kori',
'Jillian',
'Alena',
'Malaya',
'Miley',
'Milan',
'Sariyah',
'Malani',
'Clarissa',
'Nala',
'Princess',
'Amani',
'Analia',
'Estella',
'Milana',
'Aya',
'Chana',
'Jayde',
'Tenley',
'Zaria',
'Itzayana',
'Penny',
'Ailani',
'Lara',
'Aubriella',
'Clare',
'Lina',
'Rhea',
'Bria',
'Thalia',
'Keyla',
'Haisley',
'Ryann',
'Addisyn',
'Amaia',
'Chanel',
'Ellen',
'Harmoni',
'Aliana',
'Tinsley',
'Landry',
'Paisleigh',
'Lexie',
'Myah',
'Rylan',
'Deborah',
'Emilee',
'Laylah',
'Novalee',
'Ellis',
'Emmeline',
'Avalynn',
'Hadlee',
'Legacy',
'Braylee',
'Elisabeth',
'Kaylie',
'Ansley',
'Dior',
'Paula',
'Belen',
'Corinne',
'Maleah',
'Martha',
'Teresa',
'Salma',
'Louise',
'Averi',
'Lilianna',
'Amiya',
'Milena',
'Royal',
'Aubrielle',
'Calliope',
'Frankie',
'Natasha',
'Kamilah',
'Meilani',
'Raina',
'Amayah',
'Lailah',
'Rayne',
'Zaniyah',
'Isabela',
'Nathalie',
'Miah',
'Opal',
'Kenia',
'Azariah',
'Hunter',
'Tori',
'Andi',
'Keily',
'Leanna',
'Scarlette',
'Jaelyn',
'Saoirse',
'Selene',
'Dalary',
'Lindsey',
'Marianna',
'Ramona',
'Estelle',
'Giovanna',
'Holland',
'Nancy',
'Emmalynn',
'Mylah',
'Rosalee',
'Sariah',
'Zoie',
'Blaire',
'Lyanna',
'Maxine',
'Anais',
'Dana',
'Judith',
'Kiera',
'Jaelynn',
'Noor',
'Kai',
'Adalee',
'Oaklee',
'Amaris',
'Jaycee',
'Belle',
'Carolyn',
'Della',
'Karter',
'Sky',
'Treasure',
'Vienna',
'Jewel',
'Rivka',
'Rosalyn',
'Alannah',
'Ellianna',
'Sunny',
'Claudia',
'Cara',
'Hailee',
'Estrella',
'Harleigh',
'Zhavia',
'Alianna',
'Brittany',
'Jaylene',
'Journi',
'Marissa',
'Mavis',
'Iliana',
'Jurnee',
'Aislinn',
'Alyson',
'Elsa',
'Kamiyah',
'Kiana',
'Lisa',
'Arlette',
'Kadence',
'Kathleen',
'Halle',
'Erika',
'Sylvie',
'Adele',
'Erica',
'Veda',
'Whitney',
'Bexley',
'Emmaline',
'Guadalupe',
'August',
'Brynleigh',
'Gwen',
'Promise',
'Alisson',
'India',
'Madalynn',
'Paloma',
'Patricia',
'Samira',
'Aliya',
'Casey',
'Jazlynn',
'Paulina',
'Dulce',
'Kallie',
'Perla',
'Adrienne',
'Alora',
'Nataly',
'Ayleen',
'Christine',
'Kaiya',
'Ariadne',
'Karlee',
'Barbara',
'Lillianna',
'Raquel',
'Saniyah',
'Yamileth',
'Arely',
'Celia',
'Heavenly',
'Kaylin',
'Marisol',
'Marleigh',
'Avalyn',
'Berkley',
'Kataleya',
'Zainab',
'Dani',
'Egypt',
'Joyce',
'Kenley',
'Annabel',
'Kaelyn',
'Etta',
'Hadleigh',
'Joselyn',
'Luella',
'Jaylee',
'Zola',
'Alisha',
'Ezra',
'Queen',
'Amia',
'Annalee',
'Bellamy',
'Paola',
'Tinley',
'Violeta',
'Jenesis',
'Arden',
'Giana',
'Wendy',
'Ellison',
'Florence',
'Margo',
'Naya',
'Robin',
'Sandra',
'Scout',
'Waverly',
'Janessa',
'Jayden',
'Micah',
'Novah',
'Zora',
'Ann',
'Jana',
'Taliyah',
'Vada',
'Giavanna',
'Ingrid',
'Valery',
'Azaria',
'Emmarie',
'Esperanza',
'Kailyn',
'Aiyana',
'Keilani',
'Austyn',
'Whitley',
'Elina',
'Kimora',
'Maliah'
]
names2 = [
'Kevin',
'Bentley',
'Zachary',
'Everett',
'Axel',
'Tyler',
'Micah',
'Vincent',
'Weston',
'Miles',
'Wesley',
'Nathaniel',
'Harrison',
'Brandon',
'Cole',
'Declan',
'Luis',
'Braxton',
'Damian',
'Silas',
'Tristan',
'Ryder',
'Bennett',
'George',
'Emmett',
'Justin',
'Kai',
'Max',
'Diego',
'Luca',
'Ryker',
'Carlos',
'Maxwell',
'Kingston',
'Ivan',
'Maddox',
'Juan',
'Ashton',
'Jayce',
'Rowan',
'Kaiden',
'Giovanni',
'Eric',
'Jesus',
'Calvin',
'Abel',
'King',
'Camden',
'Amir',
'Blake',
'Alex',
'Brody',
'Malachi',
'Emmanuel',
'Jonah',
'Beau',
'Jude',
'Antonio',
'Alan',
'Elliott',
'Elliot',
'Waylon',
'Xander',
'Timothy',
'Victor',
'Bryce',
'Finn',
'Brantley',
'Edward',
'Abraham',
'Patrick',
'Grant',
'Karter',
'Hayden',
'Richard',
'Miguel',
'Joel',
'Gael',
'Tucker',
'Rhett',
'Avery',
'Steven',
'Graham',
'Kaleb',
'Jasper',
'Jesse',
'Matteo',
'Dean',
'Zayden',
'Preston',
'August',
'Oscar',
'Jeremy',
'Alejandro',
'Marcus',
'Dawson',
'Lorenzo',
'Messiah',
'Zion',
'Maximus',
'River',
'Zane',
'Mark',
'Brooks',
'Nicolas',
'Paxton',
'Judah',
'Emiliano',
'Kaden',
'Bryan',
'Kyle',
'Myles',
'Peter',
'Charlie',
'Kyrie',
'Thiago',
'Brian',
'Kenneth',
'Andres',
'Lukas',
'Aidan',
'Jax',
'Caden',
'Milo',
'Paul',
'Beckett',
'Brady',
'Colin',
'Omar',
'Bradley',
'Javier',
'Knox',
'Jaden',
'Barrett',
'Israel',
'Matias',
'Jorge',
'Zander',
'Derek',
'Josue',
'Cayden',
'Holden',
'Griffin',
'Arthur',
'Leon',
'Felix',
'Remington',
'Jake',
'Killian',
'Clayton',
'Sean',
'Adriel',
'Riley',
'Archer',
'Legend',
'Erick',
'Enzo',
'Corbin',
'Francisco',
'Dallas',
'Emilio',
'Gunner',
'Simon',
'Andre',
'Walter',
'Damien',
'Chance',
'Phoenix',
'Colt',
'Tanner',
'Stephen',
'Kameron',
'Tobias',
'Manuel',
'Amari',
'Emerson',
'Louis',
'Cody',
'Finley',
'Iker',
'Martin',
'Rafael',
'Nash',
'Beckham',
'Cash',
'Karson',
'Rylan',
'Reid',
'Theo',
'Ace',
'Eduardo',
'Spencer',
'Raymond',
'Maximiliano',
'Anderson',
'Ronan',
'Lane',
'Cristian',
'Titus',
'Travis',
'Jett',
'Ricardo',
'Bodhi',
'Gideon',
'Jaiden',
'Fernando',
'Mario',
'Conor',
'Keegan',
'Ali',
'Cesar',
'Ellis',
'Jayceon',
'Walker',
'Cohen',
'Arlo',
'Hector',
'Dante',
'Kyler',
'Garrett',
'Donovan',
'Seth',
'Jeffrey',
'Tyson',
'Jase',
'Desmond',
'Caiden',
'Gage',
'Atlas',
'Major',
'Devin',
'Edwin',
'Angelo',
'Orion',
'Conner',
'Julius',
'Marco',
'Jensen',
'Daxton',
'Peyton',
'Zayn',
'Collin',
'Jaylen',
'Dakota',
'Prince',
'Johnny',
'Kayson',
'Cruz',
'Hendrix',
'Atticus',
'Troy',
'Kane',
'Edgar',
'Sergio',
'Kash',
'Marshall',
'Johnathan',
'Romeo',
'Shane',
'Warren',
'Joaquin',
'Wade',
'Leonel',
'Trevor',
'Dominick',
'Muhammad',
'Erik',
'Odin',
'Quinn',
'Jaxton',
'Dalton',
'Nehemiah',
'Frank',
'Grady',
'Gregory',
'Andy',
'Solomon',
'Malik',
'Rory',
'Clark',
'Reed',
'Harvey',
'Zayne',
'Jay',
'Jared',
'Noel',
'Shawn',
'Fabian',
'Ibrahim',
'Adonis',
'Ismael',
'Pedro',
'Leland',
'Malakai',
'Malcolm',
'Alexis',
'Kason',
'Porter',
'Sullivan',
'Raiden',
'Allen',
'Ari',
'Russell',
'Princeton',
'Winston',
'Kendrick',
'Roberto',
'Lennox',
'Hayes',
'Finnegan',
'Nasir',
'Kade',
'Nico',
'Emanuel',
'Landen',
'Moises',
'Ruben',
'Hugo',
'Abram',
'Adan',
'Khalil',
'Zaiden',
'Augustus',
'Marcos',
'Philip',
'Phillip',
'Cyrus',
'Esteban',
'Braylen',
'Albert',
'Bruce',
'Kamden',
'Lawson',
'Jamison',
'Sterling',
'Damon',
'Gunnar',
'Kyson',
'Luka',
'Franklin',
'Ezequiel',
'Pablo',
'Derrick',
'Zachariah',
'Cade',
'Jonas',
'Dexter',
'Kolton',
'Remy',
'Hank',
'Tate',
'Trenton',
'Kian',
'Drew',
'Mohamed',
'Dax',
'Rocco',
'Bowen',
'Mathias',
'Ronald',
'Francis',
'Matthias',
'Milan',
'Maximilian',
'Royce',
'Skyler',
'Corey',
'Kasen',
'Drake',
'Gerardo',
'Jayson',
'Sage',
'Braylon',
'Benson',
'Moses',
'Alijah',
'Rhys',
'Otto',
'Oakley',
'Armando',
'Jaime',
'Nixon',
'Saul',
'Scott',
'Brycen',
'Ariel',
'Enrique',
'Donald',
'Chandler',
'Asa',
'Eden',
'Davis',
'Keith',
'Frederick',
'Rowen',
'Lawrence',
'Leonidas',
'Aden',
'Julio',
'Darius',
'Johan',
'Deacon',
'Cason',
'Danny',
'Nikolai',
'Taylor',
'Alec',
'Royal',
'Armani',
'Kieran',
'Luciano',
'Omari',
'Rodrigo',
'Arjun',
'Ahmed',
'Brendan',
'Cullen',
'Raul',
'Raphael',
'Ronin',
'Brock',
'Pierce',
'Alonzo',
'Casey',
'Dillon',
'Uriel',
'Dustin',
'Gianni',
'Roland',
'Landyn',
'Kobe',
'Dorian',
'Emmitt',
'Ryland',
'Apollo',
'Aarav',
'Roy',
'Duke',
'Quentin',
'Sam',
'Lewis',
'Tony',
'Uriah',
'Dennis',
'Moshe',
'Isaias',
'Braden',
'Quinton',
'Cannon',
'Ayaan',
'Mathew',
'Kellan',
'Niko',
'Edison',
'Izaiah',
'Jerry',
'Gustavo',
'Jamari',
'Marvin',
'Mauricio',
'Ahmad',
'Mohammad',
'Justice',
'Trey',
'Elian',
'Mohammed',
'Sincere',
'Yusuf',
'Arturo',
'Callen',
'Rayan',
'Keaton',
'Wilder',
'Mekhi',
'Memphis',
'Cayson',
'Conrad',
'Kaison',
'Kyree',
'Soren',
'Colby',
'Bryant',
'Lucian',
'Alfredo',
'Cassius',
'Marcelo',
'Nikolas',
'Brennan',
'Darren',
'Jasiah',
'Jimmy',
'Lionel',
'Reece',
'Ty',
'Chris',
'Forrest',
'Korbin',
'Tatum',
'Jalen',
'Santino',
'Case',
'Leonard',
'Alvin',
'Issac',
'Bo',
'Quincy',
'Mack',
'Samson',
'Rex',
'Alberto',
'Callum',
'Curtis',
'Hezekiah',
'Finnley',
'Briggs',
'Kamari',
'Zeke',
'Raylan',
'Neil',
'Titan',
'Julien',
'Kellen',
'Devon',
'Kylan',
'Roger',
'Axton',
'Carl',
'Douglas',
'Larry',
'Crosby',
'Fletcher',
'Makai',
'Nelson',
'Hamza',
'Lance',
'Alden',
'Gary',
'Wilson',
'Alessandro',
'Ares',
'Kashton',
'Bruno',
'Jakob',
'Stetson',
'Zain',
'Cairo',
'Nathanael',
'Byron',
'Harry',
'Harley',
'Mitchell',
'Maurice',
'Orlando',
'Kingsley',
'Kaysen',
'Sylas',
'Trent',
'Ramon',
'Boston',
'Lucca',
'Noe',
'Jagger',
'Reyansh',
'Vihaan',
'Randy',
'Thaddeus',
'Lennon',
'Kannon',
'Kohen',
'Tristen',
'Valentino',
'Maxton',
'Salvador',
'Abdiel',
'Langston',
'Rohan',
'Kristopher',
'Yosef',
'Rayden',
'Lee',
'Callan',
'Tripp',
'Deandre',
'Joe',
'Morgan',
'Dariel',
'Colten',
'Reese',
'Jedidiah',
'Ricky',
'Bronson',
'Terry',
'Eddie',
'Jefferson',
'Lachlan',
'Layne',
'Clay',
'Madden',
'Jamir',
'Tomas',
'Kareem',
'Stanley',
'Brayan',
'Amos',
'Kase',
'Kristian',
'Clyde',
'Ernesto',
'Tommy',
'Casen',
'Ford',
'Crew',
'Braydon',
'Brecken',
'Hassan',
'Axl',
'Boone',
'Leandro',
'Samir',
'Jaziel',
'Magnus',
'Abdullah',
'Yousef',
'Branson',
'Jadiel',
'Jaxen',
'Layton',
'Franco',
'Ben',
'Grey',
'Kelvin',
'Chaim',
'Demetrius',
'Blaine',
'Ridge',
'Colson',
'Melvin',
'Anakin',
'Aryan',
'Lochlan',
'Jon',
'Canaan',
'Dash',
'Zechariah',
'Alonso',
'Otis',
'Zaire',
'Marcel',
'Brett',
'Stefan',
'Aldo',
'Jeffery',
'Baylor',
'Talon',
'Dominik',
'Flynn',
'Carmelo',
'Dane',
'Jamal',
'Kole',
'Enoch',
'Graysen',
'Kye',
'Vicente',
'Fisher',
'Ray',
'Fox',
'Jamie',
'Rey',
'Zaid',
'Allan',
'Emery',
'Gannon',
'Joziah',
'Rodney',
'Juelz',
'Sonny',
'Terrance',
'Zyaire',
'Augustine',
'Cory',
'Felipe',
'Aron',
'Jacoby',
'Harlan',
'Marc',
'Bobby',
'Joey',
'Anson',
'Huxley',
'Marlon',
'Anders',
'Guillermo',
'Payton',
'Castiel',
'Damari',
'Shepherd',
'Azariah',
'Harold',
'Harper',
'Henrik',
'Houston',
'Kairo',
'Willie',
'Elisha',
'Ameer',
'Emory',
'Skylar',
'Sutton',
'Alfonso',
'Brentley',
'Toby',
'Blaze',
'Eugene',
'Shiloh',
'Wayne',
'Darian',
'Gordon',
'London',
'Bodie',
'Jordy',
'Jermaine',
'Denver',
'Gerald',
'Merrick',
'Musa',
'Vincenzo',
'Kody',
'Yahir',
'Brodie',
'Trace',
'Darwin',
'Tadeo',
'Bentlee',
'Billy',
'Hugh',
'Reginald',
'Vance',
'Westin',
'Cain',
'Arian',
'Dayton',
'Javion',
'Terrence',
'Brysen',
'Jaxxon',
'Thatcher',
'Landry',
'Rene',
'Westley',
'Miller',
'Alvaro',
'Cristiano',
'Eliseo',
'Ephraim',
'Adrien',
'Jerome',
'Khalid',
'Aydin',
'Mayson',
'Alfred',
'Duncan',
'Junior',
'Kendall',
'Zavier',
'Koda',
'Maison',
'Caspian',
'Maxim',
'Kace',
'Zackary',
'Rudy',
'Coleman',
'Keagan',
'Kolten',
'Maximo',
'Dario',
'Davion',
'Kalel',
'Briar',
'Jairo',
'Misael',
'Rogelio',
'Terrell',
'Heath',
'Micheal',
'Wesson',
'Aaden',
'Brixton',
'Draven',
'Xzavier',
'Darrell',
'Keanu',
'Ronnie',
'Konnor',
'Will',
'Dangelo',
'Frankie',
'Kamryn',
'Salvatore',
'Santana',
'Shaun',
'Coen',
'Leighton',
'Mustafa',
'Reuben',
'Ayan',
'Blaise',
'Dimitri',
'Keenan',
'Van',
'Achilles',
'Channing',
'Ishaan',
'Wells',
'Benton',
'Lamar',
'Nova',
'Yahya',
'Dilan',
'Gibson',
'Camdyn',
'Ulises',
'Alexzander',
'Valentin',
'Shepard',
'Alistair',
'Eason',
'Kaiser',
'Leroy',
'Zayd',
'Camilo',
'Markus',
'Foster',
'Davian',
'Dwayne',
'Jabari',
'Judson',
'Koa',
'Yehuda',
'Lyric',
'Tristian',
'Agustin',
'Bridger',
'Vivaan',
'Brayson',
'Emmet',
'Marley',
'Mike',
'Nickolas',
'Kenny',
'Leif',
'Bjorn',
'Ignacio',
'Rocky',
'Chad',
'Gatlin',
'Greysen',
'Kyng',
'Randall',
'Reign',
'Vaughn',
'Jessie',
'Louie',
'Shmuel',
'Zahir',
'Ernest',
'Javon',
'Khari',
'Reagan',
'Avi',
'Ira',
'Ledger',
'Simeon',
'Yadiel',
'Maddux',
'Seamus',
'Jad',
'Jeremias',
'Kylen',
'Rashad',
'Santos',
'Cedric',
'Craig',
'Dominique',
'Gianluca',
'Jovanni',
'Bishop',
'Brenden',
'Anton',
'Camron',
'Giancarlo',
'Lyle',
'Alaric',
'Decker',
'Eliezer',
'Ramiro',
'Yisroel',
'Howard',
'Jaxx'
]
names = [
's1lent_v01d',
'junguwu1028',
'tiktokrewind0',
'Jackson_hardin1',
'Carmen.ycsel',
'natasha_is_my_bsf',
'domina_iris',
'johnnjayy',
'ashkeke',
'gappiejwz',
'minijey',
'teenhypehouse_5',
'ava_munro08',
'alexgrecu2005',
'nishabofficial',
'charlidamelio.s',
'hotukas',
'robinrajput11',
'_s_t_e_l_l_a_7',
'luvcrack',
'fatherco0n',
'team07',
'sumitdas812',
'rondarousey00',
'panarin10',
'charmed.zoee',
'followek.exe',
'_rxbloxgirl_',
'polatnergis',
'sandysauce',
'london.adoptme',
'xx.aesthetictingz.xx',
'soph.townsend',
'kimluvsyou',
'meme.uri_amuzante',
'morababyy',
'no_username06',
'charli..vibez',
'darrkblue',
'sawyermedien',
'zodiacjj',
'enesaltu2',
'aish25warya',
'jaygocrazyyyyy',
'_____nazwa_____',
'lolly.zoe',
'theolets',
'malkeetkaur53',
'libra867',
'janzayass',
'iibenjamin',
'libster.the.boss',
'officialdakota',
'brnntrrs',
'.shipdixieeaddisonn',
'makaylatovey',
'tenatenchy',
'memes4life47',
'ethsan',
'zunair72',
'gerom26',
'itz_jada_',
'jordanxlynn',
'kawtar.99',
'1sabxlla',
'hulya_sultan',
'leonald146',
'jaydelcoriano',
'ellie.luvs.you',
'_that_roblox_girl_',
'lavernes.dreams',
'greysxsammy',
'aamani_yt',
'i_need_jason',
'_picsart_35',
'kadie.ladd',
'beemo06',
'limited.jay',
'mdawson21',
'lmaoitslex',
'.alona',
'fidanzatikarol',
'biggybigg',
'_road',
'ac_non',
'lucianodvs11',
'f0ry0upage0',
'69think',
'robyngilmore_',
'queendeja115',
'gracek67',
'08_annamaria',
'powerlav',
'killerlav',
'anejciii',
'umeshkumar0285',
'just._.kimm',
'lundynbridge',
'zoe_boba',
'mobilabi',
'woossi_1811',
'stanleysbathwater1',
'__crackhead_vibes__',
'nightmare207',
'fxck.mochi',
'babysharkdoodoo',
'anuel__doblea',
'tiktoktomtom7',
'itz_just_meee',
'discort.memes',
'user94681479',
'crybxby_lxser',
'thejohnnyhq',
'agustd148',
'zonut_forever14',
'..emilyyxo',
'summertime29',
'depressed._',
'supa.swag.sydney',
'mattiashawty',
'ivan0000000000',
'koky550',
'disneypemberton',
'kaurmanpreetmultani',
'mariana.aresta',
'mariopalgon',
'just...oscxr',
'cx1h',
'redcat033',
'alineegtm',
'insanity.boo',
'ruth_46',
'oof6969',
'lexi._.spamzzz',
'yash.___',
'gracie.periodtt',
'agentbrutus',
'danlechuga',
'harry_potter_sara',
'______addison______',
'.aubriexautumn',
'muskanwahid',
'valq60',
'patharley',
'_korkmazselin_',
'beryamxsonsuz',
'a1.arri',
'kaliyah_hughley',
'skies_14',
'hells.boy',
'struggyexplorer',
'giannabryant13',
'thatbruinsguy',
'sofiaella15',
'idk.antony',
'mrkaykay',
'harp__sidhu',
'crackheaddaisy',
'wtf.richard',
'....yoda',
'elisabetttttttt',
'https..sami',
'arlo_the_gsd',
'adri_095',
'theredcherry',
'mamabling',
'reginageorge13',
'let_oliveira05',
'theacefamilys',
'hathidieulinh',
'dumbxtchjuiche',
'liberalhypehouse',
'vibinallison',
'lorenzointhebenzo',
'y0mmyhuzl3',
'ryanpruntyofficial',
'certified._tre',
'babieliza',
'strthingsedits',
'alizeh483',
'thatonecountrykid',
'jordanmartsolf',
'best425',
'noursherif41',
'siromasna_sam.0',
'.........sydney',
'samm.lly',
'julia.laprade',
'trendysisters',
'kaloyanstmbl',
'tommy.mascotti',
'smd.isabella',
'alexisholmes1',
'hailey_mariee',
'laurysferreira2020',
'diamonddonut',
'thehypehouse_2020',
'crackhead.paige',
'pyt.briannaaa',
'hxneyy...zlp',
'mari_2524',
'livsoftball15',
'nguyenvantai2002',
'its_jay_1947',
'1phuttv',
'riayz.14',
'ceceya1',
'dxddy...sad',
'sneha2917',
'zonut_4lifee',
'lorenafernandezzz_',
'_hadon_',
'100kfollowrswithnovids',
'snehagupta1283',
'anjimaxuofficialy',
'k0ver_fanpage_',
'saucyyyquan',
'.grwmlilac',
'artsykeeley',
'sasukeswifey',
'charlixaddisonxxx',
'possiblezoe',
'happygirlfan10',
'.zoesvibes',
'dang319',
'mohak_narang24',
'bxby.lexxii',
'arifbey0',
'armylove21',
'kaylee.m11',
'og.tower.of.heck.players',
'phat26200',
'royalking018',
'indianshaikhgangavati',
'awwlara',
'japjiikaur',
'etoarda1',
'utb1889',
'anhthu0910',
'cause.zlp',
'8daydreamer4',
'ta.mig.till.4u',
'emmy._.5',
'bxbyy_billie',
'tqzy',
'zoesmuah',
'north1956',
'ii_blxssom',
'vijaythakor2121',
'kawaii.charli',
'luissantos16',
'.snipez',
'....nick',
'sunty8888',
'cyrocakes',
'zip...rainbow',
'lasagnasvs',
'hudson960',
'katie_tran',
'ay_boi1',
'caothuylinh17',
'jimmysammon',
'spencerx_5',
'stefanslowinski8',
'bxby.zahara',
'megandemmet',
'bxbby.s',
'0merali',
'shmelowa',
'....luka',
'arthexmathis',
'robert.elanga1',
'uk_hype_house_12',
'larabaron',
'5rri',
'leilanii06',
'koolaid_colin',
'bardia_727',
'white15yroldboyalmost6ft',
'worldstareggs',
'hotel..packing',
'https...error_',
'hxney33',
'g0thicccc',
'syedali110'
]
names_list = '@..amyana,@.l.o.l,@tripland,@saif_rayeen,@koronavirus.ss,@jor2dan99,@lorangray,@millieswaffles,@ezgizemvsp,@dreamerandachiever,@i_love_poop1,@antoniiog,@jenna1236,@sunflower_adopt.me_,@gracemeow,@xx_toba_xx,@trackerthekid,@iokasti_mix,@user94681479,@nur_rr,@gunjanpare,@jayden________,@jordanmartsolf,@zoesmodern,@qtycosplay,@migpin,@.roses,@nooneaskedu,@sunflower.ashley,@positivelexi,@a.pariss,@fricksauce572,@hatice.24,@0merali,@itz_just_meee,@dance.hilma,@jamesblonde007,@officialdakota,@mihaly,@strangerthings011eggo,@moon.x.editzz,@queenangel60,@wyattdougls,@zoesmonth,@cherry...lqv,@iloveshirleytemples,@esse93,@grecia145,@kaylamulvihill,@tiktoktomtom7,@diisantoss,@.laurenkim,@.roblox_queen_,@jas9596,@megamindmeg,@amiel_weiss7,@jcasella,@iibenjamin,@facts_phobias,@sweetjace55,@x._bethh_.x,@_baseball_hype_house_,@valentinaa037,@jelly_fruits_xx4,@lorenzointhebenzo,@basementcat,@maroless,@kidd.kdk,@marta_cvijetic_09,@_the_intr0vert_,@chrisreynaga,@xmrflimflamx,@jimmybhathal,@yaboijohnny96,@siept,@kingora,@baby_girl467,@nightmare207,@0kate00,@423gang,@its_kevv,@vibinallison,@jessica.k.123,@lara5580,@starbucks,@lilbigd,@_charlidamelio..fanpage_,@.crisplav,@atul.16,@sasukeswifey,@ootony1310,@dhiyadd,@heyhoo4,@jacobowens,@user12226369,@derekisboss,@nemobigbutt,@xo.mimii,@fullpower420,@.butterflyxcharli,@theacefamilys,@verifymepleasetiktok,@daintyspa,@.carebear.zlp,@d4rk_sako,@sofiad223,@magestictiktoks,@keine_videos_mehr,@mobilabi,@kjhyeon,@just325,@bruh,@smallestpp,@htv11,@abigail_416,@user39537094,@maf_gomez,@yeeet69420,@dean734,@blaze189,@chopstick13,@ranveersingh,@gucci..charli,@charli_and_zoe_fanpage,@nflmemorable,@reginageorge13,@ujjwalgupta20,@just._.kimm,@tillyrowe,@here.ixi,@shakirkhansk,@td.bon,@expired,@superc00lgamer,@nari.besh74,@naruto_x_boruto_uzumaki,@cutie..zoeee,@strxwberrykisss_,@mamabling,@flextape,@desiree910,@wasonwage,@asmrworld1,@q.p._,@plainpotatoessss,@dangerlqv,@mwry0,@playboiogie,@joshuakingdon,@g0rge0usmess,@fortnite44443,@xoxofamous,@tamanna_69,@aditipynee,@pinarergudenx,@valeria,@shirindavid,@moon_mochiii,@adry4n4,@uout,@elena.alexandra,@eancollins,@vote_trump_2020_now,@picka_person,@sunshine_zoelav,@tropicgang,@zoesgreen,@ava.cady,@brawl_tiger,@mas_o,@peachy.laverne2,@jordanphelps7,@lickyonmyblicky2,@hiii_101,@ellaluvsyouu,@dxnkin.dxmelio,@a_k12,@elisabetttttttt,@killerlav,@barberick,@styleeditz,@kaylaorozco3,@vaughngordon,@anti.trump.house,@tannermelancon,@itsallenferrell,@gamer1001,@wtf.richard,@jaden,@teletubbiesforlife,@chloeebeaty11,@thomasjarvis,@bhristopher,@rommiinaa,@crackheaddaisy,@tiktok.hypehouse7,@user71986543,@fer_zepeda,@mrkaykay,@elena_eln,@petsmont,@ultrathot,@jordy430,@idk.antony,@cherryxthetic,@jacobhumphriessucks,@bring.back.summer,@emanarshad1,@late..nights,@df0007,@elise646,@lasagnasvs,@darrkblue,@.wonderful.zlp,@valentinaschulz,@cemreismyearth,@letmedrivethebusss,@cutietwento,@antoo_8,@r.i.p_2,@polarxox,@fabianstalheuer,@walter.reacts,@aldy_ansyah,@jesus_mv,@rq1s,@solardamelio,@anjimaxuofficialy,@gothicbratz,@momsplainer,@abby5343,@chleb4,@mohi_007,@kyleadamsz,@thatbruinsguy,@ayeeyee,@09ta,@luccasluccas2,@aditya6668,@adoptme.stars,@renataleon0,@huseyinkamal033,@dek1millionbath,@cringe.org,@charlidamelio.s,@chipichop,@krawd,@lilyeezy256,@iblamekyle,@harrypotter133,@dolayesoul,@laylal123,@tr1134,@aryan_286,@sunty8888,@s3an15k3lly,@themistycope,@.90s.things,@bogie23,@martin.c2,@m_a_x_4,@queenmayathebee,@08.08,@aesthetic_peaches7,@damienbabin,@_jay1k_,@nowhyhow,@luissantos16,@lucianodvs11,@addison.rea_fan,@norah_uwu,@ahmedkadry1,@lagaaia07,@jasmineorlando2,@faizann_khan0,@wassup907,@jacqueen,@fazedark,@rixiix,@nijahmickel,@divyanegi28,@marimrl,@sebi.46,@tallglassofvinegar,@vodkasweg,@marijo141,@liammheinz,@albercik96,@._.fede._,@lilyann100,@abstercadabster,@team07,@ayushisharma94,@chrisandmegan,@meme.uri_amuzante,@nba.fax,@hothuydao19,@veronica.torress,@hexxxlu,@andreanineteen,@lam1243,@besttiktoker7,@alyssasteelee,@bbygirl.laverne,@.jennaboo,@ti.k,@stylish._.laverne,@kth_tae112,@lts_flaming0,@theooooooooooooooooooo,@daddylikes,@saccage.cecarnet,@liltrashcant,@chemtrails,@user8533527,@princess.peppa,@bimprezervatifleri66,@kitetran,@fox652,@mrjerryofficial01,@nitram01,@gagatuckertea,@billieeilish.p,@.cek,@new2546,@gappiejwz,@wolves,@oak_tree,@yeclik,@brandenlewerke,@style.mp4,@mariamb8_,@_charli..damelio._,@ufc_.moments,@actual_factual,@carsonpaw,@zachary.beal,@clauudia_araujoo,@stephclairmont,@aura_tryhard,@.chroma,@tfue.official,@timschneider7,@.alona,@evelnc,@firmanfebriana,@.candlezoe,@lmaoitslex,@_lava_1,@gabrielle444,@deactivated.lol,@its_makeup,@akashmishra082,@coronaa_hypee_housee,@ibreakdaily,@.zoesflex,@livwoodward,@fortnite_games5,@alexisriley7,@firdaous13,@.gabi_,@jellytothebean,@drxwingg,@sneha2917,@user12365417,@joelwesltur,@memeluous,@.brookie._.cookie,@saltzoe,@winniebopper,@lyssynoel,@sahibakaursherni,@thgrefg,@jelly.lavv,@aidensharp2,@gumi,@valq60,@beemo06,@kadie.ladd,@axfbit,@fallqueen,@boomer.laverne,@hayleeryan08,@whatsup978,@yesilikebillieeilish,@luvcrack,@emsicle101,@limbs,@benjaminvaldez08,@luvdqmelio,@stardustcos,@nikol.ax,@willlllly,@claudiaflores78,@lebatzer,@x._oliver_.x,@ynwmellyiscool,@dylanisdaddyyy,@anwaramr,@bxbyy_billie,@aamani_yt,@incredible,@pennywisexxlav,@yaretziramirez36,@taliah.borza,@pinkzoes,@alexoliveira332,@imyoa,@libra.charlixx,@aleshkaluanaalban,@mihannofottutoilnikname,@indian_army36,@ad0pt.__.me,@goldyx.lav,@nflgenius,@happypotato6,@fatihhjuan,@ttvd3,@riumi,@starwars312,@andreakasti,@..misskeisha,@nle_23,@yasir1997,@boomer629,@freakyy.lavv,@surayakhan,@tiktokbd03,@c5076,@whyme3210,@itz_me_madi,@aandres12,@zoeslavenderr,@followforfollow357,@ceceya1,@user26854949,@gabcookie,@liz_ne,@michaelfans,@cherrymillie,@madafaka_123,@redmenace,@narendra.meena1,@ricoune,@clownjay,@yungdesirre,@shalinisingh1,@hypehousescandinavia,@deazity28,@dino.lqverne,@loregray,@tito937,@https....lxnely,@faya010,@xitz.odalys,@ii.kxfee,@taylor...xxx,@.badassxzlp,@katherine65,@n5289,@addison...avani,@agentbrutus,@sabinittas,@jatti_ak47,@tatiebabyy,@minahilmalik_727,@billieeilishfanclub,@warzonevideos,@therealbrianlouis,@softiee....zlp,@slavasaki,@tiktokgamer2,@kookiesdelfi,@logicks,@charlielevy,@alexa697,@mj_miyaa,@robloxisgayyyy,@adg653,@vibeszody,@lil_birdy_nursery123,@vikalpmehta,@asc74,@ellamay098,@gael_88,@dec.01,@ste063,@lxnq,@divacharli,@lizbeth_sarahi,@kitkat731,@yagizaltan,@chris_838,@rachellehoffman,@thjrs,@avocado__3,@aesthetics_8800,@sugarxlavernex,@coronacallie,@sara76338,@.cupidlav,@dm839,@getmefamousrightnow,@.cj4,@abhishekbharti123,@valid.liyah,@lobell0,@maddystanszlp,@mehyo,@isabelle_.1,@sofi14a,@raihauuu,@cloudyxbliss,@satisfying.videos27,@pedrosampaioo,@skye...official,@kennyholland,@whitegold14,@deucethegsp,@anjela_ilieva,@xdrxpzx,@zoesblue,@abigail0626,@elle_ge,@rockyboy786,@its_jay_1947,@hannahgwenn,@https.cole,@just.maui,@huskyplays,@posting..random..stuff,@mattsworldd,@lilnectarine,@ameowo,@falone0,@zlp._.editzzzz,@.zoescharli,@chips.lav,@_tropical.zlp,@mardelarosa,@lulu,@hotukas,@hypehouseextras,@isauramende,@darkclan123,@aestethics0,@timshmee,@.reverse,@totallyjayden,@fcbarcelona05,@aj_bagtas,@z0eswife,@xx.aesthetictingz.xx,@taimurshah1,@diptimayadipa,@deelia,@nourashraf84,@.vka,@peaceout23,@carolineeldridge,@poolcleaningx_,@shanrosee,@positive_roblox,@angela.levy,@antoquestaemagianera,@polatnergis,@zelluscars,@og.tower.of.heck.players,@krishnakapoor5,@cx1h,@tokyox2,@yessirr1,@lakshmi962,@valentina011rg,@shreemanbhandarii,@munahiyari,@jaximax,@shienne,@conservatives2020,@armylove21,@davidnavarrop,@smweaver,@strawberry..lqv,@ashleymaeda,@2novall,@amadioha,@lebronjames007,@zainrazakhan1,@rafa.ele,@lxciq.eqits,@kaurmanpreetmultani,@typicalxjenni,@alexandrawilliams,@rory.m,@viviwanderley,@jerseyboy05,@charm.lavv,@poo_jonny,@yellowhearts.lav,@bruxinhaoficial,@kimdyy,@gayamii,@goldenpunk,@goodvibes4588,@..dx,@user87668863,@kawtar.99,@jackandgabrielle,@ne.va,@pepsi..lav,@omarhaider3,@zodiacs_____101,@fathernelly,@jjjaaahhh999,@dailydoseoftik.tok,@.bbymartinez,@mohak_narang24,@myn4m3,@._snapchat_.12,@zoesrenegade,@tootpoo,@cristiantorres09,@user5410800,@panarin10,@oceanbae,@eleni_pol,@whitekahbaa,@koky550,@deliyiz.46,@shilynnsan,@gabriela.503,@foreveralone130,@hotel..packing,@ramiro2020,@nilo0,@worldstareggs,@luckysunter,@deenkhan_,@alexisholmes1,@superliga,@smd.isabella,@zoe_lovely_,@wspcharli,@aamir_arab22,@dannaxu,@tommy.mascotti,@kats75,@.aliasofiaa,@mayrli,@bostonpro,@koolaid_colin,@m.nabil79,@rixstarr,@marwah000,@seymabs,@gerom26,@something_intresting,@unknown.sad.boy,@bad.edxts,@5rri,@jae,@fatiiiii77,@antiroosshampoo,@saifsk55,@zach_xd,@pavlinamihaylova,@snapchat.streaks33,@fricxz,@summertime29,@dawsonthewrestler,@1924s,@beanos_team,@emoji.hype.house606,@dang319,@satansbestie,@minecraft____________,@kfc_boys,@muhanned_2001,@7anzer,@pavveu,@deborahruiz,@mughal930,@selen100,@hantwee,@elizabet852,@.zoesvibes,@abdullah_x5,@random._.editszzz,@wesley.wu,@ew055,@faris_313,@donas__,@ethsan,@morgan.schneiderr,@ashlynjohnson0,@roblox._.gurll6,@agustd148,@posemalone,@vsp._.codes,@valevalesoyyo,@aesthetix98,@makaylatovey,@jbhh95i,@girlsplayroblox,@best425,@mya...grace,@..baddielqv,@paroosz,@yalikejazzzzzzzz,@kurdin_26,@matheze,@noddylly,@tiktokkarie,@butterflxy,@.leilaaaaaa,@julka_dulewicz,@jasangel,@loren.kurd,@pattijohnson1,@liam_tiktok,@aestheticvibes09,@george_12343,@jakepaul666,@just.alex.ash,@audacityyy,@firework.lavv,@babynoda,@natxxxnat,@nakshatra.14,@ivy9080,@tylerscheider,@igorsdead,@vampire._.laverne,@tingting228,@mariap113,@daymio,@kanda25,@lundynbridge,@kunlanat23,@bren472,@fxck.jax,@bknick23,@.dunkin...zonuts,@abdulrazakhan,@lizukaakhalaia,@farazkayy,@user13373185,@jaywuvsu,@pennywisexzoe,@datwiz,@thathijaabi,@small.boy,@yungk9xs,@spencerx_5,@adri_095,@philippines09,@fighterfox,@random_things_213,@xxnightmarewolfxx,@gacha_life_442,@anhtu098,@caothuylinh17,@maria_queennn,@sofia78900,@girl_hacks,@perla_28,@user59003119,@addison.dunkin.charli,@sim.d,@peach_chu__,@name638,@thisisnotevaaa,@paigealyssa,@chrisluisdan,@sararetalitv,@follow4follow16,@texting..celebs,@kitty.lqverne,@isaidstop3,@abz_yt,@aadenramclam,@kayleighmarie91,@marina.032,@nknamkhing,@shhhoe,@cukhuong26,@queendeja115,@jeffw,@bruh.chill,@.grwmlilac,@real.google.tricks,@r.y50,@juliaa_39,@booba121,@dino..lqv,@cjcastillo7,@ranchh,@ghosty___,@cayan2,@shaikmalik54,@sadboyjackson,@depressed27,@oimj,@itz.ashleyyy,@rc_leader,@flowerxxvibes,@baddie.xlaverne0,@kadenstyer,@fatkill,@ruby_cobbster,@seasidezlp,@fyp.ceo,@paolomassignani1,@bobadeana4,@andreakaraj,@duyenmynguyen,@sunnycloudss,@potatocharli,@afreenbili,@breenbot,@dawedar,@peachy...lemons,@boy,@a1.arri,@jonnyseymour,@takis...zlpp,@cinnamonxpemberton,@sabnguyen,@.c0tton,@sandywood4,@thaoo207,@tvdmills,@gamet244,@abodme,@prashanthroyprash,@undertale,@codysbed,@theycallmematt_,@aesthetic.blissss,@jester3am,@temnecessidade,@yassersk_,@dizzyangel88,@charidamilio,@unicornlaverne,@blesivedits2,@uniqueboyansh,@justfreyaandfriends,@datrie_fan2009,@_zoeorlove_,@larraysfunniest,@avani_greggs,@ana_paulax,@shadowz.fn,@canizzl,'''
names = [n[1:] for n in names_list.split(',')]
names = map(lambda n: n.lower(), names)
names = ['benthamite', 'mathematicanese']
for i in range(0,6000):
    for name in names:
        print(name)
        try:
            tiktoks = api.byUsername(name, count=50)
        except Exception as e:
            print(e)
            continue
        t_time=str(datetime.datetime.now())
        print(len(tiktoks))
        print(t_time)
        for t in tiktoks:
            new_t=json.dumps(t)
            cur.execute('INSERT INTO tiktok (time,json) VALUES (%s,%s)', (t_time,new_t))
            #outfile.write('%s\t%s\t%s\n' % (t['id'],t_time,t))
        conn.commit()
    time.sleep(600 + randint(5, 15))
cur.close()
conn.close()
#cat d:\Documents\tiktok_banque\TikTokApi.py | python
