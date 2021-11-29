library(xml2)
library(jsonlite)
library(stringr)

xml2_json <- function(output_text) {
    ###almacena el texto obtenido de xml2 en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/xml2.json")
}

run_xml2 <- function() {
    ###extraccion de texto empleando xml2###

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON("../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- read_html(key$url)
        lista_texto <- list('xxxxtest' = list("texto" = unlist(html_to_string)))
        print(class(lista_texto))

        names(lista_texto) <- str_remove(files[index], ".html")
        output <- c(output, lista_texto)
        index <- index + 1
    }
    xml2_json(output)
}

#Probador
run_xml2()