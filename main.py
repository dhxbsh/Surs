import os
from pyrogram import Client, filters

# قراءة البيانات من متغيرات البيئة في Koyeb
api_id = int(os.environ.get("API_ID", 25956262))
api_hash = os.environ.get("API_HASH", "8e6268505a15d74f195672b802e34aa9")
session_string = os.environ.get("SESSION_STRING", "")

app = Client("my_userbot", api_id=api_id, api_hash=api_hash, session_string=session_string)

STORAGE_GROUP_ID = None

COMMANDS_TEXT = """✦ ─── ✦『 قائـمـة الاوامـر 』✦ ─── ✦

. م 1 ➾ اوامر الحساب
. م 2 ➾ اوامر الخاص
. م 3 ➾ اوامر الاسبام
. م 4 ➾ اوامر الاذاعه
. م 5 ➾ اوامر التحميل
. م 6 ➾ امر الحذف
. م 7 ➾ اوامر الزخرفه
. م 8 ➾ اوامر التسطير
. م 9 ➾ اوامر الساعه
. م 10 ➾ اوامر التفليش
. م 11 ➾ اوامر الترجمه
. م 12 ➾ اوامر الوهمي
. م 13 ➾ اوامر الانتحال
. م 14 ➾ اوامر النشر
. م 15 ➾ اوامر الذكاء الاصطناعي"""

@app.on_message(filters.me & filters.regex(r"^(\.|)الاوامر$"))
async def show_help_menu(client, message):
    await message.edit_text(COMMANDS_TEXT)

@app.on_message(filters.me & filters.regex(r"^(\.|)تخزين$"))
async def create_storage_group(client, message):
    global STORAGE_GROUP_ID
    msg = await message.edit_text("جاري إنشاء كروب التخزين...")
    group = await client.create_group("تخزين السورس 📁", ["me"])
    STORAGE_GROUP_ID = group.id
    await msg.edit_text(f"تم إنشاء كروب التخزين بنجاح!\nآيدي الكروب: `{STORAGE_GROUP_ID}`")

@app.on_message(filters.private & ~filters.me & ~filters.bot)
async def forward_to_storage(client, message):
    global STORAGE_GROUP_ID
    if STORAGE_GROUP_ID is None:
        group = await client.create_group("تخزين السورس 📁", ["me"])
        STORAGE_GROUP_ID = group.id
    try:
        await message.forward(STORAGE_GROUP_ID)
    except Exception as e:
        print(f"خطأ: {e}")

app.run()
