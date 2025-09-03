import os

# Application Configuration
class Config:
    # Flask settings
    SECRET_KEY = 'your-secret-key-change-this-in-production'
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
    
    # File settings
    UPLOAD_FOLDER = 'shared_files'
    ALLOWED_EXTENSIONS = {
        'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 
        'mp4', 'mp3', 'doc', 'docx', 'zip', 'rar', 
        '7z', 'csv', 'xlsx', 'pptx', 'wav', 'flac', 'avi', 'mov'
    }
    
    # Server settings
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = False
    THREADED = True
    
    # Auto-refresh interval (in milliseconds)
    REFRESH_INTERVAL = 5000

# Ensure upload directory exists
if not os.path.exists(Config.UPLOAD_FOLDER):
    os.makedirs(Config.UPLOAD_FOLDER)
