import asyncio,tts,os,video,requests
#from scraper import scrape
from upload import upload_to_tiktok
from utils import config

posts = [
  {
    'title': 'ЩО тобі не подобається',
    'parts': [
      { 'q-en': 'собака', 'a-uk': 'dog' },
    ]
  }
]

async def main():
    # Fetching posts from r/AskReddit
    #headers = { 'user-agent':'py-reddit-scraping:0:1.0 (by u/ur_name)' }
    #posts = requests.get('https://www.reddit.com/r/AskReddit/top.json?t=day&limit=30', headers=headers).json()['data']['children']
    
    for post in posts:
        try:
            # Avoid getting banned, no NSFW posts
            #if 'nsfw' in post['data']['whitelist_status']:
            #    continue

            #url = post['data']['url']
            #name = url.split('/')[-2]
            name = post['title']
            print(f"⏱ Processing post: {name}")

            # Make sure we have not already rendered/uploaded post
            if name in [entry.split('.')[0] for entry in os.listdir('render')]:
                print("❌ Post already processed!")
                continue

            # Clean 'temporary' files from last video
            for file in os.listdir('output'):
                os.remove(f'output/{file}')

            # Scraping the post, screenshotting, etc
            print("📸 Screenshotting post...")
            #data = scrape(url)
            #if not data:
            #    print("❌ Failed to screenshot post!")
            #    continue

            # Generate TTS clips for each comment
            print("\n📢 Generating voice clips...",end="",flush=True)
            #voice = await tts.get_voice()
            texts = {}
            for i, part in enumerate(post['parts']):
                print('.',end="",flush=True)
                tts.generate_google(name, 'post', 'uk')
                for key, text in part.items():
                    q_or_a, language = key.split('-')
                    sound_file_name = f'{i}-{q_or_a}'
                    tts.generate_google(text, sound_file_name, language)
                    texts[sound_file_name] = text

            # Render & Upload
            print("\n🎥 Rendering video...")
            if video.render_qna(name, texts, name):
                # Upload video if rendered
                print("🌟 Uploading to TikTok...")
                #if upload_to_tiktok(name,data["post"]):
                #    print("✅ Uploaded successfully!")
                #else:
                #    print("❌ Failed to upload!")
        except Exception as e:
            if config['debug']:
                raise e
            pass

if __name__ == '__main__':
    [os.mkdir(dir) for dir in ['output','render','backgrounds'] if not os.path.exists(dir)]
    asyncio.run(main())
