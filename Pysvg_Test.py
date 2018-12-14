def HelloWorld2():
 svg=SVG("Hello World Example") # title is ignored still
 style=StyleHelper()
 style.setFontFamily(fontfamily="Verdana")
 style.setFontSize('5em') #no need for the keywords all the time
 style.setFilling("blue")
 t1=text("Hello World",0,100,style_dict=style.getStyleDict())
 svg.addElement(t1)
 svg.saveSVG('HelloWorld2.svg')

HelloWorld2()
