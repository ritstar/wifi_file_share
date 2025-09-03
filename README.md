# 📁 WiFi File Share

A simple and elegant web-based file sharing application that allows you to share files across devices on the same WiFi network. Upload files from any device and download them on any other device connected to the same network.

## ✨ Features

- 🌐 **Cross-Platform File Sharing**: Share files between any devices (phones, tablets, computers) on the same WiFi network
- 📱 **Responsive Web Interface**: Clean, modern UI that works on all devices
- 📤 **Multiple File Upload**: Upload multiple files at once with drag-and-drop support
- 📥 **Easy Downloads**: One-click download for any shared file
- 🗂️ **File Management**: View file details, delete files, or clear all files
- 🔄 **Auto Refresh**: Page automatically refreshes to show new files
- 🎨 **File Type Icons**: Visual file type indicators for easy recognition
- ⚡ **Fast & Lightweight**: Built with Flask for optimal performance
- 🔒 **Secure Filenames**: Automatic filename sanitization and duplicate handling

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ritstar/wifi_file_share.git
   cd wifi_file_share
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python run.py
   ```

4. **Access the app**: Open your browser and go to the URL displayed in the terminal (usually `http://YOUR_IP:8000`)

### Alternative Installation with Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## 📋 Usage

1. **Start the server** by running `python run.py`
2. **Note the displayed URL** (e.g., `http://192.168.1.100:8000`)
3. **Share the URL** with other devices on your WiFi network
4. **Upload files** by clicking "Choose Files" or dragging and dropping
5. **Download files** by clicking on any file in the list
6. **Manage files** using the delete buttons or "Clear All" option

## 🔧 Configuration

The app can be configured by modifying `config.py`:

### Server Settings
- **Host**: `0.0.0.0` (accessible from network)
- **Port**: `8000` (default port)
- **Debug Mode**: Disabled by default

### File Settings
- **Upload Directory**: `shared_files/`
- **Max File Size**: 100MB per file
- **Supported File Types**:
  - **Documents**: txt, pdf, doc, docx, csv, xlsx, pptx
  - **Images**: png, jpg, jpeg, gif
  - **Videos**: mp4, avi, mov
  - **Audio**: mp3, wav, flac
  - **Archives**: zip, rar, 7z

### Security Features
- Secure filename handling to prevent directory traversal
- File type validation
- Automatic duplicate filename handling

## 📁 Project Structure

```
wifi_file_share/
├── app.py              # Main Flask application
├── run.py              # Application runner
├── config.py           # Configuration settings
├── utils.py            # Utility functions
├── templates.py        # HTML templates
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── README.md          # This file
└── shared_files/      # Upload directory (created automatically)
```

## 🛠️ Development

### Running in Debug Mode

To enable debug mode for development:

1. Edit `config.py` and set `DEBUG = True`
2. Run the application: `python run.py`

### Adding New File Types

To support additional file types:

1. Open `config.py`
2. Add new extensions to the `ALLOWED_EXTENSIONS` set
3. Optionally, add icon mappings in `utils.py` → `get_file_icon_class()`

## 🌐 Network Access

The application binds to `0.0.0.0:8000`, making it accessible to:
- **Local machine**: `http://localhost:8000` or `http://127.0.0.1:8000`
- **Network devices**: `http://YOUR_LOCAL_IP:8000`

The server automatically displays your local IP address when starting.

## 🔒 Security Considerations

- **Network Scope**: Only accessible within your local WiFi network
- **File Validation**: Only allowed file types can be uploaded
- **Secure Storage**: Files are stored with sanitized names
- **No Authentication**: Consider adding authentication for sensitive use cases

## 🐛 Troubleshooting

### Common Issues

1. **Cannot access from other devices**:
   - Ensure all devices are on the same WiFi network
   - Check if your firewall is blocking port 8000
   - Verify the IP address displayed when starting the server

2. **File upload fails**:
   - Check if file size is under 100MB limit
   - Verify file type is in the allowed extensions list
   - Ensure sufficient disk space is available

3. **Server won't start**:
   - Check if port 8000 is already in use
   - Verify Python and pip are installed correctly
   - Install missing dependencies: `pip install -r requirements.txt`

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for easy file sharing across devices**
