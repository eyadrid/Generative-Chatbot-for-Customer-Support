# Generative Chat for Customer Support

## Description
This project aims to develop a chatbot dedicated to customer support. The chatbot's role is to efficiently and quickly respond to users' questions regarding the KYRA platform.

## Project Structure
The project is structured as follows:

```bash
Generative Chat/
├── backend              
│   ├── Dockerfile                 
│   ├── requirements.txt           
│   └── src
│       ├── controller.py         
│       ├── main.py                
│       ├── service.py             
│       └── utils
│           ├── extract_data.py    
│           └── segment_data.py   
├── frontend               
│   ├── Dockerfile                
│   ├── requirements.txt          
│   └── src
│       ├── main.py              
│       └── kyra.png             
└── docker-compose.yml           
```

## Project Components Overview

- **Backend:**
  - Manages core functionalities, including data extraction, service logic, and the chatbot API.
  - **Main directories:**
    - `src/`: Contains the main application logic.
    - `utils/`: Includes utility scripts for data handling and processing.
  - **Key files:**
    - `controller.py`: Manages routes and logic for the API.
    - `main.py`: The entry point for the backend service.
    - `service.py`: Contains the core logic of the chatbot service.
    - `Dockerfile`: Used for containerizing the backend service.
    - `requirements.txt`: Lists the dependencies required to run the backend.

- **Frontend:**
  - Manages the user interface, interacting with the backend to provide responses.
  - **Main directories:**
    - `src/`: Contains the frontend logic.
  - **Key files:**
    - `main.py`: The entry point for the frontend service.
    - `kyra.png`: A static image used in the frontend.
    - `Dockerfile`: Used for containerizing the frontend service.
    - `requirements.txt`: Lists the dependencies required to run the frontend.

- **docker-compose.yml:**
  - Orchestrates the setup of the backend and frontend services.


## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://gitlab.data-tricks.net/dt-solutions/trainee-codebase/2024/data-science-generative-chat-for-customer-support.git
    cd generative-chat
    ```

2. **Build and start the Docker containers:**

    Run the following command to build and start both backend and frontend services:

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images as specified in the `Dockerfile` for both the backend and frontend services and starts the containers.

3. **Access the application:**

    Once the containers are up and running, you can access the frontend interface at `http://localhost:8501`. The backend API should also be available at `http://localhost:8000`.

4. **Stop the application:**

    To stop the running services, press `Ctrl+C` in the terminal where `docker-compose` is running.

