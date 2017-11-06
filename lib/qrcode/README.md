# dada-qrcode
This is a QRCode generate and scan program

## dependency
brew install zbar
pip install zbarlight
pip install qrcode
pip install pillow

## usage
import DadaQrCode

```generate image```

DadaQrCode.generate('{"category":"cloths", "brand":"babary", "size":"XXXL"}', "input.jpg", "output.jpg")

result = DadaQrCode.scan("output.jpg")