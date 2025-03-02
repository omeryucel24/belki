import time
meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word=="EXİT":
        print("çıkış yapılıyor...")
        break
    if word in meme_dict.keys():
        print("aradığınız kelime",word,meme_dict[word])
        time.sleep(1)
    else:
        print("aradığınız kelime bulunmamaktadır.")
        time.sleep(1)
    if word=="NEW":
        yeni_kelime=input("hangi kelimeyi eklemek istiyorsunuz?")
        meme_dict.append(yeni_kelime)
        