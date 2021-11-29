library(XML)
library(rjson)
library(stringr)

XML_json <- function(output_text) {
    ###almacena el texto obtenido de XML en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/XML.json")
}

run_XML <- function() {
    ###extraccion de texto empleando XML###

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON(file = "../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_document <- htmlTreeParse(key$url)
        html_to_string <- xpathSApply(html_document, "//text()")
        print(html_to_string)
    }
    #XML_json(output)
}

#Probador
run_XML()