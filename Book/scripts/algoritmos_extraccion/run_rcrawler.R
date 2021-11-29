library(Rcrawler)
library(rjson)
library(stringr)

rcrawler_json <- function(output_text) {
    ###almacena el texto obtenido de rcrawler en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/rcrawler.json")
}

run_rcrawler <- function() {
    ###extraccion de texto empleando rcrawler###

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON(file = "../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- ContentScraper(Url = key$url, XpathPatterns = "//body")
        lista_texto <- list('xxxxtest' = list("texto" = gsub("\t|\n|\r|  ", "", unlist(html_to_string))))

        names(lista_texto) <- str_remove(files[index], ".html")
        output <- c(output, lista_texto)
        index <- index + 1
    }
    rcrawler_json(output)
}

#Probador
run_rcrawler()