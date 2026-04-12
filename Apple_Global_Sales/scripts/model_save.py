
import joblib
import os

# Create models directory
models_dir = 'models'
os.makedirs(models_dir, exist_ok=True)

# Model file path
xgb_model_path = os.path.join(models_dir, 'xgboost_apple_sales_model.pkl')

# Save the model
joblib.dump(xgb_final, xgb_model_path)

# Confirm
print("=" * 90)
print("✅ XGBoost Modeli Başarıyla Kaydedildi")
print("=" * 90)
print(f"📁 Kaydedilen Konum: {os.path.abspath(xgb_model_path)}")
print(f"📊 Dosya Boyutu: {os.path.getsize(xgb_model_path) / 1024:.2f} KB")
print("=" * 90)
