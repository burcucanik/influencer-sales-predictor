def predict_sales(metrics):
    try:
        followers = int(metrics['Followers'].replace(',', '').replace('K', '000').split('.')[0])
        engagement_rate = float(metrics['Engagement Rate'].replace('%', '').replace('<', '0'))
        authentic_engagement = int(metrics['Authentic Engagement'].replace(',', ''))
        reach = int(metrics['Reach'].replace(',', '').replace('K', '000').split('.')[0])
        aqs = int(metrics['Audience Quality Score (AQS)'])
        return (authentic_engagement + 0.08 * reach + 0.03 * followers + aqs * 4) * (1 + engagement_rate / 100)
    except:
        return 0.0

def calculate_sales_score(metrics):
    try:
        er = float(metrics['Engagement Rate'].replace('%', '').replace('<', '0'))
        ae = int(metrics['Authentic Engagement'].replace(',', ''))
        reach = int(metrics['Reach'].replace(',', '').replace('K', '000').split('.')[0])
        followers = int(metrics['Followers'].replace(',', '').replace('K', '000').split('.')[0])
        aqs = int(metrics['Audience Quality Score (AQS)'])

        score = 1000 / (er + 1) + ae * 1.5 + (reach * 0.02) + (aqs * 10) - (followers * 0.001)
        return max(score, 0)
    except:
        return 0.0
