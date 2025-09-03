from flask import Flask, request, send_file, render_template_string, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

# Import our modules
from config import Config
from utils import (
    allowed_file, 
    get_file_list, 
    get_local_ip, 
    print_network_info,
    get_file_icon_class
)
from templates import get_html_template

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    """Main page - display file upload form and list of shared files"""
    files = get_file_list()
    ip = get_local_ip()
    
    # Add the get_file_icon_class function to template context
    template_context = {
        'files': files, 
        'ip': ip, 
        'port': Config.PORT,
        'get_file_icon_class': get_file_icon_class
    }
    
    return render_template_string(get_html_template(), **template_context)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads"""
    if 'file' not in request.files:
        flash('No files selected for upload')
        return redirect(url_for('home'))
    
    files = request.files.getlist('file')
    uploaded_count = 0
    failed_files = []
    
    for file in files:
        if file.filename == '':
            continue
            
        if not allowed_file(file.filename):
            failed_files.append(file.filename)
            continue
            
        try:
            # Secure the filename and save
            filename = secure_filename(file.filename)
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
            
            # Handle duplicate filenames by adding a number
            counter = 1
            original_filename = filename
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original_filename)
                filename = f"{name}_{counter}{ext}"
                filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                counter += 1
            
            file.save(filepath)
            uploaded_count += 1
            
        except Exception as e:
            failed_files.append(f"{file.filename} (Error: {str(e)})")
    
    # Generate appropriate flash message
    messages = []
    if uploaded_count > 0:
        messages.append(f'{uploaded_count} file(s) uploaded successfully!')
    
    if failed_files:
        if len(failed_files) <= 3:
            messages.append(f'Failed to upload: {", ".join(failed_files)}')
        else:
            messages.append(f'Failed to upload {len(failed_files)} files (invalid format or error)')
    
    if not messages:
        messages.append('No valid files were uploaded')
    
    for message in messages:
        flash(message)
    
    return redirect(url_for('home'))

@app.route('/files/<filename>')
def download_file(filename):
    """Handle file downloads"""
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        flash(f'File "{filename}" not found')
        return redirect(url_for('home'))
    
    try:
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        flash(f'Error downloading file: {str(e)}')
        return redirect(url_for('home'))

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Handle file deletions"""
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        flash(f'File "{filename}" not found')
        return redirect(url_for('home'))
    
    try:
        os.remove(filepath)
        flash(f'File "{filename}" deleted successfully!')
    except Exception as e:
        flash(f'Error deleting file "{filename}": {str(e)}')
    
    return redirect(url_for('home'))

@app.route('/clear-all', methods=['POST'])
def clear_all_files():
    """Delete all uploaded files (optional feature)"""
    try:
        files = os.listdir(Config.UPLOAD_FOLDER)
        deleted_count = 0
        
        for filename in files:
            filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
                deleted_count += 1
        
        if deleted_count > 0:
            flash(f'All files cleared! ({deleted_count} files deleted)')
        else:
            flash('No files to delete')
            
    except Exception as e:
        flash(f'Error clearing files: {str(e)}')
    
    return redirect(url_for('home'))

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    flash(f'File too large! Maximum size is {Config.MAX_CONTENT_LENGTH // (1024*1024)}MB')
    return redirect(url_for('home'))

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return redirect(url_for('home'))

def main():
    """Main function to run the application"""
    print_network_info()
    
    try:
        app.run(
            host=Config.HOST,
            port=Config.PORT,
            debug=Config.DEBUG,
            threaded=Config.THREADED
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == '__main__':
    main()
