library(htm2txt)

run_htm2txt <- function() {
    ###extraccion de texto empleando htm2txt###

    output <- c() #diccionario salida
    files <- list.files(path = "./archivos_html", pattern = ".html")
    index <- 0
    for (key in fromJSON(file = "./documento_base.json")) {
        html_to_string <- stri_enc_toutf8(gettxt(key$url, encoding = "latin1"))
        lista_texto <- list('test' = list("texto" = html_to_string))

        names(lista_texto) <- str_remove(files[index + 1], ".html")
        output <- c(output, lista_texto)
    }

}