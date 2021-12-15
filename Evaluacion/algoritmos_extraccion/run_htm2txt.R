library(htm2txt)
library(xml2)
library(rjson)
library(stringr)
library(stringi)

htm2txt_json <- function(output_text) {
    ###almacena el texto obtenido de htm2txt en un fichero json###

    write(toJSON(output_text, indent = 4), "./archivos_salida/htm2txt.json")
}

run_htm2txt <- function() {
    ###extraccion de texto empleando htm2txt###

    output <- c()
    files <- list.files(path = "./archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON(file = "./documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- stri_enc_toutf8(gettxt(key$url, encoding = "latin1"))
        lista_texto <- list('xxxxtest' = list("texto" = html_to_string))

        names(lista_texto) <- str_remove(files[index], ".html")
        output <- c(output, lista_texto)
        index <- index + 1
    }

    htm2txt_json(output)
}

#Probador
run_htm2txt()
