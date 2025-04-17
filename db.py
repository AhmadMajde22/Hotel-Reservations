import os
import psycopg2

def insert_reservation(data, prediction):
    # Get database credentials from environment variables
    host = os.getenv("DB_HOST", "localhost")  # default to 'localhost' if the env variable is not set
    port = os.getenv("DB_PORT", "5432")  # default to '5432' if the env variable is not set
    database = os.getenv("DB_NAME", "hotel_prediction_db")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "123456")

    # Establish a connection to the database
    try:
        with psycopg2.connect(
            host=host,
            port=port,  # specify port here
            database=database,
            user=user,
            password=password
        ) as conn:
            with conn.cursor() as cur:
                # SQL query to insert reservation data
                query = """
                    INSERT INTO reservations (
                        lead_time, no_of_special_request, avg_price_per_room,
                        arrival_month, arrival_date, market_segment_type,
                        no_of_week_nights, no_of_weekend_nights, type_of_meal_plan,
                        room_type_reserved, prediction
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                # Values to be inserted into the table
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

                # Execute the query
                cur.execute(query, values)
                conn.commit()
                print("Reservation data inserted successfully.")
    except Exception as e:
        print(f"Error inserting reservation data: {e}")
