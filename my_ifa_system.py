from typing import List, Dict
import sqlite3


# a class to represent an odu
class OduIfa:
    def __init__(self, odu_name: str, verses: List[str], meanings: List[str], advice: List[str]):
        self.odu_name = odu_name
        self.verses = verses
        self.meanings = meanings
        self.advice = advice


odu_ifa = [
    OduIfa(
        odu_name="eji ogbe",
        verses=[
            '''
            Eji Ogbe ni oruko mi, mo ni oruko ajinde, mo ni oruko alafia,
            Mo ni oruko orogun, mo ni oruko agbada.
            Orunmila ti o gba enikan, ti o ni gbogbo ibi si o.
            Orunmila ni ko si ibi, ko si arun, ko si aisan,
            Eyin ti e ba n gbe aye yin ba ni owo orun, 
            Eyin ti e ba ti n gbe aye yin ba ni owo aiye.
            ''',

        ],
        meanings=[
            '''
            This Odu signifies new beginnings, success, enlightenment, and a connection to
            divine wisdom. This verse speaks about overcoming obstacles and achieving peace 
            and resurrection. This odu emphasizes the power of Orunmila, the deity of wisdom
            and divination.
            ''',

        ],
        advice=['''
        Embrace new beginnings, maintain peace and be peaceful with everybody and pay close attention
        to your health.
        ''']
    ),
    OduIfa(
        odu_name= "oyeku meji",
        verses= [
            '''
            Oyeku Meji ni gba mi l'owo iku
            Ebo ni o se, ki o le b'alafia ni ile aye
            Adifa fun Oyeku Meji
            Ti nlo sode, ti nlo reru
            Oyeku Meji ni gba mi l'owo iku
            Ebo ni o se, ki o le b'alafia ni ile aye
            '''
        ],
        meanings= [
            '''
            Oyeku Meji represents darkness, death, and transformation. 
            It signifies the importance of rituals and sacrifices to avoid 
            negative outcomes and ensure peace and stability in life. 
            This Odu warns against neglecting spiritual obligations and 
            emphasizes the need for constant spiritual vigilance.
            '''
        ],
        advice=[
            '''
            Perform ritual to avoid negative occurrences, avoid taking unnecessary risks that may lead to harm.
            '''
        ]
    ),

]


# SQLite database
def create_database():
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    # Odu ifa table
    c.execute('''
        CREATE TABLE IF NOT EXISTS odu_ifa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            odu_name TEXT NOT NULL,
            verses TEXT NOT NULL,
            meanings TEXT NOT NULL,
            advice TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


create_database()


def insert_odu_ifa(odu_ifa: OduIfa):
    conn = sqlite3.connect('ifa_divination.db')
    c = conn.cursor()

    # Insert Odu Ifa data
    c.execute('''
        INSERT INTO odu_ifa (odu_name, verses, meanings, advice)
        VALUES (?, ?, ?, ?)
    ''', (odu_ifa.odu_name, '\n'.join(odu_ifa.verses), '\n'.join(odu_ifa.meanings), '\n'.join(odu_ifa.advice)))

    conn.commit()
    conn.close()


for odu in odu_ifa:
    insert_odu_ifa(odu)


# get data from my ifa database

