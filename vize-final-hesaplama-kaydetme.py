def ogrenci_yazdir():
    bilgi = input("Lütfen öğrencinin adını soyadını giriniz:")
    vize = float(input("Lütfen vize notunu giriniz:"))
    final = float(input("Lütfen final notunu giriniz:"))

    ortalama = vize * 0.4 + final * 0.6
    harf_notu = ""

    if ortalama >= 85:
        harf_notu = "AA"
    elif ortalama >= 70:
        harf_notu = "BA"
    elif ortalama >= 60:
        harf_notu = "BB"
    elif ortalama >= 50:
        harf_notu = "CB"
    elif ortalama >= 40:
        harf_notu = "CC"
    elif 40 > ortalama:
        harf_notu = "FF"

    with open("notlar.txt", "a") as dosya:
        print("{} adli ogrencinin basari notu: {} ve bu derste elde ettigi harf notu: {}\n".format(bilgi, ortalama,
                                                                                                   harf_notu))
        dosya.writelines(
            "{} adli ogrencinin basari notu: {} ve bu derste elde ettigi harf notu: {}\n".format(bilgi, ortalama,
                                                                                                 harf_notu))

kac_ogrenci = int(input("Kaç tane ogrenciyi kaydedeceksiniz?: "))

for i in range(kac_ogrenci):
    ogrenci_yazdir()

