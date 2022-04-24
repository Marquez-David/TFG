library(rvest)

run_rvest <- function() {
    ###extraccion de texto empleando rvest###
    output <- c() #diccionario salida

    files <- list.files(path = "./archivos_html", pattern = ".html")
    index <- 0
    for (key in fromJSON(file = "./documento_base.json")) {
        html_to_string <- read_html(key$url, encoding = "UTF-8") %>% 
                        html_nodes(xpath = '//body') %>% html_text()
        lista_texto <- list('test' = list("texto" = html_to_string))

        names(lista_texto) <- str_remove(files[index + 1], ".html")
        output <- c(output, lista_texto)
    }
}