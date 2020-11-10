import time

# プログラムの説明を表示する
print('Enterを押すと開始します。その後、rを押せば経過時間を表示します。fで終了します。')
input()    #Enterを押すと開始
print('スタート')
start_time = time.time()    #プログラムと最初のラップの開始時間
last_time = start_time
lap_num = 1
t = True

# ラップタイムを計測する
while t:
    x = str(input())
    now = time.time()
    if x == "r":
        lap_time = round(now - last_time, 2) #round()は四捨五入
        total_time = round(now - start_time, 2)
        print('ラップ No{}: {}秒 ({}秒)'\
                .format(str(lap_num).rjust(3), str(total_time).rjust(6), str(lap_time).rjust(8)), end='') #rjustは右寄り
        lap_num += 1
        last_time = now # ラップタイムをリセット
    
    elif x == "f":
        print('\n終了')
        print("全体の時間は", str(round(now - start_time, 2)), "秒です。\n")
        print("お疲れ様でした。\n")
        t = int(0)
        break
    