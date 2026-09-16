# Quick Site

> Gerador de landing pages para pequenos negócios. Informe os dados e gere um site profissional em segundos.

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)

## O que é

Uma CLI Python que transforma um JSON config em uma landing page profissional, responsiva e com visual dark. Sem frameworks, sem complicação.

## Instalação

```bash
git clone https://github.com/klcombr/quick-site.git
cd quick-site
python quick_site.py --help
```

## Uso

1. Copie `config.example.json` para `config.json`
2. Edite com os dados do seu negócio
3. Rode:

```bash
python quick_site.py
```

4. Abra `index.html` gerado no navegador

## Configuração

```json
{
  "business_name": "Serralheria Status",
  "tagline": "Qualidade e confiança em alumínio",
  "phone": "(13) 3491-3574",
  "whatsapp": "551334913574",
  "address": "Rua dos Ipês, 100 - Centro, Praia Grande/SP",
  "working_hours": "Seg-Sex: 8h às 18h",
  "services": [
    {"name": "Portões", "description": "Portões de alumínio sob medida"},
    {"name": "Janelas", "description": "Janelas e vidros temperados"},
    {"name": "Manutenção", "description": "Conserto e ajustes"}
  ],
  "primary_color": "#ff2222",
  "background": "#000000"
}
```

## Gerando para seu cliente

```bash
python quick_site.py --config meu_cliente.json --output ~/sites/meu_cliente/
```

Cada config gera um site completo e independente.

## Licença

MIT — use, modifique, distribua.

---
Feito por [KL Com](https://github.com/klcombr)
