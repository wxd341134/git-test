import ddddocr                       # 导入 ddddocr

ocr = ddddocr.DdddOcr()              # 实例化
with open('a3.png', 'rb') as f:     # 打开图片
    img_bytes = f.read()             # 读取图片
res = ocr.classification(img_bytes)  # 识别
print(res)


