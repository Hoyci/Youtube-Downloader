import pytube
from pytube.exceptions import RegexMatchError
from pytube import YouTube
from termcolor import colored

print(colored('Bem-vindo ao Youtuber Downloader', 'blue'))

def link():
    link = input('Insira o link do vídeo: ')
    try:
        yt = YouTube(link)
        return yt
    except RegexMatchError as error:
        print('Link inválido')

def download():
    yt = link()
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    
def informacao():
    yt = link()
    print(colored(f'O título do vídeo é "{yt.title}".\nO vídeo tem {yt.views} visualizações.\nO autor do vídeo é : "{yt.author}"', 'red'))
    print()


def programa():
    try:
        acao = input('O que você deseja fazer? \nPara baixar o vídeo digite "download" \nPara ter informações sobre o vídeo digite "informacao": ')
        if acao.upper() == 'DOWNLOAD':
            download()
            print(colored('Download realizado com sucesso!', 'red'))
        elif acao.upper() == 'INFORMACAO':
            informacao()
        elif acao == '0':
            print('Programa encerrado!')
        else:
            print('Você solicitou uma ação inválida.')
    except AttributeError:
        print()

programa()

while True:
    seila = input('Você deseja realizar uma nova tarefa? [S/N]: ')
    if seila.upper() == 'S':
        programa()
    elif seila.upper() == 'N':
        print('Programa encerrado!')
        break
    else:
        print('Acão inválida.')