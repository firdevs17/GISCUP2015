import processing
from PyQt5.QtWidgets import QInputDialog
from qgis.gui import QgsMapToolEmitPoint
a = 0
xy_list = []
print("Choose the first point")
class PrintClickedPoint(QgsMapToolEmitPoint):
    
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

    def canvasPressEvent( self, e ):
        
        global a
        global xy_list
        global enter_method
        point = self.toMapCoordinates(self.canvas.mouseLastXY())
        a += 1
        point = list(point)
        xy_list.append(point)
        print( point)
        if a == 1:
            print("Choose the last point")
        if a == 2:
                    
            processing.run("qgis:shortestpathpointtopoint", 
            {'INPUT':'C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/sfo_roads.shp', 
            'STRATEGY':0,
            'DIRECTION_FIELD':'',
            'VALUE_FORWARD':'',
            'VALUE_BACKWARD':'',
            'VALUE_BOTH':'',
            'DEFAULT_DIRECTION':2,
            'SPEED_FIELD':'',
            'DEFAULT_SPEED':50,
            'TOLERANCE':0, 
            'START_POINT': f"{xy_list[0][0]},{xy_list[0][1]} [EPSG:3857]",
            'END_POINT': f"{xy_list[1][0]},{xy_list[1][1]} [EPSG:3857]",
            'OUTPUT':'C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/shortestpath.shp'})
            
            vlayer = QgsVectorLayer('C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/shortestpath.shp', "Shortest Path")
            vlayer.renderer().symbol().setWidth(0.8)
            vlayer.renderer().symbol().setColor(QColor("blue"))
            vlayer.triggerRepaint()
            QgsProject.instance().addMapLayer(vlayer)
            
            processing.run("qgis:shortestpathpointtopoint", 
            {'INPUT':'C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/sfo_roads.shp', 
            'STRATEGY':1,
            'DIRECTION_FIELD':'',
            'VALUE_FORWARD':'',
            'VALUE_BACKWARD':'',
            'VALUE_BOTH':'',
            'DEFAULT_DIRECTION':2,
            'SPEED_FIELD':'SPD',
            'DEFAULT_SPEED':50,
            'TOLERANCE':0, 
            'START_POINT': f"{xy_list[0][0]},{xy_list[0][1]} [EPSG:3857]",
            'END_POINT': f"{xy_list[1][0]},{xy_list[1][1]} [EPSG:3857]",
            'OUTPUT':'C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/fastestpath.shp'})
            
            vlayer = QgsVectorLayer('C:/Users/BERKAN/Desktop/III/CBS/FINAL/giscup15data-shape/fastestpath.shp', "Fastest Path")
            vlayer.renderer().symbol().setWidth(0.8)
            vlayer.renderer().symbol().setColor(QColor("red"))
            vlayer.triggerRepaint()
            QgsProject.instance().addMapLayer(vlayer)
            
canvas_clicked = PrintClickedPoint( iface.mapCanvas() )
iface.mapCanvas().setMapTool( canvas_clicked )

