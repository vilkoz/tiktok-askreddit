import random
import edge_tts
import asyncio
from gtts import gTTS

async def get_voice(language="en"):
    voices = [voice for voice in await edge_tts.list_voices() if f"{language}-" in voice["Locale"]]
    return random.choice(voices)["Name"]

async def generate(text,name,voice):
    communicate = edge_tts.Communicate()
    with open(f"output/{name}.mp3","wb") as fp:
        async for i in communicate.run(text,voice=voice):
            if i[2] is not None:
                fp.write(i[2])

def generate_google(text, name, language):
    tts = gTTS(text, lang=language)
    tts.save(f"output/{name}.mp3")
    
    

async def main(l):
    print(await get_voice(language=l))

if __name__ == "__main__":
    #asyncio.run(main('ua'))
    generate_google('доброго вечора', 'test', 'uk')
    
