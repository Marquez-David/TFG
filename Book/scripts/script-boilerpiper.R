run_boilerpipeR <- function() {
    ###extraccion de texto empleando boilepipeR###
    output <- c()

    files <- list.files(path = "./archivos_html", pattern = ".html")
    index <- 0
    for (key in fromJSON(file = "./documento_base.json")) {
        html_to_str <- stri_enc_toutf8(ArticleExtractor(key$url, asText = FALSE))
        lista_texto <- list('test' = list("texto" = html_to_str))
        
        names(lista_texto) <- str_remove(files[index + 1], ".html")
        output <- c(output, lista_texto)
    }
}