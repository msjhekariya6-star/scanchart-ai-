import yfinance as yf
import pandas as pd

# जिन स्टॉक्स को चेक करना है उनके नाम (उदाहरण के लिए NSE के कुछ स्टॉक)
stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'TATAMOTORS.NS']

def check_stock_growth(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        # पिछले 4 साल का फाइनेंशियल डेटा लेना
        financials = stock.financials # Profit & Loss account
        
        # 1. EPS (Earnings Per Share) निकालना
        eps = financials.loc['Basic EPS']
        
        # 2. OPM और NPM के लिए Revenue और Net Income लेना
        rev = financials.loc['Total Revenue']
        net_inc = financials.loc['Net Income Continuous Operations']
        op_inc = financials.loc['Operating Income']
        
        # मार्जिन कैलकुलेट करना
        opm = (op_inc / rev) * 100
        npm = (net_inc / rev) * 100

        # पिछले 3 साल का डेटा (2024, 2023, 2022) - डेटा उपलब्धता के अनुसार
        # चेक करना कि क्या हर साल बढ़ रहा है
        is_eps_growing = eps.iloc[0] > eps.iloc[1] > eps.iloc[2]
        is_opm_growing = opm.iloc[0] > opm.iloc[1] > opm.iloc[2]
        is_npm_growing = npm.iloc[0] > npm.iloc[1] > npm.iloc[2]

        if is_eps_growing and is_opm_growing and is_npm_growing:
            return True
        return False
    except:
        return False

print("फिल्टर किए जा रहे स्टॉक्स... कृपया प्रतीक्षा करें...")
growing_stocks = [s for s in stocks if check_stock_growth(s)]

print("\n--- वो शेयर्स जिनका OPM, NPM और EPS हर साल बढ़ रहा है ---")
if growing_stocks:
    for s in growing_stocks:
        print(f"✅ {s}")
else:
    print("कोई स्टॉक मैच नहीं हुआ।")
