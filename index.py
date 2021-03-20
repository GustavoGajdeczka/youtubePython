from pytube import YouTube
import PySimpleGUI as sg
import urllib.request
import sys
from moviepy.editor import *

sg.theme('DarkGreen')

def menu():
    layout = [
        [sg.Text('Destino', size=(20, 1)), sg.Input(key='path', size=(20,1)), sg.FolderBrowse(target='path')],
        [sg.Text('URL', size=(20, 1)), sg.Input(key='URL', size=(20,1))],
        [sg.Text('Tipo', size=(20, 1)), sg.Combo(['Video', 'Audio', 'Imagem'], key='tipo'), sg.Input(key='nome', size=(20,1))],
        [sg.Button('Fechar', key='close'), sg.Button('Baixar', key='baixar'), sg.Button('Converter', key='convert')]
    ]
    return sg.Window('youtubePython', layout, finalize=True)

def tela_convert():
    layout = [
        [sg.Text('Video', size=(20, 1)), sg.Input(key='video_convert', size=(20, 1)), sg.FilesBrowse(target='video_convert')],
        [sg.Text('Diretorio', size=(20, 1)), sg.Input(key='_path', size=(20,1)), sg.FolderBrowse(target='_path')],
        [sg.Text('Nome', size=(20, 1)), sg.Input(key='name', size=(20, 1))],
        [sg.Button('Converter', key='b_convert'), sg.Button('Voltar', key='voltar')]
    ]
    return sg.Window('Conversor', layout, finalize=True)

menu, tela_converter = menu(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == menu and event == sg.WIN_CLOSED or event == 'close':
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
    if window == menu and event == 'convert':
        tela_converter = tela_convert()
        menu.hide()
    if window == tela_converter and event == sg.WIN_CLOSED:
        break
    if window == tela_converter and event == 'voltar':
        menu.un_hide()
        tela_converter.hide()
    if window == tela_converter and event == 'b_convert':
        mp4_file = values['video_convert']
        mp3_file = str(values['_path'] + "/" + values['name'] + '.mp3')
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
            
window.close()