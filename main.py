import httpx
import base64

GOOGLE_API_KEY = "AIzaSyDw8dPoNvRAKOceDz_5YDNbd5NyWfGh4OA"

if not GOOGLE_API_KEY:
    raise ValueError("Пожалуйста, укажите ваш Google API ключ.")

image_url = "https://yt3.ggpht.com/o9hTH-iMyo3WntI1iXIZWntC7An1rMliO_e8-aEiAAkMKGWruJ0KZN64SD2umWRjeQG5XCpO=s88-c-k-c0x00ffffff-no-rj"
response = httpx.get(image_url)
if response.status_code != 200:
    raise ValueError("Не удалось загрузить изображение.")

image_data = base64.b64encode(response.content).decode("utf-8")

url = "https://generativeai.googleapis.com/v1beta2/models/text-bison-001:generateText"
headers = {
    "Authorization": f"Bearer {GOOGLE_API_KEY}",
    "Content-Type": "application/json",
}
payload = {
    "prompt": "Generate a caption for this image.",
    "parameters": {
        "temperature": 0.7,
        "maxOutputTokens": 100,
    },
}

api_response = httpx.post(url, headers=headers, json=payload)

if api_response.status_code == 200:
    result = api_response.json()
    print("Ответ API:", result.get("candidates", [{}])[0].get("output", "Нет данных"))
else:
    print("Ошибка при вызове API:", api_response.status_code, api_response.text)
