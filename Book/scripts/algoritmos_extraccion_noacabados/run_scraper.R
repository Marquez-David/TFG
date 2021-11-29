library(scrapeR)
library(rjson)
library(stringr)

scraper_json <- function(output_text) {
    ###almacena el texto obtenido de scraper en un fichero json###

    write(toJSON(output_text, indent = 4), "../archivos_salida/scraper.json")
}

run_scraper <- function() {
    ###extraccion de texto empleando scraper###

    output <- c()
    files <- list.files(path = "../archivos_html", pattern = ".html") #corpus de prueba
    contador <- 1
    for (key in fromJSON(file = "../documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- scrape(url = key$url, header = FALSE, parse = TRUE)
        print(html_to_string)
    }
    scraper_json(output)
}

#Probador
run_scraper()