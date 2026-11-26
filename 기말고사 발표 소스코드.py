def travel_expense():
    print("===== 여행 경비 비율 분석 프로그램 =====")

    # 여행 경비 입력
    transport = int(input("교통비 입력: "))
    hotel = int(input("숙박비 입력: "))
    food = int(input("식비 입력: "))
    tour = int(input("관광비 입력: "))
    etc = int(input("기타 경비 입력: "))

    # 전체 경비 계산
    total = transport + hotel + food + tour + etc

    if total == 0:
        print("경비가 입력되지 않았습니다.")
        return

    # 항목별 비율 계산
    expenses = {
        "교통비": transport,
        "숙박비": hotel,
        "식비": food,
        "관광비": tour,
        "기타": etc
    }

    print("\n===== 여행 경비 분석 결과 =====")
    print("총 여행 경비:", format(total, ","), "원")

    # 지출 비율 출력
    for name, amount in expenses.items():
        ratio = amount / total * 100
        print(name, ":", round(ratio, 1), "%")

    # 가장 많이 지출한 항목 분석
    highest = max(expenses, key=expenses.get)

    print("\n가장 많은 지출 항목:", highest)
    print("===============================")


travel_expense()


