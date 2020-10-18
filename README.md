# vk_crutch

* Где $OWNER_ID - или пользователь или группа(-)
* И где $POST_NAME - что мы хтим передать(плейлист, фото, и т.д.)
* А так же $POST_ID_DELL - после того как пост опубликован, нам возвращается ID (используя его можно удалить пост)

```
# Парсер плейлистов:
python3.6 $PLAYLIST_PARSER $TELEPHONE $PASSWORD $OWNER_ID

# Публикация поста:
python3.6 $POST_POST $TELEPHONE $PASSWORD $OWNER_ID $POST_NAME

# Удаление поста:
python3.6 $PLAYLIST_DEL $TELEPHONE $PASSWORD $OWNER_ID $POST_ID_DELL
