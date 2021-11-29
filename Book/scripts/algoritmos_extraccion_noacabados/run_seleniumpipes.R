library(seleniumPipes)
library(RSelenium)
library(rjson)
library(stringr)

seleniumpipes_json <- function(output_text) {
    ###almacena el texto obtenido de rcrawler en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/seleniumpipes.json")
}

run_seleniumpipes <- function() {
    ###extraccion de texto empleando seleniumpipes###

    remDr <- remoteDriver(remoteServerAddr = "localhost" , port = 4445L, browserName = "firefox")
    remDr$open()

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    contador <- 1
    for (key in fromJSON(file = "../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- remDr$navigate(key$url)
        lista_texto <- list('xxxxtest' = list("texto" = html_to_string))

        names(lista_texto) <- str_remove(files[contador], ".html")
        output <- c(output, lista_texto)
        contador <- contador + 1
    }
    remDr$close()
    seleniumpipes_json(output)
}

#Probador
run_seleniumpipes()