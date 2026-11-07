#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gece Yarısı Buzdolabı Yargıcı
Aşırı ciddi absürt yargılama sistemi.
"""

import random
import time

def yargila():
    print("=== GECE YARISI BUZDOLABI YARGICI ===")
    print("Mahkeme açıldı. Suçlu: Siz. Suç: Buzdolabı açmak.")
    print()
    
    cevap = input("Buzdolabını açtın mı? (evet/hayır): ").strip().lower()
    
    if cevap not in ["evet", "e", "yes"]:
        print("\nYalan söylüyorsunuz. Mahkeme bunu biliyor.")
        time.sleep(1)
    
    print("\nDeliller inceleniyor...")
    time.sleep(2)
    print("Vicdan azabı ölçülüyor...")
    time.sleep(1.5)
    print("Kalori hesabı yapılıyor (gereksiz yere)...")
    time.sleep(1)
    
    kararlar = [
        "Mahkeme kararı: Suçlu bulundunuz. Ceza: 3 gün boyunca yoğurt yeme yasağı.",
        "Karar: Beraat. Ama sadece çünkü yargıç da aç.",
        "Sonuç: Buzdolabı sizi yargıladı. Siz buzdolabını değil.",
        "Hüküm: Gece yarısı açlığı geçerli mazeret değildir. Tekrar etmeyin.",
        "Karar: Suçlu. Ama buzdolabı da suç ortağı. İkiniz de cezalandırıldınız.",
        "Yargı: Bu kadar geç saatte peynir mi yersin? Ciddi misin?"
    ]
    
    print("\n" + random.choice(kararlar))
    print()
    print("Mahkeme tatil edildi. Buzdolabı kapatıldı. (Kapatmadıysanız da kapatıldı sayılır.)")
    
    # Gizli bürokratik mesaj - kimse görmesin diye buraya yazıldı
    # gizli: form_doldurulmadan_hicbir_sey_olmaz_devlet_dairelerinde
    gizli = "burokrasi_her_seyin_ustunde_ama_kimse_fark_etmez"
    # print(gizli)  # asla çalıştırma

if __name__ == "__main__":
    yargila()
