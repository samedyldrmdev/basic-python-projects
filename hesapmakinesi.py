giris = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Karesini Hesapla
(6) Karekök Hesapla
"""
# Giriş kısmında ekrana ilk olarak çıkacak metni yazdırıyoruz. Tabii bunu print komutuyla yapıyoruz.

print(giris)
while True: #While komutu ile döngüyü sağlıyoruz. Bu sayede yanlış herhangi bir girişte program bizi başa döndürecektir.
    soru = input("Yapmak istediğiniz işlemin numarasını giriniz. -Çıkmak için q- : ") #input fonksiyonu ile kullanıcıdan bir değer istiyoruz.
    try: #bu kısım işlemlerden bağımsız, eğer programı çöktürecek herhangi bir değer girilmesi halinde verilecek mesajlar için kullandığımız ilk kısım. 
#         İkinci kısım aşağıda gelecek.
        if soru == "q": #if ve elif komutları ile kullanıcıdan aldığımız değerlere göre ekrana farklı değerler atıyoruz. 
#         Ve "break" ile While döngüsü sona erecek. Yani başa dönmeyecek.
            print("Çıkılıyor...") #Örneğin bu kısımda kullanıcı ekrana "q" değerini girerse "Çıkılıyor..." ifadesi yazılacak. 
            break #Ve "break" ile While döngüsü sona erecek. Yani başa dönmeyecek.
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
        print("Lütfen bir sayı giriniz!")
        
# Yukarıda yazdığımız try yani hata yakalama işleminin devamı. Şöyle ki örneğin kullanıcı hesap makinesinde sayı değil de bir harf yazdı.
# Bu sefer program ValueError hatası verecektir. Eğer program ValueError hatası verirse ekrana "Lütfen bir sayı giriniz!" ifadesi yazdırılacak.
# Ayrıca orijinal hata mesajını kullanıcıya göstermek istersek şu şekilde de yazabilirdik:
   
    except ZeroDivisionError as hata2:
        print("Sayıyı sıfıra bölemezsin!")
        print("Orijinal hata mesajı:", hata2)
        
# Görüldüğü gibi ikinci hatamız da ZeroDivisionError hatası. Hiçbir sayıyı sıfıra bölemeyiz. Eğer bölme işlemini seçip sayıyı sıfıra bölmeye çalışırsak
# bu hatayı alırız ve program çöker. Bu yüzden ekrana bir yazı yazdırarak döngü sayesinde tekrar girmelerini sağlayabiliriz. Ayrıca ZeroDivisionError hatasında
# görüldüğü gibi bu şekilde yazdığımızda orijinal hata mesajını da kullanıcıya gösterebiliyoruz. 


