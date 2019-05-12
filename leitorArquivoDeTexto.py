from gtts import gTTS
from pygame import mixer
import os.path  # conexão com dados externos

diretorio = input('Digite o diretório de arquivo de texto')

teste = os.path.isfile(diretorio)

if teste == True:
    print('O arquivo está sendo carregado, aguarde!')
    file_data = open(diretorio)  # Abre o arquivo dentro do python
    file_data = file_data.read()  # Realiza a leitura do texto

    print('Salvando o arquivo ...')
    voz = gTTS(file_data, lang='pt')
    voz.save('voz.mp3')

    print('Falando ...')

    mixer.init()
    mixer.music.load('voz.mp3')
    mixer.music.play()

else:
    print('Diretorio não encontrado!')
