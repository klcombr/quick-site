#!/usr/bin/env python3
"""Quick Site — Gerador de landing pages para pequenos negócios."""

import json
import sys
import os
import argparse

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Inter',sans-serif;background:{bg};color:#e8e8e8}}
.hero{{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:40px 20px}}
.hero h1{{font-size:clamp(36px,6vw,72px);font-weight:800;letter-spacing:-2px;margin-bottom:12px}}
.hero h1 span{{color:{accent}}}
.hero p{{font-size:18px;color:#999;max-width:500px;margin-bottom:24px}}
.hero a{{display:inline-block;background:{accent};color:#fff;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;transition:opacity .2s}}
.hero a:hover{{opacity:.85}}
.services{{padding:80px 20px;max-width:900px;margin:0 auto}}
.services h2{{font-size:28px;font-weight:700;margin-bottom:32px;text-align:center}}
.service{{border:2px solid #222;border-radius:12px;padding:24px;margin-bottom:16px;transition:border-color .2s}}
.service:hover{{border-color:{accent}}}
.service h3{{font-size:18px;font-weight:600;margin-bottom:6px}}
.service p{{font-size:14px;color:#888}}
.info{{padding:80px 20px;max-width:600px;margin:0 auto;text-align:center}}
.info p{{font-size:16px;color:#999;margin:8px 0}}
.info .label{{font-size:12px;text-transform:uppercase;letter-spacing:2px;color:{accent};margin-bottom:4px}}
footer{{text-align:center;padding:40px;font-size:13px;color:#555;border-top:1px solid #1a1a1a}}
</style>
</head>
<body>
<section class="hero">
<h1>{name}</h1>
<p>{tagline}</p>
<a href="https://wa.me/{whatsapp}">Fale Conosco</a>
</section>
<section class="services">
<h2>Nossos Serviços</h2>
{services_html}
</section>
<section class="info">
<div class="label">Telefone</div><p>{phone}</p>
<div class="label">Endereço</div><p>{address}</p>
<div class="label">Horário</div><p>{hours}</p>
</section>
<footer>© 2026 {name}. Todos os direitos reservados.</footer>
</body>
</html>"""

def generate(config_path, output_path):
    with open(config_path) as f:
        cfg = json.load(f)

    services_html = ""
    for s in cfg.get("services", []):
        services_html += f'<div class="service"><h3>{s["name"]}</h3><p>{s.get("description","")}</p></div>\n'

    html = TEMPLATE.format(
        name=cfg["business_name"],
        tagline=cfg.get("tagline", ""),
        phone=cfg.get("phone", ""),
        whatsapp=cfg.get("whatsapp", "").replace("+","").replace(" ","").replace("-",""),
        address=cfg.get("address", ""),
        hours=cfg.get("working_hours", ""),
        accent=cfg.get("primary_color", "#ff2222"),
        bg=cfg.get("background", "#000000"),
        services_html=services_html
    )

    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, "index.html"), "w") as f:
        f.write(html)

    print(f"Site gerado em {output_path}/index.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gere uma landing page para seu negócio")
    parser.add_argument("--config", default="config.json", help="Arquivo JSON de configuração")
    parser.add_argument("--output", default=".", help="Pasta de saída")
    args = parser.parse_args()
    generate(args.config, args.output)
