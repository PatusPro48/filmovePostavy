with open("postavy.txt", "r", encoding="utf-8") as soubor:
    with open("oblibene-postavy.txt", "w", encoding="utf-8") as vystup:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue

            casti = radek.split("#")
            if len(casti) != 6:
                vystup.write("neplatný formát\n")
                continue

            jmeno = casti[0]
            vek = int(casti[1])
            druh_pohlavi = casti[2]
            jezvire = casti[3]
            poslednipromitani = casti[4]
            oblibenost = float(casti[5])

            if jezvire == "ano":
                zvire = "je"
            else:
                zvire = "není"

            if oblibenost > 2.5:
                vystup.write(f"{druh_pohlavi} jménem: {jmeno}\n")
                vystup.write(f"{zvire} zvíře\n")
                vystup.write(f"film v němž existuje byl naposledy vysílán v našem kině: {poslednipromitani}\n")
                vystup.write(f"oblíbenost: {oblibenost}\n\n")

    
