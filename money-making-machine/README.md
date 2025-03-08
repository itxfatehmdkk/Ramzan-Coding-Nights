# Money Making Machine

This project is a Streamlit application that generates money, provides side hustle ideas, and shares motivational money quotes.

## Installation

To install dependencies for the money-making-machine project, you may need to increase the network timeout setting:

### Using Poetry
```bash
# Set the UV_HTTP_TIMEOUT environment variable to 60 seconds
$env:UV_HTTP_TIMEOUT=60

# Install dependencies using Poetry
cd money-making-machine
poetry install
```

### Using UV
```bash
# Set the UV_HTTP_TIMEOUT environment variable to 60 seconds
$env:UV_HTTP_TIMEOUT=60

# Install streamlit using UV
cd money-making-machine
uv add streamlit
```

Note: For Unix/Linux systems, use `export UV_HTTP_TIMEOUT=60` instead of `$env:UV_HTTP_TIMEOUT=60`.

## Running the Streamlit App
To run the Streamlit application, use the following command:

```bash
cd money-making-machine
streamlit run main.py
```
