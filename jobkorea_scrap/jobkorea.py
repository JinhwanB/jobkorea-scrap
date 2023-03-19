from requests import get
from bs4 import BeautifulSoup


def page_count(keyword):
  base_url = f"https://www.jobkorea.co.kr/Search/?stext={keyword}"
  response = get(f"{base_url}")
  soup = BeautifulSoup(response.text, "html.parser")
  div = soup.find("div", class_="tplPagination newVer wide")
  pages = div.find_all("li")
  count = len(pages)
  if count >= 5:
    return 5
  else:
    return count


def scrap_jobkorea(keyword):
  pages = page_count(keyword)
  if pages == 5:
    print("Found", pages, "or more than pages")
  else:
    print("Found", pages, "pages")
  results = []
  for page in range(1, pages + 1):
    base_url = "https://www.jobkorea.co.kr"
    final_url = f"{base_url}/Search/?stext={keyword}&Page_No={page}"
    print("Requesting", final_url)
    response = get(f"{final_url}")
    if response.status_code != 200:
      print("Cant request website")
    else:
      soup = BeautifulSoup(response.text, "html.parser")
      div = soup.find("div", class_="lists")
      lis = div.find_all("li", class_="list-post")
      for li in lis:
        anchor1 = li.find("a", class_="name dev_view")
        company = anchor1.text.replace(",", " ")
        link = anchor1["href"]
        anchor2 = li.find("a", class_="title dev_view")
        position = anchor2.text.replace("\n", "").replace("\r", "").replace(
          "                            ", "").replace("    ",
                                                      "").replace(",", " ")
        span1 = li.find("span", class_="loc long")
        location = span1.text.replace(",", " ")
        span2 = li.find("span", class_="exp")
        experience = span2.text.replace(",", " ")
        span3 = li.find("span", class_="edu")
        if span3 == None:
          education = "무관"
        else:
          education = span3.text.replace(",", " ")
        job_info = {
          "company": f"{company}",
          "position": f"{position}",
          "location": f"{location}",
          "experience": f"{experience}",
          "education": f"{education}",
          "link": f"https://www.jobkorea.co.kr{link}"
        }
        results.append(job_info)
  return results
