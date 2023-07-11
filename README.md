# Wiki_Sepep

WIkipedia SEPEP para gestão do conhecimento interno da equipe da Secretaria de Planejamento e Entregas Prioritárias da Prefeitura de São Paulo.

![img](https://raw.githubusercontent.com/Ana-CAS-Machado/wiki_sepep/main/Logo.png)

## Autores

- [@Ana-CAS-Machado](https://github.com/Ana-CAS-Machado)
- [@luaversa](https://github.com/luaversa)
- [@h-pgy](https://github.com/h-pgy)

<br>

## Referência

<br>

 - Mantido por: [Comunidade MediaWiki e Comunidade Docker:](https://github.com/wikimedia/mediawiki-docker)

<br>

## O que é MediaWiki?

O MediaWiki é um software wiki gratuito e de código aberto. Originalmente desenvolvido por Magnus Manske e aprimorado por Lee Daniel Crocker, ele é executado em muitos sites, incluindo Wikipedia, Wikcionário e Wikimedia Commons. 

Ele é escrito na linguagem de programação PHP e armazena o conteúdo em um banco de dados. Como o WordPress, que é baseado em licenciamento e arquitetura semelhantes, tornou-se o software dominante em sua categoria.

[wikipedia.org/wiki/MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)

![imagemMediawiki](https://www.mediawiki.org/static/images/icons/mediawikiwiki.svg)



<br>

# **Instalação**

<br>

## _Instalando a Wiki no container_

<br>
Nesse Software utilizamos o Docker e para as confugurações da Mediawiki, o software utiliza a linguagem PHP.
Criamos um container nomeado de sepep-mediawiki ( Utilize o nome que desejar ).

 O padrão básico para iniciar uma mediawiki é:

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

<br>

>Você pode fazer um pull deste repositorio.

<br>

## _Primeiros Passos_
---

Utilize o Script **_start_wiki.sh_** . Que ira iniciar sua wiki, adicionando o _nome_, puxar a imagem da MediaWiki, e expor o mapeamentos de porta, e adicionar o nome ao projeto. Ira atualizar o S.O. e instalar o Banco de Dados.

<br>

```bash

    #!/bin/bash

    export env

    container_name=sepep_wiki
    imagem_media_wiki="mediawiki"

    docker stop $container_name
    docker rm $container_name

    porta_aberta=80
    proj_name="wiki_sepep"

    docker run --name $container_name -v /home/$proj_name:/var/local -p $porta_aberta:80 -d $imagem_media_wiki

    docker exec $container_name apt-get update
    docker exec $container_name apt-get upgrade
    docker exec $container_name apt-get install sqlite3

```
<br>

Em seguida, acesse-o via http://localhost:8080 ou http://host-ip:8080 em um navegador.

<br>

---
### _Configuração da Wiki_

<br>

1. As Configurações da wiki se faz manualmente. <br>
    Inicialmente ela ira dizer que não encontrou o arquivo _LocalSettings.php_ em seguida cline em **set up the wiki**.

<br>

![img](https://concani3.files.wordpress.com/2010/07/tela_midiawiki_inicial.png)

<br>

O MediaWiki, ira verificar se seu sistema é compativel com as instalações que são necessarias <br>
(A propria wiki que ira instalar)

<br>

![imagem](https://mariushosting.com/wp-content/uploads/2023/02/MediaWiki-Synology-NAS-Set-up-12.png)


---
2. Na proxima pagina, selecione seu idioma. Nas proximas paginas são de preferencia do usuario, como qual Banco de Dados ira usar para o Backup de sua wiki. Para a WIKI de SEPEP, foi utilizando o SQLite, que economiza espaço na memória e não foi preciso gerar um novo container expecifico para o SQL.

<br>

Após toda a configuração de sua _Wiki_ ela ia gerar o arquivo **_LocalSettings.php_**. Jogue esse arquivo dentro do seu container.

O comando utilizado para copiar um arquivo de um sistema local para um remoto, execute o seguinte comando:

> **scp** _file.txt remote_username@10.10.0.2:/remote/diretório_

<br>

---

<br>

3. Utilize o Script **_alterar_localsettings.py_**. 

```Opção

    1. Selecione a opção JOGAR , ele irá jogar o LocalSetting na raiz da Wiki.

```

Execute-o novamente.

```opção2

    2. Selecione a opção COPIAR, que ira copiar todas as alterações, como o a alteração do Logo, o Favicon e o TimeZone, para dentro do arquivo LocalSettins.

```

<br>

## Backup
---

Para o Backup execute o script **_backup_script.sh_**. Uma das maneiras mais simples de fazer backup de um sistema é usando um script de shell . Por exemplo, um script pode ser usado para configurar quais diretórios fazer backup e passar esses diretórios como argumentos para o utilitário tar, que cria um arquivo morto. O arquivo compactado pode então ser movido ou copiado para outro local. O arquivo também pode ser criado em um sistema de arquivos remoto, como uma montagem NFS.

<br>

A maneira mais simples de executar o script de backup acima. Para deixar o arquivo deve se tornar executável:

> chmod u+x backup.sh

<br>

Em seguida, para executar:

<br>

> ./backup_script.sh

ou

> bash backup_script.sh

<br>

* Para descompactar um arquivo tar.gz, digite:

>tar -xzvf Monday.tgz /home/backup

<br> 

# Licença
 
 GNU Affero General Public License v3.0

<br>
Permissions of this strongest copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. When a modified version is used to provide a service over a network, the complete source code of the modified version must be made available.

<br>

### MediaWiki
<br>
O MediaWiki é licenciado sob os termos da GNU General Public License,
versão 2 ou posterior. Trabalhos derivados e versões posteriores do código devem ser
software livre licenciado sob a mesma licença ou uma licença compatível. Isso inclui
"extensões" que usam funções ou variáveis ​​do MediaWiki; ver
https://www.gnu.org/licenses/gpl-faq.html#GPLAndPlugins para obter detalhes.

Para o texto completo da versão 2 da licença, consulte
https://www.gnu.org/licenses/gpl-2.0.html ou '''GNU General Public License'''

---

<br>
<br>

## Secretaria Executiva de Planejamento e Entregas Prioritárias

<br>

![img](https://github.com/Ana-CAS-Machado/wiki_sepep/blob/main/Logo%20SEPEP%20-%20Branco.png?raw=true)

<br>

---

<br>

<br>

<br>

<br>

![img](https://observasampa.prefeitura.sp.gov.br/assets/img/logo_governo.webp)


## Viaduto do Chá, 15 - 11º andar - Centro | 01002-020
http://planejamento.prefeitura.sp.gov.br

Viaduto do Chá, 15 - 11º andar - Centro | 01002-020

<br>
<br>
<br>
<br>

Copyright © 2022 | Prefeitura de São Paulo | Affero General Public License (AGPL) v3
