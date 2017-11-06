import sys
sys.path.append("lib/qrcode")
import QrCode

def scan(file_path):
    result = QrCode.scan(file_path)
    return result[0].decode('utf-8') if result is not None else ''

if __name__ == '__main__':
    print(scan(sys.argv[1]))