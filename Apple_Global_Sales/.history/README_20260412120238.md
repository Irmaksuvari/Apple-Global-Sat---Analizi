# 🍎 Apple Global Sales - Kapsamlı Veri Analizi Projesi

## 📋 Proje Özeti

Bu proje, **Apple'ın küresel satış operasyonlarının** derinlemesine veri analizi ve makine öğrenmesi modellemesini gerçekleştirmektedir. Ana amaç, **indirim stratejilerinin satış hacmi ve gelire etkisini anlamak**, müşteri davranışlarını incelemek ve satış performansını tahmin etmektir.

### 🎯 Ana Problemi

Apple'ın karşılaştığı "**fiyat erozyonu paradoksu**":
- **Pazarlama Ekibi:** "İndirim oranlarını artıralım, satış hacmi (Units Sold) artacak!"
- **Finans Ekibi:** "İndirim yaparsak birim başı kar düşer, toplam gelir (Revenue) azalabilir!"

Bu proje, **`discount_pct` (indirim oranı) ve `revenue_usd` (toplam gelir)** arasındaki ilişkiyi ortaya çıkararak bu tartışmanın sonucunu belirlemeye yardımcı olur.

---

## 📁 Proje Yapısı

```
📂 Apple_Global_Sales/
├── 📂 data/
│   ├── 📂 raw/                     # Ham veri dosyaları
│   └── 📂 processed/               # İşlenmiş veri dosyaları
├── 📂 figures/                     # Görselleştirmeler (HTML, CSVs)
│   ├── 01_dtype_distribution.html
│   ├── 02_memory_usage.html
│   ├── 03_missing_values.html
│   ├── ... (50+ görselleştirme)
│   └── index.html                  # Dashboard
├── 📂 models/                      # Eğitilmiş makine öğrenmesi modelleri
├── 📂 scripts/                     # Python yardımcı scripti
│   ├── adim10_tradeoff.py
│   ├── model_save.py
│   └── save_xgboost_model.py
├── 📂 media/                       # Medya dosyaları
│   ├── video.mp4                   # Proje sunumu videosu
│   └── son.jpeg                    # Takım fotoğrafı
├── 📄 apple_global_analysis.ipynb  # Ana Jupyter Notebook (~120 cell)
└── 📄 README.md                    # Bu dosya
```

---

## 📊 Veri Sözlüğü (Data Dictionary)

Veri seti **27 değişken** içermektedir:

### Tanımsal Değişkenler (Dimensional)
| Değişken | Tür | Açıklama |
|----------|-----|----------|
| `sale_id` | Metin | İşlem benzersiz kimliği |
| `sale_date` | Tarih | İşlem tarihi |
| `year`, `quarter`, `month` | Sayı | Zamansal bilgiler |
| `country`, `region`, `city` | Metin | Coğrafik bilgiler |
| `product_name`, `category` | Metin | Ürün bilgileri |
| `storage`, `color` | Metin | Ürün özellikleri |
| `sales_channel` | Metin | Satış kanalı/mağaza |
| `payment_method` | Metin | Ödeme yöntemi |
| `customer_segment`, `customer_age_group` | Metin | Müşteri profili |
| `previous_device_os` | Metin | Önceki cihaz OS |
| `currency` | Metin | Para birimi |

### Finansal Değişkenler
| Değişken | Birim | Açıklama |
|----------|------|----------|
| `unit_price_usd` | USD | Orijinal birim fiyatı |
| `discount_pct` | % | İndirim yüzdesi (**Kritik**) |
| `discounted_price_usd` | USD | İndirimli birim fiyatı |
| `units_sold` | Adet | Satılan ürün sayısı |
| `revenue_usd` | USD | Toplam satış geliri (**Hedef**) |
| `revenue_local_currency` | Yerel | Yerel para biriminde gelir |
| `fx_rate_to_usd` | Oran | Döviz kuru |

### Müşteri Geri Bildirim
| Değişken | Aralık | Açıklama |
|----------|--------|----------|
| `customer_rating` | 1-5 | Müşteri memnuniyeti puanı |
| `return_status` | Categorical | İade durumu (Returned/Not Returned) |

---

## 🔄 Proje Adımları (Detaylı Analiz Akışı)

### **ADIM 1: Veri Yükleme ve İlk İnceleme**
- Raw veri dosyalarını pandas ile yükle
- Veri boyutu ve hafıza kullanımını analiz et
- İlk 10 satırı incele ve veri türlerini kontrol et
- **Output:** `01_dtype_distribution.html`, `02_memory_usage.html`

### **ADIM 2: Eksik Veri Analizi**
- Her sütundaki eksik değerleri tanımla
- Eksik veri dağılımını kaç % olduğunu göster
- Eksik veri pattern'ini visualize et
- İmpütasyon stratejisi geliştir (ortalama, medyan, forward fill, vb.)
- **Output:** `03_missing_values.html`, `24_missing_values_interactive.html`

### **ADIM 3: Veri Temizleme ve İşleme**
- Eksik değerleri uygun metodlarla doldur
- Duplikat kayıtları tanımla ve kaldır
- Veri türlerini düzelt (tarihler, kategoriler, sayılar)
- Tutarsızlıkları (negatif fiyatlar, %0-%100 dışı rabatlar) tespit et
- **Output:** `25_duplicate_records_analysis.html`, `27_data_preparation_results.html`

### **ADIM 4: Sayısal Değişken Analizi**
- Betimleyici istatistikler (ortalama, medyan, std, min, max)
- Dağılım şekli analizi (normal, çarpık mı?)
- **Box Plot** ile aykırı değerleri (outliers) tespit et
- **Violin Plot** ile dağılım yoğunluğunu göster
- **Output:** `04_numerical_boxplots_pastel.html`, `04_numerical_violinplots_pastel.html`, `06_individual_boxplots_outliers.html`

### **ADIM 5: Aykırı Değer (Outlier) Analizi**
- IQR (1. ve 3. çeyrekler arası) yöntemi ile aykırıları tanımla
- Z-score analizi ile uzak noktaları bul
- Aykırı değerleri visualize et
- Kaldırılacak/tutulacak aykırıları kararlaştır
- **Output:** `04_outliers_analysis.html`, `05_outliers_boxplot.html`, `27_outlier_boxplots.html`

### **ADIM 6: Kategorik Değişken Analizi**
- Kategorisel değişkenlerin sınıf dağılımını analiz et
- Sıklık tabloları oluştur
- Class imbalance sorunlarını tespit et
- **Output:** `26_target_variable_class_distribution.html`, `26_units_sold_class_imbalance.html`

### **ADIM 7: İlişki Analizi (Bivariate)**
- Sayısal değişkenler arası korelasyonu hesapla
- **Scatter Plot:** discount vs revenue, discount vs units ilişkisini göster
- **Box Plot:** kategorik vs sayısal değişkenlerin ilişkisini analiz et
  - Satış Kanalı × Revenue
  - Satış Kanalı × Units Sold
  - Kategori × Revenue/Units
  - Müşteri Segmenti × Revenue
- **Violin Plot:** dağılım karşılaştırması
- **Output:** `12_correlation_heatmap.html`, `18_scatter_discount_sales_regression.html`, `15_category_revenue_usd_boxplot_violin.html`, vb.

### **ADIM 8: Zaman Serisi Analizi**
- Yıllar/Aylar bazında satış trendlerini izle
- Mevsimsel (seasonal) pattern'leri tespit et
- Çeyrek (Quarter) ve Ay düzeyinde performansı karşılaştır
- **Output:** `11_year_timeline.html`, `21_monthly_quantile_analysis.html`, `22_interactive_quarterly_monthly_discount.html`

### **ADIM 9: Coğrafik Analiz (Ülke/Bölge)**
- Ülke ve bölge bazında satış performansını karşılaştır
- En iyi/en kötü performans gösteren bölgeleri tespit et
- Ridgeline plot'lar ile dağılımları göster
- **Output:** `17_ridgeline_region_unitssold.html`

### **ADIM 10: İndirim Stratejisi Analizi (Core Analysis)**
- **İndirim × Satış Hacmi:** Daha fazla indirim = daha fazla satış mı?
- **İndirim × Gelir:** Daha fazla indirim = daha az gelir mi?
- Ürün kategorisine göre indirim etkilerini analiz et
- Müşteri segmentine göre indirim duyarlılığını ölç
- Bölgesel farklılıkları tespit et
- **Regresyon analizi:** İndirim, fiyat ve diğer faktörlerin revenue'ya etkisini model et
- **Output:** `18_scatter_discount_sales_regression.html`, `21_scatter_discount_quantity_regression.html`, `19_boxplot_discount_product.html`, `10_tradeoff_analysis.html`

### **ADIM 11: Veri Kalitesi Raporu**
- Eksik veri, duplikat, aykırı değer özeti
- Veri tamanız ve tutarlılık puanı
- **Output:** `28_data_quality_heatmap.html`, `29_data_quality_vertical_bar.html`

### **ADIM 12: Model Geliştirme (Makine Öğrenmesi)**

#### **12.1. Veri Hazırlığı**
- Feature engineering: yeni özellikleri oluştur
- Kategorik değişkenleri one-hot encode et
- Sayısal özellikleri normalize/standardize et
- Train-Test split: 80-20 veya cross-validation

#### **12.2. Model Seçimi & Eğitimi**
Kullanılan modeller:
- **Linear Regression:** Baseline model (hızlı, yorumlanabilir)
- **Decision Tree Regressor:** Non-linear ilişkileri yakala
- **Random Forest Regressor:** Ensemble, robust tahminler
- **XGBoost Regressor:** Gradient boosting, yüksek performans
- **Support Vector Machine (SVM):** Kernel, non-linear mapping

#### **12.3. Hiperparametre Optimizasyonu**
- GridSearch veya RandomSearch ile en iyi parametreleri bul
- Cross-validation (5-Fold) ile model stabilitesini test et
- **Output:** `30_hyperparameter_optimization_comparison.html`

#### **12.4. Model Değerlendirmesi**
- **Metrikler:**
  - MAE (Mean Absolute Error) - ortalama mutlak hata
  - RMSE (Root Mean Square Error) - kare ortalama hatası
  - R² Score - açıklanan varyans oranı
  - MAPE (Mean Absolute Percentage Error) - yüzde hata
  
- **Grafikleri:**
  - Actual vs Predicted scatter plot
  - Residual (hata) dağılımı
  - Learning curves (overfitting/underfitting analizi)
  - Feature importance (hangi features en etkili?)
  
- **Output:** `08_r2_comparison_chart.html`, `09_error_metrics_rmse_mae.html`, `10_overfitting_interactive_analysis.html`, `11_cv_consistency_analysis_interactive.html`, `12_models_performance_comparison.csv`, `12_models_radar_chart.html`, `29_training_time_vs_performance.html`

#### **12.5. Cross-Validation Analizi**
- 5-Fold CV ile model stabilitesini test et
- Fold'lar arası performance farklılıklarını analiz et
- **Output:** `07_5fold_cv_analysis.html`, `11_cv_grouped_bar_interactive.html`

### **ADIM 13: Test Seti Tahminleri & Gerçek Veriler**
- Eğitilmiş modelle test setinde tahmin yap
- Gerçek değerler vs tahmin edilen değerleri karşılaştır
- Hata dağılımını analiz et
- **Output:** `31_real_data_test_sample_predictions.html`

### **ADIM 14: 3D Görselleştirmeler & İleri Analizler**
- İndirim × Fiyat × Satış Miktarı 3D scatter
- İnteraktif dashboard'lar (Plotly)
- Müşteri memnuniyeti vs diğer faktörler
- İade oranı analizi
- **Output:** `22_3d_scatter_discount_price_quantity.html`, `14_customer_rating_distribution.html`, `13_scatter_target_analysis.html`

### **ADIM 15: Model Kaydetme & Productionize**
- Eğitilmiş modelleri `.pkl` veya `.joblib` formatında kaydet
- Model meta-datası: feature names, scaler parameters, etc.
- **Scripts:** `model_save.py`, `save_xgboost_model.py`

---

## 🚀 Nasıl Çalıştırılır?

### Gereksinimler
```bash
# Python 3.8+
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost scipy statsmodels
```

### Proje Çalıştırma Adımları

1. **Jupyter Notebook'u Aç**
   ```bash
   jupyter notebook notebooks/apple_global_analysis.ipynb
   ```

2. **Tüm Cell'leri Sırayla Çalıştır**
   - Kernel → Restart & Run All
   - Veya hücre hücre çalıştır (Shift + Enter)

3. **Sonuçları Kontrol Et**
   - `figures/` klasöründe 50+ HTML görselleştirme oluşacak
   - `models/` klasöründe eğitilmiş modeller kaydedilecek
   - Notebook'ta tüm analiz resultları gösterilecek

---

## 📈 Temel Bulgular

### Veri Özeti
- **Toplam İşlem Sayısı:** [Analiz Sonrası]
- **Zaman Aralığı:** [Tarih Aralığı]
- **Ülke Sayısı:** [Sayı]
- **Ürün Kategorileri:** [Sayı]

### İndirim Paradoksu
1. **İndirim × Satış Hacmi Korelasyonu:** (+) → Daha fazla indirim = daha fazla satış
2. **İndirim × Gelir Korelasyonu:** (-) → Daha fazla indirim = daha az gelir
3. **Optimal İndirim Oranı:** [Analiz Sonrası Belirlenecek]

### Model Performansı
- **En İyi Model:** [Model Adı]
- **R² Skoru:** [Değer]
- **RMSE:** [Değer] USD
- **MAE:** [Değer] USD

---

## 📊 Görselleştirmeler (50+ Grafik)

### Veri Kalitesi
- `01_dtype_distribution.html` - Veri türü dağılımı
- `02_memory_usage.html` - Hafıza kullanımı
- `03_missing_values.html` - Eksik değerler

### İstatistiksel Analiz
- `04_numerical_boxplots_pastel.html` - Box plot
- `04_numerical_violinplots_pastel.html` - Violin plot
- `05_outliers_analysis.html` - Aykırı değer analizi
- `06_individual_boxplots_outliers.html` - Birey x birey outliers

### Segmentasyon & Kategori
- `14_customer_rating_distribution.html` - Müşteri dereceleri
- `15_category_revenue_usd_boxplot_violin.html` - Kategori × Revenue
- `15_category_units_sold_boxplot_violin.html` - Kategori × Units
- `16_bivariate_saleschannel_revenueusd_boxplot.html` - Satış Kanalı × Revenue
- `16_bivariate_saleschannel_unitssold_boxplot.html` - Satış Kanalı × Units

### İndirim Analizi
- `18_scatter_discount_sales_regression.html` - İndirim vs Satış (Regresyon)
- `21_scatter_discount_quantity_regression.html` - İndirim vs Miktar
- `19_boxplot_discount_product.html` - Ürün türü × İndirim
- `20_boxplot_discount_region.html` - Bölge × İndirim
- `21_month_percentile_discount_analysis.html` - Aylık İndirim Yüzdelikleri
- `10_tradeoff_analysis.html` - İndirim ↔ Gelir Trade-off

### Zaman Serisi
- `11_year_timeline.html` - Yıllık timeline
- `21_monthly_quantile_analysis.html` - Aylık quantile analiz
- `22_interactive_quarterly_monthly_discount.html` - Çeyrek/Ay İndirim

### Coğrafik
- `17_ridgeline_region_unitssold.html` - Bölgeler x Satış Miktarı

### 3D & İleri Analiz
- `22_3d_scatter_discount_price_quantity.html` - İndirim × Fiyat × Miktar
- `13_scatter_target_analysis.html` - Hedef değişken analizi

### Model Performansı
- `07_5fold_cv_analysis.html` - 5-Fold Cross-Validation
- `08_r2_comparison_chart.html` - R² Karşılaştırması
- `09_error_metrics_rmse_mae.html` - Hata Metrikleri (RMSE, MAE)
- `10_overfitting_interactive_analysis.html` - Overfitting Analizi
- `11_cv_consistency_analysis_interactive.html` - CV Tutarlılığı
- `12_models_performance_comparison.csv` - Model Performans Tablosu
- `12_models_radar_chart.html` - Radar Chart (Modeller)
- `12_models_test_r2_comparison.html` - Test R² Comparison
- `29_training_time_vs_performance.html` - Eğitim Zamanı vs Performans
- `31_real_data_test_sample_predictions.html` - Tahmin Sonuçları

### Veri Kalitesi Raporu
- `25_duplicate_records_analysis.html` - Duplikat Analiz
- `26_target_variable_class_distribution.html` - Hedef Sınıf Dağılımı
- `26_units_sold_class_imbalance.html` - Class Imbalance
- `27_data_preparation_results.html` - Veri Hazırlama Sonuçları
- `28_data_quality_heatmap.html` - Veri Kalitesi Heatmap
- `29_data_quality_vertical_bar.html` - Veri Kalitesi Bar
- `24_imputation_comparison.html` - İmpütasyon Karşılaştırması
- `24_missing_values_interactive.html` - İnteraktif Eksik Değersler
- `24_missing_values_vertical_interactive.html` - Dikey İnteraktif Eksik

### Korelasyon & İlişkiler
- `12_correlation_heatmap.html` - Korelasyon Heatmap
- `29_correlation_heatmap_filtered.html` - Filtrelenmiş Korelasyon
- `05_scatter_plots_relationships.html` - İlişki Scatter Plot'ları
- `30_hyperparameter_optimization_comparison.html` - Hyperparametre Optimizasyonu

---

## 🔧 Kullanılan Kütüphaneler & Teknolojiler

### Veri İşleme
- **pandas** - Veri manipülasyonu
- **numpy** - Sayısal hesaplamalar

### Görselleştirme
- **matplotlib** - Statik grafikler
- **seaborn** - İstatistiksel görselleştirme
- **plotly** - İnteraktif, web-tabanlı grafikler
- **plotly.subplots** - Subplot oluşturma

### Makine Öğrenmesi
- **scikit-learn** - ML modelleri, preprocessing, evaluation
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - SVM
  - GridSearchCV
  - KFold Cross-Validation
- **XGBoost** - Gradient boosting modeli
- **scipy** - İstatistiksel testler

### Diğer
- **statsmodels** - Regresyon analizi, istatistiksel testler
- **joblib/pickle** - Model serileştirme

---

## 📌 Önemli Noktalar

### Veri Kalitesi
✅ Eksik veri kontrol edildi ve uygun yöntemlerle dolduruldu
✅ Duplikat kayıtlar temizlendi
✅ Aykırı değerler tanımlandı ve raporlandı
✅ Veri konsistensiyesi doğrulandı

### Model Geçerliliği
✅ Train-Test split ile overfitting kontrol edildi
✅ 5-Fold Cross-Validation uygulandı
✅ Hiperparametre optimizasyonu yapıldı
✅ Birden fazla model karşılaştırıldı

### Yorumlanabilirlik
✅ Feature importance grafikleri oluşturuldu
✅ Residual analizi yapıldı
✅ Açıklanan varyans oranı (R²) hesaplandı

---

## 📚 Referanslar & Kaynaklar

- **Scikit-learn Dokumentasyon:** https://scikit-learn.org/
- **Plotly Dokumentasyon:** https://plotly.com/python/
- **XGBoost Dokumentasyon:** https://xgboost.readthedocs.io/
- **Pandas Dokumentasyon:** https://pandas.pydata.org/

---

## 👥 Proje Ekibi

*Apple Global Sales Analytics Team* 🍎

---

## 📞 Destek

Sorular veya sorunlar için lütfen:
- Notebook'taki açıklama hücrelerini (Markdown cells) okuyun
- Hata mesajlarını dikkatle inceleyin
- Gerekirse veri setinin yorum satırlarını kontrol edin

---

## 📅 Son Güncelleme

**Tarih:** 2024-2026
**Versiyon:** 1.0
**Durum:** ✅ Tamamlandı

---

## 🎓 Öğrenme Hedefleri

Bu proje tamamlandıktan sonra, aşağıdaki beceriler kazanılmıştır:

1. **Veri Analizi & Temizleme**
   - Eksik veri işleme
   - Aykırı değer tespiti
   - Veri kalitesi değerlendirmesi

2. **Istatistiksel Analiz**
   - Tanımlayıcı istatistikler
   - Korelasyon analizi
   - Hipotez testleri

3. **Görselleştirme**
   - Pandas/Matplotlib/Seaborn
   - Plotly ile interaktif grafikler
   - Dashboard oluşturma

4. **Makine Öğrenmesi**
   - Model seçimi ve eğitimi
   - Hiperparametre optimizasyonu
   - Cross-Validation
   - Model değerlendirmesi

5. **İş Analizi Bussiness Intelligence**
   - Domain bilgisi (e-ticaret, satış)
   - İş sorularını veri sorularına dönüştürme
   - İçgörüleri actionable kıl

---

**Happy Analysis! 🎉**
