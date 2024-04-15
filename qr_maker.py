import qrcode
import os


def text_to_qr(input_text, file_path, T=800):
    # 检查输入文本的长度是否超过阈值T
    if len(input_text) > T:
        # 如果超过，将文本分割成多个部分
        for i in range(0, len(input_text), T):
            # 对每个部分，生成一个二维码
            qr = qrcode.make(input_text[i:i+T])
            # 使用file_path和当前的索引来命名
            qr.save(f"{file_path}_{i//T}.png")
    else:
        # 如果没有超过阈值，直接生成二维码
        qr = qrcode.make(input_text)
        qr.save(file_path)

def file_to_qr(file_path, qr_path, T=500):
    # 使用open函数和read方法来读取文件的内容
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
    # 调用text_to_qr函数，将读取的内容和文件路径作为参数
    text_to_qr(content, qr_path, T)

def files_to_qr():
    # 文件路径列表
    file_paths = [f for f in os.listdir() if os.path.splitext(f)[1] == '.txt']

    # 遍历文件路径列表
    for file_path in file_paths:
        # 对每个文件调用file_to_qr函数
        save_path = file_path.replace(".txt", "")
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        file_to_qr(file_path, f"{save_path}//"+save_path)

if __name__ == '__main__':
    files_to_qr()