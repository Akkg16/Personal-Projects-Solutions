from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?sa=X&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=APwXEdcx64UPi1Wylzl7fNXMdmLMmE1q6A:1680177203815&q=vienna+springstall&rflfq=1&num=10&ved=2ahUKEwiZmpLry4P-AhVniIsKHStOD1gQjGp6BAgbEAE&biw=1920&bih=937&dpr=1#rlfi=hd:;si:;mv:[[48.3124399,16.5446199],[48.1097292,16.2653061]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

result = doc.find_all("div")
print(result)