import asyncio, tts, os, video, requests

# from scraper import scrape
from upload import upload_to_tiktok
from utils import config

posts = [
    # {
    #     "title": "Переклади слова рівня А1 ч. 1",
    #     "parts": [
    #         {"q-en": "Together", "a-uk": "Разом"},
    #         {"q-en": "apartment", "a-uk": "Квартира"},
    #         {"q-en": "west", "a-uk": "Захід"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 2",
    #     "parts": [
    #         {"q-en": "To laugh", "a-uk": "Сміятись"},
    #         {"q-en": "rock", "a-uk": "Скеля"},
    #         {"q-en": "Also", "a-uk": "Також"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 3",
    #     "parts": [
    #         {"q-en": "motel", "a-uk": "Мотель"},
    #         {"q-en": "ocean", "a-uk": "Океан"},
    #         {"q-en": "To communicate", "a-uk": "Спілкуватись"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 4",
    #     "parts": [
    #         {"q-en": "To drink", "a-uk": "Пити"},
    #         {"q-en": "Responsible", "a-uk": "Відповідальний, надійний"},
    #         {"q-en": "sweetheart", "a-uk": "Партнер, коханий"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 5",
    #     "parts": [
    #         {"q-en": "Eventually", "a-uk": "В кінці кінців"},
    #         {"q-en": "Big", "a-uk": "Великий"},
    #         {"q-en": "To help", "a-uk": "Допомогати"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 6",
    #     "parts": [
    #         {"q-en": "Available", "a-uk": "Доступний"},
    #         {"q-en": "To play", "a-uk": "Грати"},
    #         {"q-en": "food order", "a-uk": "Замовленя їжі"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня А1 ч. 7",
    #     "parts": [
    #         {"q-en": "dialogue", "a-uk": "Діалог"},
    #         {"q-en": "To sell", "a-uk": "Продавати"},
    #         {"q-en": "Honestly", "a-uk": "Чесно"},
    #         {"q-en": "To continue", "a-uk": "Продовжувати"},
    #     ],
    # },
    # { "title": "Переклади слова рівня A1 ч. 7", "parts": [ {"q-en": "Remote", "a-uk": "Віддалений"}, {"q-en": "wallet", "a-uk": "Гаманець"}, {"q-en": "To have", "a-uk": "Мати"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 8", "parts": [ {"q-en": "Daily", "a-uk": "Щоденно"}, {"q-en": "Beautiful", "a-uk": "Гарний"}, {"q-en": "To introduce", "a-uk": "Уявляти"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 9", "parts": [ {"q-en": "Again", "a-uk": "Знову"}, {"q-en": "To live", "a-uk": "Жити"}, {"q-en": "party", "a-uk": "Вечірка"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 10", "parts": [ {"q-en": "Foreign", "a-uk": "Іноземний"}, {"q-en": "Confident", "a-uk": "Впевнений"}, {"q-en": "Safe", "a-uk": "Безпечний"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 11", "parts": [ {"q-en": "To cook", "a-uk": "Готувати"}, {"q-en": "To let", "a-uk": "Залишати"}, {"q-en": "water", "a-uk": "Вода"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 12", "parts": [ {"q-en": "To swim", "a-uk": "Плавати"}, {"q-en": "To make", "a-uk": "Зробити"}, {"q-en": "Hot", "a-uk": "Гарячий"}, ], },
    # { "title": "Переклади слова рівня A1 ч. 13", "parts": [ {"q-en": "To hesitate", "a-uk": "Сумніватись"}, {"q-en": "To start", "a-uk": "Стартувати"}, {"q-en": "bird", "a-uk": "Птах"}, ], },
    # {
    #     "title": "Переклади слова рівня A1 ч. 15",
    #     "parts": [
    #         {"q-en": "Poor", "a-uk": "Бідний"},
    #         {"q-en": "Once", "a-uk": "Один раз"},
    #         {"q-en": "ticket", "a-uk": "Білет"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 16",
    #     "parts": [
    #         {"q-en": "house", "a-uk": "Будинок"},
    #         {"q-en": "To finish", "a-uk": "Закінчувати"},
    #         {"q-en": "To take", "a-uk": "Брати"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 17",
    #     "parts": [
    #         {"q-en": "map", "a-uk": "Мапа"},
    #         {"q-en": "work", "a-uk": "Робота"},
    #         {"q-en": "Clever", "a-uk": "Розумний"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 18",
    #     "parts": [
    #         {"q-en": "Instead", "a-uk": "Замість"},
    #         {"q-en": "Fine", "a-uk": "Чудовий"},
    #         {"q-en": "Dirty", "a-uk": "Брудний"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 19",
    #     "parts": [
    #         {"q-en": "Rare", "a-uk": "Рідкісний"},
    #         {"q-en": "fire", "a-uk": "Вогонь+"},
    #         {"q-en": "Badly", "a-uk": "Погано"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 20",
    #     "parts": [
    #         {"q-en": "To check up", "a-uk": "Перевіряти"},
    #         {"q-en": "mountain", "a-uk": "Гора"},
    #         {"q-en": "family", "a-uk": "Сімʼя"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 21",
    #     "parts": [
    #         {"q-en": "price", "a-uk": "Вартість, ціна"},
    #         {"q-en": "Inside", "a-uk": "Усередині"},
    #         {"q-en": "Dangerous", "a-uk": "Небезпечний"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 22",
    #     "parts": [
    #         {"q-en": "Above", "a-uk": "Вище"},
    #         {"q-en": "To come", "a-uk": "Приходити"},
    #         {"q-en": "To pass", "a-uk": "Проходити"},
    #     ],
    # },
    # {
    #     "title": "Переклади слова рівня A1 ч. 23",
    #     "parts": [
    #         {"q-en": "To think", "a-uk": "Думати"},
    #         {"q-en": "evening", "a-uk": "Вечір"},
    #         {"q-en": "date", "a-uk": "Побачення"},
    #     ],
    # },
    # {'title': 'Переклади слова рівня B1 ч. 1', 'parts': [{'q-en': 'To commit', 'a-uk': 'Здійснити, зафіксувати, доручити'}, {'q-en': 'verification', 'a-uk': 'Перевірка'}, {'q-en': 'Updated', 'a-uk': 'Оновлений'}]},
    # {'title': 'Переклади слова рівня B1 ч. 2', 'parts': [{'q-en': 'А youth', 'a-uk': 'Молодь, юнак, молодість'}, {'q-en': 'To consulate', 'a-uk': 'Консультувати'}, {'q-en': 'Careful', 'a-uk': 'Обережний'}]},
    # {'title': 'Переклади слова рівня B1 ч. 3', 'parts': [{'q-en': 'Fashionable', 'a-uk': 'Модний'}, {'q-en': 'Tedious', 'a-uk': 'Втомливий, копіткий, набридливий'}, {'q-en': 'immunization', 'a-uk': 'Імунізація'}]},
    # {'title': 'Переклади слова рівня B1 ч. 4', 'parts': [{'q-en': 'contest', 'a-uk': 'Змагання, боротьба, конкурс'}, {'q-en': 'Predominantly', 'a-uk': 'Постійно'}, {'q-en': 'improvement', 'a-uk': 'Поліпшення'}]},
    # {'title': 'Переклади слова рівня B1 ч. 5', 'parts': [{'q-en': 'А godliness', 'a-uk': 'Благочестя, бадьорість'}, {'q-en': 'А challenge', 'a-uk': 'Виклик, складність'}, {'q-en': 'Unmatched', 'a-uk': 'Неповторний, неперевершений'}]},
    # {'title': 'Переклади слова рівня B1 ч. 6', 'parts': [{'q-en': 'suspiciousness', 'a-uk': 'Підозрілість'}, {'q-en': 'А mindfulness', 'a-uk': 'Уважність, мислення, свідомість'}, {'q-en': 'kindness', 'a-uk': 'Доброта'}]},
    # {'title': 'Переклади слова рівня B1 ч. 7', 'parts': [{'q-en': 'At once', 'a-uk': 'Негайно'}, {'q-en': 'Private', 'a-uk': 'Особистий, приватний'}, {'q-en': 'medication', 'a-uk': 'Ліки'}]},
    # { "title": "Переклади слова рівня B1 ч. 7", "parts": [ {"q-en": "А proficiency", "a-uk": "Майстерність, уміння, кваліфікація"}, {"q-en": "rivalry", "a-uk": "Суперництво, протистояння"}, {"q-en": "Relentlessly", "a-uk": "Безперервно"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 8", "parts": [ {"q-en": "Moreover", "a-uk": "Більш того"}, {"q-en": "To reserve", "a-uk": "Резервувати"}, {"q-en": "Contemporary", "a-uk": "Сучасний, актуальний"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 9", "parts": [ {"q-en": "To connect", "a-uk": "З'єднати"}, {"q-en": "To empower", "a-uk": "Наділити повноваженнями, розширювати"}, {"q-en": "А hospitality", "a-uk": "Гостинність, привітність"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 10", "parts": [ {"q-en": "А bad luck", "a-uk": "Невезіння, нещастя"}, {"q-en": "contradiction", "a-uk": "Протиріччя"}, {"q-en": "Ridiculous", "a-uk": "Безглуздий, смішний"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 11", "parts": [ {"q-en": "circumstance", "a-uk": "Обставина, випадок, подія"}, {"q-en": "To collaborate", "a-uk": "Співпрацювати"}, {"q-en": "justice", "a-uk": "Справедливість"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 12", "parts": [ {"q-en": "To implement", "a-uk": "Впровадити, реалізувати, здійснити"}, {"q-en": "To regard", "a-uk": "Розглядати, враховувати, ставитись"}, {"q-en": "inequality", "a-uk": "Нерівність"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 13", "parts": [ {"q-en": "To encourage", "a-uk": "Стимулювати"}, {"q-en": "hopelessness", "a-uk": "Безнадійність"}, {"q-en": "fervor", "a-uk": "Палкість, запал, завзяття"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 14", "parts": [ {"q-en": "Reasonable", "a-uk": "Розумний, доцільний"}, {"q-en": "celebration", "a-uk": "Захід, подія"}, {"q-en": "А knowledge", "a-uk": "Знання, пізнання"}, ], }
    # { "title": "Переклади слова рівня B1 ч. 15", "parts": [ {"q-en": "To estimate", "a-uk": "Оцінювати"}, {"q-en": "To accomplish", "a-uk": "Виконати, завершити, здійснити"}, {"q-en": "To deliver", "a-uk": "Доставляти, постачати, приносити"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 16", "parts": [ {"q-en": "Multiple", "a-uk": "Множинний, чисельний"}, {"q-en": "To tailor", "a-uk": "Пристосувати"}, {"q-en": "Fundamental", "a-uk": "Основоположний"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 17", "parts": [ {"q-en": "To transfer", "a-uk": "Передавати, перераховувати"}, {"q-en": "To make sure", "a-uk": "Впевнитись"}, {"q-en": "А provocation", "a-uk": "Провокація"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 18", "parts": [ {"q-en": "Naughty", "a-uk": "Пустотливий"}, {"q-en": "А disorder", "a-uk": "Розлад"}, {"q-en": "Multi-channel", "a-uk": "Багатоканальний"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 19", "parts": [ {"q-en": "А prerequisite", "a-uk": "Передумова, умова"}, {"q-en": "prevention", "a-uk": "Профілактика"}, {"q-en": "Scarcely", "a-uk": "Ледве"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 20", "parts": [ {"q-en": "To unify", "a-uk": "Об'єднувати"}, {"q-en": "Actually", "a-uk": "Загалом взагалі-то"}, {"q-en": "To specialize", "a-uk": "Спеціалізуватися"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 21", "parts": [ {"q-en": "Otherwise", "a-uk": "Інакше"}, {"q-en": "Infrequently", "a-uk": "Рідко"}, {"q-en": "In vain", "a-uk": "Даремно"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 22", "parts": [ {"q-en": "Yet", "a-uk": "Ще, досі"}, {"q-en": "Individual", "a-uk": "Особистий, індивідуальний"}, {"q-en": "To elaborate", "a-uk": "Розробляти, опрацьовувати"}, ], },
    # { "title": "Переклади слова рівня B1 ч. 23", "parts": [ {"q-en": "To command", "a-uk": "Командувати"}, {"q-en": "Foremost", "a-uk": "Передовий, основний, головний"}, {"q-en": "To prioritize", "a-uk": "Розставити пріоритети"}, ], },
]


async def main():
    # Fetching posts from r/AskReddit
    # headers = { 'user-agent':'py-reddit-scraping:0:1.0 (by u/ur_name)' }
    # posts = requests.get('https://www.reddit.com/r/AskReddit/top.json?t=day&limit=30', headers=headers).json()['data']['children']

    for post in posts:
        try:
            # Avoid getting banned, no NSFW posts
            # if 'nsfw' in post['data']['whitelist_status']:
            #    continue

            # url = post['data']['url']
            # name = url.split('/')[-2]
            name = post["title"]
            print(f"⏱ Processing post: {name}")

            # Make sure we have not already rendered/uploaded post
            if name in [entry.split(".")[0] for entry in os.listdir("render")]:
                print("❌ Post already processed!")
                continue

            # Clean 'temporary' files from last video
            for file in os.listdir("output"):
                os.remove(f"output/{file}")

            # Scraping the post, screenshotting, etc
            print("📸 Screenshotting post...")
            # data = scrape(url)
            # if not data:
            #    print("❌ Failed to screenshot post!")
            #    continue

            # Generate TTS clips for each comment
            print("\n📢 Generating voice clips...", end="", flush=True)
            # voice = await tts.get_voice()
            texts = {}
            for i, part in enumerate(post["parts"]):
                print(".", end="", flush=True)
                tts.generate_google(name, "post", "uk")
                for key, text in part.items():
                    q_or_a, language = key.split("-")
                    sound_file_name = f"{i}-{q_or_a}"
                    tts.generate_google(text, sound_file_name, language)
                    texts[sound_file_name] = text

            # Render & Upload
            print("\n🎥 Rendering video...")
            if video.render_qna(name, texts, name):
                # Upload video if rendered
                print("🌟 Uploading to TikTok...")
                # if upload_to_tiktok(name,data["post"]):
                #    print("✅ Uploaded successfully!")
                # else:
                #    print("❌ Failed to upload!")
        except Exception as e:
            if config["debug"]:
                raise e
            pass


if __name__ == "__main__":
    [
        os.mkdir(dir)
        for dir in ["output", "render", "backgrounds"]
        if not os.path.exists(dir)
    ]
    asyncio.run(main())
