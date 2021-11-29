library(boilerpipeR)
library(rjson)
library(stringr)
library(stringi)

boilerpipeR_json <- function(output_text) {
    ###almacena el texto obtenido de boilepipeR en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/boilerpipeR.json")
}

run_boilerpipeR <- function() {
    ###extraccion de texto empleando boilepipeR###

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON(file = "../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- stri_enc_toutf8(ArticleExtractor(key$url, asText = FALSE, encoding = "UTF-8"))
        lista_texto <- list('xxxxtest' = list("texto" = html_to_string))
        
        names(lista_texto) <- str_remove(files[index], ".html")
        output <- c(output, lista_texto)
        index <- index + 1
    }
    boilerpipeR_json(output)
}

#Probador
run_boilerpipeR()