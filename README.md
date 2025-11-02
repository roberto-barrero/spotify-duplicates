# spotify-duplicates
A service that detects duplicates in Spotify playlists

## Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/roberto-barrero/spotify-duplicates.git
cd spotify-duplicates
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

## Running the Application

### Development Mode
```bash
python run.py
```

The application will be available at `http://localhost:5000`

### Available Endpoints

- `GET /` - API information
- `GET /health` - Health check endpoint

## Project Structure

```
spotify-duplicates/
├── app/
│   ├── __init__.py      # Flask application factory
│   ├── config.py        # Configuration settings
│   └── routes.py        # Route definitions
├── run.py               # Application entry point
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## License
See LICENSE file for details.
