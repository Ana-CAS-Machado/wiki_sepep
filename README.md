
# Wiki_Sepep

WIkipedia SEPEP para gestão do conhecimento interno da equipe da Secretaria de Planejamento e Entregas Prioritárias da Prefeitura de São Paulo.

<img src="https://observasampa.prefeitura.sp.gov.br/assets/img/logo_sepep.webp" width="150" height="50">
<br>
<img src="https://observasampa.prefeitura.sp.gov.br/assets/img/logo_sp.webp" width="250" height="100">


## Autores

- [@Ana-CAS-Machado](https://github.com/Ana-CAS-Machado)
- [@luaversa](https://github.com/luaversa)
- [@h-pgy](https://github.com/h-pgy)


## Referência

 - Mantido por: [Comunidade MediaWiki e Comunidade Docker:](https://github.com/wikimedia/mediawiki-docker)



## O que é MediaWiki?

O MediaWiki é um software wiki gratuito e de código aberto. Originalmente desenvolvido por Magnus Manske e aprimorado por Lee Daniel Crocker, ele é executado em muitos sites, incluindo Wikipedia, Wikcionário e Wikimedia Commons. 

Ele é escrito na linguagem de programação PHP e armazena o conteúdo em um banco de dados. Como o WordPress, que é baseado em licenciamento e arquitetura semelhantes, tornou-se o software dominante em sua categoria.

[wikipedia.org/wiki/MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)

![imagemMediawiki](https://www.mediawiki.org/static/images/icons/mediawikiwiki.svg)



<br>

# **Instalação**

<br>

## _Instalando a Wiki no container_
---
<br>
Nesse Software utilizamos o Docker e para as confugurações da Mediawiki, utilizamos a linguagem PHP.
Criamos um container nomeado de sepep-mediawiki ( Utilize o nome que desejar ).

 O padrão básico para iniciar uma mediawiki instância é:

```basico
  $ docker run --name some-mediawiki -d mediawiki
```

Se você quiser acessar a instância do host sem o IP do contêiner, os mapeamentos de porta padrão podem ser usados:

```mapeando_ip
  $ docker run --name some-mediawiki -p 8080:80 -d mediawiki
```

Para a wiki de SEPEP utilizamos o comando;

```sepepe_wiki
  $docker run --name sepep-mediawiki_v1 -v /home/sepepwiki:/var/local -p 8080:80 -d mediawiki
```

Em seguida, acesse-o via http://localhost:8080 ou http://host-ip:8080em um navegador.

![iamgem_inicial](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmariushosting.com%2Fhow-to-install-mediawiki-on-your-synology-nas%2F&psig=AOvVaw1BBrY9frnDPFuKWX7RD6Sp&ust=1682085451664000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCLDbvuDOuP4CFQAAAAAdAAAAABAT)

<br>

## _Idioma_
---
Na próxima página estão as opções para o idioma:

As opções são:

```seu_idioma
Seu idioma - selecione o idioma que será usado durante o processo de instalação.
```

```idioma_da_wiki
Idioma Wiki - selecione o idioma padrão que será usado para o site. Este é o idioma no qual as páginas do site e as opções serão exibidas. Observe que algumas traduções podem não estar 100% completas, o que significa que algumas sequências de texto padrão e opções que aparecem no site podem não estar traduzidas para esse idioma.
Depois de estar pronto com as opções, clique no botão Continuar .
``` 

A próxima etapa verifica automaticamente o ambiente do servidor (por exemplo, versão do PHP, biblioteca gráfica, nome de domínio e endereço URL da instalação, etc.). A página exibe o resultado dessa verificação, bem como os direitos autorais e os termos:

<img src="https://www.hostknox.com/content/images/tutorials/mediawiki/installation/3-zoom.jpg">

<br>

## _Banco de Dados_
---
Os servidores são configurados de forma que o MediaWiki seja executado sem problemas. Clique no botão Continuar para ir para a próxima página.

A próxima página é para as informações do banco de dados.


O MediaWiki suporta os sistemas de banco de dados a seguir:
<br>

>MariaDB é a base de dados preferida para o MediaWiki e a melhor suportada. O MediaWiki também trabalha com MySQL e Percona Server, que são compatíveis com MariaDB.

<br>


>PostgreSQL é um popular sistema de banco de dados de código aberto como uma alternativa para o MySQL. (Como compilar o PHP com suporte PostgreSQL)

<br>

>O SQLite é uma plataforma de base de dados ligeira muito bem suportada. (Como compilar PHP com suporte para SQLite, usa PDO.)


<br>
Para a WIKI de SEPEP, utilisamos o SQLite, economiza espaço e não foi preciso gerar um container só para o SQL


A partir desse ponto, configure o MediaWiki de acordo com suas preferencias.
Ao terminar, o instalador irá proceder à instalação de toda a estrutura da mediawiki.
Após terminar a instalação da plataforma,  o MediaWiki ira gerar o arquivo LocalSettings.php, com todas as configurações. 

<br>

<img src="https://pplware.sapo.pt/wp-content/uploads/2013/06/media_10_thumb.jpg">

Devemos descarregar o ficheiro LocalSettings.php e colocá-lo em _/var/www/mediawiki_ ou _/var/www/html_. Na raiz do MediaWiki.

<br>

_O comando usado para carregar o LocalSettings foi o SCP (cópia segura) é um utilitário de linha de comando que permite copiar arquivos e diretórios com segurança entre dois locais._

<br>
Para copiar um arquivo de um sistema local para um remoto, execute o seguinte comando:

<br>

 >scp file.txt remote_username@10.10.0.2:/remote/directory 

<br>

Feito isso, sua Wiki já esta configurada e pronta para o acesso.

<img src="https://pplware.sapo.pt/wp-content/uploads/2013/06/media_12_thumb.jpg">

<br>
<br>

## **Observações**

Foi criado _scripts_ para facilitar a instalação e configuração.

<br>

> Só lembrando que os scripts estão configurados para a wiki de sepep, altere para que fique com as configurações de sua wiki.

<br>

### start_wiki.sh

<br>

Para um S.O como o Ubuntu foi criado um Shell script para iniciar a wiki ( pode-se criar um scrip em Python ).

<br>

```start_wiki
  #!/bin/bash
  export env

  container_name=name_your_wiki
  imagem_media_wiki="mediawiki"

  docker stop $container_name
  docker rm $container_name

  porta_aberta=80
  proj_name="your_project"

  docker run --name $container_name -v /home/$proj_name:/var/local -p $porta_aberta:80 -d  $imagem_media_wiki

  docker exec $container_name apt-get update
  docker exec $container_name apt-get upgrade
  docker exec $container_name apt-get install sqlite3
```
<br>

Depois de iniciar sua wiki, configure ela manualmente, como mostrado a cima, e coloque o LocalSettings.php em seu container.

Após colocar o LocalSettings em seu container iremos alteralo.

<br>

### **Alterando o LocalSettings**

<br>

Para a wiki ficar mais a cara de SEPEP, alteramos o *logo* e adicionamos o **Favicon**, e o **TimeZone** para o fuso horario de São Paulo.
O Script de alteração foi feito em Python.

<br>

```Alterar_localsettings
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

        new_t = '$wgFavicon = "/images/favicon.ico";'
        alterar_local_settings(new_t, '')
        acrescentar_linha_local_settings(new_t)

    def timezone():

        new_t='''$wgLocaltimezone = "America/Sao_Paulo";
    $dtz = new DateTimeZone($wgLocaltimezone);
    $dt = new DateTime('now', $dtz);
    $wgLocalTZoffset = $dtz->getOffset($dt) / 60;
    unset($dtz);
    unset($dt);'''
        alterar_local_settings(new_t, '')
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
```

<br>

> Para executar um script em Python dentro do Docker se usa o comando;

> **python3 alterar_localsettings.py** 

<br>

1. Primeiro execute o script em python e selecione "Jogar" ele ira colocar o *LocalSettings* dentro do container, na raiz da wiki.

<br>

2. Execute o script novamente mas agora selecione a opção "Copiar" para que ele faça as alterações.


### Backup

<br>

O script de backup foi desenvolvido em Shell script.

```backup

#!/bin/bash
##########################################
#
# Backup to NFS mount script.
#
##########################################

#O que fazer com Backup
container_id="408586aaf301"
backup_file="/var/www/data/"

#Para onde fazer o backup
dest_tmp="backup_tmp"
dest="backup"

#Criar nome do arquivo
day=$(date +%m-%d-%Y)
hostname="backup_wiki"
archive_file="$hostname-$day.tgz"

#Imprimir mensagem de status inicial
echo "Backing up $backup_file to $dest/$archive_file"
date
echo date

#Faça o backup dos arquivos usando tar
mkdir -p $dest_tmp
mkdir -p $dest
docker cp $container_id:$backup_file $dest_tmp
tar -zcvf $dest/$archive_file $dest_tmp
rm -r $dest_tmp

#Imprimir mensagem de status final
echo
echo " backup finished"
date

#Longa lista de arquivos em $dest para verificar os tamanhos dos arquivos
ls -lh $dest
tar -ztvf $dest/$archive_file

```

Ele compacta o backup em tar (zip) e para recuperar o backup é só descompactar.

<br>

Comando para descompactar.
>tar -xzvf /local/do-seu-backup.tgz

<br>

Sua Wiki já esta pronta para uso.

<br>


### _Conclusão_
---
Existem vários tipos de banco de dados suportados por esta imagem, mais facilmente usados ​​por meio de vinculação de contêiner padrão. Na configuração padrão, o SQLite pode ser usado para evitar um segundo contêiner e gravar em arquivos simples.

Ao acessar pela primeira vez o servidor web fornecido por esta imagem, ele passará por um breve processo de configuração.
Após terminar toda a configuração na pagina de instalação 
> Lembrando que é de sua preferencia as configurações de sua wiki.

Se você configurou as configurações para as informações do banco de dados corretamente, o banco de dados será preenchido com os dados necessários e, na próxima página, você verá uma confirmação de que as tabelas do banco de dados foram criadas com sucesso e preenchidas com os dados.
<br>

A última coisa que o instalador faz é gerar um arquivo **LocalSettings.php** . Este é um arquivo essencial que você deve colocar na conta de hospedagem na pasta raiz do MediaWiki. O arquivo contém dados relacionados à configuração do seu site. Ele é configurado de acordo com a forma como você configurou as opções nas etapas anteriores do processo de instalação.

A última página informa sobre isso e fornece um link para baixar LocalSettings.php caso o download não tenha iniciado automaticamente. 
Depois de fazer isso, você pode acessar e usar seu site wiki.

<br>

> Só altere o LocalSettings, qualquer outro alquivo que foi alterado ira prejudicar sua wiki e ela não podera mais funcionar. 

<br>

>A linguagem usada para alterar o LocalSettins sempre será o PHP.

<br>

 >Há algumas informações que podem ser alteradas depois de baixado o **LocalSettings.php**.

<br>

Para adicionar manualmente sua logo.

1. - Adicionar o logo dentro da Wiki e salvar com o nome.

2. - Modificar o código dentro do LocalSettings.php colocando o endereço de IP da Imagem.

```logo

$wgLogos = [
	'1x' => "$wgResourceBasePath/resources/assets/change-your-logo.svg",
	'icon' => "$wgResourceBasePath/resources/assets/change-your-logo.svg",
];

```

<br>

O TimeZone é opcional colocar.

<br>

```timezone

$wgLocaltimezone = "América/São_Paulo" ;
$dtz = new DateTimeZone ( $wgLocaltimezone );
$dt = new DateTime ( 'agora' , $dtz );
$wgLocalTZoffset = $dtz -> getOffset ( $dt ) / 60 ;
desarmar ( $dtz );
não configurado ( $dt );

```

<br>

O Favicom precisa ser **_.ICO_** ou não ira funcionar. Lembre de pegar uma imagem ou fazer ela em HD, sempre em otima qualidade.

<br>

Para usar um favicon situada em local diferente do diretório raiz do seu site, no arquivo LocalSettings.php, adicionar ;

>$wgFavicon = "$wgScriptPath/path/to/your/favicon.ico";

Exemplo:

```favicon

  $wgFavicon = "/images/6/64/Favicon.ico";

```

<br>

# Licença
Veja as [informações de licença](https://phabricator.wikimedia.org/source/mediawiki/browse/master/COPYING) para o software contido nesta imagem.

Como acontece com todas as imagens do Docker, elas provavelmente também contêm outro software que pode estar sob outras licenças (como Bash, etc. da distribuição base, juntamente com quaisquer dependências diretas ou indiretas do software primário contido).

Algumas informações de licença adicionais que puderam ser detectadas automaticamente podem ser encontradas no diretório do [repo-inforepositóriomediawiki/](https://github.com/docker-library/repo-info/tree/master/repos/mediawiki) .

Quanto ao uso de qualquer imagem pré-construída, é responsabilidade do usuário da imagem garantir que qualquer uso desta imagem esteja em conformidade com quaisquer licenças relevantes para todos os softwares contidos nela.

