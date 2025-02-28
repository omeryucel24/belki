import time
while True:
    meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                }
    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print("aradığınız kelime",word,meme_dict[word])
               
    else:
        print("aradığınız kelime bulunmamaktadır.")
        
        # Kelime eşleşmiyorsa ne yapmalıyız?
