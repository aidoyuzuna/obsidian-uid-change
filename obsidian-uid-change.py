import os

# フォルダ指定
file_path = 'i:\\Knowledge_BackUP\\20221230_Obsidian\\01_Zettelkasten'
file_list = os.listdir(file_path)

# ファイル名取得
for i in range(len(file_list)):
    file_name = os.path.splitext(os.path.basename(os.path.basename(file_list[i])))[0]
    with open(file_path + '\\' + file_name + '.md', encoding='utf-8') as f:
        md_data = f.readlines()
# UID取得
        uid = md_data[1].replace('uid: ', '')
# ファイル名とUIDの検索
        if not file_name == uid:
            print(uid)
            uid_white = 'uid: ' + file_name + '\n'
            md_data[1] = uid_white
# 書き込み
            with open(file_path + '\\'+ file_name + '.md', mode="w") as w:
                w.writelines(md_data)
                print(md_data)