
# Hotel Management API

This is a FastAPI application for managing a hotel, built with AlloyDB.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Set up the environment:**

    Create a `.env` file with your AlloyDB instance details:

    ```
    INSTANCE_CONNECTION_NAME=<your-instance-connection-name>
    DB_USER=<your-db-user>
    DB_PASS=<your-db-password>
    DB_NAME=<your-db-name>
    DB_HOST=127.0.0.1
    DB_PORT=8080
    ```

3.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Start the AlloyDB Auth Proxy:**

    In a separate terminal, run the following command. Make sure the `alloydb-auth-proxy` executable is in your project directory and is executable (`chmod +x alloydb-auth-proxy`).

    ```bash
    ./alloydb-auth-proxy "<your-instance-connection-name>" --public-ip --port 8080
    ```

6.  **Run the application:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

The application will be accessible at `http://localhost:8000`.

## Key Endpoints

### Hotels

*   `POST /hotels/`: Create a new hotel.
*   `GET /hotels/`: Get a list of all hotels.
*   `GET /hotels/{hotel_id}`: Get a specific hotel by ID.
*   `PUT /hotels/{hotel_id}`: Update a hotel.
*   `DELETE /hotels/{hotel_id}`: Delete a hotel.

### Rooms

*   `POST /rooms/`: Create a new room.
*   `GET /rooms/`: Get a list of all rooms.
*   `GET /rooms/{room_id}`: Get a specific room by ID.
*   `PUT /rooms/{room_id}`: Update a room.
*   `DELETE /rooms/{room_id}`: Delete a room.
*   `GET /rooms/available/`: Find available rooms.

### Customers

*   `POST /customers/`: Create a new customer.
*   `GET /customers/`: Get a list of all customers.
*   `GET /customers/{customer_id}`: Get a specific customer by ID.
*   `PUT /customers/{customer_id}`: Update a customer.
*   `DELETE /customers/{customer_id}`: Delete a customer.

### Bookings

*   `POST /bookings/`: Create a new booking.
*   `GET /bookings/`: Get a list of all bookings.
*   `GET /bookings/{booking_id}`: Get a specific booking by ID.
*   `PUT /bookings/{booking_id}`: Update a booking.
*   `DELETE /bookings/{booking_id}`: Delete a booking.

### Room Types

*   `POST /room_types/`: Create a new room type.
*   `GET /room_types/`: Get a list of all room types.
*   `GET /room_types/{room_type_id}`: Get a specific room type by ID.
*   `PUT /room_types/{room_type_id}`: Update a room type.
*   `DELETE /room_types/{room_type_id}`: Delete a room type.

### Amenities

*   `POST /amenities/`: Create a new amenity.
*   `GET /amenities/`: Get a list of all amenities.
*   `GET /amenities/{amenity_id}`: Get a specific amenity by ID.
*   `PUT /amenities/{amenity_id}`: Update an amenity.
*   `DELETE /amenities/{amenity_id}`: Delete an amenity.

### Payments

*   `POST /payments/`: Create a new payment.
*   `GET /payments/`: Get a list of all payments.
*   `GET /payments/{payment_id}`: Get a specific payment by ID.
*   `PUT /payments/{payment_id}`: Update a payment.
*   `DELETE /payments/{payment_id}`: Delete a payment.
