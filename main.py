from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from moviepy.editor import *

# url do video a ser baixado
url = 'VIDEO_URL'

# pasta onde sera baixado
downloadPath = 'PATH_TO_DOWNLOAD'

try:
    # instancia o objeto do pytube
    youtube = YouTube(url)
except VideoUnavailable:
    # se o video nao estiver disponivel exibe a msg na tela
    print(f'Video {url} is unavailable, skipping.')
else:
    # pega o objeto streams que contem as opcoes disponiveis para download
    ytStreams = youtube.streams

    print('Video: ', url)
    print('Downloading in: ', downloadPath)

    # filtra o video com maior resolucao
    video = (ytStreams.filter(adaptive=True)
             .order_by('resolution')
             .desc()
             .first())

    # filtra o audio do tipo mp4
    audio = (ytStreams.filter(only_audio=True)
             .filter(file_extension='mp4')
             .order_by('itag')
             .desc()
             .first())

    #  baixa o video e o audio
    video.download(downloadPath)
    audio.download(downloadPath)

    print('\nFiles Downloaded!')
    print('\nMerging Files')

    # pega o nome dos arquivos baixados
    audio_path = downloadPath + "/" + audio.default_filename
    video_path = downloadPath + "/" + video.default_filename

    # cria o clipe de audio e video com os arquivos baixados
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # faz o merge dos dois arquivos
    video_clip_with_audio = video_clip.set_audio(audio_clip)

    # salva o novo arquivo
    video_clip_with_audio.write_videofile(downloadPath + "/mergedVideo.mp4")
    print('\nconcluido')
