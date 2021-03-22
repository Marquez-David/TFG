extraccion_tweets <- function(usuario, maxtweets = 100, archivoSalida= NULL){

  #Se crea el nombre de archivo por defecto
  if(is.null(archivoSalida)){
        archivoSalida <- paste0("datos_tweets_", usuario, ".csv")
  }
  
  #Se comprueba si el archivo csv existe o no
  if(!(archivoSalida %in% list.files())){
    datos_new <- searchTwitter(usuario, n = maxtweets, exclude:retweets)
    datos_new_df <- twListToDF(datos_new)
    write.csv(datos_new_df, archivoSalida)
  }else{
    #Obtengo los datos antiguos
    datos_old <- read.csv(file = archivoSalida)

    #Calculo el id del nuevo tweet a obtener
    ultimo_id <- tail(datos_old, 1)["id"] %>% pull()
    ultimo_id = ultimo_id + 1

    datos_old <- map_if(.x = datos_old, .p = is.numeric, .f = as.character)

    datos_new <- searchTwitter(usuario, n = maxtweets, maxID = ultimo_id, exclude:retweets)
    datos_new <- map_if(.x = datos_new, .p = is.numeric, .f = as.character)

    datos_new_df <- as.data.frame(datos_new)
    datos_old_df <- as.data.frame(datos_old)

    #Se concatenan los nuevos tweets con los antiguos
    datos_concatenados <- bind_rows(datos_old_df, datos_new_df)

    write.csv(datos_concatenados, archivoSalida)
  }
}