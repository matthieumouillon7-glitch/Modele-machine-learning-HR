with sync_playwright() as p:
    navigateur = p.chromium.launch(headless=True)
    page = navigateur.new_page()
    page.goto(url, wait_until="domcontentloaded", timeout=60_000)
    page.locator("main img[alt]").first.wait_for(timeout=20_000)
    html = page.content()
    navigateur.close()

soup = BeautifulSoup(html, "html.parser")

produits = []
for image in soup.select('main img[alt][src]'):
    nom = image.get("alt", "").strip()
    adresse_image = image.get("src", "")

    if nom and "/300x300.webp" in adresse_image:
        produits.append({
            "nom": nom,
            "image": urljoin(url, adresse_image),
        })

df_produits = pd.DataFrame(produits).drop_duplicates()
df_produits.head()