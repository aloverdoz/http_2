import yadisk

y = yadisk.YaDisk(token="y0_AgAAAABk33T_AADLWwAAAADP0R4mdGLnpH3gR0a8dvtGvAxmfqPDS0Q")
vvod = input('Введите путь до файла который необходимо загрузить: ')

with open(vvod, "rb") as f:
    split_file = vvod.split('/')
    y.upload(f, split_file[-1])
