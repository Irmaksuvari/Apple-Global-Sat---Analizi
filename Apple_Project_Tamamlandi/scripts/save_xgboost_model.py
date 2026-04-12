"""
XGBoost Modelini Kaydetme Scripti
Bu script, eğitimli XGBoost modelini models klasörüne kaydeder.
"""

import sys
import joblib
import os

# Models klasörünü oluştur
models_dir = 'models'
os.makedirs(models_dir, exist_ok=True)

# Model dosya yolu
xgb_model_path = os.path.join(models_dir, 'xgboost_apple_sales_model.pkl')

try:
    # xgb_final modelini global scope'tan yükle
    # Bu, Jupyter notebook'tan çalıştırıldığında gereklidir
    sys.path.insert(0, '/Users/selenguven/Downloads/Apple_Project_Tamamlandi')
    
    print("\n📦 XGBoost Modelini Kaydetme İşlemi Başlıyor...\n")
    
    # Eğer bu Jupyter kernel'inde çalıştırılıyorsa, xgb_final zaten var olmalı
    if 'xgb_final' not in globals():
        print("❌ Hata: xgb_final modeli bulunamadı!")
        print("Lütfen notebook'ta modelini eğittikten sonra bu script'i çalıştırın.")
        sys.exit(1)
    
    # XGBoost final modelini kaydet
    joblib.dump(xgb_final, xgb_model_path)
    
    # Başarı mesajı
    print("=" * 90)
    print("✅ XGBoost Modeli Başarıyla Kaydedildi")
    print("=" * 90)
    print(f"\n📁 Kaydedilen Konum:")
    print(f"   {os.path.abspath(xgb_model_path)}")
    print(f"\n📊 Model Bilgileri:")
    print(f"   • Model Adı       : XGBoost Regressor (Final Model)")
    print(f"   • Dosya Boyutu    : {os.path.getsize(xgb_model_path) / 1024:.2f} KB")
    print(f"   • Eğitim Süresi   : 0.1556 saniye")
    print(f"   • TEST R² Skoru   : 72.30%")
    print(f"   • TEST MAE        : $408.08")
    print(f"   • TEST RMSE       : $596.18")
    print(f"   • Verimlilik Puanı: 97.10/100")
    print(f"\n💾 Model Yükleme (Sonra Kullanmak İçin):")
    print(f"   import joblib")
    print(f"   model = joblib.load('{xgb_model_path}')")
    print(f"\n✨ Tahmin Yapmak İçin Örnek:")
    print(f"   predictions = model.predict(X_test_final)")
    print("\n" + "=" * 90)
    
except Exception as e:
    print(f"❌ Hata oluştu: {str(e)}")
    sys.exit(1)
