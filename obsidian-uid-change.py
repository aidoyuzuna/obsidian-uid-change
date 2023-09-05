import os
import datetime

# フォルダ指定
root_dir = f"{os.environ['GoogleDrive']}\\Obsidian\\01_Inbox"

# ファイル名取得
for file_base in os.listdir(root_dir):
    file_name, ext = os.path.splitext(file_base)
    if ext != ".md":
        continue
    full_path = os.path.join(root_dir, file_base)
    with open(full_path, encoding="utf-8") as f:
        md_data = f.readlines()
    # UID取得
    uid = md_data[1].replace("uid: ", "").replace("\n", "")
    print(repr(uid), repr(file_name), file_name == uid)

    # 日付取得
    date_data = md_data[2].replace("create: ", "").replace("\n", "")
    date_format = "%y%m%d%H%M%S"
    date = datetime.datetime.strptime(file_name, date_format)

    # ファイル名とUIDの検索
    if file_name == uid:
        continue
    print(file_name)
    uid_white = f"uid: {file_name}\n"
    md_data[1] = uid_white
    md_data[2] = f"create: {date:%Y/%m/%d %H:%M:%S}\n"
    # 書き込み
    with open(full_path, encoding="utf-8", mode="w") as w:
        w.writelines(md_data)
        print(md_data)
