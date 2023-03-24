
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

## Importante

A partir do MediaWiki 1.2.0, é possível instalar e configurar o wiki
"in-place", desde que você tenha os pré-requisitos necessários disponíveis.

#### Software necessário a partir do MediaWiki 1.41.0:

```softwae
  Um software de servidor web para servir páginas MediaWiki para o navegador web.
  PHP para executar o MediaWiki.
  Um servidor de banco de dados para armazenar páginas e dados do MediaWiki
```

#### Um servidor SQL, os seguintes tipos são suportados;

```bd
  MariaDB 10.3 ou superior
  MySQL 5.7.0 ou superior
  PostgreSQL 10 ou superior
  SQLite 3.8.0 ou superior
```
MediaWiki é desenvolvido e testado principalmente em plataformas Unix/Linux, mas deve
funcionam no Windows também.

O suporte para conteúdo especializado requer a instalação da extensão relevante. Para
fórmula, consulte https://www.mediawiki.org/wiki/Special:MyLanguage/Extension:Math

Não se esqueça de verificar o arquivo RELEASE-NOTES...


Documentação adicional está disponível on-line, que pode incluir informações mais detalhadas
notas sobre sistemas operacionais específicos e soluções alternativas para hospedagem difícil
ambientes:

https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Installing_MediaWiki


******************* AVISO *******************

**LEMBRE-SE: SEMPRE FAÇA BACKUP DO SEU BANCO DE DADOS ANTES
TENTANDO INSTALAR OU ATUALIZAR!!!**

******************* AVISO *******************

<br>

# Instalação

<br>

### _Instalando a Wiki no container_
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

<img src="https://www.hostknox.com/content/images/tutorials/mediawiki/installation/1-zoom.jpg" width="400" height="200" >

<br>

### _Idioma_
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

<img src="https://www.hostknox.com/content/images/tutorials/mediawiki/installation/3-zoom.jpg"  width="400" height="200" >

<br>

### _Banco de Dados_
---
Os servidores são configurados de forma que o MediaWiki seja executado sem problemas. Clique no botão Continuar para ir para a próxima página.

A próxima página é para as informações do banco de dados.

Optamos pelo banco de dados SQLite com a base de dados sepep_wiki.

Mas o Mediawiki suporta os seguntes Bancos de Dados;

<br>

```MySQL
  MySQL
```
| Tipo de BD  | Host do Banco de Dados | Nome do Banco de dados                | Prefixo da tabela BD | Nome de usuário     | Senha do DB|
| ----------- | ---------------------- | ------------------------------------- | -------------------- | ------------------- | ---------- |
|   MySQL     | Coloque o localhost    | nome do bd que você criou para a wiki | serão criadas no bd¹ | Seu nome de usuario | Sua senha | 

> ¹ Neste campo você pode digitar qualquer prefixo para as tabelas do banco de dados que serão criadas no banco de dados. O prefixo da tabela é útil se você decidir instalar mais de um aplicativo no mesmo banco de dados. Neste caso as tabelas de cada aplicação devem ter um prefixo de tabela diferente. No entanto, por motivos de segurança, é recomendável manter cada aplicativo em um banco de dados separado.

<br>
<br>

```Mariadb
  MariaDB
```
| Tipo de BD  | Host do Banco de Dados | Nome do Banco de dados                | Prefixo da tabela BD | Nome de usuário     | Senha do DB|
| ----------- | ---------------------- | ------------------------------------- | -------------------- | ------------------- | ---------- |
|   MariaDB   | Coloque o localhost    | nome do bd que você criou para a wiki | serão criadas no bd¹ | Seu nome de usuario | Sua senha | 

<br>
<br>


```sqlite
  SQLite
```
| Tipo de BD  | Diretorio do BD  | Nome do BD|
| ----------- | ---------------- | --------- |
|  SQLite     | /var/www/data    | My-wiki   |

>No SQLite, o diretorio do Banco de dados é a pasta onde ficará seus dados para backup.

>E no nome do Bando de dados é de sua escolha ( sem colocar Hifem ).

<br>

### _Conclusão_
---
Existem vários tipos de banco de dados suportados por esta imagem, mais facilmente usados ​​por meio de vinculação de contêiner padrão. Na configuração padrão, o SQLite pode ser usado para evitar um segundo contêiner e gravar em arquivos simples. Seguem instruções mais detalhadas para diferentes tipos de banco de dados (mais prontos para produção).

Ao acessar pela primeira vez o servidor web fornecido por esta imagem, ele passará por um breve processo de configuração. Os detalhes fornecidos abaixo são especificamente para a etapa "Configurar banco de dados" desse processo de configuração.

Após terminar toda a configuração na pagina de instalação 
> Lembrando que é de sua preferencia as configurações de sua wiki.

Se você configurou as configurações para as informações do banco de dados corretamente, o banco de dados será preenchido com os dados necessários e, na próxima página, você verá uma confirmação de que as tabelas do banco de dados foram criadas com sucesso e preenchidas com os dados.
<br>

A última coisa que o instalador faz é gerar um arquivo **LocalSettings.php** . Este é um arquivo essencial que você deve colocar na conta de hospedagem na pasta raiz do MediaWiki. O arquivo contém dados relacionados à configuração do seu site. Ele é configurado de acordo com a forma como você configurou as opções nas etapas anteriores do processo de instalação.
<br>

> Há algumas informações que podem ser alteradas depois de baixado o **LocalSettings.php**
<br>

A última página informa sobre isso e fornece um link para baixar LocalSettings.php caso o download não tenha iniciado automaticamente. 
Depois de fazer isso, você pode acessar e usar seu site wiki.

<br>

# Licença
Veja as [informações de licença](https://phabricator.wikimedia.org/source/mediawiki/browse/master/COPYING) para o software contido nesta imagem.

Como acontece com todas as imagens do Docker, elas provavelmente também contêm outro software que pode estar sob outras licenças (como Bash, etc. da distribuição base, juntamente com quaisquer dependências diretas ou indiretas do software primário contido).

Algumas informações de licença adicionais que puderam ser detectadas automaticamente podem ser encontradas no diretório do [repo-inforepositóriomediawiki/](https://github.com/docker-library/repo-info/tree/master/repos/mediawiki) .

Quanto ao uso de qualquer imagem pré-construída, é responsabilidade do usuário da imagem garantir que qualquer uso desta imagem esteja em conformidade com quaisquer licenças relevantes para todos os softwares contidos nela.
