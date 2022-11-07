import csv


def nameToTips(name):
    tips = ''
    with open('./file/1.csv', mode='r', encoding='utf-8') as f:
        data = csv.reader(f)
        for row in data:
            if row[2] == name:
                tips = '厂牌:' + row[0] + '\n' + '代理范围:' + row[1] + '\n' + tips

    return tips


if __name__ == "__main__":
    print(nameToTips('兆科新能源材料'))
