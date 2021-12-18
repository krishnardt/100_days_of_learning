import base64


#converts raw byte content to base64 string
base64_bytes = base64.b64encode(bytes(str(response.content),'utf-8')).decode()

#converts base64 string to bytes
temp = base64.b64decode(base64_bytes)
#there may be an issue of double forward slashes.
#in order to remove them,
temp = temp.decode('unicode_escape').encode("raw_unicode_escape")
