giris = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Karesini Hesapla
(6) Karekök Hesapla
"""

print(giris)
while True:
    soru = input("Yapmak istediğiniz işlemin numarasını giriniz. -Çıkmak için q- : ")
    try:
        if soru == "q":
            print("Çıkılıyor...")
            break
        if soru == "1":
            sayi1 = int(input("Toplamak istediğiniz 1.sayıyı giriniz:"))
            sayi2 = int(input("Toplamak istediğiniz 2.sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 + sayi2, "olarak bulunmuştur.")
        elif soru == "2":
            sayi1 = int(input("Çıkarma işlemi için  1.sayıyı giriniz:"))
            sayi2 = int(input("Çıkarma işlemi için 2.sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 - sayi2, "olarak bulunmuştur.")
        elif soru == "3":
            sayi1 = int(input("Çarpma işlemi için  1.sayıyı giriniz:"))
            sayi2 = int(input("Çarpma işlemi için  2.sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 * sayi2, "olarak bulunmuştur.")
        elif soru == "4":
            sayi1 = int(input("Bölme işlemi için  1.sayıyı giriniz:"))
            sayi2 = int(input("Bölme işlemi için  2.sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 / sayi2, "olarak bulunmuştur.")
        elif soru == "5":
            sayi1 = float(input("Karesini hesaplamak istediğiniz sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 * sayi1, "olarak bulunmuştur.")
        elif soru == "6":
            sayi1 = int(input("Karekökünü almak istediğiniz sayıyı giriniz:"))
            print("İşleminizin sonucu:", sayi1 ** 0.5 , "olarak bulunmuştur.")
        else:
            print("Yanlış giriş!")
            print("Lütfen aşağıdaki seçeneklerden birini seçiniz:", giris)

    except ValueError as hata:
        print(hata)
        print("Lütfen bir sayı giriniz!")
        print("Orijinal hata mesajı:", hata)

    except ZeroDivisionError as hata2:
        print("Sayıyı sıfıra bölemezsin!")
        print("Orijinal hata mesajı:", hata2)


