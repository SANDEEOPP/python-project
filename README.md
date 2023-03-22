lambda function for add items to cart

import json
import psycopg2
import os

def lambda_handler(event, context):
    # Extract necessary parameters from event
    user_id = event['user_id']
    product_id = event['product_id']
    quantity = event['quantity']
    
    # Connect to RDS PostgreSQL database
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_DATABASE']
    )
    
    # Insert cart item into database
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO cart_item (user_id, product_id, quantity) VALUES (%s, %s, %s)",
        (user_id, product_id, quantity)
    )
    conn.commit()
    
    # Return success response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item added to cart successfully'})
    }
    return response



lambda function for remove items from cart

import json
import psycopg2
import os

def lambda_handler(event, context):
    # Extract necessary parameters from event
    user_id = event['user_id']
    product_id = event['product_id']
    
    # Connect to RDS PostgreSQL database
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_DATABASE']
    )
    
    # Delete cart item from database
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM cart_item WHERE user_id = %s AND product_id = %s",
        (user_id, product_id)
    )
    conn.commit()
    
    # Return success response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item removed from cart successfully'})
    }
    return response


lambda function for view cart

import json
import psycopg2
import os

def lambda_handler(event, context):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    
    # Retrieve cart items for the given user ID
    user_id = event['user_id']
    cur = conn.cursor()
    cur.execute("SELECT * FROM cart WHERE user_id=%s", (user_id,))
    cart_items = cur.fetchall()
    
    # Convert result set to JSON format
    cart_data = []
    for item in cart_items:
        item_dict = {
            'product_id': item[0],
            'quantity': item[1]
        }
        cart_data.append(item_dict)
    
    response = {
        'statusCode': 200,
        'body': json.dumps(cart_data)
    }
    
    return response

lambda function for checkout 
import json
import psycopg2
import os

def lambda_handler(event, context):
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    
    # Retrieve cart items for the given user ID
    user_id = event['user_id']
    cur = conn.cursor()
    cur.execute("SELECT * FROM cart WHERE user_id=%s", (user_id,))
    cart_items = cur.fetchall()
    
    # Insert cart items into orders table
    cur.execute("INSERT INTO orders (user_id, order_items) VALUES (%s, %s)", (user_id, json.dumps(cart_items)))
    conn.commit()
    
    # Clear cart for the given user ID
    cur.execute("DELETE FROM cart WHERE user_id=%s", (user_id,))
    conn.commit()
    
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Checkout successful'})
    }
    
    return response



lambda function codes for Order tracking 
import os
import psycopg2

def lambda_handler(event, context):
    # Extract order_id from the event
    order_id = event['order_id']

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    cursor = conn.cursor()

    # Execute SQL query to retrieve order tracking data
    cursor.execute('SELECT status, date FROM order_tracking WHERE order_id = %s', (order_id,))
    rows = cursor.fetchall()

    # Convert results to a dictionary
    results = []
    for row in rows:
        results.append({'status': row[0], 'date': row[1].strftime('%Y-%m-%d %H:%M:%S')})

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the results as a JSON object
    return {'order_id': order_id, 'tracking_data': results}

implementation of the get_user_info function in Python that includes error handling:

import requests
def get_user_info(user_id):
    try:
        response = requests.get(f'https://example.com/users/{user_id}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f'User with ID {user_id} not found')
        else:
            print(f'Server error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
