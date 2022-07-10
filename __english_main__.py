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
    {
        "title": "Переклади слова рівня B1 ч. 1",
        "parts": [
            {"q-en": "To commit", "a-uk": "Здійснити, зафіксувати, доручити"},
            {"q-en": "verification", "a-uk": "Перевірка"},
            {"q-en": "Updated", "a-uk": "Оновлений"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 2",
        "parts": [
            {"q-en": "А youth", "a-uk": "Молодь, юнак, молодість"},
            {"q-en": "To consulate", "a-uk": "Консультувати"},
            {"q-en": "Careful", "a-uk": "Обережний"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 3",
        "parts": [
            {"q-en": "Fashionable", "a-uk": "Модний"},
            {"q-en": "Tedious", "a-uk": "Втомливий, копіткий, набридливий"},
            {"q-en": "immunization", "a-uk": "Імунізація"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 4",
        "parts": [
            {"q-en": "contest", "a-uk": "Змагання, боротьба, конкурс"},
            {"q-en": "Predominantly", "a-uk": "Постійно"},
            {"q-en": "improvement", "a-uk": "Поліпшення"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 5",
        "parts": [
            {"q-en": "А godliness", "a-uk": "Благочестя, бадьорість"},
            {"q-en": "А challenge", "a-uk": "Виклик, складність"},
            {"q-en": "Unmatched", "a-uk": "Неповторний, неперевершений"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 6",
        "parts": [
            {"q-en": "suspiciousness", "a-uk": "Підозрілість"},
            {"q-en": "А mindfulness", "a-uk": "Уважність, мислення, свідомість"},
            {"q-en": "kindness", "a-uk": "Доброта"},
        ],
    },
    {
        "title": "Переклади слова рівня B1 ч. 7",
        "parts": [
            {"q-en": "At once", "a-uk": "Негайно"},
            {"q-en": "Private", "a-uk": "Особистий, приватний"},
            {"q-en": "medication", "a-uk": "Ліки"},
        ],
    },
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
