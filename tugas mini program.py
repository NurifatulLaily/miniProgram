player = input(" Masukkan elemen Pokemon player:")
attack = int(input(" Masukkan attack Pokemon player:"))
lawan = input(" Masukkan elemen Pokemon lawan :")

if player == "Fire":
    if lawan == "Fire":
        new_attack = attack*1
        efektif_tidak = "Tidak terjadi perubahan kekuatan serangan"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Water":
        new_attack = attack*0.5
        efektif_tidak = "Serangan tidak efektif..."
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Grass":
        new_attack = attack*1.5
        efektif_tidak = "Serangan efektif!"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    
elif player == "Water":
    if lawan == "Water":
        new_attack = attack*1
        efektif_tidak = "Tidak terjadi perubahan kekuatan serangan"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Grass":
        new_attack = attack*0.5
        efektif_tidak = "Serangan tidak efektif..."
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Fire":
        new_attack = attack*1.5
        efektif_tidak = "Serangan efektif!"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    
elif player == "Grass":
    if lawan == "Grass":
        new_attack = attack*1
        efektif_tidak = "Tidak terjadi perubahan kekuatan serangan"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Fire":
        new_attack = attack*0.5
        efektif_tidak = "Serangan tidak efektif..."
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    if lawan == "Water":
        new_attack = attack*1.5
        efektif_tidak = "Serangan efektif!"
        print("\n", efektif_tidak, "\n", "attack sekarang :", new_attack)
    
else:
    print( "\n", "Inputan Anda salah")