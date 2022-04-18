library(Rcrawler)

run_rcrawler <- function() {
    ###extraccion de texto empleando rcrawler###

    output <- c() #diccionario salida
    files <- list.files(path = "./archivos_html", pattern = ".html")
    index <- 0
    for (key in fromJSON(file = "./documento_base.json")) {
        html_to_string <- ContentScraper(Url = key$url, XpathPatterns = "//body")
        lista_texto <- list('xxxxtest' = list("texto" = html_to_string))

        names(lista_texto) <- str_remove(files[index + 1], ".html")
        output <- c(output, lista_texto)
    }
}