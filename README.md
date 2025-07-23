# Hotel Management API

This is a FastAPI application for managing a hotel, built with AlloyDB.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:Ajay9330/alloydb_GCA_MCP_toolbox_demo.git
    cd alloydb_GCA_MCP_toolbox_demo
    ```

2.  **Set up the environment:**

    Create a `.env` file with your AlloyDB instance details:

    ```
    INSTANCE_CONNECTION_NAME=<your-instance-connection-name>
    DB_USER=<your-db-user>
    DB_PASS=<your-db-password>
    DB_NAME=<your-db-name>
    DB_HOST=127.0.0.1
    DB_PORT=5432
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

5.  **Run the application:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

The application will be accessible at `http://localhost:8000`.

## Key Endpoints

All endpoints are prefixed with `/api/v1`.

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

