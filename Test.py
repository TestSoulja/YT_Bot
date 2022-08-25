import speech_recognition as speech_recog

sample_audio = speech_recog.AudioFile('/Users/s.ekker/PycharmProjects/')

with sample_audio as audio_file:
    audio_content = recog.record(audio_file)