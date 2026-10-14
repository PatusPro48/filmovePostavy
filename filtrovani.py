with open("postavy.txt", "r", encoding="utf-8") as soubor:
    with open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue

            casti = radek.split("#")
            if len(casti) != 6:
                text = "neplatný formát\n"
                vystup.write(text)
                print(text, end="")
                continue

            jmeno = casti[0]
            vek = int(casti[1])
            druh_pohlavi = casti[2]
            jezvire = casti[3]
            poslednipromitani = casti[4]
            oblibenost = float(casti[5])

            jeto_zvire = jezvire == "ano"
            if jeto_zvire:
                zvire = "je"
            else:
                zvire = "není"

            if oblibenost > 2.5:
                print(f"{druh_pohlavi} jménem: {jmeno}")
                print(f"{zvire} zvíře")
                print(f"film v němž existuje byl naposledy vysílán v našem kině: {poslednipromitani}")
                print(f"oblíbenost: {oblibenost}\n\n")

                vystup.write(f"{jmeno}\t {vek}\t {druh_pohlavi}\t {zvire} zvíře\t {poslednipromitani}\t {oblibenost}\n")