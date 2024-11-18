# E-Commerce API

This API includes features like user authentication, order creation, order retrieval, and order cancellation.

## Features

- **User Authentication**
- **Create Order**
- **Get Orders**
- **Cancel Order**

## Setup Instructions

To get started with the E-Commerce API, follow the steps below:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/fernandobbellelis/e-commerce_API.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd e-commerce_api
   ```

3. **Initialize a Virtual Environment**

   ```bash
   python -m venv e_commerce_venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     e_commerce_venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source e_commerce_venv/bin/activate
     ```

5. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

You are now ready to start working with the E-Commerce API!


1. **Run API**

   ```bash
   python app.py
   ```

## Using Postman Collection

To facilitate testing, we've provided a Postman collection containing all possible requests for this API. Here’s how you can import and use it:

2. **Download the Postman Collection**

   Ensure you have the Postman application installed on your system. If not, you can download it [here](https://www.postman.com/downloads/). Download the `AI Engineer API.postman_collection.json` file from the repository.

3. **Import the Collection into Postman**

   - Open Postman.
   - Click on the `Import` button located at the top-left corner of the Postman UI.
   - In the Import modal, select the 'Choose Files' button.
   - Navigate to the directory where `AI Engineer API.postman_collection.json` is located and select it.
   - Click `Open` to import the collection.

4. **Using the Requests**

   - Once imported, navigate to the 'Collections' section in Postman. You should see the "AI Engineer API" collection listed there.
   - Expand the collection to view all available endpoints: `register`, `login`, `logout`, `create_order`, `cancel_order`, and `get_orders`.
   - Click on any endpoint to view its configuration.
   - Before executing requests, ensure that the API is running by checking the terminal output from the `python app.py`.
   - Execute a request by clicking the `Send` button.
   - Review the response status and body in the Postman interface.

## Notes

- Each request in the Postman collection is pre-configured with example data. Feel free to modify the request details (e.g., change usernames, passwords, or order details) to suit your testing needs.
- Ensure that the API server is running locally and listening on `http://127.0.0.1:5000`.

With this setup, you should be able to easily test and interact with the E-Commerce API using Postman. If you encounter any issues, please check the API logs for errors or review the Postman response for more details.
