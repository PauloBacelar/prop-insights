# Scraper de Imóveis

Este projeto é um web scraper que extrai dados de imóveis do [ZAP Imóveis](https://www.zapimoveis.com.br/), utilizando Selenium com um driver Chrome indetectável. Ele coleta informações sobre anúncios de imóveis, incluindo preço, área, número de quartos e outros atributos relevantes, armazenando-os em um arquivo CSV para análise posterior.

## Funcionalidades

- Raspa anúncios de imóveis do Zap Imóveis
- Usa um driver undetectable Chrome para evitar bloqueios
- Alterna entre diferentes user agents para reduzir o risco de detecção
- Extrai detalhes do imóvel, como preço, área, localização e características
- Armazena os dados coletados em um arquivo CSV para análise

## Requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.x
- Google Chrome
- ChromeDriver (compatível com a versão do seu Chrome)

Pacotes Python necessários:
```sh
pip install undetected-chromedriver selenium random-user-agent
```

## Como Funciona

1. Lê os URLs dos anúncios de imóveis a partir de `utils/links.txt`.
2. Utiliza um user-agent rotativo para cada requisição.
3. Inicia uma instância do undetectable Chrome com as opções necessárias.
4. Extrai os dados dos imóveis de cada anúncio.
5. Salva os dados extraídos em `data/properties_data.csv`.

## Uso

1. Adicione os URLs ao arquivo `utils/links.txt` (um por linha).
2. Modifique `url_params` no script para filtrar os anúncios conforme suas necessidades.
3. Execute o script:
   ```sh
   python script.py
   ```

## Configuração

Modifique `url_params` no script para personalizar os filtros de busca:
```python
url_params = {
    "tipos": ["apartamento_residencial", "casa_residencial"],
    "proximoMetro": True,
    "precoMaximo": 750000,
    "areaMinima": 40,
    # ...
}
```

## Observações

- O scraper lida automaticamente com a paginação e extrai todos os anúncios de várias páginas.
- Introduz intervalos de espera aleatórios para simular o comportamento humano.
- Certifique-se de estar em conformidade com os termos de serviço do site antes de executar o scraper.

## Licença
Este projeto é apenas para fins educacionais. Use-o com responsabilidade.

