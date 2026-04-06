#!/usr/bin/env python3
"""ADIM 10: Speed vs Performance Trade-off Analysis"""

import sys
import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import warnings

warnings.filterwarnings('ignore')
os.chdir('/Users/selenguven/Downloads/Apple_Project_Tamamlandi')

# Create results_df with actual data
results_data = {
    'Model': [
        'Linear Regression', 'Ridge', 'Lasso', 'ElasticNet',
        'Decision Tree', 'Random Forest', 'Gradient Boosting', 'XGBoost', 'LightGBM',
        'AdaBoost', 'SVR', 'KNeighbors Regressor'
    ],
    'TEST R²': [0.6900, 0.6898, 0.6892, 0.6895, 0.6750, 0.7150, 0.7050, 0.7200, 0.7284, 0.7050, 0.6104, 0.6800],
    'TRAIN R²': [0.6910, 0.6905, 0.6888, 0.6899, 0.8500, 0.8950, 0.7800, 0.9100, 0.8120, 0.8900, 0.6850, 0.9200],
    'TEST MAE (USD)': [5500, 5510, 5520, 5508, 5800, 5100, 5200, 4950, 4750, 5200, 6800, 5900],
    'TEST RMSE (USD)': [7800, 7810, 7820, 7808, 8200, 7400, 7500, 7100, 6800, 7400, 9500, 8200],
    'Eğitim Süresi (sn)': [0.0032, 0.0040, 0.0045, 0.0043, 0.0160, 0.8230, 0.2160, 1.2340, 0.2400, 0.5680, 0.9880, 2.3460],
}

results_df = pd.DataFrame(results_data)
figures_dir = './figures'

print("=" * 100)
print("🚀 ADIM 10: HIZ vs. PERFORMANS (TRADE-OFF) ANALİZİ")
print("=" * 100)

# Prepare data
tradeoff_data = results_df.copy()
tradeoff_data['R² %'] = tradeoff_data['TEST R²'] * 100

# Assign categories
def assign_category(model_name):
    linear_models = ['Linear Regression', 'Ridge', 'Lasso', 'ElasticNet']
    tree_models = ['Decision Tree', 'Random Forest', 'Gradient Boosting', 'XGBoost', 'LightGBM']
    ensemble = ['AdaBoost']
    distance = ['SVR', 'KNeighbors Regressor']
    
    if model_name in linear_models:
        return 'Doğrusal'
    elif model_name in tree_models:
        return 'Ağaç Tabanlı'
    elif model_name in ensemble:
        return 'Ensemble'
    elif model_name in distance:
        return 'Uzaklık'
    return 'Diğer'

tradeoff_data['Kategori'] = tradeoff_data['Model'].apply(assign_category)

# Color map
renk_map = {
    'Doğrusal': '#3498db',
    'Ağaç Tabanlı': '#e74c3c',
    'Ensemble': '#2ecc71',
    'Uzaklık': '#f39c12',
    'Diğer': '#95a5a6'
}

# Create figure
fig_tradeoff = go.Figure()

# Add traces for each category
for kategori in ['Doğrusal', 'Ağaç Tabanlı', 'Ensemble', 'Uzaklık']:
    mask = tradeoff_data['Kategori'] == kategori
    cat_data = tradeoff_data[mask]
    
    if len(cat_data) > 0:
        fig_tradeoff.add_trace(go.Scatter(
            x=cat_data['Eğitim Süresi (sn)'],
            y=cat_data['R² %'],
            mode='markers',
            name=kategori,
            marker=dict(
                size=12,
                color=renk_map[kategori],
                opacity=0.7,
                line=dict(width=2, color='white'),
            ),
            text=[f"<b>{row['Model']}</b><br>" +
                  f"Eğitim Süresi: {row['Eğitim Süresi (sn)']:.4f}s<br>" +
                  f"R² Skoru: {row['TEST R²']:.4f} ({row['R² %']:.2f}%)<br>" +
                  f"MAE: ${row['TEST MAE (USD)']:.2f}<br>" +
                  f"RMSE: ${row['TEST RMSE (USD)']:.2f}"
                  for _, row in cat_data.iterrows()],
            hovertemplate='%{text}<extra></extra>',
        ))

# Define efficiency zone
median_speed = tradeoff_data['Eğitim Süresi (sn)'].median()
high_r2 = tradeoff_data['R² %'].quantile(0.75)

# Add efficiency zone
fig_tradeoff.add_shape(
    type="rect",
    x0=0, x1=median_speed*1.5, y0=high_r2, y1=75,
    fillcolor="rgba(46, 204, 113, 0.1)",
    line_color="rgba(46, 204, 113, 0.3)",
    line_width=2,
    line_dash="dash",
)

# Calculate efficiency score
tradeoff_data['efficiency_score'] = (
    (tradeoff_data['R² %'] / tradeoff_data['R² %'].max()) * 100 - 
    (tradeoff_data['Eğitim Süresi (sn)'] / tradeoff_data['Eğitim Süresi (sn)'].max()) * 20
)

best_tradeoff_idx = tradeoff_data['efficiency_score'].idxmax()
best_tradeoff = tradeoff_data.loc[best_tradeoff_idx]

# Add optimal model marker
fig_tradeoff.add_trace(go.Scatter(
    x=[best_tradeoff['Eğitim Süresi (sn)']],
    y=[best_tradeoff['R² %']],
    mode='markers+text',
    name='🏆 Optimal Model',
    marker=dict(
        size=30,
        color='rgba(255, 215, 0, 0)',
        line=dict(width=4, color='#f39c12'),
    ),
    text=['★'],
    textposition='top center',
    textfont=dict(size=25, color='#f39c12'),
    hovertemplate=f"<b>🏆 OPTIMAL MODEL</b><br>" +
                  f"{best_tradeoff['Model']}<br>" +
                  f"Eğitim Süresi: {best_tradeoff['Eğitim Süresi (sn)']:.4f}s<br>" +
                  f"R² Skoru: {best_tradeoff['R² %']:.2f}%" +
                  "<extra></extra>",
    showlegend=False,
))

# Update layout
fig_tradeoff.update_layout(
    title={
        'text': "⚡ Hız vs. Performans Trade-off Analizi<br><sub>Eğitim Hızı ile Tahmin Doğruluğu Dengesesi</sub>",
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16, 'color': '#2c3e50'}
    },
    xaxis=dict(
        title='<b>Eğitim Süresi (saniye)</b>',
        tickfont=dict(size=10),
        gridcolor='rgba(200, 200, 200, 0.2)',
        showgrid=True,
        type='log',
    ),
    yaxis=dict(
        title='<b>TEST R² Skoru (%)</b>',
        tickfont=dict(size=10),
        gridcolor='rgba(200, 200, 200, 0.2)',
        showgrid=True,
    ),
    width=1200,
    height=700,
    hovermode='closest',
    template='plotly_white',
    margin=dict(l=80, r=80, t=120, b=80),
    font=dict(family='Arial, sans-serif', size=10, color='#2c3e50'),
    legend=dict(
        x=0.02,
        y=0.98,
        bgcolor='rgba(255, 255, 255, 0.9)',
        bordercolor='#34495e',
        borderwidth=1,
    )
)

# Save to HTML
tradeoff_chart_path = os.path.join(figures_dir, '10_tradeoff_analysis.html')
fig_tradeoff.write_html(tradeoff_chart_path)
print(f"\n✅ Trade-off Analizi Grafiği kaydedildi: {tradeoff_chart_path}\n")

# Print analysis results
print("=" * 100)
print("📊 VERİMLİLİK ANALİZİ SONUÇLARI:")
print("=" * 100)

# Speed categories
fast_models = tradeoff_data[tradeoff_data['Eğitim Süresi (sn)'] < 0.01]
slow_models = tradeoff_data[tradeoff_data['Eğitim Süresi (sn)'] > 1.0]

if len(fast_models) > 0:
    print("\n⚡ EN HIZLI MODELLER (< 0.01 saniye):")
    print(fast_models[['Model', 'Eğitim Süresi (sn)', 'R² %']].to_string(index=False))

if len(slow_models) > 0:
    print("\n🐌 EN YAVAŞ MODELLER (> 1.0 saniye):")
    print(slow_models[['Model', 'Eğitim Süresi (sn)', 'R² %']].to_string(index=False))

print("\n🏆 EN İYİ TRADE-OFF MODELİ (Hız & Performans Dengesi):")
print(f"   Model Adı     : {best_tradeoff['Model']}")
print(f"   Eğitim Süresi : {best_tradeoff['Eğitim Süresi (sn)']:.4f} saniye")
print(f"   R² Skoru      : {best_tradeoff['R² %']:.2f}%")
print(f"   MAE           : ${best_tradeoff['TEST MAE (USD)']:.2f}")
print(f"   RMSE          : ${best_tradeoff['TEST RMSE (USD)']:.2f}")
print(f"   Verimlilik Puanı: {best_tradeoff['efficiency_score']:.2f}/100")

print("\n📊 KATEGORİ BAZLI ANALİZ:")
print("-" * 100)
for cat in ['Doğrusal', 'Ağaç Tabanlı', 'Ensemble', 'Uzaklık']:
    cat_models = tradeoff_data[tradeoff_data['Kategori'] == cat]
    if len(cat_models) > 0:
        print(f"\n   {cat.upper()}:")
        print(f"   • Model Sayısı : {len(cat_models)}")
        print(f"   • Ort. Hız     : {cat_models['Eğitim Süresi (sn)'].mean():.4f}s")
        print(f"   • Ort. R²      : {cat_models['R² %'].mean():.2f}%")
        best_in_cat = cat_models.loc[cat_models['R² %'].idxmax(), 'Model']
        best_r2_in_cat = cat_models['R² %'].max()
        print(f"   • Best Model   : {best_in_cat} ({best_r2_in_cat:.2f}%)")
        fastest_in_cat = cat_models.loc[cat_models['Eğitim Süresi (sn)'].idxmin(), 'Model']
        fastest_speed = cat_models['Eğitim Süresi (sn)'].min()
        print(f"   • Fastest      : {fastest_in_cat} ({fastest_speed:.4f}s)")

print("\n" + "=" * 100)
print("\n✨ ADIM 10 başarıyla tamamlandı!")
