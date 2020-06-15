from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color
        #self.running()

    def running(self):
        color_d = {'красный': [7, '\033[31m'], 'желтый': [2, '\033[33m\033[5m'], 'зеленый': [7, '\033[32m']}
        list_st = ['красный', 'желтый', 'зеленый', 'желтый']
        start_color = list_st.index(self.__color)
        for i in range(start_color, len(list_st)):
            print(f"{color_d[list_st[i]][1]}{chr(1421)} {list_st[i]} {chr(1421)}")
            sleep(color_d[list_st[i]][0])
        count = 0
        while count != 3:
            for i in range(0, len(list_st)):
                print(f"{color_d[list_st[i]][1]}{chr(1421)} {list_st[i]} {chr(1421)}")
                sleep(color_d[list_st[i]][0])
            count += 1

semafor = TrafficLight('желтый')
semafor.running()




