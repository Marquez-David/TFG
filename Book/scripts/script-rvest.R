run_rvest <- function() {
    ###extraccion de texto empleando rvest###

    output <- c()
    files <- list.files(path = "./archivos_html", pattern = ".html") #corpus de prueba
    index <- 1
    for (key in fromJSON(file = "./documento_base.json")) {
        #extraccion y almacenamiento de texto
        html_to_string <- read_html(key$url, encoding = "UTF-8") %>% html_nodes(xpath = '//body') %>% html_text() %>% utf8_encode()
        lista_texto <- list('xxxxtest' = list("texto" = gsub("\\r|\\t|\\n|\  ", "", unlist(html_to_string))))

        names(lista_texto) <- str_remove(files[index], ".html")
        output <- c(output, lista_texto)
        index <- index + 1
    }
    rvest_json(output)
}