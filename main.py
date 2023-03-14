from jobkorea import scrap_jobkorea

keyword=input("검색할 키워드를 입력하세요: ")
jobkorea_infos=scrap_jobkorea(keyword)
file=open(f"{keyword}.csv","w",encoding="utf-8-sig")
file.write("company,position,location,experience,education,link\n")
for jobkorea_info in jobkorea_infos:
  file.write(f"{jobkorea_info['company']},{jobkorea_info['position']},{jobkorea_info['location']},{jobkorea_info['experience']},{jobkorea_info['education']},{jobkorea_info['link']}\n")
file.close()