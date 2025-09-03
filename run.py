#!/usr/bin/env python3
"""
Simple runner script for WiFi File Share
"""
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import main

if __name__ == '__main__':
    main()
