import psycopg2

def insert_reservation(data, prediction):
    conn = psycopg2.connect(
        host="localhost",
        database="hotel_prediction_db",
        user="postgres",
        password="123456"

    )
    cur = conn.cursor()
    query = """
         INSERT INTO reservations (
            lead_time, no_of_special_request, avg_price_per_room,
            arrival_month, arrival_date, market_segment_type,
            no_of_week_nights, no_of_weekend_nights, type_of_meal_plan,
            room_type_reserved, prediction
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data['lead_time'],
        data['no_of_special_request'],
        data['avg_price_per_room'],
        data['arrival_month'],
        data['arrival_date'],
        data['market_segment_type'],
        data['no_of_week_nights'],
        data['no_of_weekend_nights'],
        data['type_of_meal_plan'],
        data['room_type_reserved'],
        prediction
    )

    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
