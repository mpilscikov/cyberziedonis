RANDOM_POEMS_FOR_GIBBERISH_AMOUNT = 5
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}

ZIEDONIS_VOICE_URLS = (
    'https://www.youtube.com/watch?v=MIfI8mKpJZU',
    'https://www.youtube.com/watch?v=1vdtPb_xQzc',
    'https://www.youtube.com/watch?v=HcCS-OCAwmA',
    'https://www.youtube.com/watch?v=OYM4vsBxCvM&list=PLA71NlhMznlmjjNoEYDYsIxdQkss5FD4Q&index=6',
)

EPIFANIJAS_URL = 'https://www.youtube.com/watch?v=AYTtrVx74PI'

DZIVOT_COMMAND_MESSAGE = '''
Mēs dzimstam no tēva,
Mēs dzimstam no mātes,
Dzimstam gultās, migās un lizdās.
'''

NOMIRT_COMMAND_MESSAGE = '''
Neviena dzīves stunda
Nav pagājusie lieka.
Šī bija pilna zāles,
Un šī bija pilna prieka.
'''

HELP_LIST = '''```
Komanda           | Darbība 
------------------| ----------------------------------------------------------------
dzejolis          | atsūta nejauši izvēlētu I. Ziedoņa dzejoli
!bulduris         | atsūta nejauši uzģenerētu dzejoli
!dzivot           | pievienojas balss kanālam, kuram pieslēgts lietotājs
!nomirt           | atslēdzas no balss kanāla
!balss            | balss kanālā tiek atskaņots nejauši izvēlēts I. Ziedoņa dzejolis
!balss epifanijas | balss kanālā tiek atskaņotas I. Ziedoņa Epifānijas
!paliga           | atsūta sarakstu ar komandām
```'''