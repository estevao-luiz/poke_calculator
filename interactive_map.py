from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from shapely.geometry import Point

class InteractiveButton_version:
    def __init__(self, coordenadas):
        self.version = None

        self.root = Toplevel()
        self.root.title("Mapa Interativo")
        

        self.fig, self.ax = plt.subplots()
        img = plt.imread('version.jpg')
        self.ax.imshow(img)

        for regiao, coords in coordenadas.items():
            poly = Polygon(list(zip(coords[0], coords[1])), facecolor='none', edgecolor='none', label=regiao, picker=True)
            self.ax.add_patch(poly)

        self.fig.canvas.mpl_connect('button_press_event', self.on_polygon_click)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label_regiao = Label(self.root, text="Clique em uma região.")
        self.label_regiao.pack()

    def on_polygon_click(self, event):
        for poly in self.ax.patches:
            if isinstance(poly, Polygon) and poly.contains_point((event.x, event.y)):
                self.label_regiao.config(text=f'Você clicou na região: {poly.get_label()}')
                self.version = poly.get_label()
                self.version = str(self.version)
                self.root.destroy()
                
                
class InteractiveMap_paldea:
    def __init__(self, coordenadas_paldea):
        self.province = None

        self.root = Toplevel()
        self.root.title("Mapa Interativo")
        

        self.fig, self.ax = plt.subplots()
        img = plt.imread('paldeanmap.jpeg')
        self.ax.imshow(img)

        for regiao, coords in coordenadas_paldea.items():
            poly = Polygon(list(zip(coords[0], coords[1])), facecolor='none', edgecolor='none', label=regiao, picker=True)
            self.ax.add_patch(poly)

        self.fig.canvas.mpl_connect('button_press_event', self.on_polygon_click)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label_regiao = Label(self.root, text="Clique em uma região.")
        self.label_regiao.pack()

    def on_polygon_click(self, event):
        for poly in self.ax.patches:
            if isinstance(poly, Polygon) and poly.contains_point((event.x, event.y)):
                self.label_regiao.config(text=f'Você clicou na região: {poly.get_label()}')
                self.province = poly.get_label()
                self.province = str(self.province)
                self.root.destroy()
             
                
class InteractiveMap_province:
    def __init__(self, coordenadas_area, province):
        self.area = None

        self.root = Toplevel()
        self.root.title("Mapa Interativo")
        
        self.fig, self.ax = plt.subplots()
        img = plt.imread(f'{province}.jpeg')
        self.ax.imshow(img)

        for regiao, coords in coordenadas_area.items():
            poly = Polygon(list(zip(coords[0], coords[1])), facecolor='none', edgecolor='none', label=regiao, picker=True)
            self.ax.add_patch(poly)

        self.fig.canvas.mpl_connect('button_press_event', self.on_polygon_click)
 
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label_regiao = Label(self.root, text="Clique em uma área.")
        self.label_regiao.pack()

    def on_polygon_click(self, event):
        for poly in self.ax.patches:
            if isinstance(poly, Polygon) and poly.contains_point((event.x, event.y)):
                self.label_regiao.config(text=f'Você clicou na área: {poly.get_label()}')
                self.area = poly.get_label()
                self.area = str(self.area)
                self.root.destroy()            
  
                
class InteractiveButton_biome:
    def __init__(self, coordenadas, province, area):
        self.biome = None

        self.root = Toplevel()
        self.root.title("Mapa Interativo")
        
        self.fig, self.ax = plt.subplots()
        img = plt.imread('biomes.jpg')
        self.ax.imshow(img)

        for regiao, coords in coordenadas.items():
            poly = Polygon(list(zip(coords[0], coords[1])), facecolor='none', edgecolor='none', label=regiao, picker=True)
            self.ax.add_patch(poly)

        self.fig.canvas.mpl_connect('button_press_event', lambda event: self.on_polygon_click(event, province, area))
 
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.label_regiao = Label(self.root, text="Clique em uma área.")
        self.label_regiao.pack()

    def on_polygon_click(self, event, province, area):
        
        doc = 'biomas.txt'
        
        with open(doc, encoding= 'utf-8', mode='r') as file:
            lines = file.readlines()
            
            
            for poly in self.ax.patches:
                if isinstance(poly, Polygon) and poly.contains_point((event.x, event.y)):
                    self.label_regiao.config(text=f'Você clicou no bioma: {poly.get_label()}')
                    self.biome = poly.get_label()
                    for line in lines:
                        if self.biome in line:
                            if f'{province} ({area})' in line:
                                self.biome = poly.get_label()
                                self.biome = str(self.biome)
                                self.root.destroy()  
                            else:
                                self.label_regiao.config(text=f'O bioma: {poly.get_label()}, não existe na área que você selecionou')
 

def main():
    
    version = None
    
    coordenadas_version = {'Scarlet':
    ([0, 539, 539, 0, 2],
    [0, 0, 1078, 1078, 2]),
    
    'Violet':
    ([539, 539, 1078, 1080, 539],
    [0, 1080, 1080, 0, 2])
    }
    
    app_0 = InteractiveButton_version(coordenadas_version)
    
    app_0.root.wait_window()
    
    province = None
    
    # Coordenadas dos polígonos (obtidas pelo VIA - Oxford)
    coordenadas_paldea = {
        'South': (
            [59, 70, 78, 84, 89, 92, 93, 96, 99, 101, 106, 113, 118, 127, 142, 139, 129, 130, 136, 151, 155, 164, 177, 188, 198, 217, 227, 237, 252, 258, 266, 284, 286, 288, 293, 297, 303, 309, 321, 321, 319, 317, 319, 337, 331, 307, 289, 287, 274, 231, 228, 217, 196, 195, 181, 169, 159, 145, 134, 121, 114, 94, 81, 77, 51, 44, 44, 49, 60],
            [358, 356, 357, 359, 359, 361, 361, 358, 345, 339, 334, 326, 315, 316, 302, 299, 296, 287, 283, 280, 288, 287, 290, 304, 307, 306, 314, 314, 322, 320, 307, 306, 304, 308, 304, 309, 307, 316, 320, 320, 332, 343, 345, 356, 384, 402, 406, 413, 418, 416, 426, 430, 425, 413, 419, 418, 412, 412, 409, 413, 411, 421, 419, 418, 415, 404, 366, 359, 358]
        ),
        'East': (
            [338, 389, 425, 405, 389, 369, 332, 325, 316, 292, 276, 277, 265, 266, 279, 286, 266, 260, 257, 266, 265, 282, 284, 294, 296, 303, 308, 322, 320, 318, 321, 338],
            [355, 339, 280, 211, 202, 201, 188, 179, 178, 213, 218, 228, 229, 235, 242, 249, 251, 239, 239, 261, 305, 304, 301, 304, 307, 306, 314, 319, 335, 337, 347, 355]
        ),
        'West': (
            [43, 125, 145, 180, 180, 185, 189, 185, 189, 192, 198, 205, 215, 204, 204, 210, 206, 194, 190, 193, 186, 185, 179, 175, 165, 163, 156, 156, 152, 153, 150, 152, 138, 129, 129, 140, 126, 116, 112, 112, 98, 94, 68, 58, 61, 49, 42, 24, 20, 32, 40, 28, 34, 43, 43],
            [182, 185, 173, 167, 151, 149, 143, 139, 137, 137, 132, 132, 142, 165, 188, 193, 199, 204, 210, 216, 216, 224, 228, 242, 250, 250, 262, 264, 269, 276, 276, 280, 279, 287, 298, 301, 314, 313, 318, 320, 338, 359, 351, 355, 342, 333, 318, 308, 280, 249, 230, 205, 198, 192, 182]
        ),
        'North': (
            [43, 38, 102, 146, 190, 286, 364, 376, 384, 406, 417, 406, 391, 370, 359, 332, 326, 312, 290, 275, 273, 263, 261, 269, 281, 267, 266, 265, 259, 256, 254, 244, 242, 231, 217, 205, 199, 192, 196, 204, 207, 212, 205, 206, 217, 201, 190, 183, 187, 178, 178, 144, 125, 42],
            [178, 97, 58, 75, 48, 54, 95, 127, 148, 162, 202, 210, 200, 199, 192, 186, 174, 176, 209, 214, 224, 227, 233, 241, 246, 248, 248, 240, 236, 236, 230, 222, 218, 217, 207, 207, 212, 211, 205, 202, 202, 193, 186, 165, 140, 128, 136, 139, 144, 151, 166, 172, 184, 178]
        ),
        'The Great Crater of Paldea': (
            [150, 154, 173, 185, 193, 218, 228, 236, 250, 255, 262, 263, 253, 240, 227, 214, 203, 197, 194, 194, 188, 186, 179, 176, 166, 157, 154, 151],
            [281, 285, 287, 302, 306, 304, 313, 312, 320, 318, 307, 263, 234, 221, 218, 209, 211, 216, 215, 217, 217, 225, 229, 244, 251, 263, 279, 281]
        )
    }
   
    if app_0 is not None:
        app_1 = InteractiveMap_paldea(coordenadas_paldea)

    # Aguarda o fechamento da janela antes de retornar o valor da province
    app_1.root.wait_window()
    
    area = None
    
    coordenadas_area = {'South': {'Six':
    ([25, 47, 63, 78, 87, 108, 112, 110, 111, 108, 107, 79, 22, 8, 9, 25],
    [133, 129, 135, 137, 147, 150, 157, 167, 173, 194, 211, 221, 215, 195, 140, 133]),
    
    'Two':
    ([94, 116, 126, 155, 183, 201, 208, 215, 221, 227, 223, 201, 175, 175, 165, 159, 144, 133, 135, 151, 127, 119, 109, 109, 91, 95],
    [111, 124, 135, 145, 145, 139, 117, 113, 94, 92, 79, 69, 45, 33, 32, 23, 22, 34, 44, 51, 76, 71, 75, 85, 108, 111]),
    
    'Four':
    ([92, 114, 128, 157, 171, 205, 212, 218, 225, 222, 217, 226, 250, 251, 243, 229, 225, 197, 174, 153, 139, 123, 111, 111, 115, 114, 83, 91],
    [113, 127, 142, 150, 150, 143, 118, 116, 132, 151, 163, 179, 185, 193, 205, 206, 213, 217, 209, 207, 203, 209, 209, 193, 183, 149, 140, 113]),
    
    'One':
    ([232, 230, 265, 281, 345, 329, 308, 301, 295, 275, 267, 263, 271, 273, 274, 297, 272, 273, 258, 217, 194, 178, 183, 202, 225, 231, 231, 225, 220, 229, 223, 228, 251, 256, 246, 232],
    [209, 227, 237, 217, 217, 183, 171, 183, 184, 173, 177, 170, 159, 159, 140, 117, 81, 72, 57, 58, 33, 31, 47, 65, 75, 91, 95, 97, 113, 131, 165, 176, 182, 193, 208, 209]),
    
    'Three':
    ([276, 290, 307, 321, 329, 354, 381, 409, 407, 387, 374, 369, 351, 344, 334, 334, 325, 317, 308, 296, 277, 277],
    [72, 71, 82, 79, 60, 59, 60, 79, 95, 105, 100, 89, 86, 91, 89, 105, 116, 111, 116, 112, 80, 71]),
    
    'Five':
    ([348, 364, 391, 423, 431, 404, 401, 386, 373, 367, 350, 337, 337, 328, 299, 278, 275, 268, 275, 296, 307, 329, 348, 348],
    [215, 202, 195, 170, 132, 116, 103, 108, 103, 92, 91, 97, 105, 119, 117, 145, 164, 170, 169, 181, 167, 180, 212, 214]),
    
    'South Paldean Sea':
    ([0, 45, 28, 9, 5, 6, 17, 61, 71, 84, 110, 127, 138, 144, 156, 171, 190, 210, 226, 227, 236, 261, 272, 278, 280, 344, 360, 365, 389, 422, 430, 436, 434, 424, 439, 439, 0, 0],
    [70, 117, 128, 136, 150, 195, 215, 221, 224, 224, 212, 212, 208, 208, 212, 212, 220, 221, 217, 227, 234, 238, 234, 227, 219, 220, 213, 203, 198, 172, 154, 133, 130, 124, 111, 251, 250, 70])
    }, 
    
    'West': {'Two':
    ([66, 217, 227, 221, 212, 182, 145, 138, 62, 43, 70],
    [114, 119, 164, 175, 161, 152, 152, 166, 194, 156, 114]),
    
    'Asado Desert':
    ([47, 63, 143, 148, 182, 208, 223, 229, 238, 233, 215, 207, 198, 185, 166, 145, 110, 87, 87, 46],
    [228, 198, 170, 157, 158, 164, 179, 184, 205, 219, 219, 204, 206, 224, 226, 247, 248, 238, 234, 228]),
    
    'Three':
    ([219, 254, 314, 310, 325, 317, 324, 334, 342, 370, 353, 350, 364, 330, 331, 318, 315, 306, 297, 281, 273, 250, 251, 241, 235, 235, 226, 232, 221],
    [115, 94, 82, 58, 46, 38, 29, 32, 22, 38, 84, 120, 134, 153, 170, 172, 187, 190, 219, 233, 209, 194, 166, 157, 160, 182, 176, 158, 114]),
    
    'One':
    ([46, 82, 111, 150, 170, 187, 204, 214, 234, 243, 236, 238, 241, 245, 247, 271, 277, 263, 256, 230, 218, 241, 214, 194, 192, 169, 157, 126, 113, 92, 96, 74, 64, 31, 25, 47],
    [233, 238, 253, 253, 231, 228, 209, 225, 224, 214, 189, 187, 163, 169, 198, 214, 234, 254, 284, 286, 310, 322, 349, 349, 364, 388, 430, 419, 416, 422, 391, 378, 355, 334, 287, 234]),
    
    'West Paldean Sea':
    ([70, 278, 284, 301, 201, 165, 146, 136, 107, 94, 80, 70, 40, 59, 22, 28, 30, 61, 72, 92, 88, 96, 92, 0, 0, 70],
    [1, 1, 2, 39, 87, 86, 95, 104, 100, 72, 78, 110, 154, 197, 284, 332, 338, 358, 382, 393, 424, 426, 439, 439, 1, 0])
    },
    
    'East': {'Three':
    ([265, 355, 410, 406, 577, 820, 918, 948, 1371, 1619, 1717, 1738, 1679, 1546, 1555, 1499, 1452, 1281, 1183, 1196, 1034, 897, 803, 577, 504, 457, 372, 269, 269],
    [589, 594, 555, 453, 389, 60, 77, 137, 290, 316, 376, 431, 534, 577, 624, 636, 598, 538, 658, 726, 799, 777, 722, 752, 782, 726, 713, 619, 585]),
    
    'Two':
    ([581, 816, 987, 1055, 1209, 1222, 1200, 1290, 1461, 1504, 1551, 1546, 1499, 1452, 1410, 1427, 1495, 1392, 1358, 1303, 1247, 1098, 970, 807, 628, 581],
    [769, 743, 816, 812, 743, 692, 666, 555, 624, 649, 645, 701, 726, 965, 1000, 1093, 1111, 1170, 1170, 1132, 1140, 1290, 1299, 1170, 803, 769]),
    
    'One':
    ([196, 278, 286, 423, 602, 782, 940, 1119, 1273, 1311, 1358, 1414, 1448, 1546, 1602, 1649, 1640, 1598, 1504, 1452, 1418, 1119, 1025, 846, 829, 880, 713, 662, 581, 547, 525, 487, 461, 278, 269, 196],
    [666, 688, 807, 786, 803, 1170, 1307, 1311, 1162, 1158, 1187, 1192, 1158, 1119, 1153, 1256, 1345, 1465, 1512, 1589, 1704, 1781, 1867, 1777, 1649, 1504, 1444, 1363, 1371, 1358, 1397, 1337, 1375, 1358, 863, 645]),
    
    'East Paldean Sea':
    ([2042, 2042, 974, 978, 1042, 1046, 1132, 1435, 1478, 1529, 1619, 1679, 1653, 1572, 1444, 1431, 1491, 1516, 1572, 1563, 1700, 1743, 1747, 1717, 1756, 1824, 2037],
    [158, 1948, 1948, 1867, 1909, 1871, 1803, 1730, 1580, 1529, 1478, 1324, 1192, 1111, 1072, 1004, 961, 739, 718, 589, 534, 444, 419, 367, 316, 308, 162])
    },

    'North': {'Casseroya Lake':
    ([116, 137, 103, 161, 127, 89, 127, 182, 291, 329, 401, 428, 490, 582, 644, 692, 709, 743, 829, 911, 979, 997, 969, 997, 1000, 1010, 997, 959, 976, 767, 661, 599, 589, 267, 113],
    [894, 723, 664, 596, 555, 442, 366, 322, 277, 236, 202, 178, 158, 195, 205, 233, 342, 370, 462, 510, 524, 555, 582, 623, 651, 664, 695, 705, 798, 829, 901, 908, 921, 897, 897]),
    
    'Glaseado Mountain':
    ([818, 842, 870, 942, 976, 1024, 1007, 1024, 1041, 1089, 1144, 1161, 1274, 1267, 1363, 1408, 1418, 1466, 1500, 1555, 1538, 1493, 1572, 1719, 1764, 1709, 1743, 1685, 1647, 1610, 1562, 1469, 1486, 1541, 1579, 1558, 1493, 1493, 1538, 1541, 1610, 1616, 1568, 1497, 1486, 1432, 1432, 1336, 1267, 1188, 1116, 1099, 1045, 1048, 1120, 1164, 1116, 1120, 1195, 1092, 1058, 1003, 990, 1007, 1007, 945, 897, 733, 712, 709, 760, 818],
    [195, 250, 233, 216, 226, 308, 325, 346, 366, 377, 339, 260, 219, 120, 92, 113, 120, 116, 151, 147, 229, 349, 394, 527, 582, 719, 740, 801, 846, 860, 925, 1000, 1086, 1134, 1134, 1199, 1209, 1240, 1271, 1288, 1301, 1325, 1322, 1339, 1257, 1253, 1216, 1140, 1120, 1075, 1082, 1099, 1096, 1051, 1017, 979, 928, 788, 644, 579, 623, 616, 579, 568, 531, 500, 493, 336, 332, 243, 243, 199]),
    
    'Three':
    ([1031, 1236, 1253, 1257, 1140, 1130, 1079, 1045, 1027, 1034, 979, 921, 846, 832, 911, 1027, 1045],
    [68, 134, 127, 212, 253, 336, 360, 356, 318, 301, 212, 199, 229, 158, 103, 68, 75]),
    
    'One':
    ([1716, 1733, 1729, 1750, 1795, 1822, 1836, 1866, 1887, 1911, 1901, 1945, 1983, 2000, 2024, 2027, 2075, 2103, 2130, 2182, 2182, 2137, 2089, 1997, 1853, 1849, 1805, 1815, 1781, 1729, 1709, 1647, 1562, 1555, 1507, 1568, 1654, 1781, 1726, 1753, 1753, 1712],
    [798, 812, 832, 842, 829, 842, 880, 880, 901, 870, 801, 699, 699, 723, 719, 702, 664, 671, 582, 582, 548, 551, 510, 503, 473, 401, 356, 308, 243, 236, 175, 151, 147, 240, 349, 377, 438, 579, 719, 733, 753, 801]),
    
    'Tagtree Thicket':
    ([1702, 1723, 1719, 1743, 1795, 1815, 1822, 1743, 1705, 1658, 1572, 1545, 1497, 1483, 1579, 1616, 1682, 1705],
    [801, 812, 832, 856, 842, 849, 887, 979, 1031, 1089, 1123, 1120, 1075, 1003, 932, 870, 842, 801]),
    
    'Two':
    ([1897, 2079, 2164, 2295, 2363, 2380, 2425, 2353, 2336, 2295, 2274, 2281, 2332, 2305, 2188, 2158, 2158, 2182, 2182, 2140, 2110, 2075, 2038, 2031, 1997, 1973, 1952, 1914, 1925, 1897],
    [918, 993, 1027, 1038, 1079, 1034, 1027, 979, 979, 945, 887, 846, 801, 767, 747, 699, 616, 596, 589, 596, 688, 682, 709, 729, 733, 712, 712, 815, 873, 925]),
    
    'North Paldean Sea':
    ([3, 2164, 2144, 2140, 2089, 2055, 2099, 2137, 2178, 2140, 2092, 1863, 1853, 1815, 1825, 1788, 1733, 1719, 1637, 1500, 1459, 1425, 1366, 1226, 1038, 908, 832, 829, 757, 705, 623, 486, 414, 387, 308, 281, 161, 116, 75, 116, 144, 96, 127, 106, 116, 147, 0, 7],
    [3, 0, 62, 123, 199, 315, 387, 421, 541, 545, 497, 462, 387, 353, 301, 240, 226, 171, 140, 140, 99, 113, 86, 127, 62, 92, 144, 178, 229, 229, 185, 147, 171, 199, 240, 267, 322, 363, 445, 555, 589, 664, 736, 890, 911, 918, 932, 0])
    },
    
    'The Great Crater of Paldea': {'The Great Crater of Paldea':
    ([546, 626, 626, 715, 755, 856, 1017, 1117, 1270, 1350, 1350, 1347, 1290, 1215, 1063, 965, 879, 658, 546, 451, 399, 221, 175, 198, 178, 207, 195, 244, 244, 319, 333, 431, 474, 488, 543, 549],
    [147, 149, 121, 115, 75, 78, 167, 192, 333, 626, 911, 1086, 1201, 1241, 1143, 1152, 1063, 1074, 1040, 913, 879, 859, 787, 767, 741, 712, 678, 603, 586, 497, 500, 402, 302, 253, 213, 147])
    }
    }                 

    if app_1.province is not None:
        app_2 = InteractiveMap_province(coordenadas_area[app_1.province], app_1.province)

        # Aguarda o fechamento da janela antes de retornar o valor da province
        app_2.root.wait_window()
    
    coordenadas_biome = {'Grass':
    ([1, 111, 106, 1, 1],
    [1, 2, 39, 40, 2]),
    
    'Forest':
    ([109, 108, 218, 218, 108],
    [1, 41, 42, 1, 2]),
    
    'Town':
    ([219, 218, 328, 328, 218],
    [0, 42, 41, 0, 0]),
    
    'Desert':
    ([328, 328, 438, 438, 329],
    [1, 41, 41, 0, 1]),
    
    'Mountain':
    ([1, 108, 108, 0, 1],
    [42, 42, 82, 82, 41]),
    
    'Snow':
    ([108, 218, 218, 109, 109],
    [42, 41, 81, 82, 42]),
    
    'Swamp':
    ([219, 328, 328, 218, 219],
    [42, 42, 83, 82, 42]),
    
    'Lake':
    ([329, 437, 436, 328, 330],
    [41, 41, 84, 82, 41]),
    
    'River':
    ([0, 109, 108, 0, 0, 108],
    [82, 82, 125, 122, 82, 83]),
    
    'Ocean':
    ([109, 217, 218, 108, 108],
    [82, 82, 122, 123, 79]),
    
    'Underground':
    ([217, 328, 328, 218, 219],
    [82, 82, 123, 122, 82]),
    
    'Rocky':
    ([328, 436, 438, 327, 330],
    [83, 84, 123, 124, 80]),
    
    'Cave':
    ([1, 106, 106, 1, 0],
    [124, 124, 184, 186, 124]),
    
    'Beach':
    ([107, 106, 219, 218, 107],
    [125, 186, 184, 122, 123]),
    
    'Flower':
    ([219, 328, 328, 219, 218],
    [123, 124, 182, 184, 122]),
    
    'Bamboo':
    ([328, 438, 437, 327, 329],
    [124, 125, 183, 182, 123]),
    
    'Mine':
    ([1, 107, 108, 1, 1],
    [186, 186, 225, 225, 186]),
    
    'Olive':
    ([110, 218, 218, 108, 110],
    [187, 186, 226, 224, 188]),
    
    'Ruins':
    ([219, 329, 329, 218, 219],
    [186, 184, 225, 224, 186])
    }
        
    if app_2.area is not None:
         app_3 = InteractiveButton_biome(coordenadas_biome, app_1.province, app_2.area)
    
         # Aguarda o fechamento da janela antes de retornar o valor da province
         app_3.root.wait_window()
    
    
    return app_0.version, app_1.province, app_2.area, app_3.biome
    
# Obtém o valor da province após a execução da janela
version_value, province_value, area_value, biome_value = main()

# Agora você pode usar province_value fora da função main
print(version_value, province_value, area_value, biome_value)
