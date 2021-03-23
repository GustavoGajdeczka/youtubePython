from pytube import YouTube
import PySimpleGUI as sg
import urllib.request
import sys
from view import tela
from moviepy.editor import *

sg.theme('DarkGreen')

Tela = tela()

inicial, converter = Tela.inicial(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == inicial and event == sg.WIN_CLOSED or event == 'close':
        break
    if event == 'baixar':
        if values['tipo'] == 'Video' or values['tipo'] == 'Audio':
            yt = YouTube(values['URL'])
            if values['tipo'] == 'Video':
                ys = yt.streams.get_highest_resolution()
            if values['tipo'] == 'Audio':
                ys = yt.streams.get_audio_only()
            try:
                print("Baixando....")
                ys.download(values['path'])
                sg.Popup("!Baixado!")
            except ValueError:
                sg.Popup("Erro: não foi possivel Baixar")
        
        if values['tipo'] == 'Imagem':
            try:
                nome = str(values['path'] + "/" + values['nome'] + ".jpg")
                print(nome)
                urllib.request.urlretrieve(values['URL'], nome)
                sg.Popup("Imagem salva! =)")
            except:
                erro = sys.exc_info()
                print("Ocorreu um erro:", erro)
    if window == inicial and event == 'convert':
        converter = Tela.convert()
        inicial.hide()
    if window == converter and event == sg.WIN_CLOSED:
        break
    if window == converter and event == 'voltar':
        inicial.un_hide()
        converter.hide()
    if window == converter and event == 'b_convert':
        mp4_file = values['video_convert']
        mp3_file = str(values['_path'] + "/" + values['name'] + '.mp3')
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
            
window.close()