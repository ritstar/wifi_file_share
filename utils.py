import os
import socket
from config import Config

def allowed_file(filename):
    """Check if file extension is allowed"""
    return ('.' in filename and 
            filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS)

def get_file_size(filepath):
    """Convert file size to human readable format"""
    try:
        size = os.path.getsize(filepath)
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"
    except OSError:
        return "Unknown"

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Connect to a remote server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'

def get_file_list():
    """Get list of files in upload directory with metadata"""
    files = []
    try:
        for filename in os.listdir(Config.UPLOAD_FOLDER):
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                files.append({
                    'name': filename,
                    'size': get_file_size(filepath),
                    'extension': filename.split('.')[-1].lower() if '.' in filename else ''
                })
        
        # Sort files alphabetically
        files.sort(key=lambda x: x['name'].lower())
        return files
    except OSError:
        return []

def get_file_icon_class(extension):
    """Get Font Awesome icon class based on file extension"""
    icon_map = {
        # Images
        'jpg': 'fa-image', 'jpeg': 'fa-image', 'png': 'fa-image', 
        'gif': 'fa-image', 'bmp': 'fa-image', 'svg': 'fa-image',
        
        # Videos
        'mp4': 'fa-video', 'avi': 'fa-video', 'mov': 'fa-video', 
        'mkv': 'fa-video', 'wmv': 'fa-video',
        
        # Audio
        'mp3': 'fa-music', 'wav': 'fa-music', 'flac': 'fa-music',
        'aac': 'fa-music', 'ogg': 'fa-music',
        
        # Documents
        'pdf': 'fa-file-pdf',
        'doc': 'fa-file-word', 'docx': 'fa-file-word',
        'xls': 'fa-file-excel', 'xlsx': 'fa-file-excel',
        'ppt': 'fa-file-powerpoint', 'pptx': 'fa-file-powerpoint',
        'txt': 'fa-file-alt', 'rtf': 'fa-file-alt',
        
        # Archives
        'zip': 'fa-file-archive', 'rar': 'fa-file-archive', 
        '7z': 'fa-file-archive', 'tar': 'fa-file-archive',
        
        # Code
        'py': 'fa-file-code', 'js': 'fa-file-code', 'html': 'fa-file-code',
        'css': 'fa-file-code', 'json': 'fa-file-code', 'xml': 'fa-file-code'
    }
    
    return icon_map.get(extension.lower(), 'fa-file')

def print_network_info():
    """Print server startup information"""
    ip = get_local_ip()
    print(f"\n{'='*60}")
    print(f"🌐 WiFi File Sharing Server Started Successfully!")
    print(f"{'='*60}")
    print(f"📱 Access URL: http://{ip}:{Config.PORT}")
    print(f"🌍 Local URL: http://127.0.0.1:{Config.PORT}")
    print(f"📁 Upload Directory: ./{Config.UPLOAD_FOLDER}/")
    print(f"📊 Max File Size: {Config.MAX_CONTENT_LENGTH // (1024*1024)}MB")
    print(f"🔒 Allowed Extensions: {', '.join(sorted(Config.ALLOWED_EXTENSIONS))}")
    print(f"🔄 Auto-refresh: {Config.REFRESH_INTERVAL/1000}s")
    print(f"{'='*60}")
    print(f"💡 Share the access URL with devices on your network")
    print(f"⚡ Press Ctrl+C to stop the server")
    print(f"{'='*60}\n")
