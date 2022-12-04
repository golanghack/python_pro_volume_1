#! /usr/bin/env python3

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--ILLISTRATED WORK PATTERN FABRIC ON DIAGRAM FACTORY-->"""

import os 
import sys 
import tempfile

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-P':
        create_diagram(DiagramFactory).save(sys.stdout)
        cteate_diagram(SvgDiagramFactory).save(sys.stdout)
        return 
    
    text_filename = os.path.join(tempfile.gettempdir(), 'diagram.txt')
    svg_filename = os.path.join(tempfile.gettempdir(), 'diagra,.svg')
    
    text_diagram = create_diagram(DiagramFactory)
    text_diagram.save(text_filename)
    print('wrote', text_filename)
    
    svg_diagram = create_diagram(DiagramFactory)
    svg_diagram.save(svg_filename)
    print('wrote', svg_filename)
    
    
def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, 'gold')
    text = factory.make_text(7, 3, 'Abstract Factory')
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

class DiagramFactory:
    
    @classmethod
    def make_diagram(Class, width: float, height: float):
        return Class.Diagram(width, height)
    
    @classmethod
    def make_rectangle(Class, x: int, y: int, width: float, height: float, fill: str='white', stroke: str='black'):
        return Class.Rectangle(x, y, width, height, fill, stroke)
    
    @classmethod
    def make_text(Class, x: int, y: int, text: str, fontsize: int=12):
        return Class.Text(x, y, text, fontsize)
    
    BLANK = ' '
    CORNER = '+'
    HORIZONTAL = '-'
    VERTICAL = '|'
    
    class Diagram:
        
        def __init__(self, width: int, height: int):
            self.width = width
            self.height = height
            self.diagram = DiagramFactory._create_rectangle(self.width, self.height, DiagramFactory.BLANK)
            
        def add(self, component: list):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char
                    
        def save(self, filename_or_file: str):
            file = (None if isinstance(filename_or_file, str) else filename_or_file)
            try:
                if file is None:
                    file = open(filename_or_file, 'w', encoding='utf-8')
                for row in self.diagram:
                    print(''.join(row), file=file)
            finally:
                if isinstance(filename_or_file, str) and file is not None:
                    file.close()
                    
    class Rectangle:
        
        def __init__(self, x: float, y: float, width: float, height: float, fill:str, stroke: str):
            self.x = x
            self.y = y 
            self.rows = DiagramFactory._create_rectangle(width, height, DiagramFactory.BLANK if fill == 'white' else '%')
            
    
    class Text:
        
        def __init__(self, x: float, y: float, text: str, fontsize: int):
            self.x = x
            self.y = y 
            self.rows = [list(text)]
            
            
    def _create_rectangle(self, width: float, height: float, fill: str):
        rows = [[fill for _ in range(width)] for _ in range(height)]
        for x in range(1, width - 1):
            rows[0][x] = DiagramFactory.HORIZONTAL
            rows[height - 1][x] = DiagramFactory.HORIZONTAL
        for y in range(1, height - 1):
            rows[y][0] = DiagramFactory.VERTICAL
            rows[y][width - 1] = DiagramFactory.VERTICAL
        for x, y in ((0, 0), (0, width - 1), (height - 1, 0),(height - 1, width - 1)):
            rows[y][x] = DiagramFactory.CORNER
        return rows 
    
class SvgDiagramFactory(DiagramFactory):

    # The make_* class methods are inherited

    SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""

    SVG_END = "</svg>\n"

    SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" stroke="{stroke}"/>"""

    SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

    SVG_SCALE = 20


    class Diagram:

        def __init__(self, width, height):
            pxwidth = width * SvgDiagramFactory.SVG_SCALE
            pxheight = height * SvgDiagramFactory.SVG_SCALE
            self.diagram = [SvgDiagramFactory.SVG_START.format(**locals())]
            outline = SvgDiagramFactory.Rectangle(0, 0, width, height,
                    "lightgreen", "black")
            self.diagram.append(outline.svg)


        def add(self, component):
            self.diagram.append(component.svg)


        def save(self, filenameOrFile):
            file = (None if isinstance(filenameOrFile, str) else
                    filenameOrFile)
            try:
                if file is None:
                    file = open(filenameOrFile, "w", encoding="utf-8")
                file.write("\n".join(self.diagram))
                file.write("\n" + SvgDiagramFactory.SVG_END)
            finally:
                if isinstance(filenameOrFile, str) and file is not None:
                    file.close()


    class Rectangle:

        def __init__(self, x, y, width, height, fill, stroke):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            width *= SvgDiagramFactory.SVG_SCALE
            height *= SvgDiagramFactory.SVG_SCALE
            self.svg = SvgDiagramFactory.SVG_RECTANGLE.format(**locals())


    class Text:

        def __init__(self, x, y, text, fontsize):
            x *= SvgDiagramFactory.SVG_SCALE
            y *= SvgDiagramFactory.SVG_SCALE
            fontsize *= SvgDiagramFactory.SVG_SCALE // 10
            self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())


if __name__ == "__main__":
    main()
        
        
            
    