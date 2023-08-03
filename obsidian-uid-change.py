import os

# フォルダ指定
dir_path = "i:\\Knowledge_BackUP\\20221230_Obsidian\\01_Zettelkasten"
file_list = os.listdir(dir_path)

# ファイル名取得
for file in file_list:
    file_name = os.path.splitext(os.path.basename(file))[0]
    with open(dir_path + "\\" + file_name + ".md", encoding="utf-8") as f:
        md_data = f.readlines()
    # UID取得
    uid = md_data[1].replace("uid: ", "").replace("\n", "")
    print(repr(uid), repr(file_name), file_name == uid)

    # ファイル名とUIDの検索
    if file_name == uid:
        continue
    print(file_name)
    uid_white = "uid: " + file_name + "\n"
    md_data[1] = uid_white
    md_data[2] = "create: 2023/01/01 12:00:00\n"
    # 書き込み
    with open(dir_path + "\\" + file_name + ".md", encoding="utf-8", mode="w") as w:
        w.writelines(md_data)
        print(md_data)
