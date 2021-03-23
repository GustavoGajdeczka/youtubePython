import PySimpleGUI as sg
class tela:
    def __init__(self):
        self.layout = None
    def inicial(self):
        self.layout = [
            [sg.Text('Destino', size=(20, 1)), sg.Input(key='path', size=(20,1)), sg.FolderBrowse(target='path')],
            [sg.Text('URL', size=(20, 1)), sg.Input(key='URL', size=(20,1))],
            [sg.Text('Tipo', size=(20, 1)), sg.Combo(['Video', 'Audio', 'Imagem'], key='tipo'), sg.Input(key='nome', size=(20,1))],
            [sg.Button('Fechar', key='close'), sg.Button('Baixar', key='baixar'), sg.Button('Converter', key='convert')]
        ]
        return sg.Window('youtubePython', self.layout, finalize=True)
    def convert(self):
        self.layout = [
            [sg.Text('Video', size=(20, 1)), sg.Input(key='video_convert', size=(20, 1)), sg.FilesBrowse(target='video_convert')],
            [sg.Text('Diretorio', size=(20, 1)), sg.Input(key='_path', size=(20,1)), sg.FolderBrowse(target='_path')],
            [sg.Text('Nome', size=(20, 1)), sg.Input(key='name', size=(20, 1))],
            [sg.Button('Converter', key='b_convert'), sg.Button('Voltar', key='voltar')]
        ]
        return sg.Window('Conversor', self.layout, finalize=True)

