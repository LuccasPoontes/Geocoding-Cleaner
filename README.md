# Geocoding-Cleaner
 Uma Ferramenta Python para Geocodificação Reversa e Limpeza de Endereços

 # Geocoding Cleaner

Geocoding Cleaner é uma ferramenta Python projetada para realizar geocodificação reversa e limpar caracteres especiais em endereços. Utilizando o geocodificador ArcGIS da biblioteca `geopy` e a biblioteca `unidecode`, esta ferramenta oferece uma maneira simples de converter coordenadas em endereços legíveis, garantindo que caracteres especiais sejam devidamente tratados e removidos.

## Funcionalidades

- **Geocodificação Reversa**: Converta coordenadas de latitude e longitude em endereços legíveis.
- **Limpeza de Endereços**: Remova caracteres especiais dos endereços para garantir compatibilidade e legibilidade.
- **Extração de Código Postal**: Extraia códigos postais dos resultados da geocodificação.

## Começando

### Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `geopy`
- `unidecode`

Você pode instalá-las usando pip:

```bash
pip install geopy unidecode
```

## Uso
### Aqui está um exemplo simples para você começar:

```
from geopy.geocoders import ArcGIS
from unidecode import unidecode

# Inicialize o geolocalizador
geolocator = ArcGIS()

# Coordenadas a serem convertidas
latitude = -21.9845750 #Alterar conforme Latitude recebida para conversão
longitude = -47.9103380 #Alterar conforme Longitude recebida para conversão

# Realize a geocodificação reversa
location = geolocator.reverse((latitude, longitude))

# Extraia o endereço e o código postal
address = location.address
postal_code = location.raw.get('Postal')

# Limpe a string do endereço para remover problemas de caracteres especiais
clean_address = unidecode(address)

# Imprima o endereço completo e o código postal
print(f"Endereço: {clean_address}")
print(f"Código Postal Completo: {postal_code}")
```

## Contribuindo
Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
```Este README.md fornece uma visão geral clara do propósito do projeto, funcionalidades e instruções de uso, ajudando os usuários a entender e começar a usar o Geocoding Cleaner de forma eficaz.
```
