from moviepy.editor import *
import random,os

resolution = (1080,1920)

def render(name):
    # Create clip 'flow'
    flow = ['post']
    for i in range(10):
        if os.path.exists(f'output/{i}.mp3'):
            flow.append(str(i))

    # Load all the clips
    image_clips = []
    sound_clips = []
    duration = 0
    for part in flow:
        sound_clips.append(AudioFileClip(f"output/{part}.mp3"))
        image_clips.append(ImageClip(f"output/{part}.png",duration=sound_clips[-1].duration).fx(vfx.resize,width=resolution[0]*0.9).set_position(("center","center")))
        duration += sound_clips[-1].duration
        # Ensure length of video
        if duration > 90:
            break

    # Combine all the clips into one
    image_clips = concatenate_videoclips(image_clips).set_position(("center","center"))
    sound_clips = concatenate_audioclips(sound_clips)

    # 3 minute limit
    if sound_clips.duration > 60*2.9:
        return False

    #Loading background
    background_clip = "backgrounds/" + random.choice(os.listdir("backgrounds"))
    background = VideoFileClip(background_clip).fx(vfx.resize, height=resolution[1]).fx(vfx.loop, duration=image_clips.duration).set_position(("center","center"))
    
    # Composite all the components
    composite = CompositeVideoClip([background,image_clips],resolution)
    composite.audio = sound_clips
    composite.duration = sound_clips.duration

    # Render
    composite.write_videofile(f'render/{name}.mp4',threads=4,fps=24)
    return True


def render_qna(name, texts, title):
    #print(TextClip.list('font'))
    # Create clip 'flow'
    flow = ['post']
    for key in texts.keys():
        if os.path.exists(f'output/{key}.mp3'):
            flow.append(key)
            _, q_or_a = key.split('-')
            if q_or_a == 'q':
                flow.append('coundown-1')
                flow.append('coundown-2')
                flow.append('coundown-3')
            else:
                flow.append('pause')
    print('flow:', flow)
    return False
                

    # Load all the clips
    image_clips = []
    sound_clips = []
    duration = 0
    for part in flow:
        if 'coundown' in part:
            sound_clips.append(AudioClip(make_frame=lambda t: 0, duration=0.8, fps=44100))
        elif 'pause' in part:
            sound_clips.append(AudioClip(make_frame=lambda t: 0, duration=0.1, fps=44100))
        else:
            sound_clips.append(AudioFileClip(f"output/{part}.mp3"))

        #if 'coundown' not in part:
        #    sound_clips.append(AudioFileClip(f"output/{part}.mp3"))
        #else:
        #    sound_clips.append(AudioClip(make_frame=lambda t: 0, duration=0.8, fps=44100))
  
        #image_clips.append(ImageClip(f"output/{part}.png",duration=sound_clips[-1].duration).fx(vfx.resize,width=resolution[0]*0.9).set_position(("center","center")))
        text = texts.get(part, part.split('-')[1] if 'coundown' in part else title)
        print(part, texts, text)
        image_clips.append(TextClip(txt=text,
            bg_color='black',
            color='white',
            font='Helvetica-Neue',
            fontsize=32
        ).set_duration(sound_clips[-1].duration).fx(vfx.resize,width=resolution[0]*0.9).set_position(("center","center")))
        image_clips[-1].audio = sound_clips[-1]
        duration += sound_clips[-1].duration
        # Ensure length of video
        if duration > 90:
            break

    # Combine all the clips into one
    image_clips = concatenate_videoclips(image_clips).set_position(("center","center"))
    sound_clips = concatenate_audioclips(sound_clips)
    sound_clips.write_audiofile("sound.wav", 44100, 2, 2000,"pcm_s32le")

    # 3 minute limit
    if sound_clips.duration > 60*2.9:
        return False

    #Loading background
    background_clip = "backgrounds/" + random.choice(os.listdir("backgrounds"))
    background = VideoFileClip(background_clip).fx(vfx.resize, height=resolution[1]).fx(vfx.loop, duration=image_clips.duration).set_position(("center","center"))
    
    # Composite all the components
    #composite = CompositeVideoClip([image_clips],resolution)
    composite = CompositeVideoClip([background,image_clips],resolution)
    composite.audio = sound_clips
    composite.duration = sound_clips.duration

    # Render
    composite.write_videofile(f'render/{name}.mp4',threads=4,fps=24)
    return True
