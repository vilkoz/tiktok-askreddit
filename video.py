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


def __get_text_clip_with_params(text, fontsize=128):
    return TextClip(txt=text,
        bg_color='pink',
        color='white',
        stroke_color='black',
        stroke_width=1,
        font='Helvetica-Neue',
        fontsize=fontsize
    )


def _make_countdown_clip(part):
    _, count = part.split('-')
    sound_clip = AudioClip(make_frame=lambda t: 0, duration=0.8, fps=44100)
    image_clip = __get_text_clip_with_params(count, 128)
    image_clip = image_clip.set_duration(sound_clip.duration)
    #image_clip = image_clip.fx(vfx.resize,width=resolution[0]*0.9)
    #image_clip = image_clip.set_position(("center",0.7), relative=True)

    return image_clip, sound_clip


def _make_text_clip(part, texts, title):
    sound_clip = AudioFileClip(f"output/{part}.mp3")

    text = texts.get(part, title)
    print(part, texts, text)
    image_clip = __get_text_clip_with_params(text)
    image_clip = image_clip.set_duration(sound_clip.duration)
    image_clip = image_clip.fx(vfx.resize,width=resolution[0]*0.9)
    image_clip = image_clip.set_position(("center","center"))

    return image_clip, sound_clip


def _make_clip_with_text(part, texts, title):
    if 'coundown' in part:
        return _make_countdown_clip(part)
    return _make_text_clip(part, texts, title)


def __add_countdown_to_question(q_image, q_audio, countdown):
    image_clips = []
    sound_clips = [q_audio]
    for count in countdown:
        image, sound = _make_countdown_clip(count)
        image_clips.append(image)
        sound_clips.append(sound)

    image_clips = concatenate_videoclips(image_clips)

    question_duration = q_image.duration
    print('duration before:', q_image.duration)
    q_image = q_image.set_duration(question_duration + image_clips.duration)
    print('duration after:', q_image.duration)
    composite_video = CompositeVideoClip(
        [
            q_image,
            image_clips.set_start(question_duration).set_position(("center", resolution[1]*0.7)),
        ],
        size=resolution,
    )

    sound_clips = concatenate_audioclips(sound_clips)
    return composite_video, sound_clips


def render_qna(name, texts, title):
    #print(TextClip.list('font'))
    # Create clip 'flow'
    flow = ['post']
    for key in texts.keys():
        if os.path.exists(f'output/{key}.mp3'):
            flow.append(key)
            _, q_or_a = key.split('-')
            if q_or_a == 'q':
                flow.append(['coundown-1', 'coundown-2', 'coundown-3'])
    print('flow:', flow)
                

    # Load all the clips
    image_clips = []
    sound_clips = []
    duration = 0
    for part in flow:
        if type(part) == list:
            image_clip, sound_clip = __add_countdown_to_question(image_clips[-1], sound_clips[-1], part)
            image_clips[-1] = image_clip
            sound_clips[-1] = sound_clip
        else:
            image_clip, sound_clip = _make_clip_with_text(part, texts, title)
            if part.endswith('a'):
                duration = sound_clip.duration + 0.2
                sound_clip.set_duration(duration)
                image_clip.set_duration(duration)
            sound_clips.append(sound_clip)
            image_clips.append(image_clip)
        duration += sound_clips[-1].duration
        # Ensure length of video
        if duration > 90:
            break

    # Combine all the clips into one
    image_clips = concatenate_videoclips(image_clips).set_position(("center","center"))
    sound_clips = concatenate_audioclips(sound_clips)
    # convert audio from mp3 to wav
    sound_clips.write_audiofile("output/sound_clips.wav", 44100, 2, 2000,"pcm_s32le")
    sound_clips = AudioFileClip("output/sound_clips.wav")

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
    composite.write_videofile(f'render/{name}.mp4',threads=4,fps=24,
        audio_fps=44100, audio_nbytes=2, audio_bufsize=2000, audio_codec='aac'
    )
    return True
