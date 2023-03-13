import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import random
import yaml


for i in range(1,11):
   
    plt.clf()
    sikinArr =[]
    xAxis = []

    # 100万持ってスタート
    initSikin = 100000
    sikin = 0

    # 最初の賭け金
    initBet = 1000
    Bet = 0

    # 配当オッズ
    ozzu = 2

    for num in range(1,1001):
        if Bet == 0 & sikin == 0:
            Bet = initBet
            sikin = initSikin

        # 勝ち負け決める
        VictoryOrDefault = random.randint(1,1000000)%2

        if VictoryOrDefault == 0:
            profit = Bet*ozzu -Bet
            sikin = sikin + profit

            Bet = initBet


            sikinArr.append(sikin)
            xAxis.append(num)


        elif VictoryOrDefault == 1:
            sikin = sikin - Bet

            Bet = Bet*2

            sikinArr.append(sikin)
            xAxis.append(num)

        if sikinArr[-1] < 0 | Bet>sikin:
            break


    print("sikinArr")
    print(sikinArr)
    print("xAxis")
    print(xAxis)

    x = xAxis
    y = sikinArr

    yml = {"arr":sikinArr}

    with open("yaml/{0}.yaml".format(i),"w") as yf:
        yaml.dump(yml,yf,default_flow_style=False)

    plt.plot(x, y)

    plt.savefig("image/graph{0}.png".format(i))