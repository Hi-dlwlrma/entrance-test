import re
import chuanhoa
# from underthesea import word_tokenize

# remove html code
def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)
    
def text_preprocess(document):
    # xóa html code
    document = remove_html(document)
    # chuẩn hóa unicode
    document = chuanhoa.convert_unicode(document)
    print(document)
    # chuẩn hóa cách gõ dấu tiếng Việt
    document = chuanhoa.chuan_hoa_dau_cau_tieng_viet(document)
    # tách từ
    document = word_tokenize(document, format="text")
    # đưa về lower
    document = document.lower()
    # xóa các ký tự không cần thiết
    document = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]',' ',document)
    # xóa khoảng trắng thừa
    document = re.sub(r'\s+', ' ', document).strip()
    return document
    
document = 'TP HCM phạt người không đeo khẩu trang nơi công cộng Người dân ở thành phố không đeo khẩu trang nơi công cộng'
text_preprocess(document)
