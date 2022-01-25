from googletrans import Translator
from skpy import SkypeEventLoop,SkypeNewMessageEvent
from getpass import getpass
import csv
import random
import threading

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}


def guide_txt():
    return """لطفا برای استفاده از ربات مانند روش زیر عمل کنید:
    زبان مبدا زبان مقصد
    ترجمه
    
    مثال:
    en fa
    Hello How Are You?"""


def translateBot(txt):
    txt_l = str(txt).splitlines()
    if(len(txt_l)<2):
        return guide_txt()
    lang_l = txt_l[0].split(' ')
    if(len(lang_l)<2):
        return guide_txt()
    if(lang_l[0] in LANGUAGES.keys() and lang_l[1] in LANGUAGES.keys()):
        msg = txt_l[1:]
        msg = '\n'.join(msg)
        return translator.translate(msg, dest=lang_l[1], src=lang_l[0]).text
    else:
        return """زبان مقصد و یا زبان مبدا صحیح نمی باشند.
        لطفا از کد های دو حرفی زبان ها استفاده کنید. مانند:
        fa, en, ja, ar, ..."""

class MySkype(SkypeEventLoop):
    def onEvent(self, event):            
        for request in self.contacts.requests():
                request.accept()
        if isinstance(event, SkypeNewMessageEvent) \
          and not event.msg.userId == self.userId :
            for request in self.contacts.requests():
                request.accept()
            
            msg = "amirrezashams.ir" if event.msg.content == "about" else translateBot(event.msg.content)
            event.msg.chat.sendMsg(msg)
            
if __name__ == "__main__":
    translator = Translator()
    sk = MySkype("yousername@outlook.com", "Password", autoAck=True)
    print("Ready!")
    sk.loop()
