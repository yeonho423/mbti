MBTI = ""

print("MBTI검사에 오신것을 환영합니다.")
print("이제부터 1에서 5로 답해주세요.")
print("1= 전혀아니다.")
print("3= 보통이다.")
print("5= 진짜 그렇다.")
print()
# 인트로


# ==============================================
# E, I

E = 0
I = 0

while True:
    E_vs_I = input("1.스트레스를 받거나 지친 주말, 에너지를 회복하는 나의 방법은 집에서 혼자 조용히 휴식을 취하는 것이다. :")
    if E_vs_I == "1":
        I += 2
        break
    elif E_vs_I == "2":
        I += 1
        break
    elif E_vs_I == "3":
        I += 1
        E += 1
        break
    elif E_vs_I == "4":
        E += 1
        break
    elif E_vs_I == "5":
        E += 2
        break
    else:
        print('다시 임력하시 겠나요?')
print()

while True:
    E_vs_I = input("2.처음 보는 사람들이 모인 자리에서도 먼저 말을 건네거나 쉽게 대화를 주도하는 편이다. :")
    if E_vs_I == "1":
        E += 2
        break
    elif E_vs_I == "2":
        E += 1
        break
    elif E_vs_I == "3":
        I += 1
        E += 1
        break
    elif E_vs_I == "4":
        I += 1
        break
    elif E_vs_I == "5":
        I += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    E_vs_I = input("3.생각을 깊게 하기보다는 일단 말로 내뱉거나 행동으로 부딪히며 해결하는 걸 좋아한다. :")
    if E_vs_I == "1":
        E += 2
        break
    elif E_vs_I == "2":
        E += 1
        break
    elif E_vs_I == "3":
        I += 1
        E += 1
        break
    elif E_vs_I == "4":
        I += 1
        break
    elif E_vs_I == "5":
        I += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    E_vs_I = input("4.힘든 하루를 끝내고 지친 상태일 때, 친구들과 맛있는 음식을 먹으며 수다를 떨어야 스트레스가 풀린다. :")
    if E_vs_I == "1":
        I += 2
        break
    elif E_vs_I == "2":
        I += 1
        break
    elif E_vs_I == "3":
        I += 1
        E += 1
        break
    elif E_vs_I == "4":
        E += 1
        break
    elif E_vs_I == "5":
        E += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    E_vs_I = input("5.엘리베이터에 어색한 아는 사람이 타려 할 때, 일부러 폰을 보거나 다른 층 계단으로 피하고 싶었던 적이 있다. :")
    if E_vs_I == "1":
        I += 2
        break
    elif E_vs_I == "2":
        I += 1
        break
    elif E_vs_I == "3":
        I += 1
        E += 1
        break
    elif E_vs_I == "4":
        E += 1
        break
    elif E_vs_I == "5":
        E += 2
        break
    else:
        print('다시 입력하시겠나요?')

# E vs I 검사 확인
if E > I:
    MBTI += "E"
else:
    MBTI += "I"
print()
# E vs I 검사 완료


# ==============================================
# S, N

S = 0
N = 0

while True:
    S_vs_N = input("6.나는 '만약에 세상에 좀비가 나타나면 어쩌지?' 같은 엉뚱한 상상을 자주 하는 편이다. :")
    if S_vs_N in ("1", "2", "3", "4", "5"):
        break
    else:
        print('다시 입력하시겠나요?')
if E_vs_I == "1":
    N += 2
if E_vs_I == "2":
    N += 1
if E_vs_I == "3":
    N += 1
    S += 1
if E_vs_I == "4":
    S += 1
if E_vs_I == "5":
    S += 2
print()

while True:
    S_vs_N = input("7.상상이나 공상보다는 눈앞에 보이는 현실적인 사실과 데이터가 더 중요하다. :")
    if S_vs_N == "1":
        S += 2
        break
    elif S_vs_N == "2":
        S += 1
        break
    elif S_vs_N == "3":
        N += 1
        S += 1
        break
    elif S_vs_N == "4":
        N += 1
        break
    elif S_vs_N == "5":
        N += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    S_vs_N = input("8.새로운 아이디어를 떠올리기보다, 이미 검증되고 확실하게 증명된 방식을 선호한다. :")
    if S_vs_N == "1":
        S += 2
        break
    elif S_vs_N == "2":
        S += 1
        break
    elif S_vs_N == "3":
        N += 1
        S += 1
        break
    elif S_vs_N == "4":
        N += 1
        break
    elif S_vs_N == "5":
        N += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    S_vs_N = input("9.밤에 침대에 누우면 '외계인이 침공하면 어떡하지?', '우주 끝에는 뭐가 있을까?' 같은 엉뚱한 상상이 꼬리를 문다. :")
    if S_vs_N == "1":
        S += 2
        break
    elif S_vs_N == "2":
        S += 1
        break
    elif S_vs_N == "3":
        N += 1
        S += 1
        break
    elif S_vs_N == "4":
        N += 1
        break
    elif S_vs_N == "5":
        N += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    S_vs_N = input("10.멍을 때리라고 하면 주로 과거의 기억, 내일 먹을 메뉴, 눈앞에 보이는 사물을 그대로 응시한다. :")
    if S_vs_N == "1":
        S += 2
        break
    elif S_vs_N == "2":
        S += 1
        break
    elif S_vs_N == "3":
        N += 1
        S += 1
        break
    elif S_vs_N == "4":
        N += 1
        break
    elif S_vs_N == "5":
        N += 2
        break
    else:
        print('다시 입력하시겠나요?')

#
if S > N:
    MBTI += "S"
else:
    MBTI += "N"
print()
# S vs N 검사 완료


# ==============================================
# T, F

T = 0
F = 0

while True:
    T_vs_F = input("11.친구가 '나 오늘 너무 우울해서 쇼핑했어'라고 할 때, '왜 우울했어?'보다 '뭐 샀어?'라는 질문이 먼저 떠오른다.  :")
    if T_vs_F == "1":
        F += 2
        break
    elif T_vs_F == "2":
        F += 1
        break
    elif T_vs_F == "3":
        T += 1
        F += 1
        break
    elif T_vs_F == "4":
        T += 1
        break
    elif T_vs_F == "5":
        T += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    T_vs_F = input("12.누군가 고민을 털어놓을 때, 공감해주기보다 해결책이나 현실적인 조언부터 떠오른다.  :")
    if T_vs_F == "1":
        F += 2
        break
    elif T_vs_F == "2":
        F += 1
        break
    elif T_vs_F == "3":
        T += 1
        F += 1
        break
    elif T_vs_F == "4":
        T += 1
        break
    elif T_vs_F == "5":
        T += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    T_vs_F = input("13.결정 내릴 때 감정이나 주변 분위기보다는 논리와 팩트가 가장 중요하다고 생각한다.  :")
    if T_vs_F == "1":
        F += 2
        break
    elif T_vs_F == "2":
        F += 1
        break
    elif T_vs_F == "3":
        T += 1
        F += 1
        break
    elif T_vs_F == "4":
        T += 1
        break
    elif T_vs_F == "5":
        T += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    T_vs_F = input("14.친구가 '나 배탈 나서 약 먹었어'라고 했을 때, '어쩌다 배탈 났어? 무슨 약 먹었는데?'라는 질문이 '많이 아파?'보다 먼저 나온다.  :")
    if T_vs_F == "1":
        F += 2
        break
    elif T_vs_F == "2":
        F += 1
        break
    elif T_vs_F == "3":
        T += 1
        F += 1
        break
    elif T_vs_F == "4":
        T += 1
        break
    elif T_vs_F == "5":
        T += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()
while True:
    T_vs_F = input("15.영화나 드라마를 볼 때 등장인물의 사연에 깊이 몰입해 눈물을 글썽이거나 여운이 며칠씩 간다.  :")
    if T_vs_F == "1":
        F += 2
        break
    elif T_vs_F == "2":
        F += 1
        break
    elif T_vs_F == "3":
        T += 1
        F += 1
        break
    elif T_vs_F == "4":
        T += 1
        break
    elif T_vs_F == "5":
        T += 2
        break
    else:
        print('다시 입력하시겠나요?')

#
if T > F:
    MBTI += "T"
else:
    MBTI += "F"
print()
# T vs F 검사 완료


# ==============================================
# J, P

J = 0
P = 0

while True:
    J_vs_P = input("16.주말이나 쉬는 날, 별다른 계획 없이 그냥 발길 닿는 대로 움직이는 게 훨씬 편하다. :")
    if J_vs_P == "1":
        P += 2
        break
    elif J_vs_P == "2":
        P += 1
        break
    elif J_vs_P == "3":
        J += 1
        P += 1
        break
    elif J_vs_P == "4":
        J += 1
        break
    elif J_vs_P == "5":
        J += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    J_vs_P = input("17.여행을 가거나 일정을 잡을 때 시간대별로 계획을 꼼꼼하게 세우는 게 마음이 편하다. :")
    if J_vs_P == "1":
        P += 2
        break
    elif J_vs_P == "2":
        P += 1
        break
    elif J_vs_P == "3":
        J += 1
        P += 1
        break
    elif J_vs_P == "4":
        J += 1
        break
    elif J_vs_P == "5":
        J += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    J_vs_P = input("18.즉흥적인 약속이나 갑작스러운 계획 변경보다는 미리 예정된 일정을 훨씬 좋아한다. :")
    if J_vs_P == "1":
        P += 2
        break
    elif J_vs_P == "2":
        P += 1
        break
    elif J_vs_P == "3":
        J += 1
        P += 1
        break
    elif J_vs_P == "4":
        J += 1
        break
    elif J_vs_P == "5":
        J += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    J_vs_P = input("19.친구가 갑작스럽게 약속을 잡으면 거부할 때가 많다. :")
    if J_vs_P == "1":
        P += 2
        break
    elif J_vs_P == "2":
        P += 1
        break
    elif J_vs_P == "3":
        J += 1
        P += 1
        break
    elif J_vs_P == "4":
        J += 1
        break
    elif J_vs_P == "5":
        J += 2
        break
    else:
        print('다시 입력하시겠나요?')
print()

while True:
    J_vs_P = input("20.일을 미루다 항상 마지막에 해치운다. :")
    if J_vs_P == "1":
        J += 2
        break
    elif J_vs_P == "2":
        J += 1
        break
    elif J_vs_P == "3":
        J += 1
        P += 1
        break
    elif J_vs_P == "4":
        P += 1
        break
    elif J_vs_P == "5":
        P += 2
        break
    else:
        print('다시 입력하시겠나요?')

#
if J > P:
    MBTI += "J"
else:
    MBTI += "P"
print()
# J vs P 검사 완료

print("당신의 MBTI는 ", MBTI, "입니다.")
print()
# 최종 MBTI


# ==============================================
# 결과 출력

if MBTI == "INTJ":
    print("INTJ는 모든 일에 대해 계획을 세우는 상상력이 풍부한 전략가입니다.")

if MBTI == "INTP":
    print("INTP는 끊임없이 원리를 파고들다 새벽 3시에 엉뚱한 가설에 도달하는 이론가다.")

if MBTI == "ENTJ":
    print("ENTJ는 비효율을 참지 못하고 팀을 목표 지점까지 몰아붙이는 타고난 리더다.")

if MBTI == "ENTP":
    print("ENTP는 '근데 반대로 생각하면 이렇지 않아?'라며 논쟁의 불씨를 지피는 악마의 변호인이다.")
# 분석형

if MBTI == "INFJ":
    print("INFJ는 겉은 온화하지만 속은 깊은 이상과 신념으로 가득 찬 고요한 통찰자입니다.")

if MBTI == "INFP":
    print("INFP는 자신만의 내면세계와 가치관을 품고 조용히 세상을 응원하는 낭만주의자입니다.")

if MBTI == "ENFJ":
    print("ENFJ는 사람들의 잠재력을 끌어올려 더 나은 세상을 만들고 싶어 하는 열정적 멘토입니다.")

if MBTI == "ENFP":
    print("ENFP는 새로운 아이디어와 사람에 반짝이며 세상의 모든 재미를 쫓는 활력소입니다.")
# 외교형

if MBTI == "ISTJ":
    print("ISTJ는 맡은 일은 빈틈없이 끝내야 직성이 풀리는 믿음직한 원칙주의자입니다.")

if MBTI == "ISFJ":
    print("ISFJ는 묵묵히 주변 사람을 챙기고 헌신하는 따뜻하고 세심한 수호자입니다.")

if MBTI == "ESTJ":
    print("ESTJ는 질서와 규칙을 명확히 세워 혼란을 정리하는 철저한 현실 관리자입니다.")

if MBTI == "ESFJ":
    print("ESFJ는 모임의 분위기를 띄우고 모두가 소외되지 않도록 살피는 분위기 메이커입니다.")
# 관리자형

if MBTI == "ISTP":
    print("ISTP는 평소엔 무심해 보여도 위기 상황이 오면 해결책을 뚝딱 만들어내는 현실적 맥가이버입니다.")

if MBTI == "ISFP":
    print("ISFP는 다정하고 여유로우며 순간의 아름다움과 감각을 오롯이 즐기는 예술가입니다.")

if MBTI == "ESTP":
    print("ESTP는 고민할 시간에 일단 부딪히며 스릴과 즉각적인 행동을 즐기는 개척자입니다.")

if MBTI == "ESFP":
    print("ESFP는 어디서든 시선을 사로잡으며 주변에 흥과 에너지를 퍼뜨리는 슈퍼스타입니다.")
# 탐험가형

print("더 알고 싶은것이 있나요?")
아주_용함 = input("o 아니면 x로 답해주세요.")
if 아주_용함 == "o" or 아주_용함 == "O":
    print("1.MBTI의 학율을 알고싶은가요?")
    이이이 = input("2.다양한 MBTI를 알고싶나요?")
    if 이이이 == "1":
        print("[2026 공식 신규 MBTI 희귀도 등급")
        print("""■ 전설 (독보적 존재)
- INFJ-A-C
■ 극희귀 (흔치 않은 인재)
- INFJ-A-C
- ENTP-O-H
■ 희귀 (상위 10% 인재)
- INFP-A-C
- ENFJ-A-H
- ESTP-A-C
- INTP-O-H
■ 비교적 희귀 (눈에 띄는 인재)
- ENFJ-O-H
- ISTJ-O-C
- ENTJ-A-C
- ENTP-A-H
- INFJ-A-H
■ 일반 (평균 수준)
- INTJ-O-C
- INFP-O-H
- ISFP-A-H
- ENFP-A-H
- INTP-O-C
- INFJ-O-H
■ 혼합 (대중적 성향)
- ISTJ-A-H
- ISTJ-A-C
- ESFP-O-H
- ENFP-O-H
- ESFP-A-H
- ISTP-A-H
- INFP-A-H""")
    if 이이이 == "2":
        print("""분석가형 (NT)
INTJ (전략가): 모든 상황을 체계적으로 설계하며 지적 호기심과 통찰력이 뛰어난 전략가입니다.

INTP (논리술사): 끊임없는 호기심으로 세상의 원리를 탐구하는 창의적인 사색가입니다.

ENTJ (통솔자): 명확한 비전과 강한 추진력으로 목표를 달성하는 대담한 지도자입니다.

ENTP (변론가): 기존의 틀을 깨는 아이디어와 재치 있는 논리로 토론을 즐기는 발명가입니다.

외교관형 (NF)
INFJ (옹호자): 조용하지만 확고한 신념과 깊은 공감 능력으로 세상에 선한 영향력을 미치는 이상주의자입니다.

INFP (중재자): 풍부한 감수성과 내면의 가치를 중시하며 진정성을 추구하는 낭만주의자입니다.

ENFJ (선도자): 따뜻한 카리스마와 이타심으로 사람들의 성장을 이끄는 열정적인 리더입니다.

ENFP (활동가): 넘치는 에너지와 창의력으로 사람들에게 긍정적인 영감을 주는 자유로운 영혼입니다.

관리자형 (SJ)
ISTJ (현실주의자): 철저한 책임감과 원칙을 바탕으로 맡은 일을 빈틈없이 해내는 신뢰의 아이콘입니다.

ISFJ (수호자): 세심한 배려와 헌신으로 주변 사람들을 묵묵히 챙기는 따뜻한 조력자입니다.

ESTJ (경영자): 뛰어난 조직력과 현실 감각으로 질서를 세우고 일을 효율적으로 추진하는 관리자입니다.

ESFJ (집정관): 사교적이고 다정다감하며 주변의 조화와 화합을 이끌어내는 분위기 메이커입니다.

탐험가형 (SP)
ISTP (장인): 냉철한 이성과 뛰어난 손재주로 상황을 빠르게 파악하고 해결하는 실용주의자입니다.

ISFP (모험가): 겸손하고 온화한 성품으로 현재의 순간과 예술적 감각을 즐기는 유연한 예술가입니다.

ESTP (사업가): 직관적인 판단력과 과감한 행동력으로 스릴과 도전을 즐기는 현실적 해결사입니다.

ESFP (연예인): 밝고 유쾌한 에너지로 어디서든 주변을 즐겁게 만드는 타고난 엔터테이너입니다.""")
if 아주_용함 == "X" or 아주_용함 == "x":
    print("검사가 종료되었습니다.")


# --------검사 종료
