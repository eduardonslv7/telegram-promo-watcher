# Monitoramento de Mensagens - Telegram para Discord

Este projeto monitora canais do Telegram e envia notificações para um canal do Discord, com base em palavras-chave definidas.
O script pode ser usado para diferentes finalidades, como monitoramento de promoções, alertas, notícias ou qualquer outro tipo de mensagem relevante que você deseje acompanhar.

## Como funciona

1. **Monitoramento do Telegram**: O script monitora os canais do Telegram que você escolher.
    
2. **Palavras-chave**: Quando uma mensagem nos canais monitorados contém uma das palavras-chave definidas, o script envia essa mensagem para o Discord.
    
3. **Integração com Discord**: O script utiliza um Webhook do Discord para enviar as notificações.

## Clonando o Repositório

Para começar a utilizar o script, primeiro você precisa clonar o repositório. Abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
git clone https://github.com/eduardonslv7/telegram-promo-watcher
```

### A Estrutura do Repositório

Após clonar o repositório, você verá a seguinte estrutura:

```bash
/repo
├── config_example.json
├── main.py
├── requirements.txt
└── README.md
```

**Importante**: O arquivo `config_example.json` serve apenas como um modelo. Você deve criar **manualmente** um novo arquivo chamado `config.json` na raiz do projeto e configurá-lo conforme o exemplo abaixo.

## Configurando o config.json

O arquivo config.json contém todas as configurações necessárias para que o script funcione corretamente. Ele deve ser preenchido da seguinte maneira:

```json
{
  "api_id": "SUA_API_ID",
  "api_hash": "SEU_API_HASH",
  "discord_webhook": "https://discord.com/api/webhooks/SEU_WEBHOOK",
  "keywords": ["iphone", "ps5", "galaxy", "xiaomi"],
  "channels": ["@canalDePromocoes1", "@canalDePromocoes2"]
}
```

### 1. **api_id e api_hash (Telegram)**

*   **O que são?** O api_id e o api_hash são credenciais de autenticação para acessar a API do Telegram.
    
*   **Como obter?**
    
    *   Acesse [my.telegram.org](https://my.telegram.org) e faça login com seu número de telefone.
        
    *   Clique em **API development tools**.
        
    *   Crie um novo **Application** e você receberá o api_id e o api_hash.
        

### 2. **discord_webhook (Discord)**

*   **O que é?** O Webhook do Discord permite que o script envie mensagens para um canal do Discord.
    
*   **Como obter?**
    
    *   Vá até o seu servidor no Discord.
        
    *   Clique com o botão direito no canal onde deseja receber as mensagens e selecione **"Editar Canal"**.
        
    *   Vá para a aba **"Integrações"** e clique em **"Webhooks"**.
        
    *   Crie um novo webhook e copie a URL gerada.
        
    *   Coloque essa URL no campo "discord_webhook" do config.json.
        

### 3. **keywords (Palavras-chave)**

*   **O que são?** São as palavras que o script irá procurar nas mensagens dos canais monitorados. Se uma mensagem contiver alguma dessas palavras, ela será enviada para o Discord.
    
*   **Como configurar?**: Basta adicionar as palavras-chave que você deseja monitorar em uma lista dentro do arquivo config.json. Por exemplo:
  
  
```json
  "keywords": ["iphone", "ps5", "galaxy", "xiaomi"]
```

## Rodando o Script

Após configurar o arquivo `config.json`, siga os passos abaixo para rodar o script.

### 1. **Instalar Dependências**

Antes de rodar o script, você precisa instalar as dependências necessárias. Execute o seguinte comando para instalar as bibliotecas requeridas:

```bash
pip install -r requirements.txt
```


### 2. **Rodar o Script**

Após configurar o arquivo config.json e instalar as dependências, você pode rodar o script com o seguinte comando:

```bash
python main.py
```

O script ficará rodando e monitorando os canais configurados. Quando uma mensagem contendo uma das palavras-chave for encontrada, ela será enviada para o Discord.

## Considerações Finais

*   **Manter o script rodando**: O script ficará em execução até que você o interrompa (pressionando `Ctrl + C` no terminal). Para rodar o script de maneira contínua, você pode utilizar ferramentas como `screen`, `tmux` ou até mesmo hospedar o script em um servidor.

*   **Personalização**: Para adicionar mais canais ou palavras-chave, basta editar o arquivo `config.json` com os novos valores.

Agora você pode monitorar mensagens do Telegram e recebê-las diretamente no seu Discord!
