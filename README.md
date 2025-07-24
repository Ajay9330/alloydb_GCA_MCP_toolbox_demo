# Hotel Management API

This is a FastAPI application for managing a hotel, built with AlloyDB.

## Setup

1.  **Clone the repository:**

    You can clone the repository using either HTTPS or SSH.

    **Using HTTPS:**
    ```bash
    git clone https://github.com/Ajay9330/alloydb_GCA_MCP_toolbox_demo.git
    cd alloydb_GCA_MCP_toolbox_demo
    ```

    **Using SSH:**
    ```bash
    git clone git@github.com:Ajay9330/alloydb_GCA_MCP_toolbox_demo.git
    cd alloydb_GCA_MCP_toolbox_demo
    ```

2.  **Set up the environment:**

    Create a `.env` file with your AlloyDB instance details. Note that `DB_HOST` and `DB_PORT` are not required, as the application uses the secure AlloyDB Connector.

    ```
    INSTANCE_CONNECTION_NAME=<your-instance-connection-name>
    DB_USER=<your-db-user>
    DB_PASS=<your-db-password>
    DB_NAME=<your-db-name>
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

---

### Steps for the GCA + AlloyDB as MCP Demo

This section guides you through setting up your Google Cloud environment and local machine for integrating Gemini Code Assist with AlloyDB.

#### GCP Setup:

1.  **Create a GCP project.**
2.  **Create an AlloyDB instance** with a primary instance. **Enable public IP** for the demo.
3.  **Open AlloyDB Studio** (or your preferred PostgreSQL client) and run the following queries to create a user and database:
    ```sql
    CREATE DATABASE hotel_db;
    CREATE USER hotel_db_user WITH PASSWORD 'password';
    GRANT alloydbsuperuser TO hotel_db_user;
    ```
    *(*Note:** For production environments, use stronger, randomly generated passwords and follow security best practices.)*

#### Local Setup:

1.  **Install gcloud CLI** on your local machine and log in.
    * Command to install gcloud CLI (see the official [Google Cloud SDK documentation](https://cloud.google.com/sdk/docs/install) for the latest instructions):
        ```bash
        curl https://sdk.cloud.google.com | bash
        ```
    * Command to log in:
        ```bash
        gcloud auth login
        ```
    * Command to verify login:
        ```bash
        gcloud config list
        ```

2.  **Install Gemini Code Assist extension** into VS Code from the [official website](https://codeassist.google/) and log in using your GCP project.

3.  **Enable GCA Insiders Channel (for early access to features):**
    * Open the Command Palette (Cmd + Shift + P on macOS, Ctrl + Shift + P on Windows/Linux) and then select `Open User Settings (JSON)`.
    * Add the following line to your user settings JSON to get early access to features like MCP:
        ```json
        "geminicodeassist.updateChannel": "Insiders",
        ```
    * After updating, you may need to restart VS Code.

4.  **Install the MCP Toolbox for Databases:**
    For more details, visit the [genai-toolbox GitHub repository](https://github.com/googleapis/genai-toolbox).
    ```bash
    # Visit the releases page for the latest version if this one is outdated.
    export VERSION=0.9.0
    curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
    chmod +x toolbox
    ```
    > **Note:** The `toolbox` executable will be downloaded to your current directory. For easier access, consider moving it to a directory included in your system's PATH (e.g., `/usr/local/bin`).

5.  **Configure MCP toolbox for AlloyDB:**
    * Open a folder in VS Code and create a new directory named `.gemini` in the root of your project (if it doesn't exist).
    * Inside the `.gemini` directory, create a file named `settings.json` with the following MCP configuration:
        ```json
        {
          "theme": "GitHub",
          "mcpServers": {
            "alloydb": {
              "command": "path/to/toolbox",
              "args": ["--prebuilt","alloydb-postgres","--stdio"],
              "env": {
                  "ALLOYDB_POSTGRES_PROJECT": "your_gcp_project_id",
                  "ALLOYDB_POSTGRES_REGION": "your_alloydb_region",
                  "ALLOYDB_POSTGRES_CLUSTER": "your_alloydb_cluster_name",
                  "ALLOYDB_POSTGRES_INSTANCE": "your_alloydb_instance_name",
                  "ALLOYDB_POSTGRES_DATABASE": "hotel_db",
                  "ALLOYDB_POSTGRES_USER": "hotel_db_user",
                  "ALLOYDB_POSTGRES_PASSWORD": "password"
                }
            }
          }
        }
        ```
        * **Important:**
            * Replace `path/to/toolbox` with the actual path to the `toolbox` executable (e.g., `/home/user/bin/toolbox` or `./toolbox` if it's in the current directory).
            * Replace `your_gcp_project_id`, `your_alloydb_region`, `your_alloydb_cluster_name`, and `your_alloydb_instance_name` with your specific AlloyDB instance details.
            * Ensure `ALLOYDB_POSTGRES_DATABASE`, `ALLOYDB_POSTGRES_USER`, and `ALLOYDB_POSTGRES_PASSWORD` match what you set up in AlloyDB Studio.

6.  **Verify MCP configuration:**
    * Open the GCA chat window in VS Code and run the following command:
        ```
        /mcp
        ```
    * This should list the configured `alloydb` server, indicating that GCA can communicate with your AlloyDB instance via the MCP toolbox.

### Prompt Examples: Using Inbuilt Tool of the MCP Server on Hotel Management API

Once your MCP configuration is verified, you can use the following prompts in the Gemini Code Assist chat window within VS Code to interact with your AlloyDB database:

* **Prompt to setup the schema in DB:**
    ```
    Hello!!
    I want to setup my db for this project, please create required tables in alloydb and please insert some sample data 4-5 record each
    ```

* **Prompt to Add Columns 'address' and 'age' in customer's table:**
    ```
    I want to add two columns for the customer address and age
    please add it and modify the code accordingly for older customer's data keep it null add some new customer data with address also
    ```

* **Prompt to add room_type:**
    ```
    In room, there can be multiple types of the rooms Family Rooms, Suite, Deluxe, Standard. Add a table for the roomtype and do code changes accordingly
    ```
