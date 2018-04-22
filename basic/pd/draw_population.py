import pandas as pd
import matplotlib.pyplot as plt


def draw_pop(path):
    data = pd.read_csv(path, sep=',', encoding='ANSI')
    c_pop = data['2015年城市人口'].sum()
    r_pop = data['2015年农村人口'].sum()
    properties = [c_pop, r_pop, 10000]
    plt.pie(properties, labels=['Males', 'Females', 'unknown'], shadow=False, colors=['blue', 'red', 'green'],
            explode=(0, 0, 0),
            startangle=90, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title('Sex Proportion')
    plt.tight_layout()
    plt.savefig('Sex Proportion.png')
    plt.show()


if __name__ == '__main__':
    file_path = 'D:/data-csv/population.csv'
    draw_pop(file_path)
