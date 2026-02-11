import yt_dlp, os
from pytubefix import YouTube 
from pytubefix.cli import on_progress, Playlist

lista_titulo, lista_url = [], []
n = 0
substring_ig, substring_pl = "instagram", "playlist"
substring_yt = "youtu"
ytdl_opts = {
    "outtmpl": "%(id)s.%(ext)s",
}  


def definir_local(): # codigo velho podre que funciona e esta sendo reutilizado
    global local_salvo2, conteudo, local

    with open(__file__, "r", encoding="utf-8") as f:
        conteudo = f.readlines()
        if remover == True:
            local_salvo2 = input("Digite o novo local de destino dos downloads: ")
            nova_linha = f'local_salvo = r"{local_salvo2}"\n'
            conteudo[0] = nova_linha
            with open(__file__, "w", encoding="utf-8") as f:
                local = True
                f.writelines(conteudo)
            
        else:
            local_salvo2 = input("Digite o local de destino dos downloads (essa ação é necessaria apenas uma vez): ")
            nova_linha = f'local_salvo = r"{local_salvo2}"\n'
            conteudo.insert(0, nova_linha)
            with open(__file__, "w", encoding="utf-8") as f:
                f.writelines(conteudo)
    exit()
def local_downloads():
    global local, local_salvo
    try:
        if local == True:
            print(local_salvo)
        else:
            definir_local()

    except:
        definir_local()


def lista():
    global n
    if playlist == True:
        lista_titulo.append(pl.title)
    elif youtube == True:
        lista_titulo.append(yt.title)
    elif instagram == True:
        n += 1
        lista_titulo.append(f"Instagram video n° {n}")
    lista_url.append(url)


def download():
    global url
    os.system('cls')
    lista()
    link = "https://"
    print(f"Local > {local_salvo}")
    print(f"Titulo dos videos/playlist >> {lista_titulo}"); print(f"URL dos videos >> {lista_url}")
    print("Voce pode inserir mais url`s\n")
    print("Digite o numero da forma de download:")
    print("1 - MP3    2 - MP4")
    escolha = input("> ")
    if link in escolha: # + urls
        url = escolha
        config()

    elif escolha == "1": # audio \\ obs: a ordem pra nao dar problema tem que ser essa, se trocar a ordem o codigo morre
        for i in lista_url:
            if substring_ig in i:
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    ydl.download([i])

            elif substring_pl in i:
                for video in pl.videos:
                    video.streams.get_audio_only().download(output_path=f"{local_salvo}\YouTube\Playlist '{pl.title}' mp3")
                    print(f"{video.title} | ok\n")

            elif substring_yt in i:
                video = YouTube(i, on_progress_callback=on_progress)
                video.streams.get_audio_only().download(output_path=f"{local_salvo}\YouTube\Audios")
                try:
                    print(f"{video.title} | ok \n")
                except:
                    print(f"{yt.title} | ok \n")   

    elif escolha == "2": # video
        for i in lista_url:
            if substring_ig in i:
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    ydl.download([i])

            if substring_pl in i:
                for video in pl.videos:
                    video.streams.get_highest_resolution().download(output_path=f"{local_salvo}\YouTube\Playlist '{pl.title}' mp4")
                    print(f"{video.title} | ok\n")

            elif substring_yt in i:
                video = YouTube(i, on_progress_callback=on_progress)
                video.streams.get_highest_resolution().download(output_path=f"{local_salvo}\YouTube\Videos")
                try:
                    print(f"{video.title} | ok \n")
                except:
                    print(f"{yt.title} | ok \n")   

def config():
    global url, yt, substring_yt, substring_pl, substring_pl, youtube, instagram, playlist, pl, local, remover, lista_titulo, lista_url
    youtube, playlist, instagram = False, False, False
    remover = False
    local = True
    local_downloads()

    if substring_pl in url:
        playlist = True
        pl = Playlist(url)
        download()
    elif substring_yt in url:
        youtube = True
        yt = YouTube(url)
        download()
    elif substring_ig in url:
        instagram = True
        print("ig")
        download()
    elif url == "caminho" or url == "caminho":
        local = False
        remover = True
        local_downloads()
        exit()

    else:
        print("insira uma url correta.")
        url = input("URL > ")
        config()
    novamente = input("Deseja baixar novamente? s/n >> ")
    if novamente == "n" or novamente == "N":
        exit()
    else:
        lista_titulo, lista_url = [], []
        os.system('cls')
        intro()


def intro():
    global url, remover, local
    substring_local = ":"
    os.system('cls')
    try:
        if substring_local in local_salvo:
            print(f"Local > {local_salvo}")
            print("caso queira modificar o caminho dos downloads digite 'caminho'") 
        else:
            remover = False
            local = True
            local_downloads()
    except:
        remover = False
        local = True
        local_downloads()
    url = input("URL > ")
    config()
intro()