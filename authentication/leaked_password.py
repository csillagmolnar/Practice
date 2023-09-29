import hashlib
import sys

# Handle requests is installed
try:
    import requests
except ImportError:
    print('Install requests package')
    exit()

