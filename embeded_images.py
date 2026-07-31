import base64

def to_base64(filename):
    with open(filename, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

cover = to_base64("Unlocking Full Potential Cover.png")
author = to_base64("Gumroad HD DP.png")

with open("landing.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('src="Unlocking Full Potential Cover.png"', f'src="{cover}"')
html = html.replace('src="Gumroad HD DP.png"', f'src="{author}"')

with open("landing_embedded.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done! Created landing_embedded.html")