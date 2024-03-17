import random

maxNum = int(input("숫자 게임 최대값을 입력해주세요:"));
minNum = 1;
count = 0;

print(minNum,"부터", maxNum, "까지의 숫자를 하나 생각하세요.");
print(input("준비가 되면 엔터를 누르세요."));

while True:
    myAnswer = random.randint(minNum, maxNum);
    print("당신이 생각한 숫자는", myAnswer, "입니까?");
    userAnswer = input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크면 '큼', 작으면 '작음'을 입력해주세요");
    count += 1;
    if userAnswer == "맞음":
        print("정답입니다. 총", count, "번만에 맞췄습니다.");
        break;
    elif userAnswer == "큼":
        minNum = myAnswer + 1;
    elif userAnswer == "작음":
        maxNum = myAnswer - 1;