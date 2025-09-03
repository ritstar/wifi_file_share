from config import Config
from utils import get_file_icon_class

def get_html_template():
    """Return the complete HTML template"""
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WiFi File Share</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }

        .header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 30px;
            text-align: center;
            position: relative;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><radialGradient id="a"><stop offset="20%" stop-color="%23fff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23fff" stop-opacity="0"/></radialGradient></defs><rect width="100" height="20" fill="url(%23a)"/></svg>') repeat-x;
            pointer-events: none;
        }

        .header h1 {
            font-size: 2.8em;
            margin-bottom: 10px;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }

        .header p {
            opacity: 0.9;
            font-size: 1.2em;
            position: relative;
            z-index: 1;
        }

        .content {
            padding: 40px;
        }

        .upload-section {
            background: linear-gradient(145deg, #f8fafc, #e2e8f0);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            border: 3px dashed #cbd5e0;
            text-align: center;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .upload-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(102, 126, 234, 0.05) 0%, transparent 70%);
            transition: all 0.4s ease;
            transform: scale(0);
        }

        .upload-section:hover::before {
            transform: scale(1);
        }

        .upload-section:hover {
            border-color: #667eea;
            background: linear-gradient(145deg, #f1f5f9, #e6fffa);
            transform: translateY(-2px);
        }

        .upload-icon {
            font-size: 4em;
            color: #667eea;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
        }

        .upload-section:hover .upload-icon {
            transform: scale(1.1);
            color: #5a67d8;
        }

        .file-input-wrapper {
            position: relative;
            display: inline-block;
            margin: 20px 0;
            z-index: 1;
        }

        .file-input {
            opacity: 0;
            position: absolute;
            z-index: -1;
        }

        .file-input-button, .upload-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 16px 32px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            font-size: 1.1em;
            transition: all 0.3s ease;
            display: inline-block;
            border: none;
            margin: 10px;
            text-decoration: none;
        }

        .file-input-button:hover, .upload-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
        }

        .upload-btn {
            background: linear-gradient(135deg, #48bb78, #38a169);
        }

        .upload-btn:hover {
            box-shadow: 0 15px 30px rgba(72, 187, 120, 0.4);
        }

        .upload-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .message {
            padding: 18px 24px;
            border-radius: 12px;
            margin: 20px 0;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 12px;
            animation: slideIn 0.3s ease;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .message.success {
            background: linear-gradient(135deg, #f0fff4, #c6f6d5);
            color: #22543d;
            border: 1px solid #9ae6b4;
        }

        .message.error {
            background: linear-gradient(135deg, #fed7d7, #feb2b2);
            color: #742a2a;
            border: 1px solid #fc8181;
        }

        .files-section h3 {
            color: #2d3748;
            margin-bottom: 25px;
            font-size: 2em;
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 700;
        }

        .files-grid {
            display: grid;
            gap: 18px;
        }

        .file-item {
            background: linear-gradient(145deg, #ffffff, #f7fafc);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .file-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .file-item:hover::before {
            opacity: 1;
        }

        .file-item:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
            border-color: #667eea;
        }

        .file-info {
            display: flex;
            align-items: center;
            gap: 18px;
            flex: 1;
            min-width: 0;
            position: relative;
            z-index: 1;
        }

        .file-icon {
            font-size: 2.5em;
            color: #667eea;
            flex-shrink: 0;
            transition: all 0.3s ease;
        }

        .file-item:hover .file-icon {
            transform: scale(1.1);
            color: #5a67d8;
        }

        .file-details {
            overflow: hidden;
        }

        .file-details h4 {
            color: #2d3748;
            margin-bottom: 6px;
            font-weight: 600;
            font-size: 1.1em;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 250px;
        }

        .file-size {
            color: #718096;
            font-size: 0.95em;
            white-space: nowrap;
        }

        .file-actions {
            display: flex;
            gap: 12px;
            flex-shrink: 0;
            position: relative;
            z-index: 1;
        }

        .download-btn, .delete-btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 30px;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
            text-decoration: none;
            white-space: nowrap;
            font-size: 0.9em;
        }

        .download-btn:hover, .delete-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .delete-btn {
            background: linear-gradient(135deg, #e53e3e, #c53030);
        }

        .delete-btn:hover {
            box-shadow: 0 10px 20px rgba(229, 62, 62, 0.3);
        }

        .network-info {
            background: linear-gradient(135deg, #e6fffa, #b2f5ea);
            border: 2px solid #81e6d9;
            border-radius: 16px;
            padding: 25px;
            margin-top: 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .network-info::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(129, 230, 217, 0.1) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.1); opacity: 0.8; }
        }

        .network-info h4 {
            color: #234e52;
            margin-bottom: 15px;
            font-size: 1.3em;
            position: relative;
            z-index: 1;
        }

        .ip-address {
            font-family: 'SF Mono', 'Monaco', 'Inconsolata', monospace;
            font-size: 1.4em;
            color: #2c7a7b;
            font-weight: bold;
            background: rgba(255, 255, 255, 0.7);
            padding: 12px 20px;
            border-radius: 8px;
            display: inline-block;
            margin: 8px 0;
            position: relative;
            z-index: 1;
        }

        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #718096;
        }

        .empty-state i {
            font-size: 5em;
            margin-bottom: 25px;
            opacity: 0.4;
            color: #a0aec0;
        }

        .empty-state h3 {
            font-size: 1.8em;
            margin-bottom: 10px;
            color: #4a5568;
        }

        /* Enhanced Mobile Responsive Design */
        @media (max-width: 768px) {
            .container {
                margin: 10px;
                border-radius: 15px;
            }
            
            .content {
                padding: 25px;
            }
            
            .header {
                padding: 25px 20px;
            }
            
            .header h1 {
                font-size: 2.2em;
            }

            .file-details h4 {
                max-width: 180px;
            }

            .upload-section {
                padding: 30px 20px;
            }
        }

        @media (max-width: 480px) {
            body {
                padding: 8px;
            }

            .file-item {
                flex-direction: column;
                align-items: flex-start;
                gap: 20px;
                padding: 20px;
            }

            .file-info {
                width: 100%;
                gap: 15px;
            }

            .file-details h4 {
                max-width: 200px;
            }

            .file-actions {
                width: 100%;
                justify-content: space-between;
                gap: 10px;
            }

            .download-btn, .delete-btn {
                flex: 1;
                justify-content: center;
                padding: 14px 12px;
                font-size: 0.9em;
            }

            .upload-section {
                padding: 25px 15px;
            }

            .file-input-button, .upload-btn {
                padding: 14px 28px;
                font-size: 1em;
            }

            .header h1 {
                font-size: 1.8em;
            }

            .ip-address {
                font-size: 1.1em;
                padding: 10px 16px;
            }
        }

        /* Loading Animation */
        .progress-container {
            margin: 20px 0;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .progress-bar {
            width: 100%;
            height: 10px;
            background: #e2e8f0;
            border-radius: 8px;
            overflow: hidden;
            position: relative;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #48bb78, #38a169);
            transition: width 0.4s ease;
            position: relative;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            background-image: linear-gradient(
                -45deg,
                rgba(255, 255, 255, 0.2) 25%,
                transparent 25%,
                transparent 50%,
                rgba(255, 255, 255, 0.2) 50%,
                rgba(255, 255, 255, 0.2) 75%,
                transparent 75%,
                transparent
            );
            background-size: 50px 50px;
            animation: move 2s linear infinite;
        }

        @keyframes move {
            0% { background-position: 0 0; }
            100% { background-position: 50px 50px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-wifi"></i> WiFi File Share</h1>
            <p>Share files instantly across your network</p>
        </div>
        
        <div class="content">
            <div class="upload-section">
                <i class="fas fa-cloud-upload-alt upload-icon"></i>
                <h3 style="margin-bottom: 12px; color: #2d3748; position: relative; z-index: 1;">Upload Files</h3>
                <p style="color: #718096; margin-bottom: 25px; position: relative; z-index: 1;">Drag and drop or click to select multiple files</p>
                
                <form id="uploadForm" action="/upload" method="post" enctype="multipart/form-data">
                    <div class="file-input-wrapper">
                        <input type="file" id="fileInput" name="file" class="file-input" multiple>
                        <label for="fileInput" class="file-input-button">
                            <i class="fas fa-folder-open"></i> Choose Files
                        </label>
                    </div>
                    <br>
                    <button type="submit" class="upload-btn" id="uploadBtn" disabled>
                        <i class="fas fa-upload"></i> Upload Files
                    </button>
                </form>
                
                <div id="progressContainer" class="progress-container" style="display: none;">
                    <div class="progress-bar">
                        <div class="progress-fill" id="progressFill"></div>
                    </div>
                    <p id="progressText" style="margin-top: 10px; color: #4a5568; font-weight: 500;">Uploading...</p>
                </div>
            </div>

            <!-- Flash messages -->
            {% with messages = get_flashed_messages() %}
                {% if messages %}
                    {% for message in messages %}
                    <div class="message {{ 'success' if 'successfully' in message else 'error' }}">
                        <i class="fas {{ 'fa-check-circle' if 'successfully' in message else 'fa-exclamation-triangle' }}"></i>
                        {{ message }}
                    </div>
                    {% endfor %}
                {% endif %}
            {% endwith %}

            <div class="files-section">
                <h3><i class="fas fa-folder"></i> Shared Files ({{ files|length }})</h3>
                
                {% if files %}
                <div class="files-grid">
                    {% for f in files %}
                    <div class="file-item">
                        <div class="file-info">
                            <div class="file-icon">
                                <i class="fas {{ get_file_icon_class(f.extension) }}"></i>
                            </div>
                            <div class="file-details">
                                <h4 title="{{ f.name }}">{{ f.name }}</h4>
                                <div class="file-size">{{ f.size }}</div>
                            </div>
                        </div>
                        <div class="file-actions">
                            <a href="/files/{{ f.name }}" class="download-btn" download>
                                <i class="fas fa-download"></i> Download
                            </a>
                            <form method="POST" action="/delete/{{ f.name }}" onsubmit="return confirm('Are you sure you want to delete {{ f.name }}?');" style="display: inline;">
                                <button type="submit" class="delete-btn">
                                    <i class="fas fa-trash"></i> Delete
                                </button>
                            </form>
                        </div>
                    </div>
                    {% endfor %}
                </div>
                {% else %}
                <div class="empty-state">
                    <i class="fas fa-folder-open"></i>
                    <h3>No files shared yet</h3>
                    <p>Upload some files to get started!</p>
                </div>
                {% endif %}
            </div>

            <div class="network-info">
                <h4><i class="fas fa-network-wired"></i> Network Information</h4>
                <div class="ip-address">{{ ip }}:{{ port }}</div>
                <p style="margin-top: 15px; color: #2c7a7b; position: relative; z-index: 1;">
                    Share this address with devices on your network to access files
                </p>
            </div>
        </div>
    </div>

    <script>
        const fileInput = document.getElementById('fileInput');
        const uploadBtn = document.getElementById('uploadBtn');
        const progressContainer = document.getElementById('progressContainer');
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');

        fileInput.addEventListener('change', function() {
            uploadBtn.disabled = this.files.length === 0;
            if (this.files.length > 0) {
                uploadBtn.innerHTML = `<i class="fas fa-upload"></i> Upload ${this.files.length} file(s)`;
            } else {
                uploadBtn.innerHTML = `<i class="fas fa-upload"></i> Upload Files`;
            }
        });

        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            if (fileInput.files.length === 0) {
                e.preventDefault();
                alert('Please select at least one file to upload.');
                return;
            }
            
            uploadBtn.disabled = true;
            uploadBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Uploading...';
            progressContainer.style.display = 'block';
            
            let progress = 0;
            const interval = setInterval(() => {
                progress += Math.random() * 15;
                if (progress >= 90) {
                    clearInterval(interval);
                    progress = 90;
                }
                progressFill.style.width = progress + '%';
                progressText.textContent = `Uploading... ${Math.round(progress)}%`;
            }, 200);
        });

        // Auto-refresh files list
        setInterval(() => {
            if (!uploadBtn.disabled) {
                location.reload();
            }
        }, ''' + str(Config.REFRESH_INTERVAL) + ''');

        // Add drag and drop functionality
        const uploadSection = document.querySelector('.upload-section');
        
        uploadSection.addEventListener('dragover', function(e) {
            e.preventDefault();
            this.style.borderColor = '#667eea';
            this.style.backgroundColor = '#f1f5f9';
        });

        uploadSection.addEventListener('dragleave', function(e) {
            e.preventDefault();
            this.style.borderColor = '#cbd5e0';
            this.style.backgroundColor = '';
        });

        uploadSection.addEventListener('drop', function(e) {
            e.preventDefault();
            this.style.borderColor = '#cbd5e0';
            this.style.backgroundColor = '';
            
            const files = e.dataTransfer.files;
            fileInput.files = files;
            
            const event = new Event('change');
            fileInput.dispatchEvent(event);
        });
    </script>
</body>
</html>
    '''
