# मान लीजिए 'df' आपकी कंपनी का डेटा है
def check_growth(data):
    # पिछले 3 साल का डेटा चेक करना
    opm_growing = data['OPM_2025'] > data['OPM_2024'] > data['OPM_2023']
    npm_growing = data['NPM_2025'] > data['NPM_2024'] > data['NPM_2023']
    eps_growing = data['EPS_2025'] > data['EPS_2024'] > data['EPS_2023']
    
    if opm_growing and npm_growing and eps_growing:
        return "Best Stock"
