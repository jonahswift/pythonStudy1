#需求：有三个办公室，8位⽼师，8位⽼师随机分配到3个办公室
import random

rom=[[],[],[]]
techer=['te1','te2','te3','te4','te5','te6','te7','te8']


for i in techer:
    num = random.randint(0, 2)
    rom[num].insert(0,i)

print(rom)