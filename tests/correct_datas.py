"""
JSON с корректными данными.
Для упрощения данные в этом файле были взяты из соответствующих ответов GET.
Если JSON-ы, которые мы записали в файл передать методу POST,
потом запустить pytest, то все будет ОК.


"""


mcc_codes = {
    "data": [
        {
            "mcc": 742,
            "edited_description": "Veterinary Services",
            "combined_description": "Veterinary Services",
            "russian_name": "Ветеринарные услуги",
            "russian_description": "Лицензированные специалисты в основном занимающиеся практикой ветеринарии, стоматологии или хирургии для всех видов животных; таких как домашние животные (например, собаки, кошки, рыба), домашний скот и другие фермерские животные (например, рогатый скот, лошади, овцы, свиньи, козы, домашние птицы, пчелы) и экзотические животные."
        },
        {
            "mcc": 763,
            "edited_description": "Agricultural Co-operatives",
            "combined_description": "Agricultural Co-operatives",
            "russian_name": "Сельскохозяйственные кооперативы",
            "russian_description": "Ассоциации и кооперативы, которые предоставляют услуги управления фермами или оказывают помощь в сельскохозяйственных операциях. Примерами таких услуг являются финансовая помощь, управление или полное содержание сельскохозяйственных культур, подготовка почвы, посадка и культивация, аэрофотосжигание и распыление, борьба с болезнями и насекомыми, борьба с сорняками и сбор урожая.\nДля точек, которые предоставляют складские помещения и хранилища ферм, используется MCC 4225."
        },
        {
            "mcc": 780,
            "edited_description": "Horticultural Services, Landscaping Services",
            "combined_description": "Horticultural Services, Landscaping Services",
            "russian_name": "Услуги садоводства и ландшафтного дизайна",
            "russian_description": "Ландшафтные архитекторы и другие поставщики услуг по ландшафтному планированию и дизайну. Кроме того, точки, которые предлагают различные услуги по уходу за газоном и садом, такие как посадка, удобрение, выкос, мульчирование, посев, опрыскивание и укладка дерна."
        },
        {
            "mcc": 1520,
            "edited_description": "General Contractors-Residential and Commercial",
            "combined_description": "General Contractors-Residential and Commercial",
            "russian_name": "Генеральные подрядчики – жилое и коммерческое строительство",
            "russian_description": "Генеральные подрядчики, в основном занимающиеся строительством жилых и коммерческих зданий. Строительные услуги могут включать новое строительство, реконструкцию, ремонт, дополнения и изменения."
        },
        {
            "mcc": 1711,
            "edited_description": "Air Conditioning Contractors – Sales and Installation, Heating Contractors – Sales, Service, Installation",
            "combined_description": "Air Conditioning Contractors – Sales and Installation, Heating Contractors – Sales, Service, Installation",
            "russian_name": "Генеральные подрядчики по вентиляции, теплоснабжению и водопроводу",
            "russian_description": "Специальные торговые подрядчики, которые работают с системами отопления, водопровода и вентиляции. Примерами их услуг являются: балансировка и испытания вентиляционных системы, установка дренажной системы, ремонт отопления, установка опрскивателей газонов, работа с холодильными и морозильными камерами, подключения и соединения канализационных сетей, солнечное отопление, установка поливочных систем и установка и обслуживание водяных насосов."
        },
        {
            "mcc": 1731,
            "edited_description": "Electrical Contractors",
            "combined_description": "Electrical Contractors",
            "russian_name": "Подрядчики по электричеству",
            "russian_description": "Специальные торговые подрядчики, выполняющие работы по электричеству, такие как установка пожарной сигнализации, звукового, телекоммуникационного и телефонного оборудования."
        },
        {
            "mcc": 1740,
            "edited_description": "Insulation – Contractors, Masonry, Stonework Contractors, Plastering Contractors, Stonework and Masonry Contractors, Tile Settings Contractors",
            "combined_description": "Insulation – Contractors, Masonry, Stonework Contractors, Plastering Contractors, Stonework and Masonry Contractors, Tile Settings Contractors",
            "russian_name": "Изоляция, мозаика, штукатурные работы, каменная кладка, облицовка плиткой, кафелем",
            "russian_description": "Специальные торговые подрядчики, выполняющие мозаичные работы, каменные работы и другие работы с камнем, такие как строительство камина, облицовка плиткой, простая и декоративная штукатурка и изоляция. Эти подрядчики также могут выполнять работы по кирпичной кладке, керамике и мрамору, мозаичные работы, акустические работы и работы с конструкциями из гипсокартона."
        },
        {
            "mcc": 1750,
            "edited_description": "Carpentry Contractors",
            "combined_description": "Carpentry Contractors",
            "russian_name": "Столярные работы",
            "russian_description": "Специальные торговые подрядчики, которые выполняют столярные работы для строительных проектов, таких как сборка, обрамление, отделка, а также установка окон и дверей."
        },
        {
            "mcc": 1761,
            "edited_description": "Roofing – Contractors, Sheet Metal Work – Contractors, Siding – Contractors",
            "combined_description": "Roofing – Contractors, Sheet Metal Work – Contractors, Siding – Contractors",
            "russian_name": "Кровельные и сайдинговые работы, обработка листового металла",
            "russian_description": "Специальные торговые подрядчики, которые выполняют кровельные, обшивочные работы и выполняют работы из листового металла, включая архитектурные работы, потолки и световые люки, установку воздуховодов и водостоков, а также напыление, покраску или покрытие крыши."
        },
        {
            "mcc": 1771,
            "edited_description": "Contractors – Concrete Work",
            "combined_description": "Contractors – Concrete Work",
            "russian_name": "Подрядчики бетонных работ",
            "russian_description": "Специальные торговые подрядчики, выполняющие бетонные, цементные или асфальтовые работы, строят частные подъездные и пешеходные пути из всех материалов, заливают бетон для фундаментов, выполняют цементные работы и строят бетонные дворики и тротуары."
        },
        {
            "mcc": 1799,
            "edited_description": "Contractors – Special Trade, Not Elsewhere Classified",
            "combined_description": "Contractors – Special Trade, Not Elsewhere Classified",
            "russian_name": "Контрактные услуги – нигде более не классифицированные",
            "russian_description": "Специальные торговые подрядчики, выполняющие строительные работы, не классифицированные в других категориях. Примеры включают в себя установку навеса, сантехнические услуги, строительство заборов, установку пожарной лестницы, помощь при переездах, замену домашних окон, установку гаражных ворот, установку напольного покрытия, декоративные металлические работы, строительство бассейнов, стекольные работы, бурение скважин, поклейку обоев, гидроизоляцию и сварку."
        },
        {
            "mcc": 2741,
            "edited_description": "Miscellaneous Publishing and Printing",
            "combined_description": "Miscellaneous Publishing and Printing",
            "russian_name": "Различные издательства/ печатное дело",
            "russian_description": "Торговые точки, занимающиеся оптовой печатью, издательской деятельностью или переплетом книг. Примеры материалов, производимых такими точками, включают книги, периодические издания, журналы, карты и атласы, информационные бюллетени для бизнеса, каталоги, партитуры, образцы документов, технические руководства и документы, телефонные справочники и ежегодники.\n\nДля оптовых распространителей книг, брошюр и учебных материалов используется MCC 5192."
        },
        {
            "mcc": 2791,
            "edited_description": "Typesetting, Plate Making, & Related Services",
            "combined_description": "Typesetting, Plate Making, & Related Services",
            "russian_name": "Набор текстов, изготовление печатных форм и связанные услуги",
            "russian_description": "Торговые точки, которые осуществляют оптовый набор текста для полиграфии и изготавливают печатные формы для полиграфических целей. Примерами таких услуг являются набор рекламных текстов, набор фотографий, автоматизированный набор текста и цветоделение; изготовление позитивов и негативов, из которых изготавливаются офсетные литографические печатные формы; и гравировка или тиснение для печатных целей, таких как гравировка по дереву, резине, меди, стали или фотогравировка.\n\nДля торговых точек, которые в основном предоставляют оптовые услуги печати, используется MCC 2741."
        },
        {
            "mcc": 2842,
            "edited_description": "Specialty Cleaning, Polishing, and Sanitation Preparations",
            "combined_description": "Specialty Cleaning, Polishing, and Sanitation Preparations",
            "russian_name": "Санитарная обработка, полировка и специализированная подготовка",
            "russian_description": "Оптовые производители полиролей, чистящих растворов, дезинфицирующих средств, моющих средств для больниц и другие санитарные препараты. Продукты для продажи могут включать дезодоранты неличного назначения, окрашивание искусственной кожи и других материалов, средства для удаления воска, растворители для обезжиривания, химические средства для сухой чистки, средства для удаления ржавчины и пятен, а также чистящие растворы для стекла, краски или обоев."
        },
        {
            "mcc": 3000,
            "edited_description": "UNITED AIRLINES",
            "combined_description": "UNITED AIRLINES",
            "russian_name": "United Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3001,
            "edited_description": "AMERICAN AIRLINES",
            "combined_description": "AMERICAN AIRLINES",
            "russian_name": "American Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3002,
            "edited_description": "PAN AMERICAN",
            "combined_description": "PAN AMERICAN",
            "russian_name": "Pan American",
            "russian_description": "null"
        },
        {
            "mcc": 3003,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Eurofly",
            "russian_description": "null"
        },
        {
            "mcc": 3004,
            "edited_description": "TRANS WORLD AIRLINES",
            "combined_description": "TRANS WORLD AIRLINES",
            "russian_name": "Dragonair",
            "russian_description": "null"
        },
        {
            "mcc": 3005,
            "edited_description": "BRITISH AIRWAYS",
            "combined_description": "BRITISH AIRWAYS",
            "russian_name": "British Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3006,
            "edited_description": "JAPAN AIRLINES",
            "combined_description": "JAPAN AIRLINES",
            "russian_name": "Japan Air Lines",
            "russian_description": "null"
        },
        {
            "mcc": 3007,
            "edited_description": "AIR FRANCE",
            "combined_description": "AIR FRANCE",
            "russian_name": "Air France",
            "russian_description": "null"
        },
        {
            "mcc": 3008,
            "edited_description": "LUFTHANSA",
            "combined_description": "LUFTHANSA",
            "russian_name": "Lufthansa",
            "russian_description": "null"
        },
        {
            "mcc": 3009,
            "edited_description": "AIR CANADA",
            "combined_description": "AIR CANADA",
            "russian_name": "Air Canada",
            "russian_description": "null"
        },
        {
            "mcc": 3010,
            "edited_description": "KLM (ROYAL DUTCH AIRLINES)",
            "combined_description": "KLM (ROYAL DUTCH AIRLINES)",
            "russian_name": "Royal Dutch Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3011,
            "edited_description": "AEORFLOT",
            "combined_description": "AEORFLOT",
            "russian_name": "Аэрофлот",
            "russian_description": "null"
        },
        {
            "mcc": 3012,
            "edited_description": "QANTAS",
            "combined_description": "QANTAS",
            "russian_name": "Qantas",
            "russian_description": "null"
        },
        {
            "mcc": 3013,
            "edited_description": "ALITALIA",
            "combined_description": "ALITALIA",
            "russian_name": "Alitalia",
            "russian_description": "null"
        },
        {
            "mcc": 3014,
            "edited_description": "SAUDIA ARABIAN AIRLINES",
            "combined_description": "SAUDIA ARABIAN AIRLINES",
            "russian_name": "Saudi Arabian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3015,
            "edited_description": "SWISSAIR",
            "combined_description": "SWISSAIR",
            "russian_name": "Swiss International Air Lines",
            "russian_description": "null"
        },
        {
            "mcc": 3016,
            "edited_description": "SAS",
            "combined_description": "SAS",
            "russian_name": "Scandinavian Airline System",
            "russian_description": "null"
        },
        {
            "mcc": 3017,
            "edited_description": "SOUTH AFRICAN AIRWAYS",
            "combined_description": "SOUTH AFRICAN AIRWAYS",
            "russian_name": "South African Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3018,
            "edited_description": "VARIG (BRAZIL)",
            "combined_description": "VARIG (BRAZIL)",
            "russian_name": "Varig (Бразилия)",
            "russian_description": "null"
        },
        {
            "mcc": 3019,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3020,
            "edited_description": "AIR-INDIA",
            "combined_description": "AIR-INDIA",
            "russian_name": "Air India",
            "russian_description": "null"
        },
        {
            "mcc": 3021,
            "edited_description": "AIR ALGERIE",
            "combined_description": "AIR ALGERIE",
            "russian_name": "Air Algerie",
            "russian_description": "null"
        },
        {
            "mcc": 3022,
            "edited_description": "PHILIPPINE AIRLINES",
            "combined_description": "PHILIPPINE AIRLINES",
            "russian_name": "Philippine Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3023,
            "edited_description": "MEXICANA",
            "combined_description": "MEXICANA",
            "russian_name": "Mexicana",
            "russian_description": "null"
        },
        {
            "mcc": 3024,
            "edited_description": "PAKISTAN INTERNATIONAL",
            "combined_description": "PAKISTAN INTERNATIONAL",
            "russian_name": "Pakistan International",
            "russian_description": "null"
        },
        {
            "mcc": 3025,
            "edited_description": "AIR NEW ZEALAND",
            "combined_description": "AIR NEW ZEALAND",
            "russian_name": "Air New Zealand Limited International",
            "russian_description": "null"
        },
        {
            "mcc": 3026,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Emirates Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3027,
            "edited_description": "UTA/INTERAIR",
            "combined_description": "UTA/INTERAIR",
            "russian_name": "Union de Transports Aeriens",
            "russian_description": "null"
        },
        {
            "mcc": 3028,
            "edited_description": "AIR MALTA",
            "combined_description": "AIR MALTA",
            "russian_name": "Air Malta",
            "russian_description": "null"
        },
        {
            "mcc": 3029,
            "edited_description": "SABENA",
            "combined_description": "SABENA",
            "russian_name": "SN Brussels Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3030,
            "edited_description": "AEROLINEAS ARGENTINAS",
            "combined_description": "AEROLINEAS ARGENTINAS",
            "russian_name": "Aerolineas Argentinas",
            "russian_description": "null"
        },
        {
            "mcc": 3031,
            "edited_description": "OLYMPIC AIRWAYS",
            "combined_description": "OLYMPIC AIRWAYS",
            "russian_name": "Olympic Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3032,
            "edited_description": "EL AL",
            "combined_description": "EL AL",
            "russian_name": "El Al",
            "russian_description": "null"
        },
        {
            "mcc": 3033,
            "edited_description": "ANSETT AIRLINES",
            "combined_description": "ANSETT AIRLINES",
            "russian_name": "Ansett Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3034,
            "edited_description": "AUSTRAINLIAN AIRLINES",
            "combined_description": "AUSTRAINLIAN AIRLINES",
            "russian_name": "Etihad Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3035,
            "edited_description": "TAP (PORTUGAL)",
            "combined_description": "TAP (PORTUGAL)",
            "russian_name": "Tap (Португалия)",
            "russian_description": "null"
        },
        {
            "mcc": 3036,
            "edited_description": "VASP (BRAZIL)",
            "combined_description": "VASP (BRAZIL)",
            "russian_name": "VASP (Бразилия)",
            "russian_description": "null"
        },
        {
            "mcc": 3037,
            "edited_description": "EGYPTAIR",
            "combined_description": "EGYPTAIR",
            "russian_name": "EgyptAir",
            "russian_description": "null"
        },
        {
            "mcc": 3038,
            "edited_description": "KUWAIT AIRLINES",
            "combined_description": "KUWAIT AIRLINES",
            "russian_name": "Kuwait Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3039,
            "edited_description": "AVIANCA",
            "combined_description": "AVIANCA",
            "russian_name": "Avianca",
            "russian_description": "null"
        },
        {
            "mcc": 3040,
            "edited_description": "GULF AIR (BAHRAIN)",
            "combined_description": "GULF AIR (BAHRAIN)",
            "russian_name": "Gulf Air (Бахрейн)",
            "russian_description": "null"
        },
        {
            "mcc": 3041,
            "edited_description": "BALKAN-BULGARIAN AIRLINES",
            "combined_description": "BALKAN-BULGARIAN AIRLINES",
            "russian_name": "Balkan—Bulgarian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3042,
            "edited_description": "FINNAIR",
            "combined_description": "FINNAIR",
            "russian_name": "Finnair",
            "russian_description": "null"
        },
        {
            "mcc": 3043,
            "edited_description": "AER LINGUS",
            "combined_description": "AER LINGUS",
            "russian_name": "Aer Lingus",
            "russian_description": "null"
        },
        {
            "mcc": 3044,
            "edited_description": "AIR LANKA",
            "combined_description": "AIR LANKA",
            "russian_name": "Air Lanka",
            "russian_description": "null"
        },
        {
            "mcc": 3045,
            "edited_description": "NIGERIA AIRWAYS",
            "combined_description": "NIGERIA AIRWAYS",
            "russian_name": "Nigeria Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3046,
            "edited_description": "CRUZEIRO DO SUL (BRAZIJ)",
            "combined_description": "CRUZEIRO DO SUL (BRAZIJ)",
            "russian_name": "Cruzeiro do Sul (Бразилия)",
            "russian_description": "null"
        },
        {
            "mcc": 3047,
            "edited_description": "THY (TURKEY)",
            "combined_description": "THY (TURKEY)",
            "russian_name": "Turkish Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3048,
            "edited_description": "ROYAL AIR MAROC",
            "combined_description": "ROYAL AIR MAROC",
            "russian_name": "Royal Air Maroc",
            "russian_description": "null"
        },
        {
            "mcc": 3049,
            "edited_description": "TUNIS AIR",
            "combined_description": "TUNIS AIR",
            "russian_name": "Tunis Air",
            "russian_description": "null"
        },
        {
            "mcc": 3050,
            "edited_description": "ICELANDAIR",
            "combined_description": "ICELANDAIR",
            "russian_name": "Icelandair",
            "russian_description": "null"
        },
        {
            "mcc": 3051,
            "edited_description": "AUSTRIAN AIRLINES",
            "combined_description": "AUSTRIAN AIRLINES",
            "russian_name": "Austrian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3052,
            "edited_description": "LANCHILE",
            "combined_description": "LANCHILE",
            "russian_name": "LAN Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3053,
            "edited_description": "AVIACO (SPAIN)",
            "combined_description": "AVIACO (SPAIN)",
            "russian_name": "AVIACO (Испания)",
            "russian_description": "null"
        },
        {
            "mcc": 3054,
            "edited_description": "LADECO (CHILE)",
            "combined_description": "LADECO (CHILE)",
            "russian_name": "LADECO (Чили)",
            "russian_description": "null"
        },
        {
            "mcc": 3055,
            "edited_description": "LAB (BOLIVIA)",
            "combined_description": "LAB (BOLIVIA)",
            "russian_name": "LAB (Боливия)",
            "russian_description": "null"
        },
        {
            "mcc": 3056,
            "edited_description": "QUEBECAIRE",
            "combined_description": "QUEBECAIRE",
            "russian_name": "Jet Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3057,
            "edited_description": "EASTWEST AIRLINES (AUSTRALIA)",
            "combined_description": "EASTWEST AIRLINES (AUSTRALIA)",
            "russian_name": "Virgin America",
            "russian_description": "null"
        },
        {
            "mcc": 3058,
            "edited_description": "DELTA",
            "combined_description": "DELTA",
            "russian_name": "Delta",
            "russian_description": "null"
        },
        {
            "mcc": 3059,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "DBA Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3060,
            "edited_description": "NORTHWEST",
            "combined_description": "NORTHWEST",
            "russian_name": "Northwest Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3061,
            "edited_description": "CONTINENTAL",
            "combined_description": "CONTINENTAL",
            "russian_name": "Continental",
            "russian_description": "null"
        },
        {
            "mcc": 3062,
            "edited_description": "WESTERN",
            "combined_description": "WESTERN",
            "russian_name": "Hapag-Lloyd Express",
            "russian_description": "null"
        },
        {
            "mcc": 3063,
            "edited_description": "US AIR",
            "combined_description": "US AIR",
            "russian_name": "U.S. Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3064,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Adria Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3065,
            "edited_description": "AIRINTER",
            "combined_description": "AIRINTER",
            "russian_name": "Air Inter",
            "russian_description": "null"
        },
        {
            "mcc": 3066,
            "edited_description": "SOUTHWEST",
            "combined_description": "SOUTHWEST",
            "russian_name": "Southwest Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3067,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Vanguard Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3068,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Air Astana",
            "russian_description": "null"
        },
        {
            "mcc": 3069,
            "edited_description": "SUN COUNTRY AIRLINES",
            "combined_description": "SUN COUNTRY AIRLINES",
            "russian_name": "Sun Country Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3070,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3071,
            "edited_description": "AIR BRITISH COLUBIA",
            "combined_description": "AIR BRITISH COLUBIA",
            "russian_name": "Air British Columbia",
            "russian_description": "null"
        },
        {
            "mcc": 3072,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Cebu Pacific",
            "russian_description": "null"
        },
        {
            "mcc": 3073,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Air Cal",
            "russian_description": "null"
        },
        {
            "mcc": 3074,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3075,
            "edited_description": "SINGAPORE AIRLINES",
            "combined_description": "SINGAPORE AIRLINES",
            "russian_name": "Singapore Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3076,
            "edited_description": "AEROMEXICO",
            "combined_description": "AEROMEXICO",
            "russian_name": "Aeromexico",
            "russian_description": "null"
        },
        {
            "mcc": 3077,
            "edited_description": "THAI AIRWAYS",
            "combined_description": "THAI AIRWAYS",
            "russian_name": "Thai Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3078,
            "edited_description": "CHINA AIRLINES",
            "combined_description": "CHINA AIRLINES",
            "russian_name": "China Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3079,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Jetstar Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3080,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3081,
            "edited_description": "NORDAIR",
            "combined_description": "NORDAIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3082,
            "edited_description": "KOREAN AIRLINES",
            "combined_description": "KOREAN AIRLINES",
            "russian_name": "Korean Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3083,
            "edited_description": "AIR AFRIGUE",
            "combined_description": "AIR AFRIGUE",
            "russian_name": "Air Afrique",
            "russian_description": "null"
        },
        {
            "mcc": 3084,
            "edited_description": "EVA AIRLINES",
            "combined_description": "EVA AIRLINES",
            "russian_name": "Eva Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3085,
            "edited_description": "MIDWEST EXPRESS AIRLINES, INC.",
            "combined_description": "MIDWEST EXPRESS AIRLINES, INC.",
            "russian_name": "Midwest Express Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3086,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Carnival Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3087,
            "edited_description": "METRO AIRLINES",
            "combined_description": "METRO AIRLINES",
            "russian_name": "Metro Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3088,
            "edited_description": "CROATIA AIRLINES",
            "combined_description": "CROATIA AIRLINES",
            "russian_name": "Croatia Air",
            "russian_description": "null"
        },
        {
            "mcc": 3089,
            "edited_description": "TRANSAERO",
            "combined_description": "TRANSAERO",
            "russian_name": "Transaero",
            "russian_description": "null"
        },
        {
            "mcc": 3090,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Uni Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3091,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3092,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Midway Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3093,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3094,
            "edited_description": "ZAMBIA AIRWAYS",
            "combined_description": "ZAMBIA AIRWAYS",
            "russian_name": "Zambia Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3095,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3096,
            "edited_description": "AIR ZIMBABWE",
            "combined_description": "AIR ZIMBABWE",
            "russian_name": "Air Zimbabwe",
            "russian_description": "null"
        },
        {
            "mcc": 3097,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Spanair",
            "russian_description": "null"
        },
        {
            "mcc": 3098,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Asiana Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3099,
            "edited_description": "CATHAY PACIFIC",
            "combined_description": "CATHAY PACIFIC",
            "russian_name": "Cathay Pacific",
            "russian_description": "null"
        },
        {
            "mcc": 3100,
            "edited_description": "MALAYSIAN AIRLINE SYSTEM",
            "combined_description": "MALAYSIAN AIRLINE SYSTEM",
            "russian_name": "Malaysian Airline System",
            "russian_description": "null"
        },
        {
            "mcc": 3101,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3102,
            "edited_description": "IBERIA",
            "combined_description": "IBERIA",
            "russian_name": "Iberia",
            "russian_description": "null"
        },
        {
            "mcc": 3103,
            "edited_description": "GARUDA (INDONESIA)",
            "combined_description": "GARUDA (INDONESIA)",
            "russian_name": "Garuda (Индонезия)",
            "russian_description": "null"
        },
        {
            "mcc": 3104,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3105,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3106,
            "edited_description": "BRAATHENS S.A.F.E. (NORWAY)",
            "combined_description": "BRAATHENS S.A.F.E. (NORWAY)",
            "russian_name": "Braathens S.A.F.E. (Норвегия)",
            "russian_description": "null"
        },
        {
            "mcc": 3107,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3108,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3109,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3110,
            "edited_description": "WINGS AIRWAYS",
            "combined_description": "WINGS AIRWAYS",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3111,
            "edited_description": "BRITISH MIDLAND",
            "combined_description": "BRITISH MIDLAND",
            "russian_name": "British Midland",
            "russian_description": "null"
        },
        {
            "mcc": 3112,
            "edited_description": "WINDWARD ISLAND",
            "combined_description": "WINDWARD ISLAND",
            "russian_name": "Windward Island",
            "russian_description": "null"
        },
        {
            "mcc": 3113,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3114,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3115,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3116,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3117,
            "edited_description": "VIASA",
            "combined_description": "VIASA",
            "russian_name": "Venezolana International de Aviacion",
            "russian_description": "null"
        },
        {
            "mcc": 3118,
            "edited_description": "VALLEY AIRLINES",
            "combined_description": "VALLEY AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3119,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3120,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3121,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3122,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3123,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3124,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3125,
            "edited_description": "TAN",
            "combined_description": "TAN",
            "russian_name": "Tan Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3126,
            "edited_description": "TALAIR",
            "combined_description": "TALAIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3127,
            "edited_description": "TACA INTERNATIONAL",
            "combined_description": "TACA INTERNATIONAL",
            "russian_name": "Taca International",
            "russian_description": "null"
        },
        {
            "mcc": 3128,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3129,
            "edited_description": "SURINAM AIRWAYS",
            "combined_description": "SURINAM AIRWAYS",
            "russian_name": "Surinam Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3130,
            "edited_description": "SUN WORLD INTERNATIONAL",
            "combined_description": "SUN WORLD INTERNATIONAL",
            "russian_name": "Sunworld International Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3131,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "VLM Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3132,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Frontier Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3133,
            "edited_description": "SUNBELT AIRLINES",
            "combined_description": "SUNBELT AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3134,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3135,
            "edited_description": "SUDAN AIRWAYS",
            "combined_description": "SUDAN AIRWAYS",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3136,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Qatar Airways Company W.L.L.",
            "russian_description": "null"
        },
        {
            "mcc": 3137,
            "edited_description": "SINGLETON",
            "combined_description": "SINGLETON",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3138,
            "edited_description": "SIMMONS AIRLINES",
            "combined_description": "SIMMONS AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3139,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3140,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3141,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3142,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3143,
            "edited_description": "SCENIC AIRLINES",
            "combined_description": "SCENIC AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3144,
            "edited_description": "VIRGIN ATLANTIC",
            "combined_description": "VIRGIN ATLANTIC",
            "russian_name": "Virgin Atlantic",
            "russian_description": "null"
        },
        {
            "mcc": 3145,
            "edited_description": "SAN JUAN AIRLINES",
            "combined_description": "SAN JUAN AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3146,
            "edited_description": "LUXAIR",
            "combined_description": "LUXAIR",
            "russian_name": "Luxair",
            "russian_description": "null"
        },
        {
            "mcc": 3147,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3148,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Air Littoral, S.A.",
            "russian_description": "null"
        },
        {
            "mcc": 3149,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3150,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3151,
            "edited_description": "AIR ZAIRE",
            "combined_description": "AIR ZAIRE",
            "russian_name": "Air Zaire",
            "russian_description": "null"
        },
        {
            "mcc": 3152,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3153,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3154,
            "edited_description": "PRINCEVILLE",
            "combined_description": "PRINCEVILLE",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3155,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3156,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "GO FLY Ltd.",
            "russian_description": "null"
        },
        {
            "mcc": 3157,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3158,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3159,
            "edited_description": "PBA",
            "combined_description": "PBA",
            "russian_name": "Provincetown-Boston Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3160,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3161,
            "edited_description": "ALL NIPPON AIRWAYS",
            "combined_description": "ALL NIPPON AIRWAYS",
            "russian_name": "All Nippon Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3162,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3163,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3164,
            "edited_description": "NORONTAIR",
            "combined_description": "NORONTAIR",
            "russian_name": "Norontair",
            "russian_description": "null"
        },
        {
            "mcc": 3165,
            "edited_description": "NEW YORK HELICOPTER",
            "combined_description": "NEW YORK HELICOPTER",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3166,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3167,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Aero Continente",
            "russian_description": "null"
        },
        {
            "mcc": 3168,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3169,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3170,
            "edited_description": "NOUNT COOK",
            "combined_description": "NOUNT COOK",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3171,
            "edited_description": "CANADIAN AIRLINES INTERNATIONAL",
            "combined_description": "CANADIAN AIRLINES INTERNATIONAL",
            "russian_name": "Canadian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3172,
            "edited_description": "NATIONAIR",
            "combined_description": "NATIONAIR",
            "russian_name": "Nation Air",
            "russian_description": "null"
        },
        {
            "mcc": 3173,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3174,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "JetBlue Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3175,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Middle East Air",
            "russian_description": "null"
        },
        {
            "mcc": 3176,
            "edited_description": "METROFLIGHT AIRLINES",
            "combined_description": "METROFLIGHT AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3177,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "AirTran Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3178,
            "edited_description": "MESA AIR",
            "combined_description": "MESA AIR",
            "russian_name": "Mesa Air",
            "russian_description": "null"
        },
        {
            "mcc": 3179,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3180,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Westjet Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3181,
            "edited_description": "MALEV",
            "combined_description": "MALEV",
            "russian_name": "Malev Hungarian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3182,
            "edited_description": "LOT (POLAND)",
            "combined_description": "LOT (POLAND)",
            "russian_name": "LOT – Polish Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3183,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Oman Aviation Services",
            "russian_description": "null"
        },
        {
            "mcc": 3184,
            "edited_description": "LIAT",
            "combined_description": "LIAT",
            "russian_name": "LIAT",
            "russian_description": "null"
        },
        {
            "mcc": 3185,
            "edited_description": "LAV (VENEZUELA)",
            "combined_description": "LAV (VENEZUELA)",
            "russian_name": "LAV Linea Aeropostal Venezolana",
            "russian_description": "null"
        },
        {
            "mcc": 3186,
            "edited_description": "LAP (PARAGUAY)",
            "combined_description": "LAP (PARAGUAY)",
            "russian_name": "LAP Lineas Aereas Paraguayas",
            "russian_description": "null"
        },
        {
            "mcc": 3187,
            "edited_description": "LACSA (COSTA RICA)",
            "combined_description": "LACSA (COSTA RICA)",
            "russian_name": "LACSA (Коста Рика)",
            "russian_description": "null"
        },
        {
            "mcc": 3188,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Virgin Express",
            "russian_description": "null"
        },
        {
            "mcc": 3189,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3190,
            "edited_description": "JUGOSLAV AIR",
            "combined_description": "JUGOSLAV AIR",
            "russian_name": "Jugoslav Air",
            "russian_description": "null"
        },
        {
            "mcc": 3191,
            "edited_description": "ISLAND AIRLINES",
            "combined_description": "ISLAND AIRLINES",
            "russian_name": "Island Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3192,
            "edited_description": "IRAN AIR",
            "combined_description": "IRAN AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3193,
            "edited_description": "INDIAN AIRLINES",
            "combined_description": "INDIAN AIRLINES",
            "russian_name": "Indian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3194,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3195,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3196,
            "edited_description": "HAWAIIAN AIR",
            "combined_description": "HAWAIIAN AIR",
            "russian_name": "Hawaiian Air",
            "russian_description": "null"
        },
        {
            "mcc": 3197,
            "edited_description": "HAVASU AIRLINES",
            "combined_description": "HAVASU AIRLINES",
            "russian_name": "Havasu Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3198,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3199,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Servicios Aereos Militares",
            "russian_description": "null"
        },
        {
            "mcc": 3200,
            "edited_description": "FUYANA AIRWAYS",
            "combined_description": "FUYANA AIRWAYS",
            "russian_name": "Guyana Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3201,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3202,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3203,
            "edited_description": "GOLDEN PACIFIC AIR",
            "combined_description": "GOLDEN PACIFIC AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3204,
            "edited_description": "FREEDOM AIR",
            "combined_description": "FREEDOM AIR",
            "russian_name": "Freedom Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3205,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3206,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "China Eastern Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3207,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3208,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3209,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3210,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3211,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Norwegian Air Shuttle",
            "russian_description": "null"
        },
        {
            "mcc": 3212,
            "edited_description": "DOMINICANA",
            "combined_description": "DOMINICANA",
            "russian_name": "Dominicana de Aviacion",
            "russian_description": "null"
        },
        {
            "mcc": 3213,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Braathens Regional Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3214,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3215,
            "edited_description": "DAN AIR SERVICES",
            "combined_description": "DAN AIR SERVICES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3216,
            "edited_description": "CUMBERLAND AIRLINES",
            "combined_description": "CUMBERLAND AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3217,
            "edited_description": "CSA",
            "combined_description": "CSA",
            "russian_name": "CSA Ceskoslovenske Aerolinie",
            "russian_description": "null"
        },
        {
            "mcc": 3218,
            "edited_description": "CROWN AIR",
            "combined_description": "CROWN AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3219,
            "edited_description": "COPA",
            "combined_description": "COPA",
            "russian_name": "Compania Panamena de Aviacion",
            "russian_description": "null"
        },
        {
            "mcc": 3220,
            "edited_description": "COMPANIA FAUCETT",
            "combined_description": "COMPANIA FAUCETT",
            "russian_name": "Compania Faucett",
            "russian_description": "null"
        },
        {
            "mcc": 3221,
            "edited_description": "TRANSPORTES AEROS MILITARES ECCUATORANOS",
            "combined_description": "TRANSPORTES AEROS MILITARES ECCUATORANOS",
            "russian_name": "Transportes Aeros Militares Ecuatorianos",
            "russian_description": "null"
        },
        {
            "mcc": 3222,
            "edited_description": "COMMAND AIRWAYS",
            "combined_description": "COMMAND AIRWAYS",
            "russian_name": "Command Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3223,
            "edited_description": "COMAIR",
            "combined_description": "COMAIR",
            "russian_name": "Comair",
            "russian_description": "null"
        },
        {
            "mcc": 3224,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3225,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3226,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Skyways",
            "russian_description": "null"
        },
        {
            "mcc": 3227,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3228,
            "edited_description": "CAYMAN AIRWAYS",
            "combined_description": "CAYMAN AIRWAYS",
            "russian_name": "Cayman Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3229,
            "edited_description": "SAETA SOCIAEDAD ECUATORIANOS DE TRANSPORTES AEREOS",
            "combined_description": "SAETA SOCIAEDAD ECUATORIANOS DE TRANSPORTES AEREOS",
            "russian_name": "SAETA (Sociedad Ecuatorianas De Transportes Aereo)",
            "russian_description": "null"
        },
        {
            "mcc": 3230,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3231,
            "edited_description": "SASHA SERVICIO AERO DE HONDURAS",
            "combined_description": "SASHA SERVICIO AERO DE HONDURAS",
            "russian_name": "SAHSA (Servicio Aero de Honduras)",
            "russian_description": "null"
        },
        {
            "mcc": 3232,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3233,
            "edited_description": "CAPITOL AIR",
            "combined_description": "CAPITOL AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3234,
            "edited_description": "BWIA",
            "combined_description": "BWIA",
            "russian_name": "Caribbean Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3235,
            "edited_description": "BROKWAY AIR",
            "combined_description": "BROKWAY AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3236,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Air Arabia Airline",
            "russian_description": "null"
        },
        {
            "mcc": 3237,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3238,
            "edited_description": "BEMIDJI AIRLINES",
            "combined_description": "BEMIDJI AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3239,
            "edited_description": "BAR HARBOR AIRLINES",
            "combined_description": "BAR HARBOR AIRLINES",
            "russian_name": "Bar Harbor Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3240,
            "edited_description": "BAHAMASAIR",
            "combined_description": "BAHAMASAIR",
            "russian_name": "Bahamasair",
            "russian_description": "null"
        },
        {
            "mcc": 3241,
            "edited_description": "AVIATECA (GUATEMALA)",
            "combined_description": "AVIATECA (GUATEMALA)",
            "russian_name": "Aviateca (Гватемала)",
            "russian_description": "null"
        },
        {
            "mcc": 3242,
            "edited_description": "AVENSA",
            "combined_description": "AVENSA",
            "russian_name": "Avensa",
            "russian_description": "null"
        },
        {
            "mcc": 3243,
            "edited_description": "AUSTRIAN AIR SERVICE",
            "combined_description": "AUSTRIAN AIR SERVICE",
            "russian_name": "Austrian Air Service",
            "russian_description": "null"
        },
        {
            "mcc": 3244,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3245,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "EasyJet",
            "russian_description": "null"
        },
        {
            "mcc": 3246,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Ryanair",
            "russian_description": "null"
        },
        {
            "mcc": 3247,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Gol Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3248,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Tam Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3249,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3250,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3251,
            "edited_description": "ALOHA AIRLINES",
            "combined_description": "ALOHA AIRLINES",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3252,
            "edited_description": "ALM",
            "combined_description": "ALM",
            "russian_name": "ALM Antilean Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3253,
            "edited_description": "AMERICA WEST",
            "combined_description": "AMERICA WEST",
            "russian_name": "America West",
            "russian_description": "null"
        },
        {
            "mcc": 3254,
            "edited_description": "TRUMP AIRLINE",
            "combined_description": "TRUMP AIRLINE",
            "russian_name": "Trump Airline",
            "russian_description": "null"
        },
        {
            "mcc": 3255,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3256,
            "edited_description": "ALASKA AIRLINES",
            "combined_description": "ALASKA AIRLINES",
            "russian_name": "Alaska Airlines Inc.",
            "russian_description": "null"
        },
        {
            "mcc": 3257,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3258,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3259,
            "edited_description": "AMERICAN TRANS AIR",
            "combined_description": "AMERICAN TRANS AIR",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3260,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Spirit Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3261,
            "edited_description": "AIR CHINA",
            "combined_description": "AIR CHINA",
            "russian_name": "Air China",
            "russian_description": "null"
        },
        {
            "mcc": 3262,
            "edited_description": "RENO AIR, INC.",
            "combined_description": "RENO AIR, INC.",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3263,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Aero Servicio Carabobo",
            "russian_description": "null"
        },
        {
            "mcc": 3264,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "Код указан на сайте Правительства Аляски как Авиалинии"
        },
        {
            "mcc": 3265,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3266,
            "edited_description": "AIR SEYCHELLES",
            "combined_description": "AIR SEYCHELLES",
            "russian_name": "Air Seychelles",
            "russian_description": "null"
        },
        {
            "mcc": 3267,
            "edited_description": "AIR PANAMA",
            "combined_description": "AIR PANAMA",
            "russian_name": "Air Panama International",
            "russian_description": "null"
        },
        {
            "mcc": 3268,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3269,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3270,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3271,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3272,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3273,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3274,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3275,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3276,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3277,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3278,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3279,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3280,
            "edited_description": "AIR JAMAICA",
            "combined_description": "AIR JAMAICA",
            "russian_name": "Air Jamaica",
            "russian_description": "null"
        },
        {
            "mcc": 3281,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3282,
            "edited_description": "AIR DJIBOUTI",
            "combined_description": "AIR DJIBOUTI",
            "russian_name": "Air Djibouti",
            "russian_description": "null"
        },
        {
            "mcc": 3283,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3284,
            "edited_description": "AERO VIRGIN ISLANDS",
            "combined_description": "AERO VIRGIN ISLANDS",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3285,
            "edited_description": "AERO PERU",
            "combined_description": "AERO PERU",
            "russian_name": "Aero Peru",
            "russian_description": "null"
        },
        {
            "mcc": 3286,
            "edited_description": "AEROLINEAS NICARAGUENSIS",
            "combined_description": "AEROLINEAS NICARAGUENSIS",
            "russian_name": "Aero Nicaraguenses",
            "russian_description": "null"
        },
        {
            "mcc": 3287,
            "edited_description": "AERO COACH AVAIATION",
            "combined_description": "AERO COACH AVAIATION",
            "russian_name": "Aero Coach Aviation",
            "russian_description": "null"
        },
        {
            "mcc": 3288,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3289,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3290,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3291,
            "edited_description": "ARIANA AFGHAN",
            "combined_description": "ARIANA AFGHAN",
            "russian_name": "Авиалинии, авиакомпании",
            "russian_description": "null"
        },
        {
            "mcc": 3292,
            "edited_description": "CYPRUS AIRWAYS",
            "combined_description": "CYPRUS AIRWAYS",
            "russian_name": "Cyprus Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3293,
            "edited_description": "ECUATORIANA",
            "combined_description": "ECUATORIANA",
            "russian_name": "Ecuatoriana",
            "russian_description": "null"
        },
        {
            "mcc": 3294,
            "edited_description": "ETHIOPIAN AIRLINES",
            "combined_description": "ETHIOPIAN AIRLINES",
            "russian_name": "Ethiopian Airlines",
            "russian_description": "null"
        },
        {
            "mcc": 3295,
            "edited_description": "KENYA AIRLINES",
            "combined_description": "KENYA AIRLINES",
            "russian_name": "Kenya Airways",
            "russian_description": "null"
        },
        {
            "mcc": 3296,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Air Berlin",
            "russian_description": "null"
        },
        {
            "mcc": 3297,
            "edited_description": "Airlines",
            "combined_description": "Airlines",
            "russian_name": "Tarom Romanian Air Transport",
            "russian_description": "null"
        },
        {
            "mcc": 3298,
            "edited_description": "AIR MAURITIUS",
            "combined_description": "AIR MAURITIUS",
            "russian_name": "Air Mauritius",
            "russian_description": "null"
        },
        {
            "mcc": 3299,
            "edited_description": "WIDERO’S FLYVESELSKAP",
            "combined_description": "WIDERO’S FLYVESELSKAP",
            "russian_name": "Wideroes Flyveselskap",
            "russian_description": "null"
        },
        {
            "mcc": 3351,
            "edited_description": "AFFILIATED AUTO RENTAL",
            "combined_description": "AFFILIATED AUTO RENTAL",
            "russian_name": " Affiliated Auto Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3352,
            "edited_description": "AMERICAN INTL RENT-A-CAR",
            "combined_description": "AMERICAN INTL RENT-A-CAR",
            "russian_name": " American Intl Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3353,
            "edited_description": "BROOKS RENT-A-CAR",
            "combined_description": "BROOKS RENT-A-CAR",
            "russian_name": " Brooks Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3354,
            "edited_description": "ACTION AUTO RENTAL",
            "combined_description": "ACTION AUTO RENTAL",
            "russian_name": " Action Auto Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3355,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3356,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3357,
            "edited_description": "HERTZ RENT-A-CAR",
            "combined_description": "HERTZ RENT-A-CAR",
            "russian_name": " Hertz Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3358,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3359,
            "edited_description": "PAYLESS CAR RENTAL",
            "combined_description": "PAYLESS CAR RENTAL",
            "russian_name": " Payless Car Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3360,
            "edited_description": "SNAPPY CAR RENTAL",
            "combined_description": "SNAPPY CAR RENTAL",
            "russian_name": " Snappy Car Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3361,
            "edited_description": "AIRWAYS RENT-A-CAR",
            "combined_description": "AIRWAYS RENT-A-CAR",
            "russian_name": " Airways Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3362,
            "edited_description": "ALTRA AUTO RENTAL",
            "combined_description": "ALTRA AUTO RENTAL",
            "russian_name": " Altra Auto Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3363,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3364,
            "edited_description": "AGENCY RENT-A-CAR",
            "combined_description": "AGENCY RENT-A-CAR",
            "russian_name": " Agency Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3365,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3366,
            "edited_description": "BUDGET RENT-A-CAR",
            "combined_description": "BUDGET RENT-A-CAR",
            "russian_name": " Budget Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3367,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3368,
            "edited_description": "HOLIDAY RENT-A-WRECK",
            "combined_description": "HOLIDAY RENT-A-WRECK",
            "russian_name": " Holiday Rent-a-wreck",
            "russian_description": "null"
        },
        {
            "mcc": 3369,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3370,
            "edited_description": "RENT-A-WRECK",
            "combined_description": "RENT-A-WRECK",
            "russian_name": " Rent-a-wreck",
            "russian_description": "null"
        },
        {
            "mcc": 3371,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3372,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3373,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3374,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3375,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3376,
            "edited_description": "AJAX RENT-A-CAR",
            "combined_description": "AJAX RENT-A-CAR",
            "russian_name": " Ajax Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3377,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3378,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3379,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3380,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3381,
            "edited_description": "EUROP CAR",
            "combined_description": "EUROP CAR",
            "russian_name": " Europ Car",
            "russian_description": "null"
        },
        {
            "mcc": 3382,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3383,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3384,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3385,
            "edited_description": "TROPICAL RENT-A-CAR",
            "combined_description": "TROPICAL RENT-A-CAR",
            "russian_name": " Tropical Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3386,
            "edited_description": "SHOWCASE RENTAL CARS",
            "combined_description": "SHOWCASE RENTAL CARS",
            "russian_name": " Showcase Rental Cars",
            "russian_description": "null"
        },
        {
            "mcc": 3387,
            "edited_description": "ALAMO RENT-A-CAR",
            "combined_description": "ALAMO RENT-A-CAR",
            "russian_name": " Alamo Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3388,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3389,
            "edited_description": "AVIS RENT-A-CAR",
            "combined_description": "AVIS RENT-A-CAR",
            "russian_name": " Avis Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3390,
            "edited_description": "DOLLAR RENT-A-CAR",
            "combined_description": "DOLLAR RENT-A-CAR",
            "russian_name": " Dollar Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3391,
            "edited_description": "EUROPE BY CAR",
            "combined_description": "EUROPE BY CAR",
            "russian_name": " Europe By Car",
            "russian_description": "null"
        },
        {
            "mcc": 3392,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3393,
            "edited_description": "NATIONAL CAR RENTAL",
            "combined_description": "NATIONAL CAR RENTAL",
            "russian_name": " National Car Rental",
            "russian_description": "null"
        },
        {
            "mcc": 3394,
            "edited_description": "KEMWELL GROUP RENT-A-CAR",
            "combined_description": "KEMWELL GROUP RENT-A-CAR",
            "russian_name": " Kemwell Group Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3395,
            "edited_description": "THRIFTY RENT-A-CAR",
            "combined_description": "THRIFTY RENT-A-CAR",
            "russian_name": " Thrifty Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3396,
            "edited_description": "TILDEN TENT-A-CAR",
            "combined_description": "TILDEN TENT-A-CAR",
            "russian_name": " Tilden Tent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3397,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3398,
            "edited_description": "ECONO-CAR RENT-A-CAR",
            "combined_description": "ECONO-CAR RENT-A-CAR",
            "russian_name": " Econo-car Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3399,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Amerex Rent-a-Car",
            "russian_description": "null"
        },
        {
            "mcc": 3400,
            "edited_description": "AUTO HOST COST CAR RENTALS",
            "combined_description": "AUTO HOST COST CAR RENTALS",
            "russian_name": " Auto Host Cost Car Rentals",
            "russian_description": "null"
        },
        {
            "mcc": 3401,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3402,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3403,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3404,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3405,
            "edited_description": "ENTERPRISE RENT-A-CAR",
            "combined_description": "ENTERPRISE RENT-A-CAR",
            "russian_name": " Enterprise Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3406,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3407,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3408,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3409,
            "edited_description": "GENERAL RENT-A-CAR",
            "combined_description": "GENERAL RENT-A-CAR",
            "russian_name": " General Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3410,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3411,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3412,
            "edited_description": "A-1 RENT-A-CAR",
            "combined_description": "A-1 RENT-A-CAR",
            "russian_name": " A-1 Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3413,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3414,
            "edited_description": "GODFREY NATL RENT-A-CAR",
            "combined_description": "GODFREY NATL RENT-A-CAR",
            "russian_name": " Godfrey Natl Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3415,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3416,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3417,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3418,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3419,
            "edited_description": "ALPHA RENT-A-CAR",
            "combined_description": "ALPHA RENT-A-CAR",
            "russian_name": " Alpha Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3420,
            "edited_description": "ANSA INTL RENT-A-CAR",
            "combined_description": "ANSA INTL RENT-A-CAR",
            "russian_name": " Ansa Intl Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3421,
            "edited_description": "ALLSTAE RENT-A-CAR",
            "combined_description": "ALLSTAE RENT-A-CAR",
            "russian_name": " Allstae Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3422,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3423,
            "edited_description": "AVCAR RENT-A-CAR",
            "combined_description": "AVCAR RENT-A-CAR",
            "russian_name": " Avcar Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3424,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 3425,
            "edited_description": "AUTOMATE RENT-A-CAR",
            "combined_description": "AUTOMATE RENT-A-CAR",
            "russian_name": " Automate Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3426,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3427,
            "edited_description": "AVON RENT-A-CAR",
            "combined_description": "AVON RENT-A-CAR",
            "russian_name": " Avon Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3428,
            "edited_description": "CAREY RENT-A-CAR",
            "combined_description": "CAREY RENT-A-CAR",
            "russian_name": " Carey Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3429,
            "edited_description": "INSURANCE RENT-A-CAR",
            "combined_description": "INSURANCE RENT-A-CAR",
            "russian_name": " Insurance Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3430,
            "edited_description": "MAJOR RENT-A-CAR",
            "combined_description": "MAJOR RENT-A-CAR",
            "russian_name": " Major Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3431,
            "edited_description": "REPLACEMENT RENT-A-CAR",
            "combined_description": "REPLACEMENT RENT-A-CAR",
            "russian_name": " Replacement Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3432,
            "edited_description": "RESERVE RENT-A-CAR",
            "combined_description": "RESERVE RENT-A-CAR",
            "russian_name": " Reserve Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3433,
            "edited_description": "UGLY DUCKLING RENT-A-CAR",
            "combined_description": "UGLY DUCKLING RENT-A-CAR",
            "russian_name": " Ugly Duckling Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3434,
            "edited_description": "USA RENT-A-CAR",
            "combined_description": "USA RENT-A-CAR",
            "russian_name": " USA Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3435,
            "edited_description": "VALUE RENT-A-CAR",
            "combined_description": "VALUE RENT-A-CAR",
            "russian_name": " Value Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3436,
            "edited_description": "AUTOHANSA RENT-A-CAR",
            "combined_description": "AUTOHANSA RENT-A-CAR",
            "russian_name": " Autohansa Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3437,
            "edited_description": "CITE RENT-A-CAR",
            "combined_description": "CITE RENT-A-CAR",
            "russian_name": " Cite Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3438,
            "edited_description": "INTERENT RENT-A-CAR",
            "combined_description": "INTERENT RENT-A-CAR",
            "russian_name": " Interent Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3439,
            "edited_description": "MILLEVILLE RENT-A-CAR",
            "combined_description": "MILLEVILLE RENT-A-CAR",
            "russian_name": " Milleville Rent-a-car",
            "russian_description": "null"
        },
        {
            "mcc": 3440,
            "edited_description": "VIA ROUTE RENT-A-CAR",
            "combined_description": "VIA ROUTE RENT-A-CAR",
            "russian_name": "Via Route Rent-a-Car",
            "russian_description": "null"
        },
        {
            "mcc": 3441,
            "edited_description": "Car Rental",
            "combined_description": "Car Rental",
            "russian_name": "Агентства по аренде автомобилей",
            "russian_description": "null"
        },
        {
            "mcc": 3501,
            "edited_description": "HOLIDAY INNS, HOLIDAY INN EXPRESS",
            "combined_description": "HOLIDAY INNS, HOLIDAY INN EXPRESS",
            "russian_name": "Holiday Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3502,
            "edited_description": "BEST WESTERN HOTELS",
            "combined_description": "BEST WESTERN HOTELS",
            "russian_name": "Best Western Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3503,
            "edited_description": "SHERATON HOTELS",
            "combined_description": "SHERATON HOTELS",
            "russian_name": "Sheraton Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3504,
            "edited_description": "HILTON HOTELS",
            "combined_description": "HILTON HOTELS",
            "russian_name": "Hilton Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3505,
            "edited_description": "FORTE HOTELS",
            "combined_description": "FORTE HOTELS",
            "russian_name": "Forte Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3506,
            "edited_description": "GOLDEN TULIP HOTELS",
            "combined_description": "GOLDEN TULIP HOTELS",
            "russian_name": "Golden Tulip Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3507,
            "edited_description": "FRIENDSHIP INNS",
            "combined_description": "FRIENDSHIP INNS",
            "russian_name": "Friendship Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3508,
            "edited_description": "QUALITY INNS, QUALITY SUITES",
            "combined_description": "QUALITY INNS, QUALITY SUITES",
            "russian_name": "Quality Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3509,
            "edited_description": "MARRIOTT HOTELS",
            "combined_description": "MARRIOTT HOTELS",
            "russian_name": "Marriott Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3510,
            "edited_description": "DAYS INN, DAYSTOP",
            "combined_description": "DAYS INN, DAYSTOP",
            "russian_name": "Days Inn",
            "russian_description": "null"
        },
        {
            "mcc": 3511,
            "edited_description": "ARABELLA HOTELS",
            "combined_description": "ARABELLA HOTELS",
            "russian_name": "Arabella Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3512,
            "edited_description": "INTER-CONTINENTAL HOTELS",
            "combined_description": "INTER-CONTINENTAL HOTELS",
            "russian_name": "Inter-continental Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3513,
            "edited_description": "WESTIN HOTELS",
            "combined_description": "WESTIN HOTELS",
            "russian_name": "Westin Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3514,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3515,
            "edited_description": "RODEWAY INNS",
            "combined_description": "RODEWAY INNS",
            "russian_name": "Rodeway Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3516,
            "edited_description": "LA QUINTA MOTOR INNS",
            "combined_description": "LA QUINTA MOTOR INNS",
            "russian_name": "La Quinta Motor Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3517,
            "edited_description": "AMERICANA HOTELS",
            "combined_description": "AMERICANA HOTELS",
            "russian_name": "Americana Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3518,
            "edited_description": "SOL HOTELS",
            "combined_description": "SOL HOTELS",
            "russian_name": "Sol Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3519,
            "edited_description": "PULLMAN INTERNATIONAL HOTELS",
            "combined_description": "PULLMAN INTERNATIONAL HOTELS",
            "russian_name": "Pullman International Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3520,
            "edited_description": "MERIDIEN HOTELS",
            "combined_description": "MERIDIEN HOTELS",
            "russian_name": "Meridien Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3521,
            "edited_description": "CREST HOTELS (see FORTE HOTELS)",
            "combined_description": "CREST HOTELS (see FORTE HOTELS)",
            "russian_name": "Crest Hotels (see Forte Hotels)",
            "russian_description": "null"
        },
        {
            "mcc": 3522,
            "edited_description": "TOKYO HOTEL",
            "combined_description": "TOKYO HOTEL",
            "russian_name": "Tokyo Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3523,
            "edited_description": "PENNSULA HOTEL",
            "combined_description": "PENNSULA HOTEL",
            "russian_name": "Pennsula Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3524,
            "edited_description": "WELCOMGROUP HOTELS",
            "combined_description": "WELCOMGROUP HOTELS",
            "russian_name": "Welcomgroup Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3525,
            "edited_description": "DUNFEY HOTELS",
            "combined_description": "DUNFEY HOTELS",
            "russian_name": "Dunfey Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3526,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3527,
            "edited_description": "DOWNTOWNER-PASSPORT HOTEL",
            "combined_description": "DOWNTOWNER-PASSPORT HOTEL",
            "russian_name": "Downtowner-passport Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3528,
            "edited_description": "RED LION HOTELS, RED LION INNS",
            "combined_description": "RED LION HOTELS, RED LION INNS",
            "russian_name": "Red Lion Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3529,
            "edited_description": "CP HOTELS",
            "combined_description": "CP HOTELS",
            "russian_name": "Cp Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3530,
            "edited_description": "RENAISSANCE HOTELS, STOUFFER HOTELS",
            "combined_description": "RENAISSANCE HOTELS, STOUFFER HOTELS",
            "russian_name": "Renaissance Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3531,
            "edited_description": "ASTIR HOTELS",
            "combined_description": "ASTIR HOTELS",
            "russian_name": "Astir Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3532,
            "edited_description": "SUN ROUTE HOTELS",
            "combined_description": "SUN ROUTE HOTELS",
            "russian_name": "Sun Route Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3533,
            "edited_description": "HOTEL IBIS",
            "combined_description": "HOTEL IBIS",
            "russian_name": "Hotel Ibis",
            "russian_description": "null"
        },
        {
            "mcc": 3534,
            "edited_description": "SOUTHERN PACIFIC HOTELS",
            "combined_description": "SOUTHERN PACIFIC HOTELS",
            "russian_name": "Southern Pacific Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3535,
            "edited_description": "HILTON INTERNATIONAL",
            "combined_description": "HILTON INTERNATIONAL",
            "russian_name": "Hilton International",
            "russian_description": "null"
        },
        {
            "mcc": 3536,
            "edited_description": "AMFAC HOTELS",
            "combined_description": "AMFAC HOTELS",
            "russian_name": "Amfac Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3537,
            "edited_description": "ANA HOTEL",
            "combined_description": "ANA HOTEL",
            "russian_name": "Ana Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3538,
            "edited_description": "CONCORDE HOTELS",
            "combined_description": "CONCORDE HOTELS",
            "russian_name": "Concorde Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3539,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3540,
            "edited_description": "IBEROTEL HOTELS",
            "combined_description": "IBEROTEL HOTELS",
            "russian_name": "Iberotel Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3541,
            "edited_description": "HOTEL OKURA",
            "combined_description": "HOTEL OKURA",
            "russian_name": "Hotel Okura",
            "russian_description": "null"
        },
        {
            "mcc": 3542,
            "edited_description": "ROYAL HOTELS",
            "combined_description": "ROYAL HOTELS",
            "russian_name": "Royal Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3543,
            "edited_description": "FOUR SEASONS HOTELS",
            "combined_description": "FOUR SEASONS HOTELS",
            "russian_name": "Four Seasons Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3544,
            "edited_description": "CIGA HOTELS",
            "combined_description": "CIGA HOTELS",
            "russian_name": "Ciga Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3545,
            "edited_description": "SHANGRI-LA INTERNATIONAL",
            "combined_description": "SHANGRI-LA INTERNATIONAL",
            "russian_name": "Shangri-la International",
            "russian_description": "null"
        },
        {
            "mcc": 3546,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3547,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3548,
            "edited_description": "HOTELES MELIA",
            "combined_description": "HOTELES MELIA",
            "russian_name": "Hoteles Melia",
            "russian_description": "null"
        },
        {
            "mcc": 3549,
            "edited_description": "AUBERGE DES GOVERNEURS",
            "combined_description": "AUBERGE DES GOVERNEURS",
            "russian_name": "Auberge Des Governeurs",
            "russian_description": "null"
        },
        {
            "mcc": 3550,
            "edited_description": "REGAL 8 INNS",
            "combined_description": "REGAL 8 INNS",
            "russian_name": "Regal 8 Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3551,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3552,
            "edited_description": "COAST HOTELS",
            "combined_description": "COAST HOTELS",
            "russian_name": "Coast Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3553,
            "edited_description": "PARK INNS INTERNATIONAL",
            "combined_description": "PARK INNS INTERNATIONAL",
            "russian_name": "Park Inns International",
            "russian_description": "null"
        },
        {
            "mcc": 3554,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3555,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3556,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3557,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3558,
            "edited_description": "JOLLY HOTELS",
            "combined_description": "JOLLY HOTELS",
            "russian_name": "Jolly Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3559,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3560,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3561,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3562,
            "edited_description": "COMFORT INNS",
            "combined_description": "COMFORT INNS",
            "russian_name": "Comfort Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3563,
            "edited_description": "JOURNEY’S END MOTLS",
            "combined_description": "JOURNEY’S END MOTLS",
            "russian_name": "Journey’s End Motls",
            "russian_description": "null"
        },
        {
            "mcc": 3564,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3565,
            "edited_description": "RELAX INNS",
            "combined_description": "RELAX INNS",
            "russian_name": "Relax Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3566,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3567,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3568,
            "edited_description": "LADBROKE HOTELS",
            "combined_description": "LADBROKE HOTELS",
            "russian_name": "Ladbroke Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3569,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3570,
            "edited_description": "FORUM HOTELS",
            "combined_description": "FORUM HOTELS",
            "russian_name": "Forum Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3571,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3572,
            "edited_description": "MIYAKO HOTELS",
            "combined_description": "MIYAKO HOTELS",
            "russian_name": "Miyako Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3573,
            "edited_description": "SANDMAN HOTELS",
            "combined_description": "SANDMAN HOTELS",
            "russian_name": "Sandman Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3574,
            "edited_description": "VENTURE INNS",
            "combined_description": "VENTURE INNS",
            "russian_name": "Venture Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3575,
            "edited_description": "VAGABOND HOTELS",
            "combined_description": "VAGABOND HOTELS",
            "russian_name": "Vagabond Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3576,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3577,
            "edited_description": "MANDARIN ORIENTAL HOTEL",
            "combined_description": "MANDARIN ORIENTAL HOTEL",
            "russian_name": "Mandarin Oriental Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3578,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3579,
            "edited_description": "HOTEL MERCURE",
            "combined_description": "HOTEL MERCURE",
            "russian_name": "Hotel Mercure",
            "russian_description": "null"
        },
        {
            "mcc": 3580,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3581,
            "edited_description": "DELTA HOTEL",
            "combined_description": "DELTA HOTEL",
            "russian_name": "Delta Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3582,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3583,
            "edited_description": "SAS HOTELS",
            "combined_description": "SAS HOTELS",
            "russian_name": "Sas Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3584,
            "edited_description": "PRINCESS HOTELS INTERNATIONAL",
            "combined_description": "PRINCESS HOTELS INTERNATIONAL",
            "russian_name": "Princess Hotels International",
            "russian_description": "null"
        },
        {
            "mcc": 3585,
            "edited_description": "HUNGAR HOTELS",
            "combined_description": "HUNGAR HOTELS",
            "russian_name": "Hungar Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3586,
            "edited_description": "SOKOS HOTELS",
            "combined_description": "SOKOS HOTELS",
            "russian_name": "Sokos Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3587,
            "edited_description": "DORAL HOTELS",
            "combined_description": "DORAL HOTELS",
            "russian_name": "Doral Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3588,
            "edited_description": "HELMSLEY HOTELS",
            "combined_description": "HELMSLEY HOTELS",
            "russian_name": "Helmsley Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3589,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3590,
            "edited_description": "FAIRMONT HOTELS",
            "combined_description": "FAIRMONT HOTELS",
            "russian_name": "Fairmont Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3591,
            "edited_description": "SONESTA HOTELS",
            "combined_description": "SONESTA HOTELS",
            "russian_name": "Sonesta Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3592,
            "edited_description": "OMNI HOTELS",
            "combined_description": "OMNI HOTELS",
            "russian_name": "Omni Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3593,
            "edited_description": "CUNARD HOTELS",
            "combined_description": "CUNARD HOTELS",
            "russian_name": "Cunard Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3594,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3595,
            "edited_description": "HOSPITALITY INTERNATIONAL",
            "combined_description": "HOSPITALITY INTERNATIONAL",
            "russian_name": "Hospitality International",
            "russian_description": "null"
        },
        {
            "mcc": 3596,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3597,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3598,
            "edited_description": "REGENT INTERNATIONAL HOTELS",
            "combined_description": "REGENT INTERNATIONAL HOTELS",
            "russian_name": "Regent International Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3599,
            "edited_description": "PANNONIA HOTELS",
            "combined_description": "PANNONIA HOTELS",
            "russian_name": "Pannonia Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3600,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3601,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3602,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3603,
            "edited_description": "NOAH’S HOTELS",
            "combined_description": "NOAH’S HOTELS",
            "russian_name": "Noah’s Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3604,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3605,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3606,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3607,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3608,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3609,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3610,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3611,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3612,
            "edited_description": "MOVENPICK HOTELS",
            "combined_description": "MOVENPICK HOTELS",
            "russian_name": "Movenpick Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3613,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3614,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3615,
            "edited_description": "TRAVELODGE",
            "combined_description": "TRAVELODGE",
            "russian_name": "Travelodge",
            "russian_description": "null"
        },
        {
            "mcc": 3616,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3617,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3618,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3619,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3620,
            "edited_description": "TELFORD INTERNATIONAL",
            "combined_description": "TELFORD INTERNATIONAL",
            "russian_name": "Telford International",
            "russian_description": "null"
        },
        {
            "mcc": 3621,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3622,
            "edited_description": "MERLIN HOTELS",
            "combined_description": "MERLIN HOTELS",
            "russian_name": "Merlin Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3623,
            "edited_description": "DORINT HOTELS",
            "combined_description": "DORINT HOTELS",
            "russian_name": "Dorint Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3624,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3625,
            "edited_description": "HOTLE UNIVERSALE",
            "combined_description": "HOTLE UNIVERSALE",
            "russian_name": "Hotle Universale",
            "russian_description": "null"
        },
        {
            "mcc": 3626,
            "edited_description": "PRINCE HOTELS",
            "combined_description": "PRINCE HOTELS",
            "russian_name": "Prince Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3627,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3628,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3629,
            "edited_description": "DAN HOTELS",
            "combined_description": "DAN HOTELS",
            "russian_name": "Dan Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3630,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3631,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3632,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3633,
            "edited_description": "RANK HOTELS",
            "combined_description": "RANK HOTELS",
            "russian_name": "Rank Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3634,
            "edited_description": "SWISSOTEL",
            "combined_description": "SWISSOTEL",
            "russian_name": "Swissotel",
            "russian_description": "null"
        },
        {
            "mcc": 3635,
            "edited_description": "RESO HOTELS",
            "combined_description": "RESO HOTELS",
            "russian_name": "Reso Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3636,
            "edited_description": "SAROVA HOTELS",
            "combined_description": "SAROVA HOTELS",
            "russian_name": "Sarova Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3637,
            "edited_description": "RAMADA INNS, RAMADA LIMITED",
            "combined_description": "RAMADA INNS, RAMADA LIMITED",
            "russian_name": "Ramada Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3638,
            "edited_description": "HO JO INN, HOWARD JOHNSON",
            "combined_description": "HO JO INN, HOWARD JOHNSON",
            "russian_name": "Ho Jo Inn",
            "russian_description": "null"
        },
        {
            "mcc": 3639,
            "edited_description": "MOUNT CHARLOTTE THISTLE",
            "combined_description": "MOUNT CHARLOTTE THISTLE",
            "russian_name": "Mount Charlotte Thistle",
            "russian_description": "null"
        },
        {
            "mcc": 3640,
            "edited_description": "HYATT HOTEL",
            "combined_description": "HYATT HOTEL",
            "russian_name": "Hyatt Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3641,
            "edited_description": "SOFITEL HOTELS",
            "combined_description": "SOFITEL HOTELS",
            "russian_name": "Sofitel Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3642,
            "edited_description": "NOVOTEL HOTELS",
            "combined_description": "NOVOTEL HOTELS",
            "russian_name": "Novotel Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3643,
            "edited_description": "STEIGENBERGER HOTELS",
            "combined_description": "STEIGENBERGER HOTELS",
            "russian_name": "Steigenberger Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3644,
            "edited_description": "ECONO LODGES",
            "combined_description": "ECONO LODGES",
            "russian_name": "Econo Lodges",
            "russian_description": "null"
        },
        {
            "mcc": 3645,
            "edited_description": "QUEENS MOAT HOUSES",
            "combined_description": "QUEENS MOAT HOUSES",
            "russian_name": "Queens Moat Houses",
            "russian_description": "null"
        },
        {
            "mcc": 3646,
            "edited_description": "SWALLOW HOTELS",
            "combined_description": "SWALLOW HOTELS",
            "russian_name": "Swallow Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3647,
            "edited_description": "HUSA HOTELS",
            "combined_description": "HUSA HOTELS",
            "russian_name": "Husa Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3648,
            "edited_description": "DE VERE HOTELS",
            "combined_description": "DE VERE HOTELS",
            "russian_name": "De Vere Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3649,
            "edited_description": "RADISSON HOTELS",
            "combined_description": "RADISSON HOTELS",
            "russian_name": "Radisson Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3650,
            "edited_description": "RED ROOK INNS",
            "combined_description": "RED ROOK INNS",
            "russian_name": "Red Rook Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3651,
            "edited_description": "IMPERIAL LONDON HOTEL",
            "combined_description": "IMPERIAL LONDON HOTEL",
            "russian_name": "Imperial London Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3652,
            "edited_description": "EMBASSY HOTELS",
            "combined_description": "EMBASSY HOTELS",
            "russian_name": "Embassy Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3653,
            "edited_description": "PENTA HOTELS",
            "combined_description": "PENTA HOTELS",
            "russian_name": "Penta Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3654,
            "edited_description": "LOEWS HOTELS",
            "combined_description": "LOEWS HOTELS",
            "russian_name": "Loews Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3655,
            "edited_description": "SCANDIC HOTELS",
            "combined_description": "SCANDIC HOTELS",
            "russian_name": "Scandic Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3656,
            "edited_description": "SARA HOTELS",
            "combined_description": "SARA HOTELS",
            "russian_name": "Sara Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3657,
            "edited_description": "OBEROI HOTELS",
            "combined_description": "OBEROI HOTELS",
            "russian_name": "Oberoi Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3658,
            "edited_description": "OTANI HOTELS",
            "combined_description": "OTANI HOTELS",
            "russian_name": "Otani Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3659,
            "edited_description": "TAJ HOTELS INTERNATIONAL",
            "combined_description": "TAJ HOTELS INTERNATIONAL",
            "russian_name": "Taj Hotels International",
            "russian_description": "null"
        },
        {
            "mcc": 3660,
            "edited_description": "KNIGHTS INNS",
            "combined_description": "KNIGHTS INNS",
            "russian_name": "Knights Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3661,
            "edited_description": "METROPOLE HOTELS",
            "combined_description": "METROPOLE HOTELS",
            "russian_name": "Metropole Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3662,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3663,
            "edited_description": "HOTELES EL PRESIDENTS",
            "combined_description": "HOTELES EL PRESIDENTS",
            "russian_name": "Hoteles El Presidents",
            "russian_description": "null"
        },
        {
            "mcc": 3664,
            "edited_description": "FLAG INN",
            "combined_description": "FLAG INN",
            "russian_name": "Flag Inn",
            "russian_description": "null"
        },
        {
            "mcc": 3665,
            "edited_description": "HAMPTON INNS",
            "combined_description": "HAMPTON INNS",
            "russian_name": "Hampton Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3666,
            "edited_description": "STAKIS HOTELS",
            "combined_description": "STAKIS HOTELS",
            "russian_name": "Stakis Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3667,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3668,
            "edited_description": "MARITIM HOTELS",
            "combined_description": "MARITIM HOTELS",
            "russian_name": "Maritim Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3669,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3670,
            "edited_description": "ARCARD HOTELS",
            "combined_description": "ARCARD HOTELS",
            "russian_name": "Arcard Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3671,
            "edited_description": "ARCTIA HOTELS",
            "combined_description": "ARCTIA HOTELS",
            "russian_name": "Arctia Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3672,
            "edited_description": "CAMPANIEL HOTELS",
            "combined_description": "CAMPANIEL HOTELS",
            "russian_name": "Campaniel Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3673,
            "edited_description": "IBUSZ HOTELS",
            "combined_description": "IBUSZ HOTELS",
            "russian_name": "Ibusz Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3674,
            "edited_description": "RANTASIPI HOTELS",
            "combined_description": "RANTASIPI HOTELS",
            "russian_name": "Rantasipi Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3675,
            "edited_description": "INTERHOTEL CEDOK",
            "combined_description": "INTERHOTEL CEDOK",
            "russian_name": "Interhotel Cedok",
            "russian_description": "null"
        },
        {
            "mcc": 3676,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3677,
            "edited_description": "CLIMAT DE FRANCE HOTELS",
            "combined_description": "CLIMAT DE FRANCE HOTELS",
            "russian_name": "Climat De France Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3678,
            "edited_description": "CUMULUS HOTELS",
            "combined_description": "CUMULUS HOTELS",
            "russian_name": "Cumulus Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3679,
            "edited_description": "DANUBIUS HOTEL",
            "combined_description": "DANUBIUS HOTEL",
            "russian_name": "Danubius Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3680,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3681,
            "edited_description": "ADAMS MARK HOTELS",
            "combined_description": "ADAMS MARK HOTELS",
            "russian_name": "Adams Mark Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3682,
            "edited_description": "ALLSTAR INNS",
            "combined_description": "ALLSTAR INNS",
            "russian_name": "Allstar Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3683,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3684,
            "edited_description": "BUDGET HOST INNS",
            "combined_description": "BUDGET HOST INNS",
            "russian_name": "Budget Host Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3685,
            "edited_description": "BUDGETEL HOTELS",
            "combined_description": "BUDGETEL HOTELS",
            "russian_name": "Budgetel Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3686,
            "edited_description": "SUISSE CHALETS",
            "combined_description": "SUISSE CHALETS",
            "russian_name": "Suisse Chalets",
            "russian_description": "null"
        },
        {
            "mcc": 3687,
            "edited_description": "CLARION HOTELS",
            "combined_description": "CLARION HOTELS",
            "russian_name": "Clarion Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3688,
            "edited_description": "COMPRI HOTELS",
            "combined_description": "COMPRI HOTELS",
            "russian_name": "Compri Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3689,
            "edited_description": "CONSORT HOTELS",
            "combined_description": "CONSORT HOTELS",
            "russian_name": "Consort Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3690,
            "edited_description": "COURTYARD BY MARRIOTT",
            "combined_description": "COURTYARD BY MARRIOTT",
            "russian_name": "Courtyard By Marriott",
            "russian_description": "null"
        },
        {
            "mcc": 3691,
            "edited_description": "DILLION INNS",
            "combined_description": "DILLION INNS",
            "russian_name": "Dillion Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3692,
            "edited_description": "DOUBLETREE HOTELS",
            "combined_description": "DOUBLETREE HOTELS",
            "russian_name": "Doubletree Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3693,
            "edited_description": "DRURY INNS",
            "combined_description": "DRURY INNS",
            "russian_name": "Drury Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3694,
            "edited_description": "ECONOMY INNS OF AMERICA",
            "combined_description": "ECONOMY INNS OF AMERICA",
            "russian_name": "Economy Inns Of America",
            "russian_description": "null"
        },
        {
            "mcc": 3695,
            "edited_description": "EMBASSY SUITES",
            "combined_description": "EMBASSY SUITES",
            "russian_name": "Embassy Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3696,
            "edited_description": "EXEL INNS",
            "combined_description": "EXEL INNS",
            "russian_name": "Exel Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3697,
            "edited_description": "FARFIELD HOTELS",
            "combined_description": "FARFIELD HOTELS",
            "russian_name": "Farfield Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3698,
            "edited_description": "HARLEY HOTELS",
            "combined_description": "HARLEY HOTELS",
            "russian_name": "Harley Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3699,
            "edited_description": "MIDWAY MOTOR LODGE",
            "combined_description": "MIDWAY MOTOR LODGE",
            "russian_name": "Midway Motor Lodge",
            "russian_description": "null"
        },
        {
            "mcc": 3700,
            "edited_description": "MOTEL 6",
            "combined_description": "MOTEL 6",
            "russian_name": "Motel 6",
            "russian_description": "null"
        },
        {
            "mcc": 3701,
            "edited_description": "GUEST QUARTERS (Formally PICKETT SUITE HOTELS)",
            "combined_description": "GUEST QUARTERS (Formally PICKETT SUITE HOTELS)",
            "russian_name": "Guest Quarters (formally Pickett Suite Hotels)",
            "russian_description": "null"
        },
        {
            "mcc": 3702,
            "edited_description": "THE REGISTRY HOTELS",
            "combined_description": "THE REGISTRY HOTELS",
            "russian_name": "The Registry Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3703,
            "edited_description": "RESIDENCE INNS",
            "combined_description": "RESIDENCE INNS",
            "russian_name": "Residence Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3704,
            "edited_description": "ROYCE HOTELS",
            "combined_description": "ROYCE HOTELS",
            "russian_name": "Royce Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3705,
            "edited_description": "SANDMAN INNS",
            "combined_description": "SANDMAN INNS",
            "russian_name": "Sandman Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3706,
            "edited_description": "SHILO INNS",
            "combined_description": "SHILO INNS",
            "russian_name": "Shilo Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3707,
            "edited_description": "SHONEY’S INNS",
            "combined_description": "SHONEY’S INNS",
            "russian_name": "Shoney’s Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3708,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3709,
            "edited_description": "SUPER8 MOTELS",
            "combined_description": "SUPER8 MOTELS",
            "russian_name": "Super8 Motels",
            "russian_description": "null"
        },
        {
            "mcc": 3710,
            "edited_description": "THE RITZ CARLTON HOTELS",
            "combined_description": "THE RITZ CARLTON HOTELS",
            "russian_name": "The Ritz Carlton Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3711,
            "edited_description": "FLAG INNS (AUSRALIA)",
            "combined_description": "FLAG INNS (AUSRALIA)",
            "russian_name": "Flag Inns (Ausralia)",
            "russian_description": "null"
        },
        {
            "mcc": 3712,
            "edited_description": "GOLDEN CHAIN HOTEL",
            "combined_description": "GOLDEN CHAIN HOTEL",
            "russian_name": "Golden Chain Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3713,
            "edited_description": "QUALITY PACIFIC HOTEL",
            "combined_description": "QUALITY PACIFIC HOTEL",
            "russian_name": "Quality Pacific Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3714,
            "edited_description": "FOUR SEASONS HOTEL (AUSTRALIA)",
            "combined_description": "FOUR SEASONS HOTEL (AUSTRALIA)",
            "russian_name": "Four Seasons Hotel (Australia)",
            "russian_description": "null"
        },
        {
            "mcc": 3715,
            "edited_description": "FARIFIELD INN",
            "combined_description": "FARIFIELD INN",
            "russian_name": "Farifield Inn",
            "russian_description": "null"
        },
        {
            "mcc": 3716,
            "edited_description": "CARLTON HOTELS",
            "combined_description": "CARLTON HOTELS",
            "russian_name": "Carlton Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3717,
            "edited_description": "CITY LODGE HOTELS",
            "combined_description": "CITY LODGE HOTELS",
            "russian_name": "City Lodge Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3718,
            "edited_description": "KAROS HOTELS",
            "combined_description": "KAROS HOTELS",
            "russian_name": "Karos Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3719,
            "edited_description": "PROTEA HOTELS",
            "combined_description": "PROTEA HOTELS",
            "russian_name": "Protea Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3720,
            "edited_description": "SOUTHERN SUN HOTELS",
            "combined_description": "SOUTHERN SUN HOTELS",
            "russian_name": "Southern Sun Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3721,
            "edited_description": "HILTON CONRAD",
            "combined_description": "HILTON CONRAD",
            "russian_name": "Hilton Conrad",
            "russian_description": "null"
        },
        {
            "mcc": 3722,
            "edited_description": "WYNDHAM HOTEL AND RESORTS",
            "combined_description": "WYNDHAM HOTEL AND RESORTS",
            "russian_name": "Wyndham Hotel And Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3723,
            "edited_description": "RICA HOTELS",
            "combined_description": "RICA HOTELS",
            "russian_name": "Rica Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3724,
            "edited_description": "INER NOR HOTELS",
            "combined_description": "INER NOR HOTELS",
            "russian_name": "Iner Nor Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3725,
            "edited_description": "SEAINES PLANATION",
            "combined_description": "SEAINES PLANATION",
            "russian_name": "Seaines Planation",
            "russian_description": "null"
        },
        {
            "mcc": 3726,
            "edited_description": "RIO SUITES",
            "combined_description": "RIO SUITES",
            "russian_name": "Rio Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3727,
            "edited_description": "BROADMOOR HOTEL",
            "combined_description": "BROADMOOR HOTEL",
            "russian_name": "Broadmoor Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3728,
            "edited_description": "BALLY’S HOTEL AND CASINO",
            "combined_description": "BALLY’S HOTEL AND CASINO",
            "russian_name": "Bally’s Hotel And Casino",
            "russian_description": "null"
        },
        {
            "mcc": 3729,
            "edited_description": "JOHN ASCUAGA’S NUGGET",
            "combined_description": "JOHN ASCUAGA’S NUGGET",
            "russian_name": "John Ascuaga’s Nugget",
            "russian_description": "null"
        },
        {
            "mcc": 3730,
            "edited_description": "MGM GRAND HOTEL",
            "combined_description": "MGM GRAND HOTEL",
            "russian_name": "Mgm Grand Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3731,
            "edited_description": "HARRAH’S HOTELS AND CASINOS",
            "combined_description": "HARRAH’S HOTELS AND CASINOS",
            "russian_name": "Harrah’s Hotels And Casinos",
            "russian_description": "null"
        },
        {
            "mcc": 3732,
            "edited_description": "OPRYLAND HOTEL",
            "combined_description": "OPRYLAND HOTEL",
            "russian_name": "Opryland Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3733,
            "edited_description": "BOCA RATON RESORT",
            "combined_description": "BOCA RATON RESORT",
            "russian_name": "Boca Raton Resort",
            "russian_description": "null"
        },
        {
            "mcc": 3734,
            "edited_description": "HARVEY/BRISTOL HOTELS",
            "combined_description": "HARVEY/BRISTOL HOTELS",
            "russian_name": "Harvey/bristol Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3735,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3736,
            "edited_description": "COLORADO BELLE/EDGEWATER RESORT",
            "combined_description": "COLORADO BELLE/EDGEWATER RESORT",
            "russian_name": "Colorado Belle/Edgewater Resort",
            "russian_description": "null"
        },
        {
            "mcc": 3737,
            "edited_description": "RIVIERA HOTEL AND CASINO",
            "combined_description": "RIVIERA HOTEL AND CASINO",
            "russian_name": "Riviera Hotel And Casino",
            "russian_description": "null"
        },
        {
            "mcc": 3738,
            "edited_description": "TROPICANA RESORT AND CASINO",
            "combined_description": "TROPICANA RESORT AND CASINO",
            "russian_name": "Tropicana Resort And Casino",
            "russian_description": "null"
        },
        {
            "mcc": 3739,
            "edited_description": "WOODSIDE HOTELS AND RESORTS",
            "combined_description": "WOODSIDE HOTELS AND RESORTS",
            "russian_name": "Woodside Hotels And Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3740,
            "edited_description": "TOWNPLACE SUITES",
            "combined_description": "TOWNPLACE SUITES",
            "russian_name": "Townplace Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3741,
            "edited_description": "MILLENIUM BROADWAY HOTEL",
            "combined_description": "MILLENIUM BROADWAY HOTEL",
            "russian_name": "Millenium Broadway Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3742,
            "edited_description": "CLUB MED",
            "combined_description": "CLUB MED",
            "russian_name": "Club Med",
            "russian_description": "null"
        },
        {
            "mcc": 3743,
            "edited_description": "BILTMORE HOTEL AND SUITES",
            "combined_description": "BILTMORE HOTEL AND SUITES",
            "russian_name": "Biltmore Hotel And Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3744,
            "edited_description": "CAREFREE RESORTS",
            "combined_description": "CAREFREE RESORTS",
            "russian_name": "Carefree Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3745,
            "edited_description": "ST. REGIS HOTEL",
            "combined_description": "ST. REGIS HOTEL",
            "russian_name": "St. Regis Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3746,
            "edited_description": "THE ELIOT HOTEL",
            "combined_description": "THE ELIOT HOTEL",
            "russian_name": "The Eliot Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3747,
            "edited_description": "CLUBCORP/CLUB RESORTS",
            "combined_description": "CLUBCORP/CLUB RESORTS",
            "russian_name": "Clubcorp/club Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3748,
            "edited_description": "WELESLEY INNS",
            "combined_description": "WELESLEY INNS",
            "russian_name": "Welesley Inns",
            "russian_description": "null"
        },
        {
            "mcc": 3749,
            "edited_description": "THE BEVERLY HILLS HOTEL",
            "combined_description": "THE BEVERLY HILLS HOTEL",
            "russian_name": "The Beverly Hills Hotel",
            "russian_description": "null"
        },
        {
            "mcc": 3750,
            "edited_description": "CROWNE PLAZA HOTELS",
            "combined_description": "CROWNE PLAZA HOTELS",
            "russian_name": "Crowne Plaza Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3751,
            "edited_description": "HOMEWOOD SUITES",
            "combined_description": "HOMEWOOD SUITES",
            "russian_name": "Homewood Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3752,
            "edited_description": "PEABODY HOTELS",
            "combined_description": "PEABODY HOTELS",
            "russian_name": "Peabody Hotels",
            "russian_description": "null"
        },
        {
            "mcc": 3753,
            "edited_description": "GREENBRIAH RESORTS",
            "combined_description": "GREENBRIAH RESORTS",
            "russian_name": "Greenbriah Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3754,
            "edited_description": "AMELIA ISLAND PLANATION",
            "combined_description": "AMELIA ISLAND PLANATION",
            "russian_name": "Amelia Island Planation",
            "russian_description": "null"
        },
        {
            "mcc": 3755,
            "edited_description": "THE HOMESTEAD",
            "combined_description": "THE HOMESTEAD",
            "russian_name": "The Homestead",
            "russian_description": "null"
        },
        {
            "mcc": 3756,
            "edited_description": "SOUTH SEAS RESORTS",
            "combined_description": "SOUTH SEAS RESORTS",
            "russian_name": "South Seas Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 3757,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3758,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3759,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3760,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3761,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3762,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3763,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3764,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3765,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3766,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3767,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3768,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3769,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3770,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3771,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3772,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3773,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3774,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3775,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3776,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3777,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3778,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3779,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3780,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3781,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3782,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3783,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3784,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3785,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3786,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3787,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3788,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3789,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3790,
            "edited_description": "Hotels/Motels/Inns/Resorts",
            "combined_description": "Hotels/Motels/Inns/Resorts",
            "russian_name": "Отели, мотели, курорты",
            "russian_description": "null"
        },
        {
            "mcc": 3816,
            "edited_description": "Home2Suites",
            "combined_description": "null",
            "russian_name": "Home2Suites",
            "russian_description": "null"
        },
        {
            "mcc": 3835,
            "edited_description": "* MASTERS ECONOMY INNS",
            "combined_description": "* MASTERS ECONOMY INNS",
            "russian_name": "Dolce Hotels and Resorts",
            "russian_description": "null"
        },
        {
            "mcc": 4011,
            "edited_description": "Railroads",
            "combined_description": "Railroads",
            "russian_name": "Железные дороги – перевозка грузов",
            "russian_description": "Железные дороги, занимающиеся транспортировкой грузов. \nДля железных дорог, занимающихся перевозкой пассажиров, используется MCC 4112."
        },
        {
            "mcc": 4111,
            "edited_description": "Local/Suburban Commuter Passenger Transportation – Railroads, Feries, Local Water Transportation.",
            "combined_description": "Local/Suburban Commuter Passenger Transportation – Railroads, Feries, Local Water Transportation.",
            "russian_name": "Пассажирские перевозки - пригородные и местные пригородные рейсы, включая паромы",
            "russian_description": "Услуги местного и пригородного общественного пассажирского транспорта по регулярным маршрутам и с регулярным графиком, включая железнодорожные пригородные перевозки.\nДля такси и лимузинов, используется MCC 4121; для автобусов используется MCC 4131."
        },
        {
            "mcc": 4112,
            "edited_description": "Passenger Railways",
            "combined_description": "Passenger Railways",
            "russian_name": "Пассажирские железнодорожные перевозки",
            "russian_description": "Железнодорожные компании, которые в основном предоставляют услуги по перевозке пассажиров на длинные расстояния. Такие точки могут предоставлять или не предоставлять ночлег в поезде в течение длительных поездок. \nДля железнодорожных компаний, которые предоставляют транспортировку грузов, используется MCC 4011."
        },
        {
            "mcc": 4119,
            "edited_description": "Ambulance Services",
            "combined_description": "Ambulance Services",
            "russian_name": "Услуги скорой помощи",
            "russian_description": "Экстренные транспортные услуги с обученным персоналом, который может или не может оказать неотложную медицинскую помощь по пути в больницу или медицинскую помощь."
        },
        {
            "mcc": 4121,
            "edited_description": "Taxicabs and Limousines",
            "combined_description": "Taxicabs and Limousines",
            "russian_name": "Лимузины и такси",
            "russian_description": "Услуги пассажирских автомобильных перевозок, которые не следуют по регулярному графику или установленному маршруту."
        },
        {
            "mcc": 4131,
            "edited_description": "Bus Lines, Including Charters, Tour Buses",
            "combined_description": "Bus Lines, Including Charters, Tour Buses",
            "russian_name": "Автобусные линии",
            "russian_description": "Услуги пассажирского транспорта, которые работают по регулярному графику по заранее определенным маршрутам.\nДля операторов чартерных и туристических автобусов используется MCC 4722."
        },
        {
            "mcc": 4214,
            "edited_description": "Motor Freight Carriers, Moving and Storage Companies, Trucking – Local/Long Distance, Delivery Services – Local",
            "combined_description": "Motor Freight Carriers, Moving and Storage Companies, Trucking – Local/Long Distance, Delivery Services – Local",
            "russian_name": "Агентства по автотранспортным перевозкам, местные/ дальные автогрузоперевозки, компании попереезду и хранению, местная доставка",
            "russian_description": "Местные и дальние автогрузоперевозки, которые могут также предоставлять или не предоставлять услуги по хранению. Для хранения предметов домашнего обихода и хранения без услуг по перевозкам, используется MCC 4225. Для курьеров почтовых посылок, товаров, и бандеролей, используется MCC 4215."
        },
        {
            "mcc": 4215,
            "edited_description": "Courier Services – Air or Ground, Freight forwarders",
            "combined_description": "Courier Services – Air or Ground, Freight forwarders",
            "russian_name": "Услуги курьера – по воздуху и на земле, агентство по отправке грузов",
            "russian_description": "Торговые точки, занимающиеся доставкой лично адресованных писем, посылок и бандеролей (исключая американские почтовые услуги – MCC 9402). \nДля агентств, занимающихся автогрузоперевозками используется MCC 4214."
        },
        {
            "mcc": 4225,
            "edited_description": "Public warehousing, Storage",
            "combined_description": "Public warehousing, Storage",
            "russian_name": "Складское хранение общественного пользования –сельскохозяйственных продуктов, охлаждаемые продукты, хранение предметов домашнего обихода",
            "russian_description": "Поставщики складских помещений для хранения сельскохозяйственных продуктов, охлаждаемое хранение скоропортящихся продуктов, и хранение предметов домашнего обихода и мебели. Для торговых точек, предоставляющих услуги по хранению товаров в определенной местности, а также услуги по перевозке товаров, используется MCC 4214."
        },
        {
            "mcc": 4411,
            "edited_description": "Cruise and Steamship Lines",
            "combined_description": "Cruise and Steamship Lines",
            "russian_name": "Круизные линии",
            "russian_description": "Торговые точки, предлагающие пассажирский транспорт по открытому морю или внутренним водоемам с целью отдыха или ради удовольствия. Такие торговые точки обычно предлагают питание, развлечения, и каюты, включая всё в стоимость проезда, а также проведение стандартных и рекламируемых рейсов. С целью предварительного заказа билетов с каютами на круизных суднах, используется TCC с X. Для транзакций, возникающих в торговых точках, находящихся за пределами корабля, например, в магазине одежды, подарков, или цветочном, используется TCC с H."
        },
        {
            "mcc": 4457,
            "edited_description": "Boat Rentals and Leases",
            "combined_description": "Boat Rentals and Leases",
            "russian_name": "Аренда и лизинг суден",
            "russian_description": "Торговые точки, предлагающие в основном сдачу в наем и в аренду суден, включая рыболовные судна, плавучие дома без экипажа, парусные лодки, катера, водные мотоциклы и яхты."
        },
        {
            "mcc": 4468,
            "edited_description": "Marinas, Marine Service, and Supplies",
            "combined_description": "Marinas, Marine Service, and Supplies",
            "russian_name": "Пристани для яхт, их обслуживание и поставка расходных материалов",
            "russian_description": "Операторы пристаней для яхт. Предоставляемые услуги могут включать аренду буксира, хранение, мойку, мелкий ремонт лодок и розничную продажу расходных материалов для яхт. В этот MCC входят точки, расположенные в пристани, которые продают топливо для использования в лодках и у которых нет отдельного торгового соглашения с пристанью.\n\nДля заправочных станций, расположенных на пристани и имеющих отдельные торговые соглашения, используется MCC 5541."
        },
        {
            "mcc": 4511,
            "edited_description": "Airlines, Air Carriers ( not listed elsewhere)",
            "combined_description": "Airlines, Air Carriers ( not listed elsewhere)",
            "russian_name": "Авиалинии, авиакомпании - нигде более не классифицированные",
            "russian_description": "Только те авиалинии и авиакомпании, которым не выделены MCC коды"
        },
        {
            "mcc": 4582,
            "edited_description": "Airports, Airport Terminals, Flying Fields",
            "combined_description": "Airports, Airport Terminals, Flying Fields",
            "russian_name": "Аэропорты, терминалы аэропортов, лётные поля",
            "russian_description": "Торговые точки, которые управляют и обслуживают аэропорты и лётные поля. Такие точки могут предложить мойку и уборку самолетов, обслуживание, ремонт самолетов, хранение самолетов в аэропортах и сдача в аренду ангаров аэропортов. Для торговых точек, находящихся внутри терминала аэропорта, торгующих едой, газетами, подарками или сувенирами, используется соответствующий этому бизнесу MCC, например, MCC 5812, 5994 или 5947."
        },
        {
            "mcc": 4722,
            "edited_description": "Travel Agencies and Tour Operations",
            "combined_description": "Travel Agencies and Tour Operations",
            "russian_name": "Туристические агентства и организаторы экскурсий",
            "russian_description": "Туристические агентства, которые в основном предоставляют туристическую информацию и услуги бронирования.\nТакие точки выступают в качестве агентов от имени путешественников при бронировании и покупке авиабилетов, билетов на наземный или морской транспорт или бронирования, включая полеты на самолете, автобусные туры, морские круизы, прокат автомобилей, железнодорожные перевозки и проживание. Также включает в себя туроператоров, которые организуют и собирают туры для продажи через турагента или непосредственно покупателю. Путешественник также может заказать такие туристические пакеты и экскурсии через консьержа отеля или в кассе."
        },
        {
            "mcc": 4723,
            "edited_description": "Package Tour Operators (For use in Germany only)",
            "combined_description": "Package Tour Operators (For use in Germany only)",
            "russian_name": "Пакетные туроператоры - только Германия",
            "russian_description": "Точки, классифицированные этим MCC, являются туроператорами в Германии."
        },
        {
            "mcc": 4784,
            "edited_description": "Toll and Bridge Fees",
            "combined_description": "Toll and Bridge Fees",
            "russian_name": "Платные дороги и мосты",
            "russian_description": "Торговые точки, собирающие плату за проезд по платным дорогам, трассам и мостам."
        },
        {
            "mcc": 4789,
            "edited_description": "Transportation Services, Not elsewhere classified)",
            "combined_description": "Transportation Services, Not elsewhere classified)",
            "russian_name": "Услуги пассажирских перевозок – нигде более не классифицированные",
            "russian_description": "Точки, предлагающие услуги по перевозке пассажиров, нигде более не классифицированные. Такие услуги включают перевозки на конной тяге, велотакси, канатные дороги, трансфер до аэропорта или фуникулер. Не включает услуги парома, автобусные поездки, круизные линии, пассажирские поезда, такси и лимузины."
        },
        {
            "mcc": 4812,
            "edited_description": "Telecommunications Equipment including telephone sales",
            "combined_description": "Telecommunications Equipment including telephone sales",
            "russian_name": "Телекоммуникационное оборудование, включая продажу телефонов",
            "russian_description": "Торговые точки, которые продают телекоммуникационное оборудование, такое как телефоны, факсы, пейджеры, сотовые телефоны, и другое оборудование, относящееся к телекоммуникациям. \nДля продаж телекоммуникационных услуг используется MCC 4814."
        },
        {
            "mcc": 4814,
            "edited_description": "Fax services, Telecommunication Services",
            "combined_description": "Fax services, Telecommunication Services",
            "russian_name": "Телекоммуникационные услуги",
            "russian_description": "Провайдеры телекоммуникационных услуг, таких как местные и междугородные телефонные звонки и услуги факса. Включены точки, которые продают предоплаченные телефонные услуги, такие как телефонные карточки, и точки, выполняющие регулярное (например, ежемесячные) выставление счетов за телефонные звонки."
        },
        {
            "mcc": 4815,
            "edited_description": "VisaPhone",
            "combined_description": "VisaPhone",
            "russian_name": "МастерФон телефонные услуги – Ежемесячное составление телефонных счетов",
            "russian_description": "Используется исключительно для ежемесячных телефонных счетов для телефоллых услуг МастерКард МастерФон."
        },
        {
            "mcc": 4816,
            "edited_description": "Computer Network Services",
            "combined_description": "Computer Network Services",
            "russian_name": "Компьютерные сети, информационные услуги",
            "russian_description": "Провайдеры компьютерных сетей, информационные услуги и другие онлайн-сервисы, такие как хранилища файлов, электронные доски объявлений, электронная почта, услуги хостинга веб-сайтов или доступа в Интернет.\n\nДля точек, предлагающих продукты или услуги через интернет, используется MCC, который наилучшим образом описывает предлагаемый продукт или услугу.\nДля точек, которые предоставляют аудиотекст (например, психологические горячие линии) или видеотекст (например, сайты для взрослых в чате), используется MCC 5967.\nДля точек, оказывающих услуги разработки программ и обработки данных, используется MCC 7372."
        },
        {
            "mcc": 4821,
            "edited_description": "Telegraph services",
            "combined_description": "Telegraph services",
            "russian_name": "Услуги телеграфа",
            "russian_description": "Провайдеры телеграфных и других коммуникационных услуг по передаче несловесных сообщений, таких как каблограммы."
        },
        {
            "mcc": 4829,
            "edited_description": "Money Orders – Wire Transfer",
            "combined_description": "Money Orders – Wire Transfer",
            "russian_name": "Денежные переводы",
            "russian_description": "Транзакция, при которой средства доставляются или становятся доступными человеку или счету. Эти транзакции включают транзакции не лицом к лицу, а осуществляемые, например, через Интернет."
        },
        {
            "mcc": 4899,
            "edited_description": "Cable and other pay television (previously Cable Services)",
            "combined_description": "Cable and other pay television (previously Cable Services)",
            "russian_name": "Кабельные и другие платные телевизионные услуги",
            "russian_description": "Подключение и прямая подача телевизионных программ со взносом или на платной основе."
        },
        {
            "mcc": 4900,
            "edited_description": "Electric, Gas, Sanitary and Water Utilities",
            "combined_description": "Electric, Gas, Sanitary and Water Utilities",
            "russian_name": "Жилищно-коммунальные услуги",
            "russian_description": "Точки, оказывающие услуги по передаче или распределению электроэнергии, газа, по установке и обслуживанию систем водоснабжения или сбору и утилизации отходов.\n\nДля точек, предоставляющих телекоммуникационные услуги, используется MCC 4814."
        },
        {
            "mcc": 5013,
            "edited_description": "Motor vehicle supplies and new parts",
            "combined_description": "Motor vehicle supplies and new parts",
            "russian_name": "Поставщики грузовиков и запчастей",
            "russian_description": "Оптовые поставщики аксессуаров для грузовиков, инструментов, оборудования и новых запчастей.\nДля работ по ремонту автомобилей используется MCC 7531 или 7538, смотря, что больше подходит."
        },
        {
            "mcc": 5021,
            "edited_description": "Office and Commercial Furniture",
            "combined_description": "Office and Commercial Furniture",
            "russian_name": "Офисная и торговая мебель",
            "russian_description": "Оптовые производители или распространители офисной мебели (например, столы, стулья, шкафы, перегородки, стеллажи) и торговая мебель (например, столы и стулья ля ресторанов, мебель для общественных парков и строений, церковные скамьи, школьные парты, театральные ложи). Для производителей, делающих или продающих оборудование и мебель для больниц, такие, как кровати, используется MCC 5047."
        },
        {
            "mcc": 5039,
            "edited_description": "Construction Materials, Not Elsewhere Classified",
            "combined_description": "Construction Materials, Not Elsewhere Classified",
            "russian_name": "Строительные материалы – нигде более не классифицированные",
            "russian_description": "Предприятия оптовой торговли строительными материалами, такими, как здание из сборных материалов, пиломатериалы и стекло, архитектурная металлообработка, навесы, ограждения, металлические строения, и септик танк. Такие торговые точки могут продавать или не продавать краски и красящее оборудование. \nДля предприятий оптовой торговли, продающих краски и красящее оборудование, используется MCC 5198. \nДля продавцов и распространителей оборудования, используемого в строительных проектах, используется MCC 5046."
        },
        {
            "mcc": 5044,
            "edited_description": "Office, Photographic, Photocopy, and Microfilm Equipment",
            "combined_description": "Office, Photographic, Photocopy, and Microfilm Equipment",
            "russian_name": "Офисное, фотографическое, фотокопировальное, и микрофильмирующее оборудование",
            "russian_description": "Предприятия оптовой торговли офисного и фотографического оборудования, такого, как пленки, кассовые аппараты, копировальные машины, микрофильмирующие машины, камеры хранения и сейфы, пишущие машинки, факсовые машины, арифмометры, машины для приклеивания или печати адресов. Для оптовых торговцев офисной мебелью, используется MCC 5021. Для оптовых торговцев компьютерным оборудованием, используется MCC 5045."
        },
        {
            "mcc": 5045,
            "edited_description": "Computers, Computer Peripheral Equipment, Software",
            "combined_description": "Computers, Computer Peripheral Equipment, Software",
            "russian_name": "Компьютеры, периферийное компьютерное оборудование, программное обеспечение",
            "russian_description": "Оптовые распространители компьютерного оборудования, программного обеспечения, и соответствующего оборудования, которое может сопровождать или не сопровождать ремонтные работы. Товары для продажи могут включать компьютерные мониторы, драйвер дисковода, кабели, клавиатуры, принтеры, сканеры, модемы, компьютерные программы, и относящиеся аксессуары и оборудование. Такие торговые точки могут также продавать столы и другую офисную мебель, специально разработанную для использования с компьютерами. Для торговых точек, которые в основном продают компьютерную мебель, используется MCC 5021. Для торговых точек, проводящих главным образом ремонтные работы, используется MCC 7379."
        },
        {
            "mcc": 5046,
            "edited_description": "Commercial Equipment, Not Elsewhere Classified",
            "combined_description": "Commercial Equipment, Not Elsewhere Classified",
            "russian_name": "Коммерческое оборудование – нигде более не классифицированное",
            "russian_description": "Оптовые поставщики торговых машин и оборудования нигде более не классифицированного. Примеры включают пищевое оборудование и оборудование для тепловой обработки, неоновые вывески, весы, шкафчики, торговые печи и микроволновые печи, приборы для газированной воды, торговые прилавки, манекены, и торговые автоматы. Такие торговые точки могут сдавать или не сдавать в аренду или лизинг оборудование.\nДля торговых точек, сдающих в аренду или лизинг оборудование, используется MCC 7394."
        },
        {
            "mcc": 5047,
            "edited_description": "Medical, Dental Ophthalmic, Hospital Equipment and Supplies",
            "combined_description": "Medical, Dental Ophthalmic, Hospital Equipment and Supplies",
            "russian_name": "Стоматологическое / лабораторное / медицинское / офтальмологическое оборудование и материалы для больниц",
            "russian_description": "Представители оптовой торговли лабораторным, хирургическим, ортопедическим оборудованием, а также оборудованием для слежения за больными, и колясками для инвалидов, медицинскими инструментами, промышленными средствами безопасности, больничными койками, и другими сопутствующими товарами для больницы. Также включает поставщиков  стоматологических лабораторных, ортопедических, профессиональных устройств, диагностического оборудования, слуховых аппаратов, аптечек, терапевтического оборудования, рентгеновских машин и запасных частей. Для оптовых торговцев мебелью, такой как стулья, столы, журнальные стенды для медицинских или стоматологических приемных,  используется МСС 5021. Для оптовых поставщиков сопутствующих товаров для уборки больниц, используется МСС 2842."
        },
        {
            "mcc": 5051,
            "edited_description": "Metal Service Centers and Offices",
            "combined_description": "Metal Service Centers and Offices",
            "russian_name": "Центры и офисы работ по металлу",
            "russian_description": "Оптовые поставщики полуобработанных металлических изделий, исключая драгоценные металлы. Товары для продажи могут включать стальные трубы и трубопроводы, проволочное сито и скрепляющие детали, гвозди, болванки. алюминиевые стержни, рельсы, металлические или оцинкованные листы, металлические полоски, чугунные катанки, и проволочные канаты или кабели. Такие торговые точки могут сотрудничать с оптовыми магазинами (центры работ по металлу) и с не оптовыми (офисы по продаже металла).\nДля оптовых торговцев драгоценными металлами, используется МСС 5094."
        },
        {
            "mcc": 5065,
            "edited_description": "Electrical Parts and Equipment",
            "combined_description": "Electrical Parts and Equipment",
            "russian_name": "Электрические части и оборудование",
            "russian_description": "Оптовые продавцы электронных частей и коммуникационного оборудования. Товары для продажи могут включать электрические проволоки, конденсаторы, электрические конденсаторы, диоды, полупроводниковые приборы, системы громкой связи, и электрические вывески. \nДля розничных торговцев, продающих электронное оборудование, используется МСС 5732. \nДля розничных торговцев, продающих телекоммуникационное оборудование, такое, как телефоны и пейджеры, используется МСС 4812."
        },
        {
            "mcc": 5072,
            "edited_description": "Hardware Equipment and Supplies",
            "combined_description": "Hardware Equipment and Supplies",
            "russian_name": "Оборудование и сопутствующие материалы для технического обеспечения",
            "russian_description": "Предприятия оптовой торговли общим техническим обеспечением и ножами. Товары для продажи могут включать болты, гайки, заклепки, отвертки, зажимы, ручные инструменты. замки, шайбы, кнопки, скобы, гвозди, ручные пилы, пильное полотно, электрические ручные инструменты.\nДля торговых точек, продающих техническое обеспечение, используется МСС 5251."
        },
        {
            "mcc": 5074,
            "edited_description": "Plumbing and Heating Equipment and Supplies",
            "combined_description": "Plumbing and Heating Equipment and Supplies",
            "russian_name": "Оборудование для водопровода и отопительной системы",
            "russian_description": "Оптовые распространители гидравлического оборудования и сопутствующих товаров для водопроводной и отопительной систем. Товары для продажи могут включать вентили, хомуты, оснастку, конвекторы, котлы, медные товары, панели и оборудование для солнечного отопления, и водонагреватели. Для оптовых продавцов торгового морозильного оборудования и сопутствующих товаров, или электроприборов, таких как газовые и электрические кухонные плиты и торговые печи, используется МСС 5046."
        },
        {
            "mcc": 5085,
            "edited_description": "Industrial Supplies, Not Elsewhere Classified",
            "combined_description": "Industrial Supplies, Not Elsewhere Classified",
            "russian_name": "Промышленное оборудование –нигде более не классифицированное",
            "russian_description": "Оптовые распространители промышленного оборудования, нигде более не классифицированные. Товары для продажи могут включать абразивные материалы, опоры, коробки, металлическая, стеклянная и керамическая тара, контейнеры, пробки, сальники, резиновые втулки, гидравлические вентили, шланги, поршни, цепные колеса, втулки. бутылки (стеклянные или пластиковые), промышленная подгонка, канатно-веревочные изделия, шпагат и трос, металлические крышки, печатная краска для принтеров, гравировальное оборудование, кожаные ремни, сопутствующие товары для станков, ведра, резиновые товары, сопутствующие товары для печатания на ткани, и металлические бочки."
        },
        {
            "mcc": 5094,
            "edited_description": "Precious Stones and Metals, Watches and Jewelry",
            "combined_description": "Precious Stones and Metals, Watches and Jewelry",
            "russian_name": "Драгоценные камни и металлы, часы и ювелирные изделия",
            "russian_description": "Оптовые торговцы ювелирных изделий, часов, драгоценных камней и металлов. Товары для продажи могут включать дешевые украшения, часы и детали часов, изделия из серебра, жемчуга, бриллианты и другие драгоценные камни, золото, платину и другие драгоценные металлы, и трофеи. Такие торговые точки могут предлагать или не предлагать работы по ремонту. Для торговых точек, занимающихся ремонтом, используется МСС 7699. Для розничных торговцев предметами, перечисленными здесь, используется МСС 5944."
        },
        {
            "mcc": 5099,
            "edited_description": "Durable Goods, Not Elsewhere Classified",
            "combined_description": "Durable Goods, Not Elsewhere Classified",
            "russian_name": "Товары длительного пользования – нигде более не классифицированные",
            "russian_description": "Оптовые распространители товаров длительного пользования, нигде более не классифицированные. Товары для продажи могут включать огнетушители, пожарная сигнализация, газовые зажигалки, записанные кассеты, топливная древесина, лесоматериалы, древесная стружка, неэлектрические вывески, музыкальные инструменты, и багаж. \nДля оптовых поставщиков электрических вывесок, используется МСС 5065."
        },
        {
            "mcc": 5111,
            "edited_description": "Stationery, Office Supplies, Printing, and Writing Paper",
            "combined_description": "Stationery, Office Supplies, Printing, and Writing Paper",
            "russian_name": "Канцелярия, офисные сопутствующие товары, бумага для печатания и письма",
            "russian_description": "Оптовые поставщики канцелярии, офисных принадлежностей, и бумаги для печатания и письма. Товары для продажи могут включать деловые формы, копировальное оборудование, регистрационные карточки и папки-скоросшиватели, ручки, карандаши, конверты, ленты для печатных машинок и принтеров, скоросшиватели, квитанционные книжки и книги продаж, альбомы для фотографий и для наклеивания газетных вырезок. \nДля торговцев офисными машинами, такими, как печатные и копировальные машины, и для торговых точек, предлагающих копировальные услуги, используется МСС 5044. \nДля оптовых торговцев офисной мебелью, используется МСС 5021."
        },
        {
            "mcc": 5122,
            "edited_description": "Drugs, Drug Proprietors, and Druggist’s Sundries",
            "combined_description": "Drugs, Drug Proprietors, and Druggist’s Sundries",
            "russian_name": "Лекарства, их распространители, аптеки",
            "russian_description": "Оптовые распространители предписанных и запатентованных лекарств, витаминов, гигиенической косметики, антисептиков, перевязочных материалов, фармацевтической продукции, биологических и подобных товаров, и других разнообразных мелких товаров, типичных для продажи в аптеках. \nДля оптовых торговцев хирургическими, больничными, или стоматологическими товарами, используется МСС 5047."
        },
        {
            "mcc": 5131,
            "edited_description": "Piece Goods, Notions, and Other Dry Goods",
            "combined_description": "Piece Goods, Notions, and Other Dry Goods",
            "russian_name": "Штучные товары, галантерея и другие текстильные товары",
            "russian_description": "Оптовые поставки штучных и текстильных товаров. Сюда относятся: марля, мануфактурные товары, изделия из стекловолокна, застежки-молнии, натуральные или синтетические ткани, продаваемые по ярду, комплекты для сборки поясов и пряжек, текстильные соединения, пуговицы, трикотажные и кружевные полотна, ленты, швейные принадлежности, нитки и отделочные ткани. \nДля оптовых поставок гардин или других  портьерных тканей используется MCC 5719."
        },
        {
            "mcc": 5137,
            "edited_description": "Men’s Women’s and Children’s Uniforms and Commercial Clothing",
            "combined_description": "Men’s Women’s and Children’s Uniforms and Commercial Clothing",
            "russian_name": "Мужская, женская и детская спецодежда",
            "russian_description": "Оптовые поставки рабочей одежды и всех видов мужской, женской и детской спецодежды, включая обувь, дневное белье, плащи, мантии и шапочки для выпускников колледжей, форменную одежду для занятий спортом (для балета, каратэ, футбола и т.д.), а также форму для частных или религиозных учебных заведений.\nДля оптовых поставщиков спец-обуви используется MCC 5139. \nДля розничных торговцев, специализирующихся на продаже одежды и аксессуаров используется соответственно розничный MCC."
        },
        {
            "mcc": 5139,
            "edited_description": "Commercial Footwear",
            "combined_description": "Commercial Footwear",
            "russian_name": "Спец-обувь",
            "russian_description": "Оптовые поставки туфель и ботинок специального назначения, включая спортивную обувь. Для розничных торговцев обувью используется MCC 5661"
        },
        {
            "mcc": 5169,
            "edited_description": "Chemicals and Allied Products, Not Elsewhere Classified",
            "combined_description": "Chemicals and Allied Products, Not Elsewhere Classified",
            "russian_name": "Химикалии и смежные вещества - нигде более не классифицированные",
            "russian_description": "Оптовые поставки химикалий и смежных веществ, не подпавших под другую категорию. Обычно используются в промышленности. Сюда относятся: промышленные кислоты, аммиак и спирт, тяжелые, ароматические и другие хим. соединения, хлорин, сжатые и сжиженные газы, детергенты, присадки к топливу и присадки для смазочных масел, полимеры, соли, скипидар, уплотнители, антикоррозионные химические вещества, пековые продукты, сухой лед, красители, клей, желатин и взрывчатые вещества. \nДля розничной торговли пиротехническими изделиями используется MCC 5999. \nПродавцам хим. веществ для чистки и санитарной обработки присваивается MCC 2842."
        },
        {
            "mcc": 5172,
            "edited_description": "Petroleum and Petroleum Products",
            "combined_description": "Petroleum and Petroleum Products",
            "russian_name": "Нефть и нефтепродукты",
            "russian_description": "Оптовые поставки нефти и нефтепродуктов, таких как: бутан, сырая нефть, мазут(жидкое топливо), бензин, керосин, смазочные масла и жиры и нафта(тяжелый бензин). Сюда также относятся поставщики услуг по заправке самолетов. Для розничной торговли жидким топливом, печным топливом, лесом, углем или пропаном используется MCC 5983."
        },
        {
            "mcc": 5192,
            "edited_description": "Books, Periodicals, and Newspapers",
            "combined_description": "Books, Periodicals, and Newspapers",
            "russian_name": "Книги, периодические издания и газеты",
            "russian_description": "Оптовые производители и поставщики книг, периодических изданий, журналов и газет. Для издательств книг, периодики и журналов используется MCC 2741. Для розничной продажи книг используется MCC 5942."
        },
        {
            "mcc": 5193,
            "edited_description": "Florists’ Supplies, Nursery Stock and Flowers",
            "combined_description": "Florists’ Supplies, Nursery Stock and Flowers",
            "russian_name": "Принадлежности для флористов, питомник и цветы",
            "russian_description": "Оптовые дистрибьюторы цветов, материалов для питомников и флористов, свежих и искусственных цветов и горшечных растений.\nДля розничных магазинов цветов и растений используется MCC 5992."
        },
        {
            "mcc": 5198,
            "edited_description": "Paints, Varnishes, and Supplies",
            "combined_description": "Paints, Varnishes, and Supplies",
            "russian_name": "Лакокрасочная продукция и сопровождающие товары",
            "russian_description": "Оптовые поставки красок, лаков, обоев и сопровождающих товаров. Ассортимент включает краски и красители, эмали, лаки, кисти для красок, баночки для красок, наждачную бумагу, шеллак,  валики, распылители  и т.д. \nДля розничной торговли вышеупомянутыми товарами используется MCC 5231."
        },
        {
            "mcc": 5199,
            "edited_description": "Non-durable Goods, Not Elsewhere Classified",
            "combined_description": "Non-durable Goods, Not Elsewhere Classified",
            "russian_name": "Товары недлительного пользования - нигде более не классифицированные",
            "russian_description": "Оптовые дистрибьюторы товаров недлительного пользования, не классифицированные в других MCC. Ассортимент товаров таких торговцев может включать в себя продукты питания, предметы искусства и ремесла, вешалки для одежды, пенорезину, лед, сырую резину, губки, текстильные мешки, мешковину, холщовые изделия, корзины, подарки и новинки, кожа и режущие материалы, а также другие кожаные изделия, кроме обуви.\nДля оптовиков, которые в основном продают кожаную обувь, используется MCC 5139.\nДля продавцов, которые продают предметы искусства и ремесла, используется MCC 5970; для продавцов подарков и сувениров используется MCC 5947."
        },
        {
            "mcc": 5200,
            "edited_description": "Home Supply Warehouse Stores",
            "combined_description": "Home Supply Warehouse Stores",
            "russian_name": "Товары для дома",
            "russian_description": "Торговые точки, ориентированные на широкую публику, предлагающие богатый выбор товаров для дома, таких как: обои, краски, лесоматериал, садовые принадлежности, электрические и осветительные приборы, а также декорирующие материалы. Эти торговые точки предлагают как \"готовые\" товары, например, раковины, шкафчики и двери, так и наборы \"Сделай сам\"."
        },
        {
            "mcc": 5211,
            "edited_description": "Lumber and Building Materials Stores",
            "combined_description": "Lumber and Building Materials Stores",
            "russian_name": "Лесо- и строительный материал",
            "russian_description": "Продажа в розницу лесо- и строительного материала. Сюда относятся также строительные компании, предлагающие свою продукцию подрядчиком, а не широкой публике. К товарам, выставляемым на продажу здесь относятся: лесоматериал, незаконченные изделия из дерева, осветительные материалы, цемент, песок, гравий, строительные или электрические материалы, кирпичи, ограждения, трубы, стекловолокно и прессформы. Для крупных складов или сети магазинов, торгующих товарами для дома со скидкой, рассчитанных на широкую публику, используется MCC 5200. Для подрядчиков используется наиболее подходящее MCC из \"Договорных услуг\""
        },
        {
            "mcc": 5231,
            "edited_description": "Glass, Paint, and Wallpaper Stores",
            "combined_description": "Glass, Paint, and Wallpaper Stores",
            "russian_name": "Розничная продажа стекла, красок и обоев",
            "russian_description": "Продажа в розницу стекла, красок и малярных принадлежностей, обоев и сопутствующих товаров. Для оптовых поставщиков малярных принадлежностей используется MCC 5039."
        },
        {
            "mcc": 5251,
            "edited_description": "Hardware Stores",
            "combined_description": "Hardware Stores",
            "russian_name": "Скобяные товары в розницу",
            "russian_description": "Торговые точки, которые продают скобяные товары в полном ассортименте для широкой публики. Сюда относятся такие товары, как: мелкие электрические приборы, провода, гайки, болты, гвозди, шурупы, молотки, отвертки и другие мелкие инструменты, кольцевые прокладки, ключи, лампочки, скобы и сантехническое оборудование. Для крупных складов или сети магазинов, торгующих товарами для дома со скидкой, рассчитанных на широкую публику, используется MCC 5200."
        },
        {
            "mcc": 5261,
            "edited_description": "Nurseries – Lawn and Garden Supply Store",
            "combined_description": "Nurseries – Lawn and Garden Supply Store",
            "russian_name": "Садовые принадлежности (в том числе для ухода за газонами) в розницу",
            "russian_description": "Продажа инвентаря для цветочных питомников, саженцев деревьев и кустарника, растений в горшках, семян, луковиц, мульчи, почвоулучшителей, удобрений, пестицидов, садового инвентаря и  других садовых принадлежностей"
        },
        {
            "mcc": 5271,
            "edited_description": "Mobile Home Dealers",
            "combined_description": "Mobile Home Dealers",
            "russian_name": "Продажа жилых фургонов",
            "russian_description": "Торговые точки, занимающиеся продажей новых и б/у жилых фургонов, зап. частей, комплектующих и оборудования к ним."
        },
        {
            "mcc": 5300,
            "edited_description": "Wholesale Clubs",
            "combined_description": "Wholesale Clubs",
            "russian_name": "Оптовики",
            "russian_description": "Склады, специализирующиеся на продаже товаров массового потребления, предлагающие  широкий ассортимент товаров оптом по низким ценам. Такие торговые точки могут иметь или не иметь определенные требования к количеству участников \"оптового клуба\". Изделия для продажи включают бытовые принадлежности и электроприборы, офисное оборудование, сушеные бакалейные и скоропортящиеся товары, мебель для дома и офиса, электротовары , автозапчасти и аксессуары."
        },
        {
            "mcc": 5309,
            "edited_description": "Duty Free Store",
            "combined_description": "Duty Free Store",
            "russian_name": "Беспошлинные магазины Duty Free",
            "russian_description": "Магазины, торгующие различными сувенирами и импортными товарами, освобожденными от таможенных пошлин, такими как: драгоценности, косметика, табачные и спиртные изделия. Обычно такие торговые точки располагаются в здании аэропорта и отелях."
        },
        {
            "mcc": 5310,
            "edited_description": "Discount Stores",
            "combined_description": "Discount Stores",
            "russian_name": "Магазины, торгующие по сниженным ценам",
            "russian_description": "Продажа разнообразных товаров по сниженным ценам. Сюда относится одежда, посуда, бытовое оборудование, принадлежности для личной гигиены и электроприборы. Такие торговые точки обычно находятся у входа в магазин, они рекламируют и продают товары по низким ценам ."
        },
        {
            "mcc": 5311,
            "edited_description": "Department Stores",
            "combined_description": "Department Stores",
            "russian_name": "Универмаги",
            "russian_description": "Крупные торговые точки, имеющие широкий ассортимент товаров в различных секциях с отдельными кассами. Здесь продается одежда, бытовое оборудование, мебель, электроприборы, косметика, посуда и основные бытовые принадлежности"
        },
        {
            "mcc": 5331,
            "edited_description": "Variety Stores",
            "combined_description": "Variety Stores",
            "russian_name": "Универсальные магазины",
            "russian_description": "Торговцы, предлагающие разнообразный, но ограниченный выбор товаров в низком или популярном ценовом диапазоне. Такие магазины, как правило, не узкоспециализированные, не предлагают проприетарную плату или кредитные карты и не доставляют товар. Универсальные магазины предлагают товары, похожие на проданные дисконтными магазинами, но работают в гораздо меньших масштабах."
        },
        {
            "mcc": 5399,
            "edited_description": "Misc. General Merchandise",
            "combined_description": "Misc. General Merchandise",
            "russian_name": "Различные товары общего назначения",
            "russian_description": "Мелкие торговые точки и магазины среднего звена с широким ассортиментом товаров в различных секциях с отдельными кассами. Здесь торгуют одеждой, текстильными  и скобяными товарами, посудой, бытовыми принадлежностями, электроприборами, мебелью и косметикой. Такие торговые точки предоставляют скидки или отпускают товары в кредит, осуществляют доставку покупок.и продажу со складов. Магазины различных товаров общего назначения предлагают такой же ассортимент товаров, как и универмаги, но в гораздо меньшем обьеме."
        },
        {
            "mcc": 5411,
            "edited_description": "Grocery Stores, Supermarkets",
            "combined_description": "Grocery Stores, Supermarkets",
            "russian_name": "Бакалейные магазины, супермаркеты",
            "russian_description": "Торговые точки, которые продают полную линейку продуктов питания для домашнего потребления. Пищевые продукты для продажи включают бакалейные товары, мясо, продукты, молочные продукты и консервированные, замороженные, предварительно упакованные и сухие продукты. Также продукты для продажи могут включать ограниченный выбор посуды, чистящих и полирующих изделий, средств личной гигиены, косметики, поздравительных открыток, книг, журналов, предметов домашнего обихода и сухих товаров. Эти точки также могут управлять специализированными отделами, такими как лавка деликатесов, мясная лавка, аптека или цветочный отдел.\nДля магазинов, которые продают ограниченный выбор продуктов или предметов специальности, используется MCC 5499."
        },
        {
            "mcc": 5422,
            "edited_description": "Meat Provisioners – Freezer and Locker",
            "combined_description": "Meat Provisioners – Freezer and Locker",
            "russian_name": "Продажа свежего и мороженого мяса",
            "russian_description": "Продажа свежего, замороженного или консервированного мяса и рыбы, моллюсков и других морепродуктов. Сюда относятся также торговые точки, осуществляющие массовые розничные продажи мяса для хранения в замороженном виде. Такие мясные магазины могут продавать мясо либо собственного скота, либо закупать мясо через другие фирмы. \nДля магазинов домашней птицы используется MCC 5499."
        },
        {
            "mcc": 5441,
            "edited_description": "Candy, Nut, and Confectionery Stores",
            "combined_description": "Candy, Nut, and Confectionery Stores",
            "russian_name": "Кондитерские",
            "russian_description": "Продажа конфет, шоколада, орешков, сухофруктов, попкорна и др."
        },
        {
            "mcc": 5451,
            "edited_description": "Dairy Products Stores",
            "combined_description": "Dairy Products Stores",
            "russian_name": "Продажа молочных продуктов в розницу",
            "russian_description": "Торговые точки, непосредственно продающие расфасованные молочные продукты. Сюда относятся: масло, сыр, расфасованное мороженое и молоко."
        },
        {
            "mcc": 5462,
            "edited_description": "Bakeries",
            "combined_description": "Bakeries",
            "russian_name": "Булочные",
            "russian_description": "Торговые точки, продающие хлебобулочные изделия, а также изготавливающие продукцию на заказ. Сюда относятся: рогалики, хлеб, пирожные, пончики, изделия из слоеного теста, булочки и свадебные торты."
        },
        {
            "mcc": 5499,
            "edited_description": "Misc. Food Stores – Convenience Stores and Specialty Markets",
            "combined_description": "Misc. Food Stores – Convenience Stores and Specialty Markets",
            "russian_name": "Различные продовольственные магазины - нигде более не классифицированные",
            "russian_description": "Торговые точки, продающие продукты, не классифицированные в других категориях. Сюда относятся: специализированные продовольственные рынки, магазины диетических продуктов, деликатесов, домашней птицы, кофейни, овощные и фруктовые рынки, а также магазины мороженого, йогуртов и полуфабрикатов и небольшие магазины у дома. \nДля магазинов, которые также продают автомобильный бензин, используется MCC 5541. \nДля точек, которые в основном продают мясо и морепродукты, используется MCC 5422."
        },
        {
            "mcc": 5511,
            "edited_description": "Car and Truck Dealers (New and Used) Sales, Service, Repairs, Parts, and Leasing",
            "combined_description": "Car and Truck Dealers (New and Used) Sales, Service, Repairs, Parts, and Leasing",
            "russian_name": "Легковой и грузовой транспорт – продажа, сервис, ремонт, запчасти и лизинг.",
            "russian_description": "Магазины, продающие новые и подержанные автомобили, грузовики, пикапы и микроавтобусы. Эти торговые точки могут также производить ремонтные работы и предоставлять запчасти и аксессуары в ассортименте. \nДля точек, специализирующихся на ремонтных работах, используется МСС 7538."
        },
        {
            "mcc": 5521,
            "edited_description": "Automobile and Truck Dealers (Used Only)",
            "combined_description": "Automobile and Truck Dealers (Used Only)",
            "russian_name": "Продажа легковых и грузовых автомобилей (только подержанных)",
            "russian_description": "Магазины, торгующие только подержанными автомобилями и грузовиками,  не осуществляющие продажу новых автотранспортных средств.Сюда относятся: подержанные пикапы, микроавтобусы, антикварные и старинные автомобили."
        },
        {
            "mcc": 5531,
            "edited_description": "Automobile Supply Stores",
            "combined_description": "Automobile Supply Stores",
            "russian_name": "Автомагазины и товары для дома",
            "russian_description": "Торговые точки, продающие различные товары для дома, а также для ремонта и усовершенствования автомобилей. Сюда относятся: новые автошины, аккумуляторы и другие автозапчасти и аксессуары, а также бытовые принадлежности, оборудование и техника. \nДля торговых точек, реализующих товары и принадлежности для дома со склада, используется МСС 5200. \nДля магазинов, продающих автозапчасти, оборудование и сопутствующие аксессуары, используется МСС 5533."
        },
        {
            "mcc": 5532,
            "edited_description": "Automotive Tire Stores",
            "combined_description": "Automotive Tire Stores",
            "russian_name": "Автошины",
            "russian_description": "Торговые точки, продающие шины для автомобилей и грузовиков, а также сопутствующие запасные части. Эти магазины производят также замену шин и ремонтное обслуживание. \nДля торговых точек, специализирующихся на восстановлении протекторов и починке шин, используется МСС 7534."
        },
        {
            "mcc": 5533,
            "edited_description": "Automotive Parts, Accessories Stores",
            "combined_description": "Automotive Parts, Accessories Stores",
            "russian_name": "Автозапчасти и аксессуары",
            "russian_description": "Торговые точки, продающие автозапчасти, оборудование и аксессуары. Сюда относятся: масла и масляные фильтры, запчасти, глушители, чистящие и полирующие средства, свечи зажигания, освежители, стеклоочистители и краски. В отдельных случаях здесь также могут продаваться автомагнитолы и усилители.\nДля магазинов, специализирующихся на продаже автомагнитол и усилителей, используется МСС 5732."
        },
        {
            "mcc": 5541,
            "edited_description": "Service Stations ( with or without ancillary services)",
            "combined_description": "Service Stations ( with or without ancillary services)",
            "russian_name": "Заправочные станции (с вспомогательными услугами или без)",
            "russian_description": "Торговые точки, которые продают топливо для потребительского использования и могут или не могут также иметь на территории магазин, автомойку или авторемонтную мастерскую. Этот MCC включает станции техобслуживания, расположенных в гавани, у которых есть отдельное торговое соглашение от торгового терминала.\nДля транзакций, совершаемых на автоматических заправочных станциях, используется MCC 5542."
        },
        {
            "mcc": 5542,
            "edited_description": "Automated Fuel Dispensers",
            "combined_description": "Automated Fuel Dispensers",
            "russian_name": "Автоматические заправочные станции",
            "russian_description": "Торговые точки, которые продают автомобильный бензин, используя, как правило, автоматические топливораздаточные колонки, позволяя держателям карт оплачивать топливо на колонке."
        },
        {
            "mcc": 5551,
            "edited_description": "Boat Dealers",
            "combined_description": "Boat Dealers",
            "russian_name": "Продажа лодок",
            "russian_description": "Торговые точки, продающие новые и подержанные плавсредства, водные принадлежности и подвесные моторы. Сюда относятся: моторные лодки, катера, парусники, рыболовные суда, специализированные лодки для занятия водными лыжами."
        },
        {
            "mcc": 5561,
            "edited_description": "Recreational and Utility Trailers, Camp Dealers",
            "combined_description": "Recreational and Utility Trailers, Camp Dealers",
            "russian_name": "Дома- автоприцепы, жилые неразборные и грузовые прицепы",
            "russian_description": "Торговые точки, продающие новые и подержанные дома-автоприцепы, прицепы для отдыха и грузовые прицепы. Сюда относятся: жилые неразборные прицепы, прицепы с откидным верхом,    сопутствующие запчасти и аксессуары."
        },
        {
            "mcc": 5571,
            "edited_description": "Motorcycle Dealers",
            "combined_description": "Motorcycle Dealers",
            "russian_name": "Продажа мотоциклов",
            "russian_description": "Торговые точки, продающие новые и подержанные мотоциклы, скутеры, мопеды, сопутствующие запчасти, оборудование и аксессуары. В отдельных случаях здесь также могут продаваться: шлемы, одежда для мотоциклистов – куртки, брюки, головные уборы и перчатки."
        },
        {
            "mcc": 5592,
            "edited_description": "Motor Home Dealers",
            "combined_description": "Motor Home Dealers",
            "russian_name": "Продажа домов на колесах",
            "russian_description": "Торговые точки, продающие новые и подержанные дома на колесах и сопутствующие запчасти и аксессуары. \nДля домов-автоприцепов и жилых неразборных прицепов используется МСС 5561."
        },
        {
            "mcc": 5598,
            "edited_description": "Snowmobile Dealers",
            "combined_description": "Snowmobile Dealers",
            "russian_name": "Продажа снегоходов",
            "russian_description": "Используется исключительно для торговых точек, продающих новые и подержанные снегоходы, сопутствующие запчасти и аксессуары."
        },
        {
            "mcc": 5599,
            "edited_description": "Miscellaneous Auto Dealers ",
            "combined_description": "Miscellaneous Auto Dealers ",
            "russian_name": "Продажа различного рода автомобилей, авиа- и с/х оборудования - нигде более не классифицированные",
            "russian_description": "Торговые точки, занимающиеся продажей новых и б/у автомобилей, авиасредств и с/х техники, запчастей к ним, оборудования и  сопутствующих товаров. На продажу здесь могут выставляться вездеходы, багги с широкопрофильными шинами, миниавтомобили для гольфа, легкие открытые коляски, снегоходы, тракторы, комбайны и уборочные машины"
        },
        {
            "mcc": 5611,
            "edited_description": "Men’s and Boy’s Clothing and Accessories Stores",
            "combined_description": "Men’s and Boy’s Clothing and Accessories Stores",
            "russian_name": "Мужская одежда и аксессуары, включая одежду для мальчиков",
            "russian_description": "Продажа готовой мужской одежды и аксессуаров, включая одежду для мальчиков. Сюда также относятся торговые точки, занимающиеся продажей галстуков, и магазины головных уборов"
        },
        {
            "mcc": 5621,
            "edited_description": "Women’s Ready-to-Wear Stores",
            "combined_description": "Women’s Ready-to-Wear Stores",
            "russian_name": "Готовая женская одежда",
            "russian_description": "Продажа разнообразной готовой одежды для женщин, например, платьев, брюк, костюмов и пальто. Сюда относятся и магазины, специализирующиеся на продаже свадебных платьев или одежды для беременных."
        },
        {
            "mcc": 5631,
            "edited_description": "Women’s Accessory and Specialty Shops",
            "combined_description": "Women’s Accessory and Specialty Shops",
            "russian_name": "Аксессуары для женщин",
            "russian_description": "Продажа различных женских аксессуаров, включая сумочки, головные уборы, дешевые украшения, шарфы, пояса, заколки для волос и береты, белье, колготки и чулки."
        },
        {
            "mcc": 5641,
            "edited_description": "Children’s and Infant’s Wear Stores",
            "combined_description": "Children’s and Infant’s Wear Stores",
            "russian_name": "Детская одежда, включая одежду для самых маленьких",
            "russian_description": "Продажа детской одежды, принадлежностей и аксессуаров."
        },
        {
            "mcc": 5651,
            "edited_description": "Family Clothing Stores",
            "combined_description": "Family Clothing Stores",
            "russian_name": "Одежда для всей семьи",
            "russian_description": "Торговые точки, занимающиеся продажей мужской, женской и детской одежды, принадлежностей и аксессуаров, не специализируясь на конкретной половой или возрастной категории. Сюда же относятся магазины джинсовой или кожаной одежды и магазины одежды для мужчин  и женщин."
        },
        {
            "mcc": 5655,
            "edited_description": "Sports Apparel, Riding Apparel Stores",
            "combined_description": "Sports Apparel, Riding Apparel Stores",
            "russian_name": "Спортивная одежда, одежда для верховой езды и езды на мотоцикле",
            "russian_description": "Продажа одежды для людей, ведущих активный образ жизни, одежды для занятий спортом, легкой атлетикой, верховой ездой или для езды на мотоцикле. Такие торговые точки могут специализироваться на одежде для верховой езды, одежде ковбойского стиля, одежде для езды на мотоцикле или мотокросса и могут также выставлять на продажу спортивную обувь и ковбойские сапоги."
        },
        {
            "mcc": 5661,
            "edited_description": "Shoe Stores",
            "combined_description": "Shoe Stores",
            "russian_name": "Обувные магазины",
            "russian_description": "Продажа мужской, женской и детской обуви, включая спортивную обувь. В таких магазинах часто также продаются в ограниченном ассортименте сумки, носки, декоративные элементы для обуви, крем для обуви, перчатки и чулочные изделия."
        },
        {
            "mcc": 5681,
            "edited_description": "Furriers and Fur Shops",
            "combined_description": "Furriers and Fur Shops",
            "russian_name": "Изготовление и продажа меховых изделий",
            "russian_description": "Продажа  в розницу разнообразных изделий из натурального меха, включая шубы, куртки, головные уборы и перчатки."
        },
        {
            "mcc": 5691,
            "edited_description": "Men’s and Women’s Clothing Stores",
            "combined_description": "Men’s and Women’s Clothing Stores",
            "russian_name": "Магазины мужской и женской одежды",
            "russian_description": "Продажа мужской и женской одежды и аксессуаров. Эти торговые точки не занимаются продажей детской одежды."
        },
        {
            "mcc": 5697,
            "edited_description": "Tailors, Seamstress, Mending, and Alterations",
            "combined_description": "Tailors, Seamstress, Mending, and Alterations",
            "russian_name": "Услуги по переделке, починке и пошиву одежды",
            "russian_description": "Выполнение и продажа одежды по индивидуальным заказам, переделка, починка.  Сюда относятся также торговые точки, которые специализируются на восстановлении старинной одежды и создании оригинальных костюмов."
        },
        {
            "mcc": 5698,
            "edited_description": "Wig and Toupee Stores",
            "combined_description": "Wig and Toupee Stores",
            "russian_name": "Парики и накладки из искусственных волос",
            "russian_description": "Продажа накладок постоянного или временного ношения, париков, фальшивых локонов и искусственных прядей для мужчин и женщин, сюда относятся также торговые точки, предоставляющие услуги по завивке. \nДля торговых точек, которые предоставляют услуги по наращиванию волос, требующие хирургического вмешательства, используется MCC 8099."
        },
        {
            "mcc": 5699,
            "edited_description": "Miscellaneous Apparel and Accessory Shops",
            "combined_description": "Miscellaneous Apparel and Accessory Shops",
            "russian_name": "Различные магазины одежды и аксессуаров",
            "russian_description": "Продажа специализированной одежды (кроме изделий из меха) и аксессуаров, не классифицированных ранее. Сюда, например, относятся торговые точки, специализирующиеся на продаже теннисок, форменной одежды, купальных костюмов. Для торговых точек, специализирующихся на меховых изделиях, используется MCC 5681."
        },
        {
            "mcc": 5712,
            "edited_description": "Furniture, Home Furnishings, and Equipment Stores, ExceptAppliances",
            "combined_description": "Furniture, Home Furnishings, and Equipment Stores, ExceptAppliances",
            "russian_name": "Оборудование, мебель и бытовые принадлежности (кроме электрооборудования)",
            "russian_description": "Торговые точки, занимающиеся продажей бытовых принадлежностей, предлагающие широкий выбор мебели для дома и аксессуаров. Сюда относятся постельные принадлежности и матрацы, мебель для столовой и гостиной, обстановка для веранды или патио, для детской комнаты, а также светильники, коврики и занавески. Такие торговые точки могут заниматься продажей электроприборов в ограниченном ассортименте (например, телевизоров, стерео- и видеомагнитофонов.). \nДля торговых точек, специализирующихся только на продаже электрооборудования, используется MCC 5732."
        },
        {
            "mcc": 5713,
            "edited_description": "Floor Covering Stores",
            "combined_description": "Floor Covering Stores",
            "russian_name": "Покрытия для пола",
            "russian_description": "Продажа различных покрытий для пола, таких как ковры и ковровые покрытия, плитка для пола, линолеум, камень, паркет или кирпичи. Такие торговые точки могут также предоставлять услуге по установке. \nДля торговых точек, занимающихся исключительно установкой, используется MCC 1799."
        },
        {
            "mcc": 5714,
            "edited_description": "Drapery, Window Covering and Upholstery Stores",
            "combined_description": "Drapery, Window Covering and Upholstery Stores",
            "russian_name": "Ткани, обивочный материал, гардины и портьеры, жалюзи",
            "russian_description": "Продажа тканей, занавесей, жалюзи, штор и обивочного материала. \nДля торговых точек, преимущественно занимающихся обивкой или починкой мебели, используется MCC 7641."
        },
        {
            "mcc": 5718,
            "edited_description": "Fireplace, Fireplace Screens, and Accessories Stores",
            "combined_description": "Fireplace, Fireplace Screens, and Accessories Stores",
            "russian_name": "Продажа каминов, экранов для каминов и аксессуаров",
            "russian_description": "Торговые точки, продающие камины, деревянные печи, отдельные части каминов и аксессуары, такие как инструменты и экраны для каминов. \nДля подрядчиков, выполняющих каменную кладку и установку каминов используется МСС 1740."
        },
        {
            "mcc": 5719,
            "edited_description": "Miscellaneous Home Furnishing Specialty Stores",
            "combined_description": "Miscellaneous Home Furnishing Specialty Stores",
            "russian_name": "Различные специализированные магазины бытовых принадлежностей",
            "russian_description": "Торговые точки, продающие различные бытовые принадлежности. Сюда относятся: посуда, кухонные ножи, постельное белье и принадлежности, лампы и абажуры, зеркала, картины, гончарные и керамические изделия. \nДля торговцев изделиями из стекла и хрусталя используется МСС 5950."
        },
        {
            "mcc": 5722,
            "edited_description": "Household Appliance Stores",
            "combined_description": "Household Appliance Stores",
            "russian_name": "Бытовое оборудование",
            "russian_description": "Торговые точки, продающие бытовое оборудование. Сюда относятся: газовые или электрические печи и плиты, духовки, холодильники, посудомоечные машины, водонагреватели, стиральные машины, сушилки, корзины для мусора, швейные машинки, автономные кондиционеры и пылесосы. Такие торговцы могут выполнять также ремонтные работы. \nДля торговцев, занимающихся преимущественно ремонтом, используются МСС 7623."
        },
        {
            "mcc": 5732,
            "edited_description": "Electronic Sales",
            "combined_description": "Electronic Sales",
            "russian_name": "Продажа электронного оборудования",
            "russian_description": "Торговые точки, продающие широкий спектр электронного оборудования, а также отдельных частей и аксессуаров для ремонта, сборки или монтажа электронного оборудования. Могут также выполнять ремонтные работы. Товары для продажи включают в себя: телевизоры, радио, кассетные видеомагнитофоны, видеокамеры и стереосистемы.\nДля торговых точек, занимающихся исключительно ремонтом электроники, используется МСС 7622."
        },
        {
            "mcc": 5733,
            "edited_description": "Music Stores, Musical Instruments, Piano Sheet Music",
            "combined_description": "Music Stores, Musical Instruments, Piano Sheet Music",
            "russian_name": "Продажа музыкальных инструментов, фортепиано, нот.",
            "russian_description": "Торговые точки, продающие музыкальные инструменты, ноты, электромузыкальные клавишные инструменты, самоучители, пианино, гитары, сопутствующие товары и оборудование; могут также предлагать музыкальные консультации. Для магазинов, осуществляющих в основном музыкальные консультации, используется МСС 8299."
        },
        {
            "mcc": 5734,
            "edited_description": "Computer Software Stores",
            "combined_description": "Computer Software Stores",
            "russian_name": "Продажа компьютерного программного обеспечения",
            "russian_description": "Торговые точки, продающие компьютерные программы для делового и личного пользования и могут продавать или передавать в лизинг ограниченный ассортимент компьютерного оборудования и других сопутствующих товаров. \nДля преимущественной продажи и лизинга компьютерной техники и электроники используется МСС 5732. \nДля торговых точек, предоставляющих услуги по обработке данных и консалтингу, используется МСС 7372."
        },
        {
            "mcc": 5735,
            "edited_description": "Record Shops",
            "combined_description": "Record Shops",
            "russian_name": "Магазины звукозаписи",
            "russian_description": "Торговые точки, продающие пластинки, компакт диски (СD), кассеты, музыкальные и видео лазерные диски, чистые аудио- и видеокассеты, а также занимающиеся прокатом видеокассет. \nДля торговых точек, занимающихся преимущественно прокатом видеокассет, используется МСС 7841."
        },
        {
            "mcc": 5811,
            "edited_description": "Caterers",
            "combined_description": "Caterers",
            "russian_name": "Поставщики провизии",
            "russian_description": "Торговые точки, занимающиеся приготовлением и доставкой (обычно по конкретному адресу) еды и напитков для немедленного потребления. Поставщики таких услуг также могут или не могут предоставлять услуги по очистке, столы, обслуживающее оборудование, украшения и персонал для обслуживания и уборки на месте.\nДля ресторанов, которые в основном подают питание для потребления в помещениях, а также предоставляют услуги общественного питания, используется MCC 5812."
        },
        {
            "mcc": 5812,
            "edited_description": "Eating places and Restaurants",
            "combined_description": "Eating places and Restaurants",
            "russian_name": "Места общественного питания, рестораны",
            "russian_description": "Торговые точки, занимающиеся приготовлением еды и напитков для немедленного потребления, обычно на заказ. Могут оказывать услуги по обслуживанию столиков официантами. Места общественного питания включают в себя: кафе, кафетерии, грили, кофейни, закусочные, охлаждаемые прилавки для продажи мороженого и напитков, пиццерии, столовые, магазины деликатесов, бистро.\n\nДля точек, продающих еду быстрого приготовления, используется МСС 5814.  Для точек, торгующих алкогольными напитками на заказ, используется МСС 5813."
        },
        {
            "mcc": 5813,
            "edited_description": "Drinking Places (Alcoholic Beverages), Bars, Taverns, Cocktail lounges, Nightclubs and Discotheques",
            "combined_description": "Drinking Places (Alcoholic Beverages), Bars, Taverns, Cocktail lounges, Nightclubs and Discotheques",
            "russian_name": "Бары, коктейль-бары, дискотеки, ночные клубы и таверны – места продажи алкогольных напитков",
            "russian_description": "Торговые точки, продающие алкогольные напитки, такие как вино, пиво, эль, смешанные напитки и другие ликеры и напитки для потребления на заказ. Места продажи алкогольных напитков включают в себя: бары, пивные, пабы, коктейль-бары, дискотеки, ночные клубы, таверны и винные бары."
        },
        {
            "mcc": 5814,
            "edited_description": "Fast Food Restaurants",
            "combined_description": "Fast Food Restaurants",
            "russian_name": "Фастфуд",
            "russian_description": "Торговые точки, продающие готовую еду и напитки для немедленного потребления, как на заказ, так и упакованную на вынос. Такие рестораны могут использовать мак-драйв для приема и выдачи заказов и обычно не предоставляют услуги по обслуживанию столиков официантами и не берут чаевые. Эти торговые точки обычно не продают алкогольные напитки."
        },
        {
            "mcc": 5815,
            "edited_description": "Digital Goods: Media, Books, Movies, Music",
            "combined_description": "null",
            "russian_name": "Цифровые товары - аудиовизуальные медиа, включая книги, фильмы и музыку",
            "russian_description": "Точки, которые продают аудиовизуальные произведения держателю карты в цифровом формате. Такие работы предоставляются посредством электронной передачи (например, скачивание или потоковая передача) и включают в себя, например, аудиокниги, музыкальные файлы, рингтоны, фильмы, видеозаписи, живые или записанные события, цифровые периодические издания или журналы, цифровые фотографии, цифровые презентации, а также новости и развлекательные программы."
        },
        {
            "mcc": 5816,
            "edited_description": "Digital Goods: Games",
            "combined_description": "null",
            "russian_name": "Цифровые товары – игры",
            "russian_description": "Торговые точки, которые разрабатывают видео- или электронные игры для игр на смартфонах, оснащены телефонами, персональными компьютерами, планшетами, консолями или другими устройствами с сетевыми возможностями. Такие игры могут предоставлять платформы для совершения покупок электронных или виртуальных предметов in-app для использования во время игры, включая, помимо прочего, игровые элементы, жетоны, очки или другие формы игровой ценности."
        },
        {
            "mcc": 5817,
            "edited_description": "Digital Goods: Applications (Excludes Games)",
            "combined_description": "null",
            "russian_name": "Цифровые товары - приложения (кроме игр)",
            "russian_description": "Точки, которые продают предварительно написанные программные приложения, доступные держателю карты через удаленный доступ (например, сервер) или скачиваемые.\nДля игр используется MCC 5816."
        },
        {
            "mcc": 5818,
            "edited_description": "Digital Goods: Large Digital Goods Merchant",
            "combined_description": "null",
            "russian_name": "Цифровые товары - мультикатегория",
            "russian_description": "Точки, которые продают по крайней мере два из следующих указанных цифровых продуктов:\n- MCC 5815 (аудиовизуальные медиа, включая книги, фильмы и музыку)\n- MCC 5816 (игры)\n- MCC 5817 (приложения, исключая игры)\nЦифровой товар передается электронным путем покупателю и получен с помощью иных средств, чем материальные носители."
        },
        {
            "mcc": 5832,
            "edited_description": "Antique Shops – Sales, Repairs, and Restoration Services",
            "combined_description": "Antique Shops – Sales, Repairs, and Restoration Services",
            "russian_name": "null",
            "russian_description": "null"
        },
        {
            "mcc": 5912,
            "edited_description": "Drug Stores and Pharmacies",
            "combined_description": "Drug Stores and Pharmacies",
            "russian_name": "Аптеки",
            "russian_description": "Точки, которые продают лекарственные средства, отпускаемые по рецепту и запатентованному препарату, и лекарства без рецепта (внебиржевые). В аптеках также могут продаваться сопутствующие товары и изделия из него, такие как косметика, туалетные принадлежности, табак, грелки, задние опоры, товары для новинок, открытки и некоторый запас продуктов питания. Продавцы напитков и закусочные в аптеках также должны использовать этот MCC."
        },
        {
            "mcc": 5921,
            "edited_description": "Package Stores – Beer, Wine, and Liquor",
            "combined_description": "Package Stores – Beer, Wine, and Liquor",
            "russian_name": "Магазины с продажей спиртных напитков навынос",
            "russian_description": "Точки, которые продают упакованные алкогольные напитки, такие как эль, пиво, вино и ликер для потребления вне помещений. Такие точки могут или не могут также продавать ограниченное количество закусок, газет и журналов, а также туалетные принадлежности и лекарства без рецепта.\nДля точек, которые продают ликер для потребления в помещениях, используйте MCC 5813."
        },
        {
            "mcc": 5931,
            "edited_description": "Used Merchandise and Secondhand Stores",
            "combined_description": "Used Merchandise and Secondhand Stores",
            "russian_name": "Секонд-хенды, магазины б/у товаров, комиссионки",
            "russian_description": "Точки, которые продают использованные или подержанные товары. Товары для продажи могут включать аксессуары, обувь и одежду, мебель, книги, велосипеды, музыкальные инструменты, швейные машины, электронное оборудование, приборы и другие предметы домашнего обихода. Как правило, предметы для продажи были пожертвованы или отправлены на консигнацию. Такие точки могут или не могут также продавать антиквариат.\nДля точек, которые в основном продают антиквариат, используется MCC 5932. \nДля ломбардов используется MCC 5933."
        },
        {
            "mcc": 5932,
            "edited_description": "Antique Shops",
            "combined_description": "Antique Shops",
            "russian_name": "Антикварные магазины – продажа, ремонт и услуги реставрации",
            "russian_description": "Точки, которые продают антиквариат и могут или не могут также выполнять некоторые ремонтные или реставрационные работы. Товары для продажи могут включать мебель, ювелирные изделия, камеры и фотооборудование, инструменты, произведения искусства, книги, бытовую технику и другие предметы домашнего обихода.\nДля точек, продающих старинные автомобили, используется MCC 5521.\nДля точек, которые в основном ремонтируют или восстанавливают антикварную мебель, используется MCC 7641."
        },
        {
            "mcc": 5933,
            "edited_description": "Pawn Shops and Salvage Yards",
            "combined_description": "Pawn Shops and Salvage Yards",
            "russian_name": "Ломбарды",
            "russian_description": "Точки, которые одалживают деньги в обмен на личную собственность, которая остается в точке в качестве обеспечения. Ломбарды могут после невозврата займа продавать собственность широкой публике. Собственность, оставленная в качестве обеспечения, может включать такие предметы, как ювелирные изделия, часы, музыкальные инструменты, велосипеды, мебель, монеты, камеры и фотооборудование."
        },
        {
            "mcc": 5935,
            "edited_description": "Wrecking and Salvage Yards",
            "combined_description": "Wrecking and Salvage Yards",
            "russian_name": "Уничтожение и сбор остатков",
            "russian_description": "Точки, которые предоставляют услуги по уничтожению и сбору остатков транспортных средств, оборудования и других предметов. Такие точки могут или не могут предоставлять услуги по доставке и буксировке.\nДля точек, которые в основном предоставляют услуги буксировки, используется MCC 7549."
        },
        {
            "mcc": 5937,
            "edited_description": "Antique Reproductions",
            "combined_description": "Antique Reproductions",
            "russian_name": "Магазины репродукций и антиквариата",
            "russian_description": "Точки, которые продают антикварные репродукции или факсимиле - точные копии. Товары для продажи могут включать одежду, мебель, ковры, картины и произведения искусства, зеркала, изделия из стекла, ювелирные изделия и другие предметы домашнего обихода и предметы личной гигиены. Такие точки могут также предоставлять услуги по воспроизведению и восстановлению старинных фонографов.\nДля точек, которые продают добросовестный (\"bona fide\") антиквариат, используется MCC 5932."
        },
        {
            "mcc": 5940,
            "edited_description": "Bicycle Shops – Sales and Service",
            "combined_description": "Bicycle Shops – Sales and Service",
            "russian_name": "Веломагазины – продажа и обслуживание",
            "russian_description": "Точки, которые продают велосипеды, детали и аксессуары. Веломагазины могут также продавать ограниченное разнообразие спортивной одежды, а также могут или не могут также проводить ремонтные работы или давать велосипеды в аренду.\nДля торговцев, которые в основном ремонтируют велосипеды, используйте MCC 7699. Для торговцев, которые в основном дают велосипеды в аренду, используйте MCC 7999."
        },
        {
            "mcc": 5941,
            "edited_description": "Sporting Goods Stores",
            "combined_description": "Sporting Goods Stores",
            "russian_name": "Спорттовары",
            "russian_description": "Торговые точки, торгующие спортивными товарами, спортивным инвентарем и сопутствующими частями и аксессуарами. В продажу могут входить скейтборды, водные лыжи, роликовые коньки, доски для серфинга, оборудование для гольфа, снежные лыжи, виндсерфинг, дайвинг и подводное снаряжение, приманка и снасти, альпинизм, кемпинг, пешеходное и альпинистское снаряжение, оборудование для тренировок, бильярдные столы, теннис оборудование, оборудование и принадлежности для боулинга, оборудование для охоты и снаряжения, оборудование для игровых площадок. Магазины спортивных товаров могут или не могут также проводить ремонтные работы или арендовать спортивное снаряжение.\nДля торговцев, которые в основном проводят ремонтные работы, используется MCC 7699.\nДля торговцев, которые в основном дают спортивное оборудование в аренду, используется MCC 7999."
        },
        {
            "mcc": 5942,
            "edited_description": "Book Stores",
            "combined_description": "Book Stores",
            "russian_name": "Книжные магазины",
            "russian_description": "Торговые точки, которые продают новые или б/у книги, журналы, учебники, карты и атласы, аудиокниги и календари. Этот MCC также включает в себя религиозные книжные магазины."
        },
        {
            "mcc": 5943,
            "edited_description": "Stationery Stores, Office and School Supply Stores",
            "combined_description": "Stationery Stores, Office and School Supply Stores",
            "russian_name": "Магазины офисных, школьных принадлежностей, канцтоваров",
            "russian_description": "Торговцы, которые продают различные офисные и школьные принадлежности и бумажные товары. Товары для продажи могут включать в себя ручки, карандаши, календари, настольные органайзеры, степлеры, папки с файлами, бумагу для бумаг, портфели, почтовые ящики, маркеры, компьютерные дискеты, чернильные картриджи для компьютерных принтеров, ограниченный набор программного обеспечения для компьютеров и малое офисное оборудование, такое как офисные шкафы, стулья, мусорные корзины и настольные лампы. Такие торговые точки дополнительно продают большое или дорогостоящее офисное оборудование, такое как компьютеры или настольные компьютеры.\nДля торговых точек, которые в основном продают компьютерное оборудование, используется MCC 5732.\nДля торговых точек, которые в основном продают компьютерное программное обеспечение, используется MCC 5734."
        },
        {
            "mcc": 5944,
            "edited_description": "Watch, Clock, Jewelry, and Silverware Stores",
            "combined_description": "Watch, Clock, Jewelry, and Silverware Stores",
            "russian_name": "Часы, ювелирные и серебряные изделия",
            "russian_description": "Торговые точки, которые продают часы и ручные часы; драгоценные металлы; мелкие ювелирные изделия, такие как алмазы или другие драгоценные камни, смонтированные в драгоценных металлах; и стерлингового серебра и покрытых столовых приборов и аксессуаров, таких как тарелки, сервировочные чаши, триплеты и кувшины. Такие торговые точки могут также проводить ремонтные работы.\nДля торговых точек, которые в основном ремонтируют ювелирные изделия, часы или часы, используется MCC 7699.\nДля торговых точек, которые в основном продают фарфор или кристалл, используется MCC 5950."
        },
        {
            "mcc": 5945,
            "edited_description": "Hobby, Toy, and Game Shops",
            "combined_description": "Hobby, Toy, and Game Shops",
            "russian_name": "Игрушки, игры и хобби-товары",
            "russian_description": "Торговые точки, которые продают игрушки и игры, и могут продавать ограниченный выбор самодельных ремесел или наборов для хобби.\nДля торговых точек, которые в основном продают ресурсы, материалы и оборудование, используемые для сборки ремесел, используется MCC 5970."
        },
        {
            "mcc": 5946,
            "edited_description": "Camera and Photographic Supply Stores",
            "combined_description": "Camera and Photographic Supply Stores",
            "russian_name": "Магазины фотооборудования и фотоприборов",
            "russian_description": "Торговые точки, которые специализируются на продаже фотоаппаратов, плёнки, видео и другого фотооборудования и расходных материалов, включая химикаты для обработки и бумагу. Такие торговые точки могут или не могут также предоставлять услуги по обработке фильмов.\nДля торговых точек, которые продают камеры и видеооборудование в дополнение к множеству других электронных устройств, таких как видеомагнитофоны, телевизоры и стереосистемы, используется MCC 5732.\nДля торговых точек, которые в первую очередь предоставляют услуги по обработке и печати фильмов, используется MCC 7395."
        },
        {
            "mcc": 5947,
            "edited_description": "Card Shops, Gift, Novelty, and Souvenir Shops",
            "combined_description": "Card Shops, Gift, Novelty, and Souvenir Shops",
            "russian_name": "Магазины открыток, подарков, новинок и сувениров",
            "russian_description": "Торговые точки, которые продают подарки и новинки, поздравительные открытки, воздушные шары, сувениры, праздничные украшения, канцелярские принадлежности, оберточные бумаги и банты, фотоальбомы и ограниченный набор канцелярских принадлежностей, таких как ручки, ноутбуки и календари.\nДля торговых точек, которые в основном продают офисные и школьные принадлежности, используется MCC 5943."
        },
        {
            "mcc": 5948,
            "edited_description": "Leather Goods Stores",
            "combined_description": "Leather Goods Stores",
            "russian_name": "Магазины кожаных изделий, дорожных принадлежностей",
            "russian_description": "Торговцы, которые продают дорожные сумки, сундуки, портфели, кожаные рюкзаки, кошельки, бумажники, перчатки и другие изделия из кожи, и могут продавать ограниченный выбор кожаной одежды."
        },
        {
            "mcc": 5949,
            "edited_description": "Sewing, Needle, Fabric, and Price Goods Stores",
            "combined_description": "Sewing, Needle, Fabric, and Price Goods Stores",
            "russian_name": "Магазины ткани, ниток, рукоделия, шитья",
            "russian_description": "Торговые точки, которые продают ткани, выкройки, пряжу и другие материалы для шитья и рукоделия такие как нитки, пуговицы, заклепки, подкладочная ткань, шнурки, отделки, ножницы, кружева и застежки-молнии. Такие торговые точки могут также предлагать консультации по шитью.\nДля торговых точек, которые прежде всего предлагают инструкции по шитью и вязанию, используется МСС 8299."
        },
        {
            "mcc": 5950,
            "edited_description": "Glassware/Crystal Stores",
            "combined_description": "Glassware/Crystal Stores",
            "russian_name": "Магазины хрусталя и изделий из стекла",
            "russian_description": "Торговые точки, которые продают посуду, фарфор и хрусталь для сервировки стола (например, бокалы с вином и шампанским, сервировочные чаши и тарелки), а также подарочные изделия (например, статуэтки, подставки для книг, цветочные вазы, шкатулки для драгоценностей и подсвечники)."
        },
        {
            "mcc": 5960,
            "edited_description": "Direct Marketing- Insurance Service",
            "combined_description": "Direct Marketing- Insurance Service",
            "russian_name": "Прямой маркетинг – страховые услуги",
            "russian_description": "Торговые точки, которые продают страховые услуги через прямую почтовую рассылку, накладные выписки по счетам, а также журналы или телевизионные объявления, все из которых включают либо бесплатный номер телефона, либо адрес или веб-сайт, на который потенциальные клиенты могут ответить. Предлагаемые страховые услуги могут включать все формы страхования жизни, страхование от страхового возмещения (дополнительное покрытие, обычно оплачиваемое непосредственно потребителю), страхование от случайной смерти и разделения, страхование по кредитным картам, в которых непогашенный остаток застрахован от смерти, инвалидности или страхования по безработице, и медицинская страховка для путешественников. Продажи могут быть нацелены на специальные группы, такие как ветераны, пенсионеры, школьные учителя или члены определенных организаций. Биллинг страховых премий обычно происходит в периодических (ежемесячных, ежеквартальных или годовых) взносах и продолжается до тех пор, пока не будет отменен держателем карты или страховой компанией. Еще одна общая особенность - бесплатный пробный период в 60 или 90 дней с выставлением счета первой партии после окончания пробного периода.\nДля личных услуг по страхованию и гарантированию используется MCC 6300."
        },
        {
            "mcc": 5961,
            "edited_description": "Mail Order Houses Including Catalog Order Stores, Book/Record Clubs (No longer permitted for U.S. original presentments)",
            "combined_description": "Mail Order Houses Including Catalog Order Stores, Book/Record Clubs (No longer permitted for U.S. original presentments)",
            "russian_name": "Заказы по почте, включая заказы по каталогу",
            "russian_description": "MCC отсутствует в справочниках, найдено в справочниках SIC кодов"
        },
        {
            "mcc": 5962,
            "edited_description": "Direct Marketing – Travel Related Arrangements Services",
            "combined_description": "Direct Marketing – Travel Related Arrangements Services",
            "russian_name": "Прямой маркетинг – услуги, относящиеся к туризму",
            "russian_description": "Торговые точки, которые продают услуги по организации поездок с помощью исходящего телемаркетинга, в которых продавец начинает контактировать с потребителем посредством прямой почты, рекламы или других методов прямого маркетинга, требующих ответа потребителей, в попытке произвести продажу. Также включены дисконтные туристические клубы и подписные услуги или информационные бюллетени, из которых подписчики выбирают расфасованные поездки; для них часто требуется ежегодный членский взнос, который может быть выставлен счету держателя карты каждый год, пока он не будет отменен владельцем карты или торговцем.\nДля турагентов и туроператоров используется MCC 4722."
        },
        {
            "mcc": 5963,
            "edited_description": "Door-to-Door Sales",
            "combined_description": "Door-to-Door Sales",
            "russian_name": "Продажа \"от двери до двери\"",
            "russian_description": "Продавцы, которые продают товары \"от двери до двери\" или из грузовых автомобилей или вагонов или других временных мест. Товары, продаваемые от двери до двери, могут включать косметику, предметы домашнего обихода, хлебобулочные изделия, молочные продукты и подписки на журналы."
        },
        {
            "mcc": 5964,
            "edited_description": "Direct Marketing – Catalog Merchant",
            "combined_description": "Direct Marketing – Catalog Merchant",
            "russian_name": "Прямой маркетинг – торговля по каталогам",
            "russian_description": "Торговые точки, которые инициируют прямой контакт с потребителями и часто описываются как дома заказов по почте или как индустрия \"товары почтой\". Такие торговые точки предлагают свои товары через каталоги и принимают заказы на товары исключительно по электронной почте, телефону, факсу, электронной торговле или другим методам, не предусматривающих личный контакт. Бумажный каталог - это многостраничный документ, который отправляется по почте, факсом и т.п. непосредственно потребителю. Электронный каталог отображает товар через кабельное телевидение или видеотекст на интернет-сайте. Каталоги отображают и описывают товар и включают в себя форму заказа по почте, номер телефона или адрес интернет-сайта для размещения заказов.\nЛистовки и брошюры не считаются каталогами.\nПроизводитель с прайс-листом не считается продавцом по каталогу."
        },
        {
            "mcc": 5965,
            "edited_description": "Direct Marketing – Catalog and Catalog and Retail Merchant",
            "combined_description": "Direct Marketing – Catalog and Catalog and Retail Merchant",
            "russian_name": "Прямой маркетинг – комбинированный каталог и розничные продавцы",
            "russian_description": "Продавцы, которые также работают с одним или несколькими розничными точками. Этот MCC используется только для транзакций, происходящих по почте, телефону, электронной коммерции или другим не предусматривающим личного контакта с покупателем, даже если товар доставляется в магазин для самовывоза.\nВ этом MCC исключаются личные продажи, в том числе те, в которых заказ помещен на стол каталога или где-либо еще в магазине в ответ на каталог или другое сообщение прямых продаж.\nВсе розничные продажи должны проходить с соответствующим розничным MCC."
        },
        {
            "mcc": 5966,
            "edited_description": "Direct Marketing- Outbound Telemarketing Merchant",
            "combined_description": "Direct Marketing- Outbound Telemarketing Merchant",
            "russian_name": "Прямой маркетинг - исходящий телемаркетинг",
            "russian_description": "Торговцы, которые инициируют прямые контакты с потребителями для продажи товаров и услуг. Поставщики исходящих телемаркетингов связываются (а иногда и стимулируют) с потенциальным покупателем по телефону, рекламе, прямой почте (кроме каталога) или другому методу прямого маркетинга, который включает либо бесплатный номер телефона, либо почтовый адрес. Товары, рекламируемые и продаваемые с помощью таких методов, могут включать косметику, продукты медицинского назначения, витамины и недвижимость с долевым сроком.\nДля благотворительных организаций, которые запрашивают взносы любыми способами, в том числе через исходящий телемаркетинг, используется MCC 8398."
        },
        {
            "mcc": 5967,
            "edited_description": "Direct Marketing – Inbound Teleservices Merchant",
            "combined_description": "Direct Marketing – Inbound Teleservices Merchant",
            "russian_name": "Прямой маркетинг – входящий телемаркетинг",
            "russian_description": "Торговцы, которые предоставляют одну или несколько служб аудиотекста или видеотекста, к которым можно получить доступ по телефону, факсу или по Интернету. Владелец карты инициирует контакт с торговцем и все последующие транзакции. Этот MCC применяется к информационным услугам, предлагаемым по телефону или в Интернете, а также к товарам, которые могут быть проданы через такие службы. Информационные услуги предоставляются за вознаграждение и могут включать в себя опросы, лотереи, чаты для взрослых и развлечения, спортивные результаты, котировки на фондовом рынке, показания гороскопа или другие аудиотексты или видеотексты, которые потребители слушают, просматривают или участвуют в них.\nДля поставщиков электронного доступа к доске объявлений или онлайн-сервисам, предоставляемым через компьютеры, используется MCC 4816."
        },
        {
            "mcc": 5968,
            "edited_description": "Direct Marketing – Continuity/Subscription Merchant",
            "combined_description": "Direct Marketing – Continuity/Subscription Merchant",
            "russian_name": "Прямой маркетинг – Продажа по подписке",
            "russian_description": "Точки, которые продают продукты или услуги по подписке через прямую почтовую рассылку, телефон, интернет или другой метод прямого маркетинга, который включает в себя бесплатный номер, почтовый адрес, адрес электронной почты или URL-адрес веб-сайта. Такие точки могут предлагать серии продуктов (например, одну книгу в месяц на один год) или ежегодное обновление одного продукта. Счет владельцу карты выставляется за продукт или услугу на постоянной или периодической основе (например, один раз в месяц или два раза в год), а предоставление продукта или услуги продолжается до тех пор, пока не закончится подписка или серия, или владелец карты или продавец не расторгнет соглашение. Этот MCC включает в себя книжные клубы, подписку на журналы и газеты, аудиоклубы, продающие записи, кассеты и компакт-диски (CD), клубы с видеокассетами и цифровыми видеодисками (DVD), подписки на коллекционные серии (например, серии марок, монет, книг, таблички, фарфоровые рисунки или тарелки), подписки на журналы, подписки на продукты для здоровья, подписки на косметику, подписки на витамины."
        },
        {
            "mcc": 5969,
            "edited_description": "Direct Marketing – Not Elsewhere Classified",
            "combined_description": "Direct Marketing – Not Elsewhere Classified",
            "russian_name": "Прямой маркетинг – другие торговые точки прямого маркетинга (нигде более не классифицированные)",
            "russian_description": "Торговые точки, которые продают товары и услуги с помощью различных методов прямого ответа, в которых включена форма заказа или адрес или номер телефона для размещения заказа по почте, телефону или факсу. Эти торговцы часто используют методы массового маркетинга, такие как брошюры, объявления с прямым ответом на радио и телевидении, а также телевизионные «рекламные ролики» (рекламные ролики с расширенной длиной с форматом ток-шоу). Такие торговцы обычно предлагают только один или два продукта на рекламу, такие как кухонные столовые приборы, бытовые гаджеты, товары для снижения веса, спортивное оборудование, косметику, специальные записи или книги, которые доступны только через телевизионную рекламу. Это включает рекламу в газетах, продаваемую по методам прямого маркетинга.\nДля билетов, заказанных по телефону, но оплаченных в билетной кассе, используется MCC 7922.\nИсключаются розничные торговцы лицом к лицу, которые иногда принимают заказы на почту или телефон для удобства клиентов.\nДля розничных продаж, проводимых через интернет-сайт, используется наиболее подходящий розничный MCC с TCC T."
        },
        {
            "mcc": 5970,
            "edited_description": "Artist’s Supply and Craft Shops",
            "combined_description": "Artist’s Supply and Craft Shops",
            "russian_name": "Магазины художественных и ремесляных изделий",
            "russian_description": "Розничные торговцы которые продают материалы, оборудование, и  т.п., которое используется для создания художественных и ремесляных  изделий и т.п. вещей. Товары для распродажи  могут включать  все типы картин (живописи), краски, шелковые цветы, ручки, карандаши, бумагу, конструкторы для сборки, пряжу, штуковины для изготовления конфет, декоративные резиновые штампы, и.т.п. вещи. Для торговцев которые специализируются на продаже  ткани, выкроек, принадлежностей  для шитья, используют МСС 5949."
        },
        {
            "mcc": 5971,
            "edited_description": "Art Dealers and Galleries",
            "combined_description": "Art Dealers and Galleries",
            "russian_name": "Галереи и художественные посредники",
            "russian_description": "Розничные торговцы, которые продают  художественные работы, такие как картины, фотографии, скульптуры. Распродажа может проводиться  прямо с посредниками, художниками, в галереях."
        },
        {
            "mcc": 5972,
            "edited_description": "Stamp and Coin Stores – Philatelic and Numismatic Supplies",
            "combined_description": "Stamp and Coin Stores – Philatelic and Numismatic Supplies",
            "russian_name": "Магазины монет и марок (филателические и нумизматические)",
            "russian_description": "Розничные торговцы, которые продают почтовые марки, монеты и подобные аксессуары для коллекций или сбережений. \nДля распродажи почтовых марок (почта США), используется МСС 9402.\nДля почты и почтовых услуг, которые тоже используют почтовые марки, используется МСС 7399."
        },
        {
            "mcc": 5973,
            "edited_description": "Religious Goods Stores",
            "combined_description": "Religious Goods Stores",
            "russian_name": "Магазины религиозных товаров",
            "russian_description": "Розничные торговые точки, которые продают такие товары как статуэтки, открытки, религиозные штучки, иконы, картины, книги и кассеты,  декоративные  вещи. \nДля торговых точек, которые первоначально продают религиозные книги, используют МСС 5942."
        },
        {
            "mcc": 5975,
            "edited_description": "Hearing Aids – Sales, Service, and Supply Stores",
            "combined_description": "Hearing Aids – Sales, Service, and Supply Stores",
            "russian_name": "Слуховые аппараты – продажа, сервис, снабжение",
            "russian_description": "Розничные торговые точки, которые продают слуховые аппараты и связанные с ними материалы, а также могут или не могут также проводить ремонтные работы.\nДля точек, которые в основном проводят ремонтные работы, используйте MCC 7699."
        },
        {
            "mcc": 5976,
            "edited_description": "Orthopedic Goods Prosthetic Devices",
            "combined_description": "Orthopedic Goods Prosthetic Devices",
            "russian_name": "Ортопедические товары",
            "russian_description": "Розничные торговые точки, которые продают различные ортопедические товары, протезы и которые также могут заниматься их починкой. Товары для продажи могут включать костыли, палочки и др. вспомогательные детали для передвижения, эластичный трикотаж, абдоминальные поддержатели, обвязки, растяжки, инвалидные коляски, и т.п. \nДля торговых точек, которые первоначально занимаются починкой подобных товаров, используется МСС 7699."
        },
        {
            "mcc": 5977,
            "edited_description": "Cosmetic Stores",
            "combined_description": "Cosmetic Stores",
            "russian_name": "Магазины косметики",
            "russian_description": "Розничные торговые точки, которые продают натуральную или синтетическую косметику, в том числе театральный грим, медицинскую и повседневную косметику."
        },
        {
            "mcc": 5978,
            "edited_description": "Typewriter Stores – Sales, Rental, Service",
            "combined_description": "Typewriter Stores – Sales, Rental, Service",
            "russian_name": "Магазины печатающих устройств – аренда, продажа, услуги",
            "russian_description": "Розничные торговые точки, которые продают, сдают в аренду, разные печатающие устройства. Такие торговые точки могут также продавать ограниченный выбор офисных принадлежностей, канцтоваров, и могут проводить или не проводить починные работы. \nДля точек, которые в основном занимаются починкой подобных товаров, используется МСС 7699."
        },
        {
            "mcc": 5983,
            "edited_description": "Fuel – Fuel Oil, Wood, Coal, Liquefied Petroleum",
            "combined_description": "Fuel – Fuel Oil, Wood, Coal, Liquefied Petroleum",
            "russian_name": "Поставщики топлива – уголь, мазут, сжиженная нефть, древесина",
            "russian_description": "Розничные торговые точки, которые продают мазут, древесину, уголь, сжиженную нефть, авиационное топливо, топочный мазут или газ-пропан. Такие точки могут или не могут продавать бензин для потребительского использования в автомобилях.\nДля точек, которые в основном продают автомобильный бензин, используется MCC 5541 или MCC 5542, если это необходимо."
        },
        {
            "mcc": 5992,
            "edited_description": "Florists",
            "combined_description": "Florists",
            "russian_name": "Флористика",
            "russian_description": "Розничные торговые точки, которые продают обрезанные цветы, всякие цветочные приспособления, саженцы. Такие торговые точки могут  или не могут также продавать разные товары типа гелиумных воздушных шаров. Для торговцев, продающих первоначально семена, шары, парники, инвентарь, используют МСС 5261."
        },
        {
            "mcc": 5993,
            "edited_description": "Cigar Stores and Stands",
            "combined_description": "Cigar Stores and Stands",
            "russian_name": "Табачные магазины",
            "russian_description": "Розничные торговые точки, которые продают табак, сигареты, сигары, трубки и все курительные аксессуары."
        },
        {
            "mcc": 5994,
            "edited_description": "News Dealers and Newsstands",
            "combined_description": "News Dealers and Newsstands",
            "russian_name": "Дилеры по продаже печатной продукции",
            "russian_description": "Розничные торговые точки, которые продают газеты, журналы и другую периодику. \nДля подписки на газеты используется МСС 5968."
        },
        {
            "mcc": 5995,
            "edited_description": "Pet Shops, Pet Foods, and Supplies Stores",
            "combined_description": "Pet Shops, Pet Foods, and Supplies Stores",
            "russian_name": "Зоомагазины",
            "russian_description": "Розничные торговые точки, которые продают домашних питомцев (собачки, кошки, птички, рыбки, рептилии, хомячки, кролики), еду для них и все связанные с ними аксессуары."
        },
        {
            "mcc": 5996,
            "edited_description": "Swimming Pools – Sales, Service, and Supplies",
            "combined_description": "Swimming Pools – Sales, Service, and Supplies",
            "russian_name": "Плавательные бассейны – продажа и снабжение",
            "russian_description": "Розничные торговые точки, которые продают домашние бассейны (наземные или сборные надземные бассейны), курорты, гидромассажные ванны, гидромассажные ванны и принадлежности для бассейна. Такие точки могут или не могут также предоставлять услуги по установке и техническому обслуживанию.\nДля точек, которые в первую очередь предоставляют услуги по установке, используется MCC 1799. Эти торговцы также могут или не могут предоставлять услуги по ремонту.\nДля точек, которые в первую очередь предоставляют услуги по ремонту, используется MCC 7699."
        },
        {
            "mcc": 5997,
            "edited_description": "Electric Razor Stores – Sales and Service",
            "combined_description": "Electric Razor Stores – Sales and Service",
            "russian_name": "Магазины электрических бритвенных принадлежностей – распродажа и услуги.",
            "russian_description": "Розничные торговые точки, которые продают электрические бритвенные принадлежности, которые также могут или не могут предоставлять услуги по ремонту. \nДля торговых точек, которые изначально обеспечивают услугами по ремонту, используют МСС 7699."
        },
        {
            "mcc": 5998,
            "edited_description": "Tent and Awning Shops",
            "combined_description": "Tent and Awning Shops",
            "russian_name": "Магазины палаток и навесов",
            "russian_description": "Розничные точки, которые продают палатки и навесы для дома или бизнеса. Товары для продажи могут включать палатки для кемпинга, тентовые палатки и преднастроенные или изготовленные на заказ оконные или дверные тенты для дома или бизнеса. Такие точки могут или не могут также оказывать услуги по ремонту.\nДля точек, которые в первую очередь предоставляют услуги по ремонту, используется MCC 7699."
        },
        {
            "mcc": 5999,
            "edited_description": "Miscellaneous and Specialty Retail Stores",
            "combined_description": "Miscellaneous and Specialty Retail Stores",
            "russian_name": "Различные магазины и специальные розничные магазины",
            "russian_description": "Розничные торговые точки, которые продают уникальные или специализированные товары, которые не попадают ни под какое МСС описание. Этот МСС код должен быть использован только когда этот товар не подходит под другие МСС. Примерами могут послужить специальные магазины, которые торгуют картами и атласами, льдом, дистиллированной водой, аксессуары для магии, вечеринок, красоты, и т.п. вещи."
        },
        {
            "mcc": 6010,
            "edited_description": "Financial Institutions – Manual Cash Disbursements",
            "combined_description": "Financial Institutions – Manual Cash Disbursements",
            "russian_name": "Финансовые учреждения – выдача наличных в кассе",
            "russian_description": "Используется для определения транзакций лично, когда владелец карты использует карту в кассе, чтобы получить наличные.\n\nДля получение денежных средств в автоматических устройствах, типа банкоматов, используется МСС 6011."
        },
        {
            "mcc": 6011,
            "edited_description": "Financial Institutions – Manual Cash Disbursements",
            "combined_description": "Financial Institutions – Manual Cash Disbursements",
            "russian_name": "Финансовые учреждения – снятие наличных автоматически",
            "russian_description": "Используется для определения операций выдачи наличных денежных средств и нефинансовых операции в банкоматах клиентов международных платежных систем.\n\nДля снятий наличных, совершаемых в кассе финансовых учреждений, используется MCC 6010."
        },
        {
            "mcc": 6012,
            "edited_description": "Financial Institutions – Merchandise and Services",
            "combined_description": "Financial Institutions – Merchandise and Services",
            "russian_name": "Финансовые учреждения – торговля и услуги",
            "russian_description": "Покупка товаров или услуг в финансовых учреждениях. Такими товарами и услугами могут быть чеки и другие финансовые продукты, рекламные товары, сборы за предоставление кредита и плата за услуги финансового консультирования, пополнение счета преодоплаченных карт. По документам Visa этот MCC также должен использоваться для погашения долгов, займов или остатка по кредитной карте держателем карты в финансовом учреждении. Также этот MCC используется при оплате услуг микрофинансовых организаций.\n\nДля оплаты услуг по ценным бумагам и брокерским операциям или других соответствующих расходов используется MCC 6211.\n\nДля денежных выплат используется MCC 6010 для очных операций и MCC 6011 для транзакций, которые происходят в банкоматах."
        },
        {
            "mcc": 6051,
            "edited_description": "Non-Financial Institutions – Foreign Currency, Money Orders (not wire transfer) and Travelers Cheques",
            "combined_description": "Non-Financial Institutions – Foreign Currency, Money Orders (not wire transfer) and Travelers Cheques",
            "russian_name": "Квази-Кэш – Нефинансовые учреждения",
            "russian_description": "Покупка чеков, иностранной валюты, пополнение электронных кошельков, торговых счетов и другие квази-кэш операции в нефинансовых учреждениях"
        },
        {
            "mcc": 6211,
            "edited_description": "Security Brokers/Dealers",
            "combined_description": "Security Brokers/Dealers",
            "russian_name": "Услуги брокеров на рынке ценных бумаг",
            "russian_description": "Точки, которые покупают и продают ценные бумаги, акции, облигации, товары и фонды"
        },
        {
            "mcc": 6300,
            "edited_description": "Insurance Sales, Underwriting, and Premiums",
            "combined_description": "Insurance Sales, Underwriting, and Premiums",
            "russian_name": "Услуги страховых компаний",
            "russian_description": "Розничные торговые точки, которые продают все виды личных или коммерческих страховых полисов, включая страхование автомобилей, жизни, здоровья, прав собственности на недвижимость, медицинские и стоматологические страховки, страхование для домовладельцев и арендаторов, страхование здоровья домашних животных, страхование от наводнений, пожаров или землетрясений.\n\nДля точек, которые продают страховые продукты и услуги с использованием методов прямого маркетинга, используется MCC 5960."
        },
        {
            "mcc": 6381,
            "edited_description": "Insurance Premiums, (no longer valid for first presentment work)",
            "combined_description": "Insurance Premiums, (no longer valid for first presentment work)",
            "russian_name": "Страховые премии",
            "russian_description": "В справочниках платёжных систем не найдено, но есть в исключениях некоторых банков. По некоторым данным код уже не используется."
        },
        {
            "mcc": 6399,
            "edited_description": "Insurance, Not Elsewhere Classified ( no longer valid forfirst presentment work)",
            "combined_description": "Insurance, Not Elsewhere Classified ( no longer valid forfirst presentment work)",
            "russian_name": "Страхование – нигде более не классифицированные",
            "russian_description": "По некоторым данным код не используется"
        },
        {
            "mcc": 6513,
            "edited_description": "Real Estate Agents and Managers - Rentals",
            "combined_description": "Real Estate Agents and Managers - Rentals",
            "russian_name": "Агенты недвижимости и менеджеры - Аренда",
            "russian_description": "Сборы, взимаемые точками, занимающихся арендой и управлением жилой и коммерческой недвижимостью, такими как агенты по недвижимости, брокеры и менеджеры, а также услуги по аренде квартир. Такие сборы могут включать плату за управление, комиссионные за аренду недвижимости и платежи за аренду недвижимости."
        },
        {
            "mcc": 7011,
            "edited_description": "Lodging – Hotels, Motels, Resorts, Central Reservation Services (not elsewhere classified)",
            "combined_description": "Lodging – Hotels, Motels, Resorts, Central Reservation Services (not elsewhere classified)",
            "russian_name": "Отели и мотели - нигде более не классифицированные",
            "russian_description": "Заведения размещения, для которых не был определен уникальный MCC, включая гостиницы, курорты, коттеджи, коттеджи и общежития."
        },
        {
            "mcc": 7012,
            "edited_description": "Timeshares",
            "combined_description": "Timeshares",
            "russian_name": "Тайм-шер",
            "russian_description": "Розничные продавцы, которые продают, арендуют и арендуют недвижимость в тайм-шер и организуют обмен кондоминиумами в тайм-шер."
        },
        {
            "mcc": 7032,
            "edited_description": "Sporting and Recreational Camps",
            "combined_description": "Sporting and Recreational Camps",
            "russian_name": "Рекреационные и спортивные лагеря",
            "russian_description": "Торговцы, которые управляют детскими лагерями, лагерями отдыха и спортивными лагерями. Примеры таких лагерей включают летние лагеря для мальчиков и девочек, рыболовные и охотничьи лагеря, а также учебные или спортивные лагеря.\nДля кемпингов, используемых для палаточного или прицепного кемпинга, используется MCC 7033."
        },
        {
            "mcc": 7033,
            "edited_description": "Trailer Parks and Camp Grounds",
            "combined_description": "Trailer Parks and Camp Grounds",
            "russian_name": "Кемпинги и трейлер-парки",
            "russian_description": "Торговцы, которые предоставляют ночные или краткосрочные кемпинги для рекреационных автомобилей, прицепов, кемперов или палаток. Такие кемпинги могут быть расположены в государственных парках, или находиться в частной собственности и эксплуатироваться, и могут включать или не включать водные и электричество для рекреационных транспортных средств."
        },
        {
            "mcc": 7210,
            "edited_description": "Laundry, Cleaning, and Garment Services",
            "combined_description": "Laundry, Cleaning, and Garment Services",
            "russian_name": "Услуги по уборке и прачечной",
            "russian_description": "Торговцы, которые управляют парами или другими видами прачечных для коммерческих предприятий или физических лиц. Еженедельно или ежемесячно эти торговцы предоставляют отмытые предметы, такие как униформа, халаты, фартуки, столовое белье, постельное белье и полотенца. Этот MCC также включает в себя обслуживание подгузников, предлагающие вывоз из дома, уборку и доставку."
        },
        {
            "mcc": 7211,
            "edited_description": "Laundry – Family and Commercial",
            "combined_description": "Laundry – Family and Commercial",
            "russian_name": "Услуги прачечной - семейные и коммерческие",
            "russian_description": "Точки, которые предоставляют стиральные и сушильные машины самообслуживания для общего пользования, в том числе услуги прачечной с платой за вес. Такие прачечные самообслуживания обычно известны как лондроматы (прачечные-автоматы), но их также можно найти в общежитиях, многоквартирных домах или других подобных местах."
        },
        {
            "mcc": 7216,
            "edited_description": "Dry Cleaners",
            "combined_description": "Dry Cleaners",
            "russian_name": "Химчистка",
            "russian_description": "Точки, которые предоставляют услуги химчистки для частных лиц или предприятий, и могут предлагать ограниченные услуги по переделке. Обычно в химчистках чистят одежду, шторы, свадебные платья и постельные принадлежности."
        },
        {
            "mcc": 7217,
            "edited_description": "Carpet and Upholstery Cleaning",
            "combined_description": "Carpet and Upholstery Cleaning",
            "russian_name": "Чистка ковров и обивки мебели",
            "russian_description": "Точки, которые чистят для частных лиц и предприятий ковры, ткани и обивку мебели. \n\nДля точек, которые предоставляют услуги замены обивки, используется MCC 7641."
        },
        {
            "mcc": 7221,
            "edited_description": "Photographic Studios",
            "combined_description": "Photographic Studios",
            "russian_name": "Фотостудии",
            "russian_description": "Торговцы, которые производят фотосъемку или видеосъемку для широкой публики, в том числе фотографии детей в школах или свадебные фото и видео.\nДля продавцов, которые предоставляют услуги по разработке и печати плёнки, используется MCC 7395."
        },
        {
            "mcc": 7230,
            "edited_description": "Barber and Beauty Shops",
            "combined_description": "Barber and Beauty Shops",
            "russian_name": "Парикмахерские и салоны красоты",
            "russian_description": "Торговцы, которые предоставляют персональные услуги по уходу за волосами, такие как стрижка волос, укладка волос, окраска волос и наращивание волос. Парикмахерские и салоны красоты могут также выполнять маникюр и педикюр и продавать ограниченный ассортимент средств по уходу за волосами."
        },
        {
            "mcc": 7251,
            "edited_description": "Shop Repair Shops and Shoe Shine Parlors, and Hat Cleaning Shops",
            "combined_description": "Shop Repair Shops and Shoe Shine Parlors, and Hat Cleaning Shops",
            "russian_name": "Чистка шляп, ремонт и полировка обуви",
            "russian_description": "Точки, которые ремонтируют обувь и предоставляют услуги по чистке и полировке обуви, а также точки, которые предоставляют услуги по чистке и блокировке шляп."
        },
        {
            "mcc": 7261,
            "edited_description": "Funeral Service and Crematories",
            "combined_description": "Funeral Service and Crematories",
            "russian_name": "Ритуальные услуги и крематории",
            "russian_description": "Точки, которые предоставляют услуги по подготовке похорон, кремации и проводят похороны. К таким точкам относятся морги, крематории, похоронные дома и похоронные бюро.\n\nДля услуг кремации и захоронения животных используется MCC 7299."
        },
        {
            "mcc": 7273,
            "edited_description": "Dating and Escort Services",
            "combined_description": "Dating and Escort Services",
            "russian_name": "Знакомства",
            "russian_description": "Торговцы, предоставляющие услуги знакомств и эскорта, в том числе через компьютеры, личные видео и сервисы знакомств"
        },
        {
            "mcc": 7276,
            "edited_description": "Tax Preparation Service",
            "combined_description": "Tax Preparation Service",
            "russian_name": "Служба налоговой подготовки",
            "russian_description": "Торговцы, которые исключительно предоставляют услуги по подготовке декларации по налогу на прибыль без аудита, бухгалтерского учета или бухгалтерских услуг.\nДля продавцов, предоставляющих услуги аудита, бухгалтерского учета или бухгалтерского учета в дополнение к услугам по подготовке налоговой декларации, используйте MCC 8931."
        },
        {
            "mcc": 7277,
            "edited_description": "Counseling Service – Debt, Marriage, Personal",
            "combined_description": "Counseling Service – Debt, Marriage, Personal",
            "russian_name": "Долги, брак, личные вопросы - консультирование",
            "russian_description": "Точки, предоставляющие разнообразные консультационные услуги, такие как консультирование по вопросам задолженности и финансов, консультирование по вопросам брака, консультирование по вопросам семьи, консультирование по вопросам злоупотребления алкоголем и наркотиками и другие личные консультации.\nДля точек, которые предоставляют юридические услуги, используется MCC 8111."
        },
        {
            "mcc": 7278,
            "edited_description": "Buying/Shopping Services, Clubs",
            "combined_description": "Buying/Shopping Services, Clubs",
            "russian_name": "Услуги покупок/шоппинга",
            "russian_description": "Торговые точки которые предлагают услуги по продаже товаров как для частных, так и для корпоративных лиц. Напрямую эти точки товары не продают, а лишь оказывают услуги посредника по продаже за определённую плату."
        },
        {
            "mcc": 7296,
            "edited_description": "Clothing Rental – Costumes, Formal Wear, Uniforms",
            "combined_description": "Clothing Rental – Costumes, Formal Wear, Uniforms",
            "russian_name": "Сдача в аренду костюмов, униформы, простой одежды",
            "russian_description": "Торговые точки, сдающие в аренду костюмы, смокинги, одежду, униформу и другие типы верхней одежды и аксессуары."
        },
        {
            "mcc": 7297,
            "edited_description": "Massage Parlors",
            "combined_description": "Massage Parlors",
            "russian_name": "Массажные салоны",
            "russian_description": "Терапевтические приемные, предлагающие услуги массажа. Некоторые из них могут также оказывать индивидуальные процедуры, такие как массаж лица и ароматерапию."
        },
        {
            "mcc": 7298,
            "edited_description": "Health and Beauty Shops",
            "combined_description": "Health and Beauty Shops",
            "russian_name": "Салоны красоты и здоровья",
            "russian_description": "Торговцы, обычно известные как дневные курорты, предоставляющие разнообразные личные или терапевтические услуги без ночевки. Такие услуги могут включать уход за лицом, массаж, грязевые ванны, травяные обертывания, сеансы загара, гидромассажные ванны, паровые ванны, индивидуальные программы упражнений, консультирование по вопросам питания, а также консультирование и укладка волос и макияжа, а также учебные занятия, такие как аэробика, Контроля, приготовления пищи и занятий спортом.\nДля спа-услуг, предлагаемых в рамках плана пакета, который включает проживание в торговом представительстве, используется MCC 7011."
        },
        {
            "mcc": 7299,
            "edited_description": "Miscellaneous Personal Services ( not elsewhere classifies)",
            "combined_description": "Miscellaneous Personal Services ( not elsewhere classifies)",
            "russian_name": "Различные услуги - нигде более не классифицированные",
            "russian_description": "Точки, предоставляющие личные услуги, которые не подпадают какой-либо другой MCC.\n\nПримерами таких услуг являются пансионы для животных, бани, услуги сиделок, услуги горничной, уход за животными и питомники, обучение или разведение животных, агенты по недвижимости, брокеров и менеджеров, пирсинг и татуировка, услуги по очистке воды, таксидермисты, свадебные часовни, а также кремация и погребение животных.\nДля агентов по недвижимости, брокеров и менеджеров, а также услуги по аренде квартир, используется MCC 6513."
        },
        {
            "mcc": 7311,
            "edited_description": "Advertising Services",
            "combined_description": "Advertising Services",
            "russian_name": "Рекламные услуги",
            "russian_description": "Точки, которые занимаются подготовкой рекламы (копирайтинг, художественные работы, графика и другие творческие работы) и размещают рекламу в периодических изданиях, газетах, на радио, телевидении или других рекламных носителях для клиентов по договору или на платной основе.\nТакже включены другие виды рекламы, такие как реклама и надписи в небе, распространение купонов и распространение образцов."
        },
        {
            "mcc": 7321,
            "edited_description": "Consumer Credit Reporting Agencies",
            "combined_description": "Consumer Credit Reporting Agencies",
            "russian_name": "Кредитные бюро",
            "russian_description": "Точки, предоставляющие услуги по предоставлению кредитных отчетов, такие как определение кредитоспособности, расчетно-клиринговые и другие сопутствующие услуги. Этот MCC не включает коллекторские агентства."
        },
        {
            "mcc": 7332,
            "edited_description": "Blueprinting and Photocopying Services",
            "combined_description": "Blueprinting and Photocopying Services",
            "russian_name": "Услуги синьки и фотокопирования",
            "russian_description": "null"
        },
        {
            "mcc": 7333,
            "edited_description": "Commercial Photography, Art and Graphics",
            "combined_description": "Commercial Photography, Art and Graphics",
            "russian_name": "Коммерческое искусство, графика, фотография",
            "russian_description": "Точки, которые предоставляют коммерческое искусство или услуги графического дизайна для рекламных агентств, издателей и других предприятий. Такие услуги могут включать в себя дизайн шелкографии, кинопроизводство и слайд-фильм, графический дизайн, коммерческое искусство и иллюстрации.\nДля продавцов, которые предоставляют фото, видео и портретную съемку для личных целей, используется MCC 7221."
        },
        {
            "mcc": 7338,
            "edited_description": "Quick Copy, Reproduction and Blueprinting Services",
            "combined_description": "Quick Copy, Reproduction and Blueprinting Services",
            "russian_name": "Быстрое копирование, репродуцирование и услуги по созданию чертежей",
            "russian_description": "Точки, которые воспроизводят текст, рисунки, планы, карты и подобные материалы путем создания чертежей, фотокопирования или использования других методов воспроизведения. Такие точки также могут предоставлять услуги сортировки и сшивания."
        },
        {
            "mcc": 7339,
            "edited_description": "Stenographic and Secretarial Support Services",
            "combined_description": "Stenographic and Secretarial Support Services",
            "russian_name": "Услуги стенографии и секретарского дела",
            "russian_description": "Торговцы, предоставляющие стенографические, секретарские и другие канцелярские услуги, такие как обработка текстов, машинопись, редактирование, письмо, корректура, составление резюме и услуги по составлению судебных отчетов.\nДля служб занятости, которые в основном занимаются заполнением секретарских должностей, используется MCC 7361."
        },
        {
            "mcc": 7342,
            "edited_description": "Exterminating and Disinfecting Services",
            "combined_description": "Exterminating and Disinfecting Services",
            "russian_name": "Дезинсекция, дезинфекция и дератизация",
            "russian_description": "Точки, которые предоставляют услуги по борьбе с вредителями, уничтожению, дезинфекции и фумигации, включая уничтожение термитов, насекомых и грызунов."
        },
        {
            "mcc": 7349,
            "edited_description": "Cleaning and Maintenance, Janitorial Services",
            "combined_description": "Cleaning and Maintenance, Janitorial Services",
            "russian_name": "Уборка и техническое обслуживание зданий и помещений",
            "russian_description": "Точки, которые предоставляют услуги по уборке и, обслуживанию зданий, такие как мытье окон, полов, услуги школьного сторожа, уборка офисов и помещений по договору или на платной основе."
        },
        {
            "mcc": 7361,
            "edited_description": "Employment Agencies, Temporary Help Services",
            "combined_description": "Employment Agencies, Temporary Help Services",
            "russian_name": "Агентства по трудоустройству, временные справочные службы",
            "russian_description": "Торговцы, которые предоставляют услуги по трудоустройству для работодателей или лиц, ищущих работу с постоянными или временными должностями."
        },
        {
            "mcc": 7372,
            "edited_description": "Computer Programming, Integrated Systems Design and Data Processing Services",
            "combined_description": "Computer Programming, Integrated Systems Design and Data Processing Services",
            "russian_name": "Программирование, обработка данных, проектирование интегрированных систем",
            "russian_description": "Услуги программирования, проектирования систем и обработки данных на основе контракта и платы. Такие услуги могут включать проектирование и анализ компьютерного программного обеспечения, модификацию систем и программного обеспечения, ввод или обработку данных и обучение использованию программного обеспечения."
        },
        {
            "mcc": 7375,
            "edited_description": "Information Retrieval Services",
            "combined_description": "Information Retrieval Services",
            "russian_name": "Информационно-поисковые услуги",
            "russian_description": "Провайдеры информационных технологий, информации о базах данных, услуги интернет-провайдера."
        },
        {
            "mcc": 7379,
            "edited_description": "Computer Maintenance and Repair Services, Not Elsewhere Classified",
            "combined_description": "Computer Maintenance and Repair Services, Not Elsewhere Classified",
            "russian_name": "Ремонт компьютеров",
            "russian_description": "Техническое обслуживание компьютерного оборудования. Консультации специалиста в этой области. Внедрение баз данных, восстановление информации с пленки, дискет, анализ компьютерных требований."
        },
        {
            "mcc": 7392,
            "edited_description": "Management, Consulting, and Public Relations Services",
            "combined_description": "Management, Consulting, and Public Relations Services",
            "russian_name": "Услуги по консультированию, управлению и связям с общественностью",
            "russian_description": "Торговцы, которые предоставляют консультации и помощь в управлении частными, некоммерческими и общественными организациями по договору или на платной основе. Предоставляемые услуги могут включать стратегическое и организационное планирование, финансовое планирование и бюджетирование, разработку маркетинговых целей, планирование информационных систем, разработку кадровой политики, планирование процедур и услуги по связям с общественностью."
        },
        {
            "mcc": 7393,
            "edited_description": "Protective and Security Services – Including Armored Carsand Guard Dogs",
            "combined_description": "Protective and Security Services – Including Armored Carsand Guard Dogs",
            "russian_name": "Детективные агентства, охранные агентства, службы безопасности, включая бронированные автомобили, сторожевых собак",
            "russian_description": "Точки, предоставляющие охранные устройства и службы безопасности. Примерами таких устройств и услуг являются бронированные автомобили, системы безопасности (установка, мониторинг и обслуживание), частные следователи, сторожевые собаки и детекторы лжи."
        },
        {
            "mcc": 7394,
            "edited_description": "Equipment Rental and Leasing Services, Tool Rental, Furniture Rental, and Appliance Rental",
            "combined_description": "Equipment Rental and Leasing Services, Tool Rental, Furniture Rental, and Appliance Rental",
            "russian_name": "Аренда оборудования и лизинговые услуги, аренда мебели, прокат инструментов",
            "russian_description": "Торговцы, которые арендуют и сдают в лизинг оборудование, инструменты, мебель, бытовую технику и оргтехнику (за исключением пишущих машинок).\nДля проката пишущих машинок используется MCC 5978."
        },
        {
            "mcc": 7395,
            "edited_description": "Photofinishing Laboratories, Photo Developing",
            "combined_description": "Photofinishing Laboratories, Photo Developing",
            "russian_name": "Фотостудии, фотолаборатории",
            "russian_description": "Печать фотографий, проявка плёнки, ретуширование, фотоувеличение, весь спектр фотомонтажа и ремастеринга. Продажа рамок, фотоальбомов, фотопленки, фотоаппаратов."
        },
        {
            "mcc": 7399,
            "edited_description": "Business Services, Not Elsewhere Classified",
            "combined_description": "Business Services, Not Elsewhere Classified",
            "russian_name": "Бизнес услуги – нигде более не классифицированные",
            "russian_description": "Точки, которые предоставляют коммерческие и торговые услуги, которые обычно не считаются профессиями. Этот MCC должен использоваться, только если другой более конкретный MCC не описывает бизнес точки. Примерами таких бизнес-услуг являются издательские компании, компании по управлению конференциями, организаторы совещаний, компании по проведению семинаров, слесари, почтовые и упаковочные услуги (включая продажу марок), службы обработки сообщений и пейджинга, а также услуги по управлению отходами."
        },
        {
            "mcc": 7511,
            "edited_description": "Truck Stop",
            "combined_description": "Truck Stop",
            "russian_name": "Стоянка грузового транспорта",
            "russian_description": "null"
        },
        {
            "mcc": 7512,
            "edited_description": "Car Rental Companies ( Not Listed Below)",
            "combined_description": "Car Rental Companies ( Not Listed Below)",
            "russian_name": "Агентства по прокату автомобилей - нигде более не классифицированные",
            "russian_description": "Агентства по аренде автомобилей, для которых не назначен уникальный MCC."
        },
        {
            "mcc": 7513,
            "edited_description": "Truck and Utility Trailer Rentals",
            "combined_description": "Truck and Utility Trailer Rentals",
            "russian_name": "Прокат аксессуаров для трэйлеров и грузовиков.",
            "russian_description": "Лизинг оборудования для грузовиков, фургонов, трэйлеров."
        },
        {
            "mcc": 7519,
            "edited_description": "Motor Home and Recreational Vehicle Rentals",
            "combined_description": "Motor Home and Recreational Vehicle Rentals",
            "russian_name": "Прокат домиков на колесах, аксессуары к наземному транспорту.",
            "russian_description": "Прокат прицепов, вагончиков, фургонов, кемпов, тентов для грузовиков как на короткие сроки, так и на большие."
        },
        {
            "mcc": 7523,
            "edited_description": "Automobile Parking Lots and Garages",
            "combined_description": "Automobile Parking Lots and Garages",
            "russian_name": "Паркинги и гаражи",
            "russian_description": "Компании предоставляющие услуги временного паркования для автомобилей, с ежедневной или помесячной оплатой. На контрактной основе или за отдельную плату."
        },
        {
            "mcc": 7531,
            "edited_description": "Automotive Body Repair Shops",
            "combined_description": "Automotive Body Repair Shops",
            "russian_name": "Кузовной ремонт автомобилей",
            "russian_description": "Точки, которые выполняют кузовные работы. Такие точки также могут или не могут покрасить автомобили в связи с ремонтом кузова.\n\nДля точек, которые в основном красят автомобили, используется MCC 7535.\n\nДля точек, которые выполняют ремонтные работы, кроме ремонта кузова, используется MCC 7538."
        },
        {
            "mcc": 7534,
            "edited_description": "Tire Re-treading and Repair Shops",
            "combined_description": "Tire Re-treading and Repair Shops",
            "russian_name": "Шиномонтаж и вулканизация",
            "russian_description": "Этот MCC определяет точки, которые продают, устанавливают, ремонтируют или восстанавливают старые шины.\n\nДля точек, которые предоставляют другие виды услуг по ремонту автомобилей, используется MCC 7538.\nДля точек, которые в основном продают новые автомобильные шины, используется MCC 5532."
        },
        {
            "mcc": 7535,
            "edited_description": "Paint Shops – Automotive",
            "combined_description": "Paint Shops – Automotive",
            "russian_name": "Покраска автомобилей",
            "russian_description": "Точки, которые красят и полируют исключительно автомобили, в том числе те, которые специализируются на реставрации старинных автомобилей, а также делают покраску на заказ."
        },
        {
            "mcc": 7538,
            "edited_description": "Automotive Service Shops",
            "combined_description": "Automotive Service Shops",
            "russian_name": "Автосервисы",
            "russian_description": "Точки, которые проводят ремонт автомобилей и общее обслуживание, такое как обслуживание двигателей, тормозной системы, системы кондиционирования воздуха, глушителей, передней части и рамы, топливной системы, карбюраторов, радиаторов, ветровых стекол и окон, а также электроники. В этот MCC входят точки быстрой замены масла и продавцы смазочных материалов. Такие автосервисы также могут выполнять или не выполнять услуги по шиномонтажу."
        },
        {
            "mcc": 7542,
            "edited_description": "Car Washes",
            "combined_description": "Car Washes",
            "russian_name": "Автомойки",
            "russian_description": "Точки, которые моют, чистят воском и полируют автомобили, в том числе щеточные мойки, ручные мойки и мойки самооблуживания."
        },
        {
            "mcc": 7549,
            "edited_description": "Towing Services",
            "combined_description": "Towing Services",
            "russian_name": "Услуги буксировки и эвакуации",
            "russian_description": "Точки, которые предоставляют услуги буксировки транспортных средств."
        },
        {
            "mcc": 7622,
            "edited_description": "Radio Repair Shops",
            "combined_description": "Radio Repair Shops",
            "russian_name": "Ремонт электроники",
            "russian_description": "Ремонт электроники, такой, как радиоприёмников, телевизоров, аудио аппаратуры, СD-проигрывателей, компьютеров."
        },
        {
            "mcc": 7623,
            "edited_description": "Air Conditioning and Refrigeration Repair Shops",
            "combined_description": "Air Conditioning and Refrigeration Repair Shops",
            "russian_name": "Ремонт кондиционеров и холодильников",
            "russian_description": "Точки, которые обслуживают и ремонтируют бытовые и коммерческие кондиционеры, а также холодильные системы.\nДля точек, обслуживающих и ремонтирующих небольшие бытовые приборы, используется MCC 7629.\nДля точек, которые обслуживают и ремонтируют большие бытовые приборы, используется MCC 7699."
        },
        {
            "mcc": 7629,
            "edited_description": "Electrical And Small Appliance Repair Shops",
            "combined_description": "Electrical And Small Appliance Repair Shops",
            "russian_name": "Ремонт электрооборудования и малой бытовой техники",
            "russian_description": "Точки, которые обслуживают и ремонтируют бытовые и коммерческие электрические компоненты и небольшие приборы, такие как микроволновые печи, тостеры, а также точки, которые обслуживают и ремонтируют электрические офисные машины, за исключением пишущих машин.\nДля точек, специализирующихся на ремонте пишущей машинки, используется MCC 5978. \nДля точек по ремонту электроники используется MCC 7622.\nДля точек, которые ремонтируют большие бытовые приборы, используется MCC 7699."
        },
        {
            "mcc": 7631,
            "edited_description": "Watch, Clock, and Jewelry Repair",
            "combined_description": "Watch, Clock, and Jewelry Repair",
            "russian_name": "Центры ремонта часов и чистки ювелирных изделий",
            "russian_description": "Торговые точки по ремонту часов, чистке ювелирных изделий, украшений."
        },
        {
            "mcc": 7641,
            "edited_description": "Furniture, Furniture Repair, and Furniture Refinishing",
            "combined_description": "Furniture, Furniture Repair, and Furniture Refinishing",
            "russian_name": "Обивка, ремонт и отделка мебели",
            "russian_description": "Точки, которые занимаются обивкой, ремонтом и отделкой мебели, включая реставраторов антикварной мебели."
        },
        {
            "mcc": 7692,
            "edited_description": "Welding Repair",
            "combined_description": "Welding Repair",
            "russian_name": "Ремонт с помощью сварки",
            "russian_description": "Торговые точки специализирующиеся по ремонту с помощью сварки."
        },
        {
            "mcc": 7699,
            "edited_description": "Repair Shops and Related Services –Miscellaneous",
            "combined_description": "Repair Shops and Related Services –Miscellaneous",
            "russian_name": "Ремонтные услуги – нигде более не классифицированные",
            "russian_description": "Агенства по ремонтным работам, которые не могут быть классифицированы как какие-либо конкретные. Некоторые из этих агенств могут предлагать отдельные услуги по ремонту бытовой техники (к примеру: сушилки, посудомоечные машины, нагреватели воды), велосипедов, спортивных тренажеров, слуховых аппаратов, протезов, музыкальных инструментов, палаток и подвесок, видеокамер и фотоаппаратов, газонокосилок, чемоданов и кожаных изделий. Также включают в себя центры по чистке и обслуживанию котлов и дымовых труб."
        },
        {
            "mcc": 7800,
            "edited_description": "Government-Owned Lotteries",
            "combined_description": "null",
            "russian_name": "Государственные лотереи (только США)",
            "russian_description": "Государственные органы, которые управляют лотереями, а также занимаются продажей лотерейных билетов или акций в Интернете или в офисе напрямую или через назначенных агентов.\n\nИспользование этого MCC ограничено точками, расположенными в регионе США."
        },
        {
            "mcc": 7801,
            "edited_description": "Government-Licensed On-Line Casinos (On-Line Gambling)",
            "combined_description": "null",
            "russian_name": "Азартные игры в интернете (только США)",
            "russian_description": "Торговцы, получившие лицензию в соответствии с действующим законодательством или правилами, чтобы управлять системой или платформой интернет-азартных игр, принимающей размещение ставок.\nИспользование этого MCC ограничено точками, расположенными в США"
        },
        {
            "mcc": 7802,
            "edited_description": "Government-Licensed Horse/Dog Racing",
            "combined_description": "null",
            "russian_name": "Лошадиные / собачьи бега (только США)",
            "russian_description": "Торговцы, получившие лицензию в соответствии с применимым законодательством или правилами для проведения в отношении лошадей или собачьих гонок или пари-мутул, или в обоих случаях.\nИспользование этого MCC ограничено продавцами, расположенными в США"
        },
        {
            "mcc": 7829,
            "edited_description": "Motion Pictures and Video Tape Production and Distribution",
            "combined_description": "Motion Pictures and Video Tape Production and Distribution",
            "russian_name": "Производство и распространение кинофильмов и видеокассет",
            "russian_description": "Оптовые производители и распространители образовательных и промышленных фильмов и видеороликов для выставок и продаж, в том числе рекламных роликов и учебных фильмов.\n\nДля предприятий розничной торговли, которые сдают в аренду видеокассеты потребителям, используется MCC 7841."
        },
        {
            "mcc": 7832,
            "edited_description": "Motion Picture Theaters",
            "combined_description": "Motion Picture Theaters",
            "russian_name": "Кинотеатры",
            "russian_description": "Точки, которые управляют кинотеатрами, в том числе под открытым небом (drive-in). Такие продавцы продают билеты и напитки и могут предлагать или не предлагать предварительное бронирование билетов по телефону."
        },
        {
            "mcc": 7841,
            "edited_description": "Video Tape Rental Stores",
            "combined_description": "Video Tape Rental Stores",
            "russian_name": "Видеопрокат",
            "russian_description": "Точки которые сдают в аренду видеокассеты, CD, DVD и видеоигры для домашнего использования. Такие продавцы могут продавать или не продавать ограниченный выбор использованных видео, напитки, конфеты, закуски и чистые кассеты."
        },
        {
            "mcc": 7911,
            "edited_description": "Dance Halls, Studios and Schools",
            "combined_description": "Dance Halls, Studios and Schools",
            "russian_name": "Танцевальные залы, школы и студии",
            "russian_description": "Точки, которые управляют танцевальными студиями, танцевальными школами и общественными танцевальными залами или бальными залами, взимающие плату за вход, уроки и прохладительные напитки. Такие точки могут обучать многим видам танца или специализироваться на чечетке и балете, бальных, кадриле и других видах танца."
        },
        {
            "mcc": 7922,
            "edited_description": "Theatrical Producers (Except Motion Pictures), Ticket Agencies",
            "combined_description": "Theatrical Producers (Except Motion Pictures), Ticket Agencies",
            "russian_name": "Театральные продюсеры (кроме кинофильмов), билетные агентства",
            "russian_description": "Точки, которые управляют живыми театральными постановками, такими как дорожные компании и летние театральные группы. Сюда также входят услуги, связанные с театральными постановками и концертами, такие как кастинговые агентства, агентства бронирования, декорации, освещение и другое оборудование, а также театральные билетные агентства.\n\nДля кинотеатров используется MCC 7832."
        },
        {
            "mcc": 7929,
            "edited_description": "Bands, Orchestras, and Miscellaneous Entertainers (Not Elsewhere Classified)",
            "combined_description": "Bands, Orchestras, and Miscellaneous Entertainers (Not Elsewhere Classified)",
            "russian_name": "Музыкальные группы, оркестры и прочие развлекательные услуги",
            "russian_description": "Точки, которые обеспечивают развлечения кроме театральных постановок, и включают музыкантов, группы, оркестры, комиков и фокусников. Точки, которые специализируются на музыке (живые группы или диджеи) для свадеб или мероприятий, также включены."
        },
        {
            "mcc": 7932,
            "edited_description": "Billiard and Pool Establishments",
            "combined_description": "Billiard and Pool Establishments",
            "russian_name": "Бильярд-клубы",
            "russian_description": "Заведения, которые сдают в аренду бильярдные столы для развлечения. Такие точки могут предлагать бильярдные столы, управляемые монетами, или могут арендовать бильярдные столы на игру или по часам. Также могут быть доступны шаффлборд, дартс и другие игры и напитки."
        },
        {
            "mcc": 7933,
            "edited_description": "Bowling Alleys",
            "combined_description": "Bowling Alleys",
            "russian_name": "Боулинг",
            "russian_description": "Точки, которые используют дорожки для боулинга для развлечения и могут принимать карты за арендную плату, покупки в магазине, напитки.\n\nТочки, расположенные в пределах дорожек для боулинга, которыми управляют отдельно, должны быть классифицированы с соответствующим MCC для этого типа бизнеса. Например, ресторан, расположенный в кегельбане, должен использовать MCC 5812, бар должен использовать MCC 5813."
        },
        {
            "mcc": 7941,
            "edited_description": "Commercial Sports, Athletic Fields, Professional Sport Clubs, and Sport Promoters",
            "combined_description": "Commercial Sports, Athletic Fields, Professional Sport Clubs, and Sport Promoters",
            "russian_name": "Атлетические поля, коммерческие виды спорта, профессиональные спортивные клубы, промоутеры спорта",
            "russian_description": "Точки, которые управляют и продвигают полупрофессиональные и профессиональные спортивные клубы (такие как бейсбол, баскетбол, футбол, хоккей и футбол), продвигают любительские и профессиональные атлетические события и управляют индивидуальными спортсменами. Сюда также входят спортивные арены и стадионы."
        },
        {
            "mcc": 7991,
            "edited_description": "Tourist Attractions and Exhibits",
            "combined_description": "Tourist Attractions and Exhibits",
            "russian_name": "Туристические достопримечательности и выставки",
            "russian_description": "Точки, которые управляют туристическими достопримечательностями и выставками для развлечений, таких как экспозиции, ботанические сады, ремесленные шоу, музеи и винодельни.\n\nДля художественных выставок, проводимых в художественных галереях, используется MCC 5971."
        },
        {
            "mcc": 7992,
            "edited_description": "Golf Courses – Public",
            "combined_description": "Golf Courses – Public",
            "russian_name": "Публичные поля для гольфа",
            "russian_description": "Торговые точки, которые управляют общественными полями для гольфа. Предлагаемые услуги могут включать в себя оплату за поле, прокат гольф-каров или прокат снаряжения.\nДля ресторанов и кафе, расположенных на поле для гольфа, используется MCC 5812. \nДля профессиональных магазинов, продающих принадлежности для гольфа и оборудование, используется MCC 5941. \nДля загородных клубов и частных полей для гольфа используется MCC 7997."
        },
        {
            "mcc": 7993,
            "edited_description": "Video Amusement Game Supplies",
            "combined_description": "Video Amusement Game Supplies",
            "russian_name": "Принадлежности для видеоигр",
            "russian_description": "Торговые точки, которые продают игровые автоматы, оборудование и расходные материалы. Товары для продажи могут включать в себя автоматы с видеоиграми, музыкальные автоматы, пинбольные машины, слот-машины, механические игры и фотокабины.\nДля торговых точек, которые управляют видео и игровыми аркадами, используется MCC 7994."
        },
        {
            "mcc": 7994,
            "edited_description": "Video Game Arcades/Establishments",
            "combined_description": "Video Game Arcades/Establishments",
            "russian_name": "Клубы видеоигр",
            "russian_description": "Точки, которые используют интерактивные игры и развлекательные машины, такие как музыкальные автоматы, видеоигры, пинбольные машины, пейнтбол и игры с лазертегом, механические игры и будки мгновенной фотографии.\n\nДля точек, которые продают оборудование для развлечений, используется MCC 7993.\n\nДля точек, работающих с играми, использующими ставки, используется MCC 7995."
        },
        {
            "mcc": 7995,
            "edited_description": "Betting (including Lottery Tickets, Casino Gaming Chips, Off-track Betting and Wagers at Race Tracks)",
            "combined_description": "Betting (including Lottery Tickets, Casino Gaming Chips, Off-track Betting and Wagers at Race Tracks)",
            "russian_name": "Азартные игры",
            "russian_description": "Любая транзакция, кроме транзакции через банкомат, включающая в себя размещение ставки, покупку лотерейного билета, распространение ставок, коммерческие игры в полете или покупку фишек или другой ценности, используемой для азартных игр в сочетании с игровой деятельностью, предоставляемой заведения для ставок или пари, такие как казино, ипподромы, карточные салоны, авиакомпании и тому подобное."
        },
        {
            "mcc": 7996,
            "edited_description": "Amusement Parks, Carnivals, Circuses, Fortune Tellers",
            "combined_description": "Amusement Parks, Carnivals, Circuses, Fortune Tellers",
            "russian_name": "Парки аттракционов, карнавалы, цирки, гадалки",
            "russian_description": "Торговые точки, которые управляют парками аттракционов и карнавалами, предлагают механические аттракционы, закуски и киоски с едой, игры, выставки животных и развлечения. Также включены цирки, гадалки, астрологи, читатели карт таро и мистики."
        },
        {
            "mcc": 7997,
            "edited_description": "Membership Clubs (Sports, Recreation, Athletic), Country Clubs, and Private Golf Courses",
            "combined_description": "Membership Clubs (Sports, Recreation, Athletic), Country Clubs, and Private Golf Courses",
            "russian_name": "Клубы – загородные клубы, членство (отдых, спорт), частные поля для гольфа",
            "russian_description": "Торговые точки, которые управляют спортивными и рекреационными объектами, требующими членства. Примерами таких объектов могут быть спортивные и оздоровительные клубы, загородные клубы, частные поля для гольфа, лодочные яхт-клубы, клубы плавания, теннисные клубы, лиги для боулинга, клубы верховой езды, стрелковые клубы и клубы для игры в ракетбол. Такие точки могут или не могут предоставлять услуги массажа и спа-услуги, такие как уход за лицом, консультации по контролю веса, ароматерапия, паровые бани и джакузи.\n\nДля торговцев, которые в основном предоставляют массаж, используется MCC 7297.\nДля торговцев, которые в основном управляют спа и связанных с ним услугах, используется MCC 7298."
        },
        {
            "mcc": 7998,
            "edited_description": "Aquariums, Sea-aquariums, Dolphinariums",
            "combined_description": "Aquariums, Sea-aquariums, Dolphinariums",
            "russian_name": "Аквариумы, дельфинарии, зоопарки и морские парки",
            "russian_description": "Торговые точки, которые управляют парками морской жизни и зоопарками для развлечения и образования широкой общественности.\nДругие услуги, расположенные на территории, такие как рестораны или магазины подарков, должны быть отнесены к MCC, которые лучше всего описывают этот тип бизнеса."
        },
        {
            "mcc": 7999,
            "edited_description": "Recreation Services (Not Elsewhere Classified)",
            "combined_description": "Recreation Services (Not Elsewhere Classified)",
            "russian_name": "Услуги отдыха - нигде более не классифицированные",
            "russian_description": "Точки, которые предоставляют широкий спектр услуг для отдыха и развлечений, которые не описаны другим, более конкретным MCC. Как правило, эти точки предоставляют услуги, которые требуют активного физического участия, такие как плавание, игра в минигольф, катание на лыжах, мини автомобильные гонки, катание на коньках, скалолазание, катание на скейте и катание на лошадях. Эти точки могут также сдавать в аренду велосипеды, самолеты, мотоциклы, карты и другое спортивное оборудование. Как правило, эти точки не являются клубами и не требуют членства.\n\nДля частных спортивных клубных и клубов отдыха, требующих членство, используется MCC 7997.\n\nПри аренде лодок используется MCC 4457. Для общественных полей для гольфа используется MCC 7992."
        },
        {
            "mcc": 8011,
            "edited_description": "Doctors and Physicians (Not Elsewhere Classified)",
            "combined_description": "Doctors and Physicians (Not Elsewhere Classified)",
            "russian_name": "Врачи – нигде более не классифицированные",
            "russian_description": "Лицензированные врачи, занимающиеся общей или специализированной медициной и хирургией, которая не описана другим, более конкретным MCC. К таким точкам относятся пластические и косметические хирурги, дерматологи, психиатры, рентгенологи, ортопеды, педиатры, неврологи, акушеры и гинекологи."
        },
        {
            "mcc": 8021,
            "edited_description": "Dentists and Orthodontists",
            "combined_description": "Dentists and Orthodontists",
            "russian_name": "Стоматологи, ортодонты",
            "russian_description": "Лицензированные врачи, которые практикуют общую или специализированную стоматологию, а также стоматологическую хирургию."
        },
        {
            "mcc": 8031,
            "edited_description": "Osteopaths",
            "combined_description": "Osteopaths",
            "russian_name": "Остеопаты",
            "russian_description": "Лицензированные врачи, которые проводят терапию с использованием нехирургических манипуляций и корректировки костных структур.\n\nДля ортопедов, которые проводят хирургическое лечение, используется MCC 8011."
        },
        {
            "mcc": 8041,
            "edited_description": "Chiropractors",
            "combined_description": "Chiropractors",
            "russian_name": "Мануальные терапевты",
            "russian_description": "Медицинские работники, выполняющие лечение позвоночника, опорно-двигательной системы и др."
        },
        {
            "mcc": 8042,
            "edited_description": "Optometrists and Ophthalmologists",
            "combined_description": "Optometrists and Ophthalmologists",
            "russian_name": "Оптометристы, офтальмологи",
            "russian_description": "Оптометристы - это медицинские работники, которые проверяют и лечат дефекты глаз с помощью корректирующих линз или упражнений. Офтальмологи являются лицензированными врачами, которые специализируются на структурах, функциях и заболеваниях глаз и могут выполнять операции. Эти точки могут или не могут заполнять рецепты для очков или контактных линз или продавать оправы для очков."
        },
        {
            "mcc": 8043,
            "edited_description": "Opticians, Opticians Goods and Eyeglasses",
            "combined_description": "Opticians, Opticians Goods and Eyeglasses",
            "russian_name": "Оптика, оптические товары и очки",
            "russian_description": "Торговые точки, которые читают предписания по исправления зрения, заказывают линзы, производят и продают очки и контактные линзы, и могут проводить проверку глаза. Оптики могут также продавать различные оптические товары, такие как защитные очки, солнцезащитные очки (обычные и специальные), футляры для очков и контактных линз. Также включены т.н. \"Очки за час\", располагаемые в торговых центрах. \n\nДля торговых точек, которые проверяют глаза и проводят процедуры при дефектах глаз с использованием операционных или хирургических методов, используется MCC 8042."
        },
        {
            "mcc": 8044,
            "edited_description": "Opticians, Optical Goods, and Eyeglasses (no longer validfor first presentments)",
            "combined_description": "Opticians, Optical Goods, and Eyeglasses (no longer validfor first presentments)",
            "russian_name": "Оптические товары и очки (TSYS)",
            "russian_description": "Торговые точки, которые читают предписания по исправления зрения, заказывают линзы, производят и продают очки и контактные линзы, и могут проводить проверку глаза. Оптики могут также продавать различные оптические товары, такие как защитные очки, солнцезащитные очки (обычные и специальные), футляры для очков и контактных линз. Также включены т.н. \"Очки за час\", располагаемые в торговых центрах.\n\nКод используется системой TSYS. Для Visa и Mastercard используется MCC 8043."
        },
        {
            "mcc": 8049,
            "edited_description": "Podiatrists and Chiropodists",
            "combined_description": "Podiatrists and Chiropodists",
            "russian_name": "Ортопеды",
            "russian_description": "Лицензированные врачи, специализирующиеся на диагностике и лечении болезней ноги"
        },
        {
            "mcc": 8050,
            "edited_description": "Nursing and Personal Care Facilities",
            "combined_description": "Nursing and Personal Care Facilities",
            "russian_name": "Услуги персонального ухода",
            "russian_description": "Точки, которые предоставляют стационарные услуги по уходу за больными и связанные со здоровьем персональные услуги. Из-за их психического или физического состояния пациентам в этих учреждениях могут потребоваться введения лекарств и лечения или наблюдения за самостоятельными лекарствами в соответствии с указаниями врача. Этот MCC включает в себя дома для выздоравливающих, дома престарелых, помещения для хосписа и учреждения для престарелых, которые обеспечивают длительный уход и обычно не выполняют хирургическое вмешательство."
        },
        {
            "mcc": 8062,
            "edited_description": "Hospitals",
            "combined_description": "Hospitals",
            "russian_name": "Больницы",
            "russian_description": "Больницы, которые оказывают диагностические услуги, обширное медицинское лечение, включая хирургическое вмешательство и другие больничные услуги, а также услуги постоянного ухода для больных и раненых. Включает психиатрические больницы, детские больницы и родильные дома.\nДля ветеринарных клиник или больниц для животных используется MCC 0742."
        },
        {
            "mcc": 8071,
            "edited_description": "Medical and Dental Laboratories",
            "combined_description": "Medical and Dental Laboratories",
            "russian_name": "Стоматологические и медицинские лаборатории",
            "russian_description": "Точки, которые предоставляют услуги медицинских и стоматологических специалистов. Включает медицинские лаборатории, которые выполняют биологический анализ, анализ крови, анализ мочи, рентгенологический анализ, бактериологический анализ и диагностический анализ, а также стоматологические лаборатории, которые делают зубные протезы, искусственные зубы, коронки и мосты и индивидуальные ортодонтические приборы."
        },
        {
            "mcc": 8099,
            "edited_description": "Medical Services and Health Practitioners (Not Elsewhere Classified)",
            "combined_description": "Medical Services and Health Practitioners (Not Elsewhere Classified)",
            "russian_name": "Медицинские работники, медицинские услуги – нигде более не классифицированные",
            "russian_description": "Медицинские специалисты, которые не описаны другим, более конкретным MCC. Примеры включают физиотерапевтов, профессиональных терапевтов, психологов и других медицинских работников, таких как банки крови, клиники по планированию семьи, центры химической зависимости, службы тестирования слуха, лицензированные массажисты, хирургические клиники для замены волос и клиники спортивной медицины."
        },
        {
            "mcc": 8111,
            "edited_description": "Legal Services and Attorneys",
            "combined_description": "Legal Services and Attorneys",
            "russian_name": "Адвокаты, юридические услуги",
            "russian_description": "Точки, которые предоставляют юридические консультации и услуги. Такие точки могут специализироваться в одной области судебных процессов, таких как развод или банкротство или предоставлять полный спектр юридических услуг."
        },
        {
            "mcc": 8211,
            "edited_description": "Elementary and Secondary Schools",
            "combined_description": "Elementary and Secondary Schools",
            "russian_name": "Начальная и средняя школы",
            "russian_description": "Начальные и средние школы, обеспечивающие академическое обучение от детского сада до колледжа, включая государственные, частные, приходские школы, а также школы-интернаты. \n\nДля дошкольных заведений используется MCC 8351."
        },
        {
            "mcc": 8220,
            "edited_description": "Colleges, Junior Colleges, Universities, and ProfessionalSchools",
            "combined_description": "Colleges, Junior Colleges, Universities, and ProfessionalSchools",
            "russian_name": "Колледжи, университеты, профессиональные училища и техникумы",
            "russian_description": "Колледжи, университеты, теологические семинарии и профессиональные училища (в том числе стоматологические, юридические, инженерные и медицинские), которые предоставляют академические курсы и предоставляют ученые степени. Требованием для поступления должно быть, по крайней мере, диплом средней школы или его эквивалент.\n\nДля бизнес-школ и секретарских школ используется MCC 8244. Для профессиональных школ используется MCC 8249."
        },
        {
            "mcc": 8241,
            "edited_description": "Correspondence Schools",
            "combined_description": "Correspondence Schools",
            "russian_name": "Дистанционные школы",
            "russian_description": "Школы заочного обучения, которые предлагают учебные пособия по почте, отправляя студентам уроки и экзамены."
        },
        {
            "mcc": 8244,
            "edited_description": "Business and Secretarial Schools",
            "combined_description": "Business and Secretarial Schools",
            "russian_name": "Бизнес / секретарские школы",
            "russian_description": "Бизнес и секретарские школы, которые предлагают общие бизнес-тренинги, такие как управление бизнесом, офисные процедуры, обработка текстов, стенография и другие канцелярские навыки. Такие школы предлагают свидетельство об обучении, но не предлагают ученых степеней.\n\nДля профессиональных школ используется MCC 8249."
        },
        {
            "mcc": 8249,
            "edited_description": "Vocational Schools and Trade Schools",
            "combined_description": "Vocational Schools and Trade Schools",
            "russian_name": "Профессиональные школы и училища",
            "russian_description": "Профессионально-технические училища, которые предлагают обучение и инструктаж по таким специальностям, как сварка, механика, столярные работы, недвижимость и вождение грузовых автомобилей. Такие школы предлагают свидетельство об обучении, но не предлагают ученых степеней."
        },
        {
            "mcc": 8299,
            "edited_description": "Schools and Educational Services ( Not Elsewhere Classified)",
            "combined_description": "Schools and Educational Services ( Not Elsewhere Classified)",
            "russian_name": "Образовательные услуги,  нигде более не классифицированные",
            "russian_description": "Точки, которые предлагают образовательные услуги, которые не описаны другим, более конкретным MCC. К таким точкам относятся школы, в которых преподают музыку, театр, искусство, кулинарию, лепку, школы каратэ, обучение вождению автомобилей и безопасному движению, обучение полетам, обучение шитью и вязанию и т.д.\n\nДля танцевальных школ используется MCC 7911.\n\nДля музыкальных, театральных и художественных школ, которые предоставляют документы об академической степени, используется MCC 8220."
        },
        {
            "mcc": 8351,
            "edited_description": "Child Care Services",
            "combined_description": "Child Care Services",
            "russian_name": "Услуги ухода за детьми",
            "russian_description": "Точки, которые предоставляют услуги по уходу за детьми включая нянь, ясли и детские сады. Такие точки обычно ухаживают за младенцами и дошкольниками, но могут также заботиться о детях старшего возраста и могут предоставлять или не предоставлять образовательные программы.\n\nДля школ используется MCC 8211."
        },
        {
            "mcc": 8398,
            "edited_description": "Charitable and Social Service Organizations",
            "combined_description": "Charitable and Social Service Organizations",
            "russian_name": "Благотворительные организации и социальные службы - сбор средств",
            "russian_description": "Благотворительные (не политические) организации, которые собирают взносы, организации социального обслуживания, которые предоставляют услуги социального обеспечения, группы защиты интересов, общественные организации и агентства здравоохранения."
        },
        {
            "mcc": 8641,
            "edited_description": "Civic, Fraternal, and Social Associations",
            "combined_description": "Civic, Fraternal, and Social Associations",
            "russian_name": "Гражданские, социальные и братские ассоциации",
            "russian_description": "Ассоциации, занимающиеся гражданской, социальной или братской деятельностью. К таким ассоциациям относятся ассоциации и клубы выпускников, клубы повышения квалификации, клубы предпринимателей, общины, братские ложи, братства и клубы, социальные клубы, организации ветеранов и молодежные ассоциации.\n\nДеятельность этих групп может включать сбор политических средств; однако, если это является основной целью организации, используется MCC 8651."
        },
        {
            "mcc": 8651,
            "edited_description": "Political Organizations",
            "combined_description": "Political Organizations",
            "russian_name": "Политические организации",
            "russian_description": "Членские организации, которые поддерживают интересы национальных, государственных или местных политических партий или кандидатов, включая политические группы, организованные специально для сбора средств для политической партии или отдельного кандидата."
        },
        {
            "mcc": 8661,
            "edited_description": "Religious Organizations",
            "combined_description": "Religious Organizations",
            "russian_name": "Религиозные организации",
            "russian_description": "Религиозные организации, предоставляющие богослужения, религиозную подготовку или учебу, религиозные мероприятия и сбор средств. Примерами являются церкви, монастыри, мечети, святилища, синагоги и храмы."
        },
        {
            "mcc": 8675,
            "edited_description": "Automobile Associations",
            "combined_description": "Automobile Associations",
            "russian_name": "Автомобильные ассоциации",
            "russian_description": "Такие торговые точки предоставляют своим членам специальные услуги, такие как информация о путешествиях и состоянии дороги, карты и путеводители, а также специальные тарифы в ресторанах, отелях и агентствах по прокату автомобилей. Эти торговые точки часто взимают ежегодный членский взнос."
        },
        {
            "mcc": 8699,
            "edited_description": "Membership Organizations ( Not Elsewhere Classified)",
            "combined_description": "Membership Organizations ( Not Elsewhere Classified)",
            "russian_name": "Членские организации – нигде более не классифицированные",
            "russian_description": "Организации или ассоциации, которые не описаны другим, более конкретным MCC. Например, это могут быть исторические клубы, профсоюзы, поэтические клубы, художественные советы и ассоциации арендаторов или кондоминиумов.\n\nДля членства в оздоровительных и спортивных клубах используется MCC 7997."
        },
        {
            "mcc": 8734,
            "edited_description": "Testing Laboratories ( non-medical)",
            "combined_description": "Testing Laboratories ( non-medical)",
            "russian_name": "Испытательные лаборатории (немедицинские)",
            "russian_description": "Торговые точки, которые предоставляют немедицинские услуги тестирования другим предприятиям. Примерами таких услуг являются автомобильные испытания, калибровка и сертификация, тестирование продуктов питания, судебно-медицинская экспертиза, тестирование продуктов и загрязнений, а также услуги промышленной рентгенографии.\n\nДля медицинских испытательных лабораторий используется MCC 8071."
        },
        {
            "mcc": 8911,
            "edited_description": "Architectural – Engineering and Surveying Services",
            "combined_description": "Architectural – Engineering and Surveying Services",
            "russian_name": "Архитектурные, инженерные и геодезические услуги",
            "russian_description": "Точки, которые предоставляют профессиональные архитектурные, инженерные и земельно-, водно- и воздушные услуги геодезии. Сюда входят проектировщики домов и зданий, инженеры-кораблестроители, инженеры и проектировщики машин, а также инженеры-архитекторы."
        },
        {
            "mcc": 8931,
            "edited_description": "Accounting, Auditing, and Bookkeeping Services",
            "combined_description": "Accounting, Auditing, and Bookkeeping Services",
            "russian_name": "Аудит и бухгалтерский учет",
            "russian_description": "Точки, предоставляющие услуги бухгалтерского учета, бухгалтерии, выставления счетов, начисления заработной платы и другие сопутствующие аудиторские услуги, включая сертифицированных общественных бухгалтеров (CPA). Такие точки также могут предоставлять услуги по подготовке подоходного налога в дополнение к бухгалтерским и аудиторским услугам.\n\nДля точек, которые предоставляют услуги по подготовке подоходного налога, не предоставляя также аудиторские и бухгалтерские услуги, используется MCC 7276."
        },
        {
            "mcc": 8999,
            "edited_description": "Professional Services ( Not Elsewhere Defined)",
            "combined_description": "Professional Services ( Not Elsewhere Defined)",
            "russian_name": "Профессиональные услуги - нигде более не классифицированные",
            "russian_description": "Точки, занимающиеся традиционными «профессиями», которые предлагают узкоспециализированные услуги, и часто требуют от сотрудников получения дополнительного или специального образования или обучения для предоставления услуг. Этот MCC следует использовать только в том случае, если бизнес торговой точки не описывается другим, более конкретным MCC. К примерам таких точек относятся ипотечные брокеры, исследовательские фирмы, специалисты по финансовому планированию, графические дизайнеры, приглашенные докладчики и преподаватели, судебные стенографисты, оценщики недвижимости, исследовательские фирмы и аукционные дома."
        },
        {
            "mcc": 9211,
            "edited_description": "Court Costs, including Alimony and Child Support",
            "combined_description": "Court Costs, including Alimony and Child Support",
            "russian_name": "Судебные выплаты, включая алименты и детскую поддержку",
            "russian_description": "Местные, региональные и федеральные суды, которые администрируют и обрабатывают судебные издержки (такие как расходы на ведение дел и судебные издержки) и алименты."
        },
        {
            "mcc": 9222,
            "edited_description": "Fines",
            "combined_description": "Fines",
            "russian_name": "Штрафы",
            "russian_description": "Государственные органы, которые управляют и обрабатывают местные, региональные и федеральные штрафы и пени, штрафы за нарушение правил эксплуатации транспортных средств и штрафы, налагаемые на сообщество или имущество."
        },
        {
            "mcc": 9223,
            "edited_description": "Bail and Bond Payments",
            "combined_description": "Bail and Bond Payments",
            "russian_name": "Платежи по залогам и облигациям",
            "russian_description": "Торговые точки, которые отправляют залог в судебную систему в качестве гарантии появления обвиняемого"
        },
        {
            "mcc": 9311,
            "edited_description": "Tax Payments",
            "combined_description": "Tax Payments",
            "russian_name": "Налоговые платежи",
            "russian_description": "Местные, региональные и федеральные организации, которые занимаются финансовым администрированием и налогообложением, включая сбор налогов и штрафов, а также хранение и расходование средств. К таким торговым точкам относятся офисы оценщиков налога на имущество, таможенные бюро и государственные налоговые комиссии."
        },
        {
            "mcc": 9399,
            "edited_description": "Government Services ( Not Elsewhere Classified)",
            "combined_description": "Government Services ( Not Elsewhere Classified)",
            "russian_name": "Государственные услуги - нигде более не классифицированные",
            "russian_description": "Торговые точки, предоставляющие правительству общие вспомогательные услуги, такие как услуги управления персоналом, аудит, закупки и услуги по управлению зданиями, которые не описаны другим, более конкретным MCC кодом. Примерами могут служить комиссии по гражданским правам и государственной службе, бухгалтерии сектора государственного управления, офисы общего обслуживания, государственные органы снабжения, полицейские, пожарные и автотранспортные службы, а также национальные, государственные и городские парки. \n\nДля транзакций по программе внутригосударственных трансфертов (IGOTS) используется MCC 9405. \n\nДля государственных университетов и колледжей используется MCC 8220.\n\nТорговые точки, участвующие в продаже товаров или услуг правительству, должны использовать оптовый MCC, который лучше всего описывает бизнес."
        },
        {
            "mcc": 9402,
            "edited_description": "Postal Services – Government Only",
            "combined_description": "Postal Services – Government Only",
            "russian_name": "Почтовые услуги – только государственные",
            "russian_description": "Государственные почтовые отделения, включая местные почтовые отделения. Предоставляемые услуги включают в себя прием и обработку посылок и почты для доставки, продажу почтовых марок и услуги экспресс-рассылки.\n\nДля магазинов упаковки для почты, которые предоставляют услуги упаковки и продают марки, поздравительные открытки и упаковку, а также могут предоставлять услуги для UPS, Federal Express и других служб экспресс-почты, используется MCC 7399"
        },
        {
            "mcc": 9405,
            "edited_description": "Intra – Government Transactions",
            "combined_description": "Intra – Government Transactions",
            "russian_name": "Внутригосударственные закупки - только государственные",
            "russian_description": "Определяет транзакции между правительственными учреждениями, департаментами или агентствами, которые участвуют в программе внутригосударственных трансфертов (IGOTS)."
        },
        {
            "mcc": 9700,
            "edited_description": "Automated Referral Service ( For Visa Only)",
            "combined_description": "Automated Referral Service ( For Visa Only)",
            "russian_name": "Automated Referral Service (только VISA)",
            "russian_description": "Автоматизированная справочная служба - это сервис VisaNet, который позволяет авторизовать участника VIP. Ответ «реферальной» системы, чтобы набрать единственный бесплатный номер телефона, чтобы получить немедленный положительный или отрицательный ответ авторизации от эмитента, его уполномочивающего участника или резервного центра."
        },
        {
            "mcc": 9701,
            "edited_description": "Visa Credential Service ( For Visa Only)",
            "combined_description": "Visa Credential Service ( For Visa Only)",
            "russian_name": "Служба проверки учетных данных Visa (только VISA)",
            "russian_description": "Использование ограничено процессом аутентификации для обеспечения транзакций банковских карт через Интернет и другие сети в режиме онлайн."
        },
        {
            "mcc": 9702,
            "edited_description": "GCAS Emergency Services ( For Visa Only)",
            "combined_description": "GCAS Emergency Services ( For Visa Only)",
            "russian_name": "Аварийные службы GCAS (только VISA)",
            "russian_description": "Этот MCC предназначен для использования Visa только для того, чтобы члены и обработчики могли идентифицировать экстренные транзакции из Глобальных служб поддержки клиентов (GCAS)."
        },
        {
            "mcc": 9950,
            "edited_description": "Intra – Company Purchases ( For Visa Only)",
            "combined_description": "Intra – Company Purchases ( For Visa Only)",
            "russian_name": "Покупки внутри компании",
            "russian_description": "Продавцы, классифицируемые в рамках этого MCC обрабатывают транзакции по закупкам, представляющим внутренние переводы товаров и услуг между подразделениями"
        }
    ]
}
