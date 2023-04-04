import subprocess
from dotenv import load_dotenv
import os

def pegar_id_container()->str:
    
    container_id=subprocess.run(['sudo', 'docker', 'ps', '-aqf', 'name=sepep-mediawiki_v2.0'], capture_output=True)
    container_id=container_id.stdout.decode('utf-8')
    print(f"O id do container eh: {container_id}")
    
    return container_id

def copiar_localsettings_do_docker(container_name:str)->None:
    
    caminho_local_settings='/var/www/html/LocalSettings.php'
    comando = ['docker', 'cp', '-a', f'{container_name}:{caminho_local_settings}', '.']
    subprocess.run(comando)

def jogar_localsettings_no_docker(container_name:str)->None:

    caminho_local_settings='/var/www/html/LocalSettings.php'
    comando = ['docker', 'cp', 'LocalSettings.php', f'{container_name}:{caminho_local_settings}']
    subprocess.run(comando)

def jogar_logo_imgs(container_name:str)->None:

    caminho_imgs='/var/www/html/images'
    comando = ['docker', 'cp', 'Logo.png', f'{container_name}:{caminho_imgs}']
    subprocess.run(comando)

def alterar_local_settings(txt_original:str, novo_texto:str)->None:

    with open('LocalSettings.php', 'r') as f:
        t = f.read()

    new_t = t.replace(txt_original, novo_texto)

    with open('LocalSettings.php', 'w') as f:
        f.write(new_t)


def mudar_logo():

    search_string = "$wgResourceBasePath/resources/assets/change-your-logo.svg"
    
    new_t = "images/Logo.png"

    alterar_local_settings(search_string, new_t)

    search_string_2 = "$wgResourceBasePath/resources/assets/change-your-logo.svg"
    alterar_local_settings(search_string_2, new_t)

def jogar_favicon(container_name:str)->None:

    caminho_imgs='/var/www/html/images'
    comando = ['docker', 'cp', 'favicon.ico', f'{container_name}:{caminho_imgs}']
    subprocess.run(comando)

def acrescentar_linha_local_settings(nova_linha:str)->None:

    with open('LocalSettings.php', 'r') as f:
        t = f.read()

    new_t = t + '\n' + nova_linha + '\n'
    with open('LocalSettings.php', 'w') as f:
        f.write(new_t)


def mudar_favicon():

    new_t = '$wgFavicon = "/images/favicon.ico"'
    acrescentar_linha_local_settings(new_t)



if __name__ == "__main__":
    
    load_dotenv()
    container_name = os.environ['container_name']
    print(container_name)

    jogar_ou_copiar = input('Deseja <jogar> ou <copiar> o arquivo LocalSettings?')
    if jogar_ou_copiar not in {'jogar', 'copiar'}:
        raise ValueError(f'Deve ser <jogar> ou <copiar>. Resposta dada: {jogar_ou_copiar}')
    if jogar_ou_copiar=='jogar':
        jogar_localsettings_no_docker(container_name)
    else:
        copiar_localsettings_do_docker(container_name)
        jogar_logo_imgs(container_name)
        mudar_logo()
        jogar_favicon(container_name)
        mudar_favicon()
        jogar_localsettings_no_docker(container_name)
       
