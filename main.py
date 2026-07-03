# 1. 기본 프롬프트 데이터 세팅
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 본문과 제목 3개를 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성 키워드",
        "content": "의류 쇼핑몰에 사용할 배경이 깔끔하고 트렌디한 제품 썸네일 이미지를 생성하기 위한 미드저니 프롬프트입니다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "노션 대학 생활 자동화 템플릿 안내",
        "content": "대학생들을 위한 학점 관리 및 일정 자동화 노션 템플릿의 복제 안내 문구를 작성해주는 프롬프트입니다.",
        "category": "자동화",
        "favorite": False
    }
]

# 2. 메뉴판 출력 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("==========================")

# 3. 2번 메뉴: 목록 보기
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("[안내] 등록된 프롬프트가 없습니다.")
        return
    for idx, p in enumerate(prompts, start=1):
        fav_star = " ⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")

# 4. 1번 메뉴: 추가
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    while True:
        title = input("제목: ").strip()
        if title: break
        print("[에러] 제목은 비어있을 수 없습니다.")
    while True:
        content = input("내용: ").strip()
        if content: break
        print("[에러] 내용은 비어있을 수 없습니다.")
        
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}) {cat}")
        
    while True:
        cat_choice = input("선택 (번호 입력): ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        print("[에러] 올바른 번호를 선택해 주세요.")
        
    prompts.append({"title": title, "content": content, "category": category, "favorite": False})
    print(f"\n[성공] '{title}' 프롬프트가 추가되었습니다!")

# 5. 3번 메뉴: 카테고리별 조회
def view_by_category():
    print("\n=== 카테고리별 조회 ===")
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    for i, cat in enumerate(categories, start=1):
        print(f"{i}) {cat}")
    while True:
        cat_choice = input("선택: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            selected_cat = categories[int(cat_choice) - 1]
            break
        print("[에러] 올바른 번호를 선택해 주세요.")
        
    print(f"\n[{selected_cat}] 카테고리 프롬프트:")
    count = 0
    for idx, p in enumerate(prompts, start=1):
        if p["category"] == selected_cat:
            fav_star = " ⭐" if p["favorite"] else ""
            print(f"{idx}. {p['title']}{fav_star}")
            count += 1
    if count == 0: print("[안내] 등록된 프롬프트가 없습니다.")
    else: print(f"\n총 {count}개의 프롬프트")

# 6. 4번 메뉴: 검색
def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 입력: ").strip()
    if not keyword: return
    print(f"\n'{keyword}' 검색 결과:")
    count = 0
    for idx, p in enumerate(prompts, start=1):
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower():
            fav_star = " ⭐" if p["favorite"] else ""
            print(f"{idx}. [{p['category']}] {p['title']}{fav_star}")
            count += 1
    if count == 0: print("[안내] 검색 결과가 없습니다.")
    else: print(f"\n총 {count}개의 프롬프트를 찾았습니다.")

# ⭐ 7. 5번 메뉴: 상세 보기 함수 추가
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    choice = input("번호 입력: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(prompts):
        p = prompts[int(choice) - 1]
        fav_star = " ⭐" if p["favorite"] else "없음"
        print("─" * 40)
        print(f"제목: {p['title']}")
        print(f"카테고리: {p['category']}")
        print(f"즐겨찾기: {fav_star}")
        print("─" * 40)
        print(f"내용:\n{p['content']}")
        print("─" * 40)
    else:
        print("[에러] 잘못된 번호입니다.")

# ⭐ 8. 6번 메뉴: 즐겨찾기 관리(토글) 함수 추가
def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    choice = input("즐겨찾기 추가/해제할 프롬프트 번호 입력: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(prompts):
        p = prompts[int(choice) - 1]
        p["favorite"] = not p["favorite"]  # True는 False로, False는 True로 토글
        status = "등록" if p["favorite"] else "해제"
        print(f"\n[성공] '{p['title']}' 프롬프트가 즐겨찾기 {status}되었습니다!")
    else:
        print("[에러] 잘못된 번호입니다.")

# ⭐ 9. 7번 메뉴: 즐겨찾기 목록 보기 함수 추가
def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    count = 0
    for idx, p in enumerate(prompts, start=1):
        if p["favorite"]:
            print(f"{idx}. [{p['category']}] {p['title']} ⭐")
            count += 1
    if count == 0:
        print("[안내] 즐겨찾기된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 즐겨찾기")

# 10. 메인 루프 함수
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1": add_prompt()
        elif choice == "2": show_list()
        elif choice == "3": view_by_category()
        elif choice == "4": search_prompt()
        elif choice == "5": show_detail()       # 연결 완
        elif choice == "6": toggle_favorite()    # 연결 완
        elif choice == "7": show_favorites()     # 연결 완
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n[에러] 잘못된 번호입니다. 0~7 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()