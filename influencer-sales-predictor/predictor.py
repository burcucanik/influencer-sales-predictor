def predict_sales(metrics):
    try:
        followers = int(metrics['Followers'].replace(',', '').replace('K', '000').split('.')[0])
        engagement_rate = float(metrics['Engagement Rate'].replace('%', ''))
        authentic_engagement = int(metrics['Authentic Engagement'].replace(',', ''))
        reach = int(metrics['Reach'].replace('K', '000').replace(',', '').split('.')[0])
        aqs = int(metrics['Audience Quality Score (AQS)'])

        # Basit skor bazlı tahmin algoritması
        score = (authentic_engagement + (reach * 0.1) + (followers * 0.05) + (aqs * 10)) * (1 + engagement_rate / 100)
        return round(score / 100, 2)
    except:
        return 0.0
